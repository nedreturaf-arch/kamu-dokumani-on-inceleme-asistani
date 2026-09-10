# Karar ve Toplantı Günlüğü

## 2026-09-09 — Başlangıç kararları

- Tez prototipi gerçek bir kurumsal kullanım aracına dönüştürülecek.
- İlk hedef kamu alımlarında teknik şartname, sözleşme ve protokol ön incelemesi.
- İlk hedef İzmir Büyükşehir Belediyesi Sosyal Hizmetler Dairesi Başkanlığı dokümanlarıdır.
- Skor ve ceza puanı kaldırılacak.
- Kanıt, sayfa/bölüm bilgisi, mevzuat kaynağı ve düzeltme önerisi temel çıktı olacak.
- Gemini mevcut kod nedeniyle ilk MVP adayı; ancak mimari sağlayıcı bağımsız olacak.
- Kurumsal üretim için merkezi AI Gateway, SSO ve rol tabanlı erişim tercih edilecek.
- Ham API anahtarları kullanıcılara dağıtılmayacak.
- Gerçek belgelerde veri saklamama, erişim kontrolü ve sağlayıcı sözleşmesi zorunlu değerlendirme başlıkları olacak.
- İlk mevzuat kapsamı 4734, 4735, hizmet alımı mevzuatı, KVKK, bilgi güvenliği ve kurum içi kaynaklar olacak.

## 2026-09-09 — Pilot ve kurumsal portal yaklaşımı

- İlk aşamada EKAP'tan indirilen birkaç teknik şartname, sözleşme ve protokol taranacak.
- Bu belgeler test ve karşılaştırma veri seti olarak kullanılacak; mümkün olduğunca anonimleştirilecek.
- Yapay zekâ çıktıları önce uzmanlarca hazırlanmış elle değerlendirmelerle karşılaştırılacak.
- Doğrulama sonrasında tek bir daire başkanlığı pilot olarak seçilecek.
- Kullanıcılar kurumsal kimlik/SSO ile giriş yapacak.
- Sistem tek bir kurumsal portal olarak geliştirilecek; teknik şartname, sözleşme, protokol ve mevzuat kontrolü modülleri bulunacak.
- Kullanıcıların sağlayıcı API anahtarlarını görmesi veya paylaşması gerekmeyecek.
- İç web sistemlerine bağlantı yalnızca kurum tarafından izin verilen API, SSO veya servis hesabı ile yapılacak.
- Sistem bilirkişi veya hukukçu yerine uzman karar destek ve ön inceleme aracı olarak tanımlanacak.
- Nihai hukuki ve idari değerlendirme kullanıcı uzman tarafından yapılacak.

## 2026-09-09 — Teknik geliştirmeye geçiş kararı

- Artık proje kodlama aşamasına alınacak.
- Geliştirme sıralı ilerleyecek: kapsam ve kullanıcı senaryoları, mevzuat kaynak envanteri, güvenlik/veri işleme kuralları, ardından teknik MVP.
- İlk teknik MVP'de sayısal uyum skoru ve ceza puanı olmayacak.
- Öncelik seviyeleri yalnızca niteliksel etiket olarak kullanılacak.
- İlk MVP kontrollü PDF/DOCX yükleme ile başlayacak.
- EKAP otomatik bağlantısı, SSO, çoklu model ve kurumsal yaygınlaştırma sonraki aşamalara bırakılacak.
- MVP'nin temel başarısı; kanıt, mevzuat kaynağı ve düzeltme önerisinin birlikte sunulması olacak.

## 2026-09-09 — KT-01 kapsam taslağı

- İlk pilot İzmir Büyükşehir Belediyesi Sosyal Hizmetler Dairesi Başkanlığı olacak.
- İlk pilot sosyal yardım ve sosyal hizmet alımı teknik şartnamesi, sözleşmesi ve ilişkili protokollerle başlayacak.
- Yapım, mal alımı ve özel sektör mevzuatı ilk MVP kapsamına alınmayacak.
- İlk kullanım biçimi kontrollü dosya yükleme ve rapor indirme olacak.
- Belge hazırlayan kullanıcı, ihale/mevzuat uzmanı, teknik uzman ve sistem yöneticisi rolleri tanımlandı.
- Bulgularda kanıt, sayfa/bölüm, mevzuat kaynağı, tespit ve düzeltme önerisi zorunlu olacak.
- Pilot daire başkanlığı; düzenli doküman üreten, uzman doğrulaması yapabilecek ve anonim örnek sağlayabilecek birimlerden seçilecek.
- Ayrıntılı çalışma notu `07_KT01_KAPSAM_VE_KULLANICI_SENARYOLARI.md` dosyasına eklendi.

## 2026-09-09 — Kurum ve pilot birim kesinleşti

- Kurum: İzmir Büyükşehir Belediyesi.
- Pilot: Sosyal Hizmetler Dairesi Başkanlığı.
- İlk alt birim henüz belirlenmedi; belge hacmi, uzman erişimi ve veri hassasiyetine göre seçilecek.
- KT-02 mevzuat envanterine sosyal hizmet, sosyal yardım, engelli, kadın/çocuk, yaşlı, aşevi ve özel nitelikli kişisel veri başlıkları eklenecek.

## 2026-09-09 — KT-02 kaynak envanteri taslağı

- Kamu alımı çekirdeği, belediye mevzuatı, sosyal hizmet sektörel kaynakları, KVKK ve İzmir Büyükşehir Belediyesi kurum içi kaynakları ayrı paketler olarak tanımlandı.
- Kaynakların belgeye uygulanması, hizmet konusu ve alım bağlamına göre koşullu olacak.
- Her kaynak için yürürlük, sürüm, resmî bağlantı, uygulanabilirlik ve uzman doğrulaması tutulacak.
- Ayrıntılı envanter `08_KT02_MEVZUAT_KAYNAK_ENVANTERI.md` dosyasına eklendi.

## 2026-09-09 — Yapılandırılmış kaynak kataloğu

- Mevzuat ve kurum içi kaynaklar makine tarafından okunabilir bir katalog formatına alındı.
- Kaynaklar bağlayıcı, kurum içi bağlayıcı, koşullu, yorum/uygulama ve sözleşmeye bağlı olarak sınıflandırıldı.
- Her kaynağa uygulanabilirlik koşulu, resmî bağlantı ve doğrulama durumu eklendi.
- Doğrulanmamış kaynakların üretim analizinde kullanılmaması kararlaştırıldı.
- Katalog `09_KAYNAK_KATALOGU.yaml` dosyasına eklendi.

## 2026-09-09 — KT-03 güvenlik ve veri işleme taslağı

- Pilot belgeler V0 kamuya açık, V1 kurum içi, V2 kişisel veri içeren ve V3 özel nitelikli/yüksek hassasiyetli olarak sınıflandırıldı.
- İlk geliştirme ve model karşılaştırmasında V0 belgeler kullanılacak.
- V2/V3 belgeler için anonimleştirme veya kurum tarafından onaylanmış özel ortam zorunlu olacak.
- Kullanıcılara sağlayıcı API anahtarı verilmeyecek; merkezi AI Gateway kullanılacak.
- Belge içeriği kalıcı olarak saklanmayacak; sınırlı metadata için kurum saklama politikası belirlenecek.
- SSO, rol tabanlı erişim, kota, model/katalog sürümü ve insan onayı zorunlu tasarım unsurları olarak belirlendi.
- Ayrıntılı plan `10_KT03_VERI_ISLEME_VE_GUVENLIK_PLANI.md` dosyasına eklendi.

## 2026-09-09 — KT-04 ilk teknik MVP iskeleti

- İlk Streamlit arayüzü oluşturuldu.
- PDF ve DOCX için yerel metin çıkarma katmanı eklendi.
- PDF sayfa, DOCX paragraf ve tablo konumları çıktıya taşınacak şekilde modellendi.
- Gemini sağlayıcısı güncel `google-genai` istemcisi ve yapılandırılmış JSON çıktısı ile bağlandı.
- Bulgular; kanıt, konum, kaynak, tespit ve düzeltme önerisi alanlarıyla modellendi.
- Skor, ceza puanı ve yüzdelik uyum hesabı eklenmedi.
- İlk MVP'de V2/V3 belgeler güvenlik onayı olmadan işlenemeyecek şekilde engellendi.
- Markdown ve JSON rapor indirme eklendi.
- Uçtan uca API testi için kurum tarafından onaylı geliştirme anahtarı ve örnek belge gerekiyor.

## 2026-09-10 — İlk aşevi teknik şartname testi ve mevzuat eşleştirme açığı

- Çekmeköy Belediyesi 2026 Yılı Aşevi Mutfağı İçin Gıda Alımı teknik şartnamesi, 52 sayfalık PDF olarak V0 kamuya açık test belgesi şeklinde işlendi.
- Belge türü ve konu seçimi doğruydu: teknik şartname, yemek/aşevi/kumanya ve V0 kamuya açık.
- İlk rapor beş belge içi bulgu üretti: ürün tanımı çelişkisi, metraj/adet çelişkisi, terim kopyalama ve sipariş iletişim yöntemi belirsizliği.
- Rapor 5216 veya 4734 sayılı mevzuatı madde düzeyinde taramadı. Bunu raporun sınırlılıklar bölümü de açıkça belirtti.
- Kök nedenler: onaylı mevzuat/kriter bağlamının boş bırakılması, kaynak kataloğunun henüz analiz akışına bağlı olmaması ve mevzuat metinleri için arama/eşleştirme katmanının bulunmaması.
- Bu sonuç, KT-04'ün belge içi kalite kontrol kısmının çalıştığını; mevzuat eşleştirme kabul ölçütünün ise henüz karşılanmadığını gösterdi.
- Çekmeköy örneği mal alımı niteliğinde olduğundan, ilk MVP'nin hizmet alımı ağırlıklı kapsamı genişletilmeden 4734 ve ilgili Mal Alımı İhaleleri Uygulama Yönetmeliği eşleştirmesi tamamlanamayacak.
- Sonraki teknik iş olarak KT-04A mevzuat eşleştirme ve kaynak gösterme kilometre taşı planlandı.

## Not alma kuralı

Yeni bir konu konuşulduğunda asistan önce bunun proje kararı, kilometre taşı, kapsam değişikliği veya geçici fikir olup olmadığını ayırt edecek. Kalıcı bir karar veya önemli plan değişikliği ise kullanıcıya “Bunu proje notlarına ekleyeyim mi?” diye sorulacak.
