from schemas import AnalysisReport


def report_to_markdown(report: AnalysisReport, metadata: dict) -> str:
    lines = [
        "# Kamu Dokümanı Ön İnceleme Raporu",
        "",
        f"- Belge: {metadata.get('filename', '')}",
        f"- Belge türü: {metadata.get('document_type', '')}",
        f"- Alım türü: {metadata.get('procurement_kind', '')}",
        f"- Veri sınıfı: {metadata.get('data_class', '')}",
        f"- Model: {metadata.get('model', '')}",
        f"- Analiz zamanı: {metadata.get('completed_at', '')}",
        "",
        "> Bu rapor hukukî görüş veya otomatik onay değildir; uzman ön incelemesine yardımcı olmak amacıyla üretilmiştir.",
        "",
        "## Özet",
        "",
        report.document_summary,
        "",
        "## Bulgular",
        "",
    ]

    if not report.findings:
        lines.append("Kanıtlı bulgu üretilmedi.")
    else:
        for finding in report.findings:
            lines.extend(
                [
                    f"### {finding.finding_id} — {finding.category} ({finding.priority})",
                    "",
                    f"- Konum: {finding.location}",
                    f"- Orijinal metin: \"{finding.source_text}\"",
                    f"- Tespit: {finding.finding}",
                    f"- Kaynak: {finding.reference}",
                    f"- Kaynakla ilişki: {finding.source_reason}",
                    f"- Düzeltme önerisi: {finding.recommendation}",
                    "",
                ]
            )

    if report.overlooked_requirements:
        lines.extend(["## Gözden Kaçan Kritik Gereksinimler", ""])
        lines.extend(f"- {item}" for item in report.overlooked_requirements)
        lines.append("")

    if report.limitations:
        lines.extend(["## Sınırlılıklar", ""])
        lines.extend(f"- {item}" for item in report.limitations)
        lines.append("")

    return "\n".join(lines)
