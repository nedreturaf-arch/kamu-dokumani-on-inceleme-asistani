# İBB Kurumsal Yapay Zekâ Destekli İhale ve Sözleşme Ön İnceleme Sistemi

## Projenin amacı

İBB bünyesinde hazırlanan teknik şartname, idari şartname, sözleşme ve protokollerin; uygulanabilir mevzuat, kurum içi düzenlemeler ve seçilen kalite kriterleriyle karşılaştırılmasını sağlayan, kanıt temelli bir yapay zekâ destekli ön inceleme sistemi geliştirmek.

Sistem hukuki karar vermeyecek; uzmanların inceleme süresini kısaltacak, riskli veya eksik ifadeleri kaynak metinleriyle birlikte gösterecek ve düzeltme önerileri sunacaktır.

## Başlangıç kapsamı

- Sosyal yardım ve sosyal hizmet alımı teknik şartnameleri
- Sosyal hizmet alımı sözleşmeleri
- Aşevi, yemek ve kumanya hizmetleri
- Protokoller
- 4734 ve 4735 çekirdeği
- Hizmet alımı mevzuatı
- KVKK ve ilgili rehberler
- Bilgi güvenliği ve veri koruma hükümleri
- Kurum içi tip dokümanlar ve yönergeler

## Temel kararlar

- Sayısal uyum skoru ve ceza puanı kullanılmayacak.
- Her bulgu dokümandaki gerçek bir alıntıya ve konum bilgisine dayanacak.
- Her bulgu ilgili mevzuat/kriter kaynağıyla gösterilecek.
- Yapay zekâ önerisi insan onayı olmadan belgeye otomatik işlenmeyecek.
- Kullanıcıya doğrudan sağlayıcı API anahtarı dağıtılmayacak; merkezi erişim katmanı kullanılacak.
- Gerçek kamu belgeleri herkese açık Streamlit uygulamasında işlenmeyecek.

## Dosyalar

- [Kilometre Taşları](01_KILOMETRE_TASLARI.md)
- [Mimari ve Güvenlik](02_MIMARI_VE_GUVENLIK.md)
- [Yapay Zekâ Seçimi](03_YAPAY_ZEKA_SECIMI.md)
- [Mevzuat Kapsamı](04_MEVZUAT_KAPSAMI.md)
- [Değerlendirme ve Test Planı](05_TEST_VE_DEGERLENDIRME.md)
- [Karar ve Toplantı Günlüğü](06_KARAR_GUNLUGU.md)
- [KT-01 Kapsam ve Kullanıcı Senaryoları](07_KT01_KAPSAM_VE_KULLANICI_SENARYOLARI.md)
- [KT-02 Mevzuat Kaynak Envanteri](08_KT02_MEVZUAT_KAYNAK_ENVANTERI.md)
- [Yapılandırılmış Kaynak Kataloğu](09_KAYNAK_KATALOGU.yaml)
- [KT-03 Veri İşleme ve Güvenlik Planı](10_KT03_VERI_ISLEME_VE_GUVENLIK_PLANI.md)
- [Sosyal Hizmetler Mevzuat Paketleri](11_MEVZUAT_PAKETLERI.md)
- [Mevzuat Paket Yönlendirme Katmanı](legal_packages.py)
- [Teknik MVP uygulaması](app.py)
- [MVP bağımlılıkları](requirements.txt)

## Streamlit üzerinde çalıştırma

1. GitHub deposunu Streamlit Community Cloud'a bağlayın.
2. Repository olarak `nedreturaf-arch/kamu-dokumani-on-inceleme-asistani`, branch olarak `main`, dosya olarak `app.py` seçin.
3. Advanced settings içindeki Secrets alanına aşağıdaki bilgileri ekleyin:

```toml
GEMINI_API_KEY = "buraya-kurum-onayli-gelistirme-anahtari"
GEMINI_MODEL = "kurum-tarafindan-onaylanmis-model-adi"
```

Anahtarlar GitHub'a veya bu dosyaya yazılmamalıdır. Gerçek kurum içi ve kişisel veri içeren belgeler, kamuya açık Community Cloud uygulamasında kullanılmamalıdır.

## Güncelleme kuralı

Yeni bir kilometre taşı, mimari kararı, mevzuat paketi veya model seçimi kesinleştiğinde ilgili dosya güncellenecek. Kullanıcı özellikle not tutulmasını istemediği sürece geçici fikirler karar olarak kaydedilmeyecek.
