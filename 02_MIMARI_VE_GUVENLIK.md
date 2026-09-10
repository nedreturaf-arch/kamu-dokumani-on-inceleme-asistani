# Mimari ve Güvenlik

## Önerilen mimari

```text
İBB SSO / kurumsal giriş
        ↓
Web uygulaması
        ↓
Yetki ve politika katmanı
        ↓
Merkezi AI Gateway
        ↓
Belge işleme + mevzuat erişimi + model çağrısı
        ↓
Geçici analiz sonucu ve kullanıcıya rapor
```

## API anahtarı yaklaşımı

Kullanıcılara ham sağlayıcı API anahtarı verilmemeli. Anahtarlar yalnızca merkezi backend veya AI Gateway üzerinde tutulmalı. Kullanıcılar İBB kimliğiyle giriş yapmalı.

Gerekirse daire başkanlığı bazında ayrı proje/servis hesabı, kota ve harcama sınırı tanımlanabilir. Kullanıcı ayrıntılı loglarda kimliklendirilirken sağlayıcı anahtarı paylaşılmamalıdır.

## Durumsuz çalışma hedefi

- Yüklenen belge kalıcı veritabanına yazılmayacak.
- Belge analiz boyunca geçici bellekte veya şifreli geçici alanda tutulacak.
- İşlem tamamlanınca geçici dosya silinecek.
- Sağlayıcının kalıcı dosya, konuşma geçmişi, vektör deposu ve arka plan işlem özellikleri kullanılmayacak.
- Loglarda belge metni ve kişisel veri tutulmayacak.
- Yalnızca kullanıcı, birim, zaman, model sürümü, işlem durumu ve hata kodu gibi sınırlı metadata tutulabilecek.

## Güvenlik kontrolleri

- SSO ve rol tabanlı erişim
- Daire başkanlığı ve görev bazlı yetkilendirme
- Dosya türü, boyutu ve zararlı içerik kontrolü
- Şifreli aktarım ve şifreli geçici depolama
- API key gizli yönetimi ve düzenli rotasyon
- Kota ve maliyet alarmı
- Yönetici müdahalesiyle erişim iptali
- Belge içeriği olmayan denetim logları
- İnsan onayı olmadan otomatik belge değişikliği yapılmaması

## Kritik uyarı

Uygulamanın veritabanı kullanmaması, model sağlayıcının hiç geçici log tutmadığı anlamına gelmez. Üretim seçimi; sağlayıcı sözleşmesi, veri işleme eki, veri yerleşimi, saklama politikası ve İBB bilgi güvenliği onayı birlikte değerlendirilerek yapılmalıdır.
