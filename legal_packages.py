from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LegalPackage:
    package_id: str
    title: str
    reason: str


PACKAGES = {
    "KAMU_CORE": LegalPackage(
        "KAMU_CORE",
        "Belediye ve kamu yönetimi çekirdeği",
        "Belediye görevi, yetki, bütçe ve iç kontrol bağlamı",
    ),
    "KIK_CORE": LegalPackage(
        "KIK_CORE",
        "Kamu ihale ve sözleşme çekirdeği",
        "İhale, sözleşme, teminat, yeterlik ve uygulama hükümleri",
    ),
    "KIK_MAL": LegalPackage(
        "KIK_MAL",
        "Mal alımı ihale paketi",
        "Mal alımı veya gıda/mutfak malzemesi tedariki",
    ),
    "KIK_HIZMET": LegalPackage(
        "KIK_HIZMET",
        "Hizmet alımı ihale paketi",
        "Yemek hazırlama, dağıtım, bakım veya sosyal hizmet alımı",
    ),
    "SOSYAL_YARDIM": LegalPackage(
        "SOSYAL_YARDIM",
        "Sosyal yardım ve sosyal hizmet paketi",
        "Sosyal yardım, yararlanıcı ve hizmet sunumu",
    ),
    "ENGELLI": LegalPackage(
        "ENGELLI",
        "Engelli hizmetleri ve erişilebilirlik paketi",
        "Engelli bireylere veya özel gereksinimli kişilere yönelik hizmet",
    ),
    "COCUK": LegalPackage(
        "COCUK",
        "Çocuk koruma ve çocuk hizmetleri paketi",
        "Çocuklara yönelik destek veya koruma hizmeti",
    ),
    "KADIN_SIDDET": LegalPackage(
        "KADIN_SIDDET",
        "Kadın, konukevi ve şiddetle mücadele paketi",
        "Kadın, aile, şiddet veya konukevi hizmeti",
    ),
    "YASLI_HUZUREVI": LegalPackage(
        "YASLI_HUZUREVI",
        "Yaşlı ve huzurevi hizmetleri paketi",
        "Yaşlı bakım, huzurevi veya gündüzlü bakım hizmeti",
    ),
    "GIDA_ASEVI": LegalPackage(
        "GIDA_ASEVI",
        "Aşevi, yemek ve gıda güvenliği paketi",
        "Gıda tedariki, mutfak, yemek hazırlama veya dağıtım hizmeti",
    ),
    "ISG_PERSONEL": LegalPackage(
        "ISG_PERSONEL",
        "Personel ve iş sağlığı güvenliği paketi",
        "Yüklenici personeli, mutfak çalışanı veya saha çalışanı",
    ),
    "KVKK": LegalPackage(
        "KVKK",
        "KVKK ve bilgi güvenliği paketi",
        "Kişisel veri veya özel nitelikli veri işleme ihtimali",
    ),
    "CEVRE_ATIK": LegalPackage(
        "CEVRE_ATIK",
        "Çevre, atık ve tesis işletme paketi",
        "Aşevi, sosyal tesis, atık, ambalaj veya atık yağ konusu",
    ),
}


def select_legal_packages(
    *,
    procurement_kind: str,
    procurement_type: str,
    data_class: str,
) -> list[LegalPackage]:
    """Return routing metadata; this does not replace indexed source texts."""
    selected = [PACKAGES["KAMU_CORE"], PACKAGES["KIK_CORE"]]

    if procurement_kind == "Mal alımı":
        selected.append(PACKAGES["KIK_MAL"])
    elif procurement_kind == "Hizmet alımı":
        selected.append(PACKAGES["KIK_HIZMET"])
    else:
        selected.extend([PACKAGES["KIK_MAL"], PACKAGES["KIK_HIZMET"]])

    selected.append(PACKAGES["SOSYAL_YARDIM"])

    topic = procurement_type.lower()
    if any(term in topic for term in ["yemek", "aşevi", "kumanya"]):
        selected.extend([PACKAGES["GIDA_ASEVI"], PACKAGES["CEVRE_ATIK"]])
    if "yaşlı" in topic:
        selected.append(PACKAGES["YASLI_HUZUREVI"])
    if "engelli" in topic:
        selected.append(PACKAGES["ENGELLI"])
    if "kadın" in topic or "çocuk" in topic:
        selected.append(PACKAGES["KADIN_SIDDET"])
    if "çocuk" in topic:
        selected.append(PACKAGES["COCUK"])
    if procurement_kind == "Hizmet alımı" or any(
        term in topic for term in ["yemek", "aşevi", "kumanya", "sosyal hizmet"]
    ):
        selected.append(PACKAGES["ISG_PERSONEL"])
    if data_class != "V0 — Kamuya açık":
        selected.append(PACKAGES["KVKK"])

    unique: dict[str, LegalPackage] = {}
    for package in selected:
        unique[package.package_id] = package
    return list(unique.values())
