# KT-03 — Güvenlik ve Veri İşleme Onayı

## Amaç

İzmir Büyükşehir Belediyesi Sosyal Hizmetler Dairesi Başkanlığı pilotunda belgelerin hangi koşullarda yapay zekâ ile analiz edilebileceğini, hangi verilerin işlenemeyeceğini ve erişim/saklama kontrollerini belirlemek.

Bu belge teknik tasarım ve ön onay çerçevesidir. Kurumun bilgi güvenliği, hukuk ve KVKK yetkililerinin onayı olmadan üretim kullanımına geçilmemelidir.

## Veri sınıflandırması

### V0 — Kamuya açık

EKAP veya kurum web sitesinde yayımlanmış, kişisel veri ve ticari sır içermeyen örnek belgeler. İlk geliştirme ve model karşılaştırmasında kullanılabilir.

### V1 — Kurum içi

Kurum çalışanlarının erişebildiği, kamuya açık olmayan ancak yüksek hassasiyet içermeyen belgeler. Pilot öncesi kurum politikasıyla değerlendirilmeli.

### V2 — Kişisel veri içeren

Ad-soyad, iletişim, adres, başvuru, sosyal inceleme veya hizmet yararlanıcısı bilgisi içeren belgeler. Yetkili kullanıcı, onaylı ortam ve veri işleme şartları olmadan dış modele gönderilmemeli.

### V3 — Özel nitelikli veya yüksek hassasiyetli

Sağlık, engellilik, çocuk, şiddet, biyometrik, sosyal yardım/muhtaçlık ve benzeri hassas bilgiler ile ticari sır veya güvenlik açısından kritik içerikler. İlk pilotta mümkünse anonimleştirilmeli; üretimde yalnızca kurum tarafından onaylanmış özel ortamda işlenmeli.

## İlk pilot veri politikası

- Geliştirme ve model karşılaştırmasında V0 belgeler kullanılacak.
- İç pilotta V1 belgeler, kurum onayı ve erişim kontrolüyle kullanılabilecek.
- V2/V3 belgeler için önce maskeleme/anonimleştirme yapılacak.
- Anonimleştirme mümkün değilse belge yalnızca kurumun onayladığı model ve çalışma ortamında işlenecek.
- Kullanıcıya gerçek kişi verisini gereksiz yere yüklememe uyarısı gösterilecek.
- Dosya analiz tamamlanınca geçici kopya silinecek.

## Saklama politikası

### Saklanmayacaklar

- Yüklenen belgenin kalıcı kopyası
- Belge metninin tamamı
- Kişisel veri ve ticari sır içeren prompt/yanıt
- Model sağlayıcının kalıcı dosya, konuşma veya vektör deposu

### Sınırlı olarak saklanabilecekler

- Kullanıcı ve birim kimliği
- İşlem zamanı
- Belge türü ve dosya özeti/hash değeri
- Kullanılan model ve katalog sürümü
- İşlem durumu ve hata kodu
- Kullanıcının bulguya ilişkin anonim geri bildirim etiketi

Bu metadata'nın saklama süresi ve erişim yetkisi kurum tarafından ayrıca belirlenmelidir.

## Erişim ve kimlik

- Kurumsal SSO veya onaylı kurum dizini kullanılacak.
- Rol tabanlı erişim uygulanacak.
- Kullanıcı yalnızca kendi dairesinin izin verdiği belgeleri görebilecek.
- Mevzuat yöneticisi kaynak katalogunu güncelleyebilecek.
- Sistem yöneticisi altyapıyı yönetecek; belge içeriğine varsayılan olarak erişemeyecek.
- Hukuk/ihale uzmanı bulguları doğrulayabilecek.
- Personel ayrıldığında erişim kurum kimlik sistemi üzerinden kapatılacak.

## Merkezi AI Gateway gereksinimleri

- Sağlayıcı API anahtarı backend dışında görünmeyecek.
- Daire ve kullanıcı bazında kota uygulanabilecek.
- Model ve kaynak kataloğu sürümü kaydedilecek.
- İsteklerde belge saklayan özellikler varsayılan olarak kapalı olacak.
- Web araması ve üçüncü taraf veri aktarımı ilk pilotta kapalı olacak.
- Yanıtlar yapılandırılmış şemaya göre doğrulanacak.
- Sağlayıcıya gönderilecek veri sınıfı politika motoruyla kontrol edilecek.

## Sağlayıcı değerlendirme şartları

- Veri işleme sözleşmesi ve alt işleyen bilgisi
- Verinin işlendiği ve saklandığı coğrafya
- Prompt/çıktı saklama süresi
- Sıfır veri saklama veya eşdeğer kurumsal kontrolün sözleşme kapsamı
- Model eğitimi için kullanım durumu
- Dosya, konuşma geçmişi, cache ve kötüye kullanım logları
- Silme ve erişim taleplerinin nasıl yürütüldüğü
- Güvenlik olayı bildirim süresi
- Alt yüklenici ve yurt dışı aktarım hükümleri
- Kurumun denetim ve fesih sonrası veri silme hakkı

## İnsan onayı

- Sistem “uygunsuzluk var” sonucunu nihai hukukî karar olarak sunmayacak.
- Kullanıcı her bulguyu kabul, reddet veya inceleme gerekli olarak işaretleyebilecek.
- Önerilen sözleşme/şartname metni kullanıcı onayı olmadan belgeye yazılmayacak.
- Kritik veya özel nitelikli veri içeren bulgular uzman incelemesine yönlendirilecek.

## Pilot öncesi onay kontrol listesi

- [ ] Pilot birim ve sorumlu kişi belirlendi.
- [ ] Belge veri sınıflandırması onaylandı.
- [ ] Kullanılacak model sağlayıcısı ve ortam onaylandı.
- [ ] Veri işleme sözleşmesi incelendi.
- [ ] SSO ve rol matrisi belirlendi.
- [ ] Saklama/silme politikası onaylandı.
- [ ] API anahtarı yönetimi ve kota belirlendi.
- [ ] Olay müdahale süreci belirlendi.
- [ ] Uzman doğrulama ve geri bildirim süreci belirlendi.
- [ ] Gerçek belgelerle pilot başlatma izni verildi.

## KT-03 sınırı

Bu plan bir kurum onayı yerine geçmez. Özellikle V2/V3 belgelerde veri işleme, yurt dışı aktarım, sağlayıcı logları ve erişim kayıtları hukuk/KVKK/bilgi güvenliği birimlerince ayrıca değerlendirilmelidir.
