# Kilometre Taşları

## KT-00 — Proje yönünün netleştirilmesi

Durum: Tamamlandı

- Tez prototipinin gerçek bir kurumsal araca dönüştürülmesine karar verildi.
- Amaç skor üretmek değil; mevzuata dayalı, kanıt gösteren ön inceleme yapmak.
- İlk hedef İzmir Büyükşehir Belediyesi Sosyal Hizmetler Dairesi Başkanlığı dokümanlarıdır.

## KT-01 — Kapsam ve kullanıcı senaryoları

Durum: Tamamlandı

- Kullanıcı rolleri belirlenecek.
- Belge türleri ve alım senaryoları kesinleştirilecek.
- İlk veri seti EKAP'tan indirilen kamuya açık teknik şartname, sözleşme ve protokollerden oluşturulacak.
- Örnek belgeler mümkün olduğunca anonimleştirilecek.
- Önce uzmanlar tarafından elle değerlendirilmiş bir karşılaştırma seti hazırlanacak.
- Yapay zekâ bulguları uzman değerlendirmeleriyle karşılaştırılacak.
- Sonraki aşamada tek bir daire başkanlığı pilot seçilecek.
- Pilot kullanıcıları kurumsal kimlik/SSO ile giriş yapacak.
- İlk pilotta belgelerin kullanıcı tarafından yüklenmesi tercih edilecek.
- Sistem bir bilirkişi veya hukukçu yerine kurum içi uzman karar destek ve ön inceleme aracı olarak konumlandırılacak.
- Nihai hukuki ve idari sorumluluk ilgili uzmanlarda kalacak.
- Ayrıntılı kapsam, rol ve kullanım senaryoları [KT-01 çalışma notunda](07_KT01_KAPSAM_VE_KULLANICI_SENARYOLARI.md) tanımlandı.

### Hedef kullanıcı akışı

1. Kullanıcı kurumsal kimliğiyle portala giriş yapar.
2. Belge türünü ve alım bağlamını seçer.
3. Teknik şartname, sözleşme veya protokolü yükler.
4. Sistem uygulanabilir mevzuat paketini belirler.
5. Bulguları sayfa/bölüm, orijinal alıntı ve kaynakla gösterir.
6. Kullanıcı düzeltme önerisini inceler, kabul eder veya düzenler.
7. Sonucu rapor olarak dışa aktarır.

## KT-02 — Mevzuat ve kurum içi kaynak envanteri

Durum: Envanter taslağı hazır

- Uygulanacak mevzuat paketleri listelenecek.
- Kurum içi tip şartname, sözleşme, yönerge ve yetki belgeleri sınıflandırılacak.
- Her kaynağın yürürlük tarihi ve sürümü tutulacak.
- Sosyal Hizmetler Dairesi Başkanlığı pilotuna özel ilk kaynak sınıflandırması [KT-02 çalışma notunda](08_KT02_MEVZUAT_KAYNAK_ENVANTERI.md) oluşturuldu.
- İlk yapılandırılmış kaynak kataloğu [09_KAYNAK_KATALOGU.yaml](09_KAYNAK_KATALOGU.yaml) dosyasına eklendi.
- Katalogdaki kaynaklar doğrulanmadan üretim kararlarında kullanılmayacak.

## KT-03 — Güvenlik ve veri işleme onayı

Durum: Taslak hazır

- Belge sınıflandırması yapılacak.
- Veri saklamama, erişim, loglama ve yurt dışı aktarım kuralları belirlenecek.
- Bilgi güvenliği, hukuk ve KVKK birimlerinin onay gereksinimleri çıkarılacak.
- Pilot veri sınıflandırması ve güvenlik planı [KT-03 çalışma notunda](10_KT03_VERI_ISLEME_VE_GUVENLIK_PLANI.md) oluşturuldu.
- Kurumsal onay alınmadan V2/V3 belgelerle üretim kullanımına geçilmeyecek.

## KT-04 — Teknik MVP

Durum: İlk kod iskeleti hazır; mevzuat eşleştirme katmanı eksik

- PDF/DOCX yükleme
- Sayfa, bölüm ve tablo konumlarının korunması
- Yapılandırılmış bulgu üretimi
- Mevzuat kaynağı gösterimi
- Düzeltme önerisi
- Rapor dışa aktarma
- Sayısal uyum skoru ve ceza puanı bulunmayacak.
- Öncelik yalnızca niteliksel etiket olarak kullanılacak: Kritik, Yüksek, Orta, Düşük.
- İlk MVP yalnızca kontrollü dosya yükleme ile çalışacak.
- EKAP otomatik bağlantısı, SSO ve çoklu model desteği sonraki aşamalara bırakılacak.
- İlk Streamlit arayüzü ve Gemini sağlayıcı katmanı [app.py](app.py), [gemini_provider.py](gemini_provider.py) ve [document_parser.py](document_parser.py) dosyalarına eklendi.
- Yapılandırılmış çıktı modelleri [schemas.py](schemas.py) dosyasına eklendi.
- MVP, kaynak kataloğunu kendiliğinden mevzuat metnine dönüştürmez; onaylı bağlam boş bırakılırsa yalnızca belge içi tutarlılık incelemesi yapar.
- 5216 ve 4734 gibi mevzuatların madde düzeyinde incelenmesi için doğrulanmış kaynak metni, sürüm bilgisi ve arama/eşleştirme katmanı ayrıca geliştirilmelidir.

### MVP kabul ölçütleri

- Kullanıcı bir PDF veya DOCX yükleyebilmeli.
- Sistem sayfa/bölüm bilgisiyle metin çıkarabilmeli.
- Her bulgu dokümandan birebir kanıt içermeli.
- Her bulgu ilgili mevzuat/kriter kaynağını göstermeli.
- Her bulgu için uygulanabilir düzeltme önerisi üretilmeli.
- Çıktı insan tarafından incelenip rapor olarak indirilebilmeli.
- Belge analiz sonrasında kalıcı olarak saklanmamalı.

### Mevcut MVP'nin sınırı

Mevcut kabul ölçütlerinden "her bulgunun ilgili mevzuat/kriter kaynağını göstermesi" henüz tamamlanmış değildir. Bu ölçüt, mevzuat kaynakları doğrulanıp analiz akışına bağlandıktan sonra yeniden test edilecektir.

## KT-04A — Mevzuat eşleştirme ve kaynak gösterme

Durum: İlk yönlendirme katmanı hazır; kaynak metni indeksleme bekliyor

- Belge türü ve alım türüne göre uygulanabilir mevzuat paketi seçilecek.
- 4734/4735, ilgili uygulama yönetmeliği, Kamu İhale Genel Tebliği ve belediye/sosyal hizmet kaynakları doğrulanmış metinlerle tutulacak.
- Her bulgu için kaynak adı, madde/fıkra, kaynak alıntısı, yürürlük/sürüm bilgisi ve belge kanıtı birlikte üretilecek.
- Kaynak bulunamadığında sistem açıkça "kaynak doğrulaması gerekli" diyecek; madde numarası uydurmayacak.
- İlk testte Çekmeköy belgesinin mal alımı olması nedeniyle Mal Alımı İhaleleri Uygulama Yönetmeliği de kapsam kontrolüne eklenecek.
- Belge ve alım türüne göre etkin paketleri seçen yönlendirme katmanı [legal_packages.py](legal_packages.py) dosyasına eklendi.
- Uygulama arayüzünde seçilen paketler görünür hale getirildi; paket adlarının tek başına mevzuat taraması sayılmayacağı açıkça belirtildi.
- Ayrıntılı paket tanımları [11_MEVZUAT_PAKETLERI.md](11_MEVZUAT_PAKETLERI.md) dosyasına eklendi.

## KT-05 — Pilot ve doğrulama

Durum: Başlanmadı

- Anonimleştirilmiş gerçek örneklerle pilot yapılacak.
- Uzman değerlendirmesiyle bulgular karşılaştırılacak.
- Yanlış pozitif, yanlış negatif ve kaynak doğruluğu ölçülecek.

## KT-06 — Kurumsal yaygınlaştırma

Durum: Başlanmadı

- Daire başkanlığı bazlı yetki ve kota
- SSO entegrasyonu
- Merkezi yönetim paneli
- Mevzuat güncelleme süreci
- Denetim ve kullanım raporları

## KT-07 — Kurumsal portal ve erişim modeli

Durum: Başlanmadı

- Tek bir kurumsal portal oluşturulacak; farklı web siteleri yerine modüler ekranlar kullanılacak.
- Kullanıcı adı ve şifre uygulama içinde tutulmayacak.
- İBB SSO, kurumsal dizin veya onaylı kimlik altyapısı kullanılacak.
- Daire başkanlığı, rol ve belge erişimi yetkilendirilecek.
- API anahtarları kullanıcılara verilmeyecek; merkezi AI Gateway üzerinden yönetilecek.
- İç sistemlere bağlantı yalnızca izinli API, SSO veya servis hesabı üzerinden kurulacak.
- İlk pilotta otomatik sistem entegrasyonu yerine kontrollü dosya yükleme kullanılacak.
