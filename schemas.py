from typing import Literal

from pydantic import BaseModel, Field


Priority = Literal["Kritik", "Yüksek", "Orta", "Düşük", "Belirsiz"]


class Finding(BaseModel):
    finding_id: str = Field(description="Bulguyu benzersiz tanımlayan kısa kimlik")
    category: str = Field(description="Belirsizlik, eksiklik, çelişki, mevzuat riski veya kalite sorunu")
    priority: Priority
    location: str = Field(description="Sayfa, paragraf, tablo veya bölüm konumu")
    source_text: str = Field(description="Dokümandan birebir ve kısa alıntı")
    source_reason: str = Field(description="Alıntının neden sorunla ilişkili olduğu")
    reference: str = Field(description="Verilen kaynak bağlamındaki ilgili mevzuat/kriter; yoksa 'Kaynak bağlamı verilmedi'")
    finding: str = Field(description="Açık ve kanıta dayalı tespit")
    recommendation: str = Field(description="Uygulanabilir düzeltme veya yeniden yazım önerisi")
    needs_expert_review: bool = Field(default=True)


class AnalysisReport(BaseModel):
    document_summary: str
    applicable_scope: list[str] = Field(default_factory=list)
    findings: list[Finding] = Field(default_factory=list)
    overlooked_requirements: list[str] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)
