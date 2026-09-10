# KT-01 — Kapsam ve Kullanıcı Senaryoları

## Amaç

İlk pilotta, kamu alımına ilişkin teknik şartname, sözleşme ve protokollerin uzman incelemesini hızlandıran bir ön kontrol akışı oluşturmak.

Sistem; eksik, belirsiz, çelişkili, ölçülemeyen veya mevzuat açısından incelenmesi gereken ifadeleri kaynak metniyle birlikte gösterecek ve düzeltme taslağı önerecek.

## İlk pilot kapsamı

### Dahil

- İzmir Büyükşehir Belediyesi Sosyal Hizmetler Dairesi Başkanlığı
- Sosyal yardım ve sosyal hizmet alımı teknik şartnameleri
- Yemek, kumanya, aşevi ve sosyal tesis hizmetleri
- Yaşlı, engelli, kadın, çocuk ve diğer dezavantajlı gruplara yönelik hizmet sözleşmeleri
- Sosyal hizmetlerle ilişkili protokoller
- Kişisel veri ve özel nitelikli kişisel veri işlenen hizmetlere ilişkin maddeler
- Hizmet kalitesi, hijyen, teslimat, kabul, süreklilik ve veri iadesi hükümleri
- 4734/4735, hizmet alımı mevzuatı, KVKK ve kurum içi onaylı kaynaklar

### İlk aşamada kapsam dışı

- Yapım işleri
- Mal alımı
- Sağlık, ulaşım veya başka özel sektör mevzuatının derin analizi
- İhale sürecinin otomatik yürütülmesi
- EKAP'a otomatik belge yükleme veya EKAP üzerinde işlem yapma
- Otomatik hukuki onay
- Kullanıcı adına sözleşme veya şartnameyi otomatik değiştirme

## Kullanıcı rolleri

### Belge hazırlayan kullanıcı

Belgeyi yükler, alım bağlamını seçer, bulguları inceler ve düzeltme önerilerini taslak olarak kullanır.

### İhale/mevzuat uzmanı

Bulgunun ve mevzuat eşleştirmesinin doğruluğunu inceler; doğru, yanlış veya ek inceleme gerekli şeklinde işaretler.

### Teknik uzman

Teknik gereksinimlerin ölçülebilirliğini, test edilebilirliğini, hizmet seviyelerini ve kabul kriterlerini değerlendirir.

### Sistem yöneticisi

Kullanıcı, rol, mevzuat paketi, model, kota ve güvenlik ayarlarını yönetir. Belge içeriğine varsayılan olarak erişmez.

## Temel kullanım senaryoları

### US-01 — Yeni doküman ön incelemesi

1. Kullanıcı kurumsal giriş yapar.
2. Belge türünü ve alım bağlamını seçer.
3. PDF veya DOCX yükler.
4. Sistem uygulanabilir mevzuat paketini önerir.
5. Sistem bulguları kanıt, konum, kaynak ve öneriyle gösterir.
6. Kullanıcı raporu indirir.

### US-02 — Belirli bir maddenin düzeltilmesi

Kullanıcı bir bulguyu seçer ve sistemden yalnızca o maddenin daha açık, ölçülebilir ve uygulanabilir bir taslağını ister.

### US-03 — Mevzuat eşleştirmesinin incelenmesi

Uzman, bulgunun dayandığı mevzuat maddesini ve sistemin eşleştirme gerekçesini görür; eşleştirmeyi onaylar veya düzeltir.

### US-04 — Sürüm karşılaştırması

Kullanıcı aynı dokümanın iki sürümünü karşılaştırır ve önceki bulguların giderilip giderilmediğini kontrol eder.

### US-05 — Pilot geri bildirimi

Kullanıcı her bulgu için doğru/yanlış/kısmen doğru ve açıklama bilgisi girer. Bu geri bildirimler model ve kural kalitesini ölçmek için kullanılır.

## Her bulgunun zorunlu alanları

- Bulgu kimliği
- Kategori
- Doküman sayfası/bölümü
- Orijinal metin
- İlgili mevzuat veya kriter
- Mevzuat maddesi/bölümü
- Tespit
- Düzeltme önerisi
- Öncelik etiketi
- Güven düzeyi
- Uzman değerlendirme durumu

## Pilot daire başkanlığı ve seçim ölçütleri

- İzmir Büyükşehir Belediyesi Sosyal Hizmetler Dairesi Başkanlığı
- İlk alt birim; belge hacmi, uzman erişimi ve veri hassasiyetine göre ayrıca belirlenecek.

- Düzenli olarak teknik şartname veya sözleşme hazırlaması
- İnceleme sürecinde teknik ve ihale uzmanlarının birlikte bulunması
- Pilot sonuçlarını değerlendirecek sorumlu bir kişinin olması
- Anonimleştirilmiş örnek doküman sağlayabilmesi
- Kullanım öncesi bilgi güvenliği ve KVKK kurallarına uyabilmesi
- Başarı ölçümü için mevcut manuel inceleme sürecinin gözlemlenebilir olması

## KT-01 tamamlanma ölçütü

- İlk pilot belge türleri onaylanmış olmalı.
- Kullanıcı rolleri ve sorumlulukları belirlenmiş olmalı.
- Pilot daire başkanlığı belirlenmiş olmalı.
- İlk kullanım akışı ve kapsam dışı konular tanımlanmış olmalı.

Bu ölçütler karşılandı. EKAP örnek seti ve uzman doğrulama formu, KT-02/KT-05 kapsamında hazırlanacak.
