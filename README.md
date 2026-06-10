# 🛡️ PersonalSecurity-TR — Dijital Güvenlik Rehberi
"Translations (EN, RU etc.) are welcome! Feel free to fork and submit a Pull Request." (Çevirilere açığım, fork edip bana gönderebilirsiniz)
> Kişisel siber güvenliğini kendin yönet. Sade, uygulanabilir, Türkçe.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 👋 Bu Repo Ne İçin Var?

İnternette her gün milyonlarca insan farkında olmadan saldırıya uğruyor. Sahte bir e-posta bağlantısına tıklamak, zayıf bir parola kullanmak ya da telefona gelen "bankandan arıyorum" mesajına inanmak — bunların hepsi gerçek ve yaygın tehditler. Ama korunmak için siber güvenlik uzmanı olmana gerek yok.

Bu rehber **sıradan bir kullanıcı** için yazıldı. Teknik bilgin olmasa da olur. **Telefonundan da bilgisayarından da** adımların büyük çoğunluğunu uygulayabilirsin — her rehber hangi cihazda ne yapılacağını açıkça belirtiyor.

---

### 🔍 İçeride Ne Var?

**Kendi şifre üreticini yaz.**
`passwordGenerator.py` dosyasıyla hazır bir servise güvenmek zorunda değilsin. Python ile çalışan, kriptografik olarak güvenli, entropi skoru gösteren ve parolayı otomatik panonuza kopyalayan bir araç — tamamen senin bilgisayarında, hiçbir yere veri göndermeden.

**E-postanı ve hesaplarını kilitle.**
2FA nedir, nasıl kurulur, Passkey ne işe yarar, e-posta alias neden hayat kurtarır — bunların hepsini `mailProtect.md` içinde bulursun. Gmail, Outlook, ProtonMail için ayrı ayrı adımlar var.

**Cihazını sertleştir.**
`deviceHardening.md` telefon ve bilgisayar için disk şifreleme, tarayıcı eklentileri, parola yöneticisi kurulumu ve otomatik güncelleme ayarlarını anlatıyor. Bir kere yaparsın, yıllarca koruma sağlar.

**Oltalama (phishing) tuzaklarını tanı.**
Sahte bankacılık SMS'i, kurumsal görünümlü e-posta, "hesabın askıya alındı" tehdidi — `pishingBilgilendirme.md` bunların nasıl göründüğünü, nasıl anlaşıldığını ve tıkladıktan sonra ne yapman gerektiğini adım adım açıklıyor.

**Şantaj veya siber saldırıya uğrarsan ne yaparsın?**
`155_911.md` sadece acil numaraları değil, sosyal mühendislik saldırılarını, şantaj durumunda izlenecek yolu ve BTK / Emniyet Siber Suç birimine nasıl ihbarda bulunacağını da kapsıyor. Paniklemeden, sırayla ne yapman gerektiğini bilmek zaman kazandırır.

**Sosyal medya hesaplarını gizli tut.**
Instagram, Twitter/X, LinkedIn, Facebook, TikTok ve WhatsApp için Türkçe arayüz üzerinden adım adım gizlilik ayarları — `socialMediaPrivacy.md` ile varsayılan ayarların seni nasıl ifşa ettiğini ve nasıl düzelteceğini öğren.

**Çocuğunu internette koru.**
`parentalGuide.md` grooming, deepfake tehditler, siber zorbalık ve ebeveyn denetim araçlarını yaş gruplarına göre anlatıyor. "Çocuğumla bu konuyu nasıl konuşurum?" sorusuna da cevap var.

**Bilgilerin sızdı mı? Ne yapacaksın?**
`dataBreachResponse.md` ile haveibeenpwned çıktısını nasıl okuyacağını, hangi sızıntı türünün ne anlama geldiğini ve Türkiye'de kimlik hırsızlığına karşı hangi adımları atacağını öğren.

**Kafede veya havalimanında güvende kal.**
`publicWifi.md` ortak Wi-Fi'de gerçek riskleri abartmadan anlatıyor — evil twin saldırısı nedir, VPN olmadan minimum ne yapmalısın, hangi işlemleri ertele.

---

### 📱 Telefon mu, Bilgisayar mı?

Her iki cihazda da çalışan adımlar açıkça işaretlenmiştir. Python scriptini çalıştırmak için bilgisayar gerekirken, e-posta güvenliği, 2FA kurulumu, tarayıcı ayarları ve ihbar adımları tamamen telefondan da yapılabilir.

---

## 📋 İçindekiler

| # | Dosya | Konu |
|---|-------|------|
| 1 | [📧 mailProtect.md](mailProtect.md) | E-posta & hesap güvenliği |
| 2 | [🔑 passwordGenerator.py](passwordGenerator.py) | Güçlü parola üretici (script) |
| 3 | [📱 155_911.md](155_911.md) | Acil ihbar & sosyal mühendislik |
| 4 | [💻 deviceHardening.md](deviceHardening.md) | Cihaz sertleştirme & şifreleme |
| 5 | [🎣 pishingBilgilendirme.md](pishingBilgilendirme.md) | Oltalama saldırısı tanıma |
| 6 | [📲 socialMediaPrivacy.md](socialMediaPrivacy.md) | Sosyal medya gizlilik ayarları |
| 7 | [👨‍👩‍👧 parentalGuide.md](parentalGuide.md) | Ebeveyn rehberi & çocuk güvenliği |
| 8 | [🔓 dataBreachResponse.md](dataBreachResponse.md) | Veri sızıntısı sonrası eylem planı |
| 9 | [📶 publicWifi.md](publicWifi.md) | Ortak Wi-Fi güvenliği |

---

## ⚡ Hızlı Başlangıç

### 30 Dakikada Temel Koruma

```
✅ 1. Tüm önemli hesaplara 2FA ekle              → mailProtect.md
✅ 2. Parola yöneticisine geç                    → deviceHardening.md
✅ 3. Güçlü parola üret                          → passwordGenerator.py
✅ 4. Tarayıcını sertleştir                      → deviceHardening.md
✅ 5. Phishing tuzaklarını tanımayı öğren        → pishingBilgilendirme.md
✅ 6. Sosyal medya gizlilik ayarlarını düzenle   → socialMediaPrivacy.md
✅ 7. E-postanın sızdırılıp sızdırılmadığını kontrol et → dataBreachResponse.md
```

### Parola Üreticisini Çalıştır
Python dilini kullanarak oluşturulan bu şifre üreticisinde bizim için gerekli olan Mobilde Çalışacak Python derleyicisidir bu sebeple önce indirme adımına geçelim.
Mobilde Uygulama Mağazana gir ve arama kısmına "Pydroid 3 - IDE for Python 3" indir kurulumu tamamladıktan sonrasında [🔑 passwordGenerator.py](passwordGenerator.py) ilerle. Kodu kopyala. indirdiğin "Pydroid 3" uygulamasının içerisine yapıştır ve kodu çalıştır. Başarılı Şifreniz üretildi.

```bash
# Kurulum (opsiyonel — pano kopyalama için)
pip install pyperclip

# Tek parola (varsayılan 20 karakter)
python passwordGenerator.py

# 5 adet 32 karakterli parola
python passwordGenerator.py -n 5 -l 32

# Sembolsüz, karıştırıcı karaktersiz
python passwordGenerator.py --no-symbols --no-ambiguous

# Tüm seçenekler
python passwordGenerator.py --help
```

---

## 🗂️ Dosya Açıklamaları

### 📧 mailProtect.md
E-posta hesabını korumanın adım adım rehberi: 2FA / Passkey kurulumu, e-posta alias kullanımı, piksel takipçi engelleme, oturum çerezi saldırıları ve kurtarma zinciri.

### 🔑 passwordGenerator.py
Kriptografik olarak güvenli parola üretici: her karakter grubundan minimum garanti, Shannon entropi skoru ve güç etiketi, otomatik pano kopyalama, tam CLI desteği.

> ÖNEMLİ: https://github.com/globaldefensive/PersonalSecurity-TR kaynağından indirdiğinizden emin olun, 3.kişilerin attığı programlara güvenmeyin

### 📱 155_911.md
Siber kriz protokolü: RAT/hack durumunda dakika dakika ne yapılır, hesap çalındıysa kurtarma adımları, şantaj ve tehdit mesajlarında eylem planı, BTK / Emniyet Siber Suç ihbar kılavuzu.

### 💻 deviceHardening.md
Cihaz ve tarayıcı güvenliği: Windows / macOS / Linux disk şifreleme, tarayıcı eklentileri, parola yöneticisi kurulumu, VPN & DNS şifreleme, Wi-Fi güvenliği.

### 🎣 pishingBilgilendirme.md
Oltalama saldırısı tanıma ve önleme: URL & e-posta adres analizi, spear phishing / smishing / vishing türleri, deepfake dolandırıcılıkları, gerçek dünya senaryolar.

### 📲 socialMediaPrivacy.md
Instagram, Twitter/X, LinkedIn, Facebook, TikTok ve WhatsApp için Türkçe arayüz menü yollarıyla adım adım gizlilik ayarları. Varsayılan ayarlar seni değil, platformu korur.

### 👨‍👩‍👧 parentalGuide.md
Yaş gruplarına göre online riskler, grooming sürecinin uyarı işaretleri, deepfake sextortion tehdidi, siber zorbalık türleri ve ebeveyn denetim araçları. Çocuğunla bu konuları nasıl konuşacağına dair somut rehber.

### 🔓 dataBreachResponse.md
Haveibeenpwned çıktısını anlama kılavuzu, sızıntı türüne göre öncelik sırası, Türkiye'de kimlik hırsızlığı kontrolü (e-Devlet, Findeks/KKB), credential stuffing nedir ve kalıcı koruma adımları.

### 📶 publicWifi.md
Ortak ağlarda gerçek risk analizi: evil twin, MITM, ARP spoofing saldırıları — abartısız anlatım. VPN seçimi, bağlanmadan önce cihaz ayarları, havalimanı/otel/kafe risk karşılaştırması.

---

## 🔬 Cihazın Hakkında Daha Fazlasını Öğrenmek İster misin?

Cihazının **arka planda hangi uygulamaların çalıştığını**, **internete nasıl çıktığını**, hangi sunuculara bağlandığını veya sisteminde beklenmedik bir aktivite olup olmadığını merak ediyorsan — bunlar için bu repoda genel bir araç sunmak yerine kişiye özel çözüm geliştirmeyi tercih ediyorum.

Her cihazın yapılandırması, işletim sistemi ve ağ ortamı farklıdır. Bu nedenle **ağ izleme ve süreç analizi konularında doğrudan benimle iletişime geçebilirsin** — durumuna göre ne yapman gerektiğini birlikte değerlendiririz.

> 📬 **İletişim:** GitHub üzerinden [issue aç](../../issues) veya profil sayfasındaki iletişim bilgilerini kullan.

---

## 🤝 Katkı

Rehbere katkıda bulunmak ister misin? → [CONTRIBUTING.md](CONTRIBUTING.md)

Hata buldun veya eksik gördün? [Issue aç](../../issues) veya PR gönder.

---

## 📄 Lisans

[MIT License](LICENSE) © 2025 globaldefensive

---

> ⚠️ **Not:** Bu rehber bilgilendirme amaçlıdır. Hukuki veya resmi güvenlik danışmanlığının yerini tutmaz.

---

## 🎭 "Hacker" Diye Korkulanların Gerçeği — Script Kiddie Nedir?

Sosyal medyada "seni hackliyorum", "sistemine girdim", "her şeyini biliyorum" diyen insanların büyük çoğunluğu **script kiddie** denen bir kategoriye girer. Ne olduğunu net anlatalım:

### Script Kiddie Kim?

Başkasının yazdığı hazır araçları, YouTube videolarından veya forumlardan kopyaladığı komutları çalıştıran, bunların arkasında ne olduğunu **hiç anlamayan** kişilerdir. Bunların büyük çoğunluğu:

- Kullandığı aracın kaynak kodunu okuyamaz
- Hedef sistemin nasıl çalıştığını bilmez
- Saldırı başarısız olduğunda ne yapacağını bilemez
- Tek "becerisi" bir komutu kopyalayıp yapıştırmaktır

Gerçek bir siber güvenlik uzmanının yıllarca çalışarak öğrendiği şeyleri "ben de yapıyorum" zanneder — yapmaz.

### Klasik Taktikleri ve Gerçeği

| Söyledikleri | Gerçekte Ne Olduğu |
|---|---|
| "IP'ni aldım, adresini biliyorum" | IP adresi zaten herkese açık bir bilgidir. Ev adresin değil, internet servis sağlayıcının sunucu lokasyonudur. |
| "Kamerana girdim, seni izliyorum" | Ekran görüntüsü sahte veya başkasından çalıntı. Gerçek bir erişim olsaydı bunu söylemezdi. |
| "Tüm şifrelerini ele geçirdim" | Eğer gerçekten ele geçirseydi sessiz kalır, kullanırdı. Bağırıyorsa yoktur. |
| "Dosyalarını sildim / şifreledim" | Büyük olasılıkla blöf. Gerçekse zaten olmuştur, paniklemek işe yaramaz. |
| "Şu kadar para öde yoksa..." | Klasik sosyal mühendislik. Korkutarak para almaya çalışır, çoğunun elinde hiçbir şey yoktur. |

### Neden Tehlikeli Sayılırlar?

Teknik bilgileri olmasa da **sosyal mühendislik** yapabilirler. Yani seni korkutarak, kandırarak veya manipüle ederek **kendin** bir şey yaptırabilirler. Asıl tehlike budur — yazılım değil, psikoloji.

Seni panikletirse kazanır. Sakin kalırsan, elinde genellikle hiçbir şey yoktur.

### Ne Yapmalısın?

- **Paniklememe.** Bağıran birinin elinde genellikle bir şey yoktur.
- **Yanıt verme.** Her yanıt onlara bilgi verir ve cesaretlendirir.
- **Ekran görüntüsü al**, sonra engelle.
- Gerçek bir tehdit söz konusuysa → [155_911.md](155_911.md) adımlarını uygula.
- Hesap güvenliğini şimdiden al → [mailProtect.md](mailProtect.md)

> 💬 Gerçek bir siber güvenlik uzmanı sana "seni hackliyorum" demez. Sessizce çalışır ya da hiç ilgilenmez. Bağıran script kiddie'dir.

---

> 📌 Aşağıdaki cezalar bilgi amaçlıdır. Güncel ve kesin bilgi için
> mevzuat.gov.tr veya bir hukuk danışmanına başvurun.

### ⚖️ Bunların Başına Ne Geliyor? — Yasal Yaptırımlar

Türkiye'de siber suçlar ve şantaj son derece ağır yaptırımlarla karşılanır. "Anonim" olduğunu sanan, VPN kullandığını düşünen, "beni bulamazlar" diyen çok kişi yakalanmış ve hayatı tamamen kararmıştır.
"Bu rehber bilgilendirme amaçlıdır. Hukuki veya resmi güvenlik danışmanlığının yerini tutmaz."

#### Türk Hukuku'nda İlgili Suçlar ve Cezalar

| Suç | Kanun Maddesi | Ceza |
|-----|--------------|------|
| Bilişim sistemine izinsiz girme | TCK 243 | 1–3 yıl hapis |
| Sistemi engelleme, bozma, veri yok etme | TCK 244 | 1–5 yıl hapis |
| Şantaj | TCK 107 | 1–3 yıl hapis (tehdidin niteliğine göre artabilir) |
| Tehdit | TCK 106 | 6 ay – 2 yıl hapis |
| Hakaret / kişilik haklarına saldırı | TCK 125–131 | 3 ay – 2 yıl hapis |
| Kişisel verileri ele geçirme/yayma | TCK 136 | 2–4 yıl hapis |
| Özel hayatın gizliliğini ihlal | TCK 134 | 1–3 yıl hapis |

Bu cezalar ertelenebilir olmaktan çıkıp fiili hapise dönüşebilir — özellikle mağdur şikayetçi olursa ve birden fazla suç bir arada işlenmişse.

#### "Anonim Kaldım, VPN Kullandım" Diyenlere

Bu düşünce tamamen yanlış. Dijital iz **her zaman** kalır:

- VPN şirketleri mahkeme kararıyla log teslim eder — Türkiye'deki veya AB/ABD'deki sağlayıcıların tamamı
- Sosyal medya platformları IP ve cihaz bilgisini savcılık talebiyle verir — Meta, Google, Discord, Telegram hepsi verir
- Kullandığı hazır araçların ağ trafiği kayıt altına alınır
- Ödeme aldıysa — kripto bile olsa — işlem zinciri izlenebilir
- Kendi çevresinden birine övündüyse ihbar zaten oradan gelir

Türk Emniyet Siber Suçlar Birimi bu tür vakaları rutin olarak çözüyor. Küçük görünen bir tehdit mesajı bile soruşturma başlatmaya yeter.

#### Yakalandıklarında Hayatlarına Ne Oluyor?

- **Adli sicil kaydı** — devlet memurluğu, güvenlik soruşturması gerektiren her iş, yurt dışı vize başvuruları kalıcı olarak etkilenir
- **Üniversite disiplin süreci** — çoğu henüz öğrencidir; okuldan uzaklaştırma veya ilişik kesme gündeme gelir
- **Tazminat davaları** — cezai davanın yanında mağdur ayrıca maddi ve manevi tazminat davası açabilir
- **Dijital cihazlara el koyma** — telefon, bilgisayar, tablet delil olarak alınır; dava süresince iade edilmez
- **Sosyal ve aile baskısı** — dava süreci aile, okul ve iş çevresine yansır

#### Özet

Hazır bir araç indirip çalıştırmak, birkaç tehdit mesajı atmak veya şantaj denemesi yapmak — bunların hiçbiri küçük suç denilip geçilmemelidir. **Her biri suç unsurudur.** Türk hukuku bu fiilleri açıkça tanımlamış ve mahkemeler bu davaları ciddiye almaktadır.

Bunu yapanlar genellikle kendilerini zeki sanır. Yakalandıklarında ise karşılarında beklemenin çok ötesinde kalıcı sonuçlar bulurlar.

> 🔵 Mağdursan: Ekran görüntüsünü al, yanıt verme, şikayetini yap → [155_911.md](155_911.md)
> 🔴 Bunu yapmayı düşünüyorsan: Yukarıdaki tabloyu tekrar oku. Kendini tutamıyorsan, illa "bir yerlere saldıracağım" diyorsan — o enerjiyi doğru yöne çevir. Güvenlik uzmanı olma yolunda ilerleyerek sektörde gerçekçi olarak var olan ve saygı duyulan kişi olabilirsin. 🙂
