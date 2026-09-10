# Yapay Zekâ Seçimi

## Başlangıç kararı

İlk MVP, mevcut uygulama Gemini ile yazıldığı için Gemini tabanlı geliştirilebilir; ancak kod, model sağlayıcısından bağımsız bir arayüzle tasarlanmalıdır.

## Adaylar

### Gemini / Vertex AI

- Mevcut koda en hızlı uyum sağlayan seçenek.
- PDF belge işleme ve yapılandırılmış çıktı desteği güçlü.
- Üretim için ücretsiz AI Studio kullanımı yerine ücretli/kurumsal yapı değerlendirilmelidir.

### Azure OpenAI

- İBB’nin Microsoft/Azure altyapısı varsa güçlü adaydır.
- Kurumsal kimlik, ağ ve güvenlik yönetimiyle birlikte değerlendirilebilir.

### OpenAI API / kurumsal OpenAI çözümleri

- Yapılandırılmış JSON çıktıları ve dosya arama yetenekleri değerlendirilebilir.
- Veri saklama kontrolleri, bölgesel işleme ve kurumsal sözleşme şartları incelenmelidir.

### Claude

- PDF, tablo ve belge analizi için güçlü bir alternatiftir.
- Türkiye’de kurumsal veri işleme, erişilebilirlik ve sözleşme koşulları ayrıca incelenmelidir.

### Kurum içinde barındırılan açık kaynak model

- Belgelerin kurum dışına çıkmaması gereken senaryolarda değerlendirilebilir.
- Donanım, bakım, Türkçe mevzuat doğruluğu ve model güncelleme maliyeti dikkate alınmalıdır.

## Seçim yöntemi

Model pazarlama iddiasıyla değil, aynı anonimleştirilmiş belge setiyle karşılaştırılmalı:

- Kanıt alıntısı doğruluğu
- Sayfa/bölüm konumu doğruluğu
- Uygulanabilir mevzuat seçimi
- Uydurma bulgu oranı
- Yanlış pozitif ve yanlış negatif oranı
- Düzeltme önerisinin kullanılabilirliği
- Maliyet, gecikme ve hata oranı

## Uygulama ilkesi

İlk sürümde bir ana model kullanılmalı. İkinci bir model yalnızca seçili bulguları doğrulamak için devreye alınmalı; her istekte çoklu model çalıştırmak ilk aşamada gerekli değildir.
