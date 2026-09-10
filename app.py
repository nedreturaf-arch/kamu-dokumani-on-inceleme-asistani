import json
import os
from datetime import datetime

import streamlit as st

from document_parser import parse_document
from gemini_provider import analyze_document
from legal_packages import select_legal_packages
from reporting import report_to_markdown


def configured_secret(name: str, default: str = "") -> str:
    """Read a deployment secret without failing during local development."""
    try:
        return str(st.secrets.get(name, os.getenv(name, default)))
    except Exception:
        return os.getenv(name, default)


st.set_page_config(
    page_title="Kamu Dokümanı Ön İnceleme Asistanı",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 Kamu Dokümanı Ön İnceleme Asistanı")
st.caption(
    "İzmir Büyükşehir Belediyesi Sosyal Hizmetler Dairesi Başkanlığı pilotu için ilk teknik MVP"
)
st.warning(
    "Bu araç hukukî görüş veya otomatik onay vermez. Bulgular uzman incelemesine sunulan ön değerlendirmelerdir."
)

with st.sidebar:
    st.header("Analiz bağlamı")
    document_type = st.selectbox(
        "Belge türü",
        ["Teknik şartname", "Sözleşme", "Protokol", "Diğer"],
    )
    procurement_kind = st.selectbox(
        "Alım türü",
        ["Belirlenmedi", "Mal alımı", "Hizmet alımı", "Yapım işi", "Doğrudan temin"],
    )
    procurement_type = st.selectbox(
        "Alım/hizmet konusu",
        [
            "Sosyal yardım",
            "Sosyal hizmet",
            "Yemek / aşevi / kumanya",
            "Yaşlı hizmeti",
            "Engelli hizmeti",
            "Kadın / çocuk hizmeti",
            "Sosyal tesis",
            "Diğer",
        ],
    )
    data_class = st.selectbox(
        "Belge veri sınıfı",
        ["V0 — Kamuya açık", "V1 — Kurum içi", "V2 — Kişisel veri", "V3 — Yüksek hassasiyet"],
    )
    model_name = st.text_input(
        "Gemini model adı",
        value=configured_secret("GEMINI_MODEL", "gemini-3.7-flash"),
        help="Üretimde kurum tarafından onaylanmış model adı kullanılmalıdır.",
    )
    api_key = st.text_input(
        "Geliştirme API anahtarı",
        value=configured_secret("GEMINI_API_KEY"),
        type="password",
        help="Bu alan yalnızca yerel geliştirme içindir. Üretimde anahtar backend üzerinde tutulmalıdır.",
    )

uploaded_file = st.file_uploader(
    "PDF veya DOCX yükleyin",
    type=["pdf", "docx"],
    help="İlk MVP'de dosya yalnızca analiz süresince işlenir; uygulama kalıcı belge arşivi oluşturmaz.",
)

approved_context = st.text_area(
    "Onaylı mevzuat/kriter bağlamı (opsiyonel)",
    height=180,
    placeholder=(
        "İncelemede kullanılacak onaylı madde veya kriter özetlerini buraya ekleyin. "
        "Kaynak metni verilmemiş bir mevzuat maddesini sistem uydurmamalıdır."
    ),
)

active_packages = select_legal_packages(
    procurement_kind=procurement_kind,
    procurement_type=procurement_type,
    data_class=data_class,
)
with st.expander("Bu seçimlerle etkinleşen mevzuat paketleri", expanded=False):
    st.caption(
        "Bunlar yönlendirme bilgileridir. Madde düzeyinde tarama için doğrulanmış kaynak metni ayrıca sisteme bağlanmalıdır."
    )
    for package in active_packages:
        st.write(f"- **{package.title}** — {package.reason}")

if st.button("🔍 Ön İncelemeyi Başlat", type="primary", disabled=uploaded_file is None):
    if not api_key.strip():
        st.error("Geliştirme için Gemini API anahtarı gerekli.")
    elif data_class in {"V2 — Kişisel veri", "V3 — Yüksek hassasiyet"}:
        st.error(
            "V2/V3 belgeler bu yerel MVP'de işlenmemeli. Önce kurumun bilgi güvenliği, hukuk ve KVKK onayı alınmalı."
        )
    else:
        try:
            raw_bytes = uploaded_file.getvalue()
            parsed = parse_document(uploaded_file.name, raw_bytes)
            if not parsed.text.strip():
                st.error("Belgeden işlenebilir metin çıkarılamadı. Taranmış PDF için OCR aşaması gereklidir.")
            else:
                with st.spinner("Belge inceleniyor..."):
                    report = analyze_document(
                        api_key=api_key.strip(),
                        model_name=model_name.strip(),
                        document=parsed,
                        document_type=document_type,
                        procurement_kind=procurement_kind,
                        procurement_type=procurement_type,
                        data_class=data_class,
                        approved_context=approved_context.strip(),
                        legal_packages=active_packages,
                    )
                st.session_state["analysis_report"] = report
                st.session_state["analysis_meta"] = {
                    "filename": uploaded_file.name,
                    "document_type": document_type,
                    "procurement_kind": procurement_kind,
                    "data_class": data_class,
                    "model": model_name.strip(),
                    "completed_at": datetime.now().isoformat(timespec="seconds"),
                }
                st.success("Ön inceleme tamamlandı.")
        except Exception as exc:
            st.error(f"Analiz sırasında hata oluştu: {exc}")

report = st.session_state.get("analysis_report")
meta = st.session_state.get("analysis_meta", {})

if report:
    st.subheader("Analiz özeti")
    st.write(report.document_summary)

    if report.applicable_scope:
        st.subheader("İncelemeye alınan kapsam")
        for item in report.applicable_scope:
            st.write(f"- {item}")

    st.subheader(f"Bulgular ({len(report.findings)})")
    if not report.findings:
        st.success("Belgede kanıtlı bir bulgu üretilmedi.")
    for finding in report.findings:
        title = f"{finding.priority} · {finding.category} · {finding.location}"
        with st.expander(title):
            st.markdown(f"**Orijinal metin:** \"{finding.source_text}\"")
            st.markdown(f"**Tespit:** {finding.finding}")
            st.markdown(f"**İlgili kaynak:** {finding.reference}")
            st.markdown(f"**Kaynakla ilişki:** {finding.source_reason}")
            st.markdown(f"**Düzeltme önerisi:** {finding.recommendation}")
            st.checkbox(
                "Uzman incelemesine gönderildi",
                value=finding.needs_expert_review,
                key=f"review_{finding.finding_id}",
            )

    if report.overlooked_requirements:
        st.subheader("Gözden kaçan kritik gereksinimler")
        for item in report.overlooked_requirements:
            st.write(f"- {item}")

    if report.limitations:
        st.subheader("Sınırlılıklar")
        for item in report.limitations:
            st.write(f"- {item}")

    st.divider()
    st.subheader("Raporu dışa aktar")
    report_markdown = report_to_markdown(report, meta)
    report_json = json.dumps(report.model_dump(), ensure_ascii=False, indent=2)
    col1, col2 = st.columns(2)
    col1.download_button(
        "Markdown raporu indir",
        data=report_markdown,
        file_name="on_inceleme_raporu.md",
        mime="text/markdown",
    )
    col2.download_button(
        "JSON raporu indir",
        data=report_json,
        file_name="on_inceleme_raporu.json",
        mime="application/json",
    )
