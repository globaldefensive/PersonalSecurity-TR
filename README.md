# 🛡️ PersonalSecurity-TR — Dijital Güvenlik Rehberi
"Translations (EN, RU etc.) are welcome! Feel free to fork and submit a Pull Request." (Çevirilere açığım, fork edip bana gönderebilirsiniz)
> Kişisel siber güvenliğini kendin yönet. Sade, uygulanabilir, Türkçe.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub Sponsor](https://img.shields.io/badge/Sponsor-GitHub_Sponsors-ff69b4.svg)](https://github.com/sponsors/globaldefensive)
[![Crypto Support](https://img.shields.io/badge/Support-USDT_(TRC20)-26a17b?style=flat&logo=tether&logoColor=white)](#-crypto-support-kripto-ile-destek)

---

## 👋 Bu Repo Ne İçin Var?

İnternette her gün milyonlarca insan farkında olmadan saldırıya uğruyor. Sahte bir e-posta bağlantısına tıklamak, zayıf bir parola kullanmak ya da telefona gelen "bankandan arıyorum" mesajına inanmak — bunların hepsi gerçek ve yaygın tehditler. Ama korunmak için siber güvenlik uzmanı olmana gerek yok.

Bu rehber **sıradan bir kullanıcı** için yazıldı. Teknik bilgin olmasa da olur. **Telefonundan da bilgisayarından da** adımların büyük çoğunluğunu uygulayabilirsin — her rehber hangi cihazda ne yapılacağını açıkça belirtiyor.

---

### 🔍 İçeride Ne Var?

🔑**Kendi şifre üreticini yaz.**

`passwordGenerator.py` dosyasıyla hazır bir servise güvenmek zorunda değilsin. Python ile çalışan, kriptografik olarak güvenli, entropi skoru gösteren ve parolayı otomatik panonuza kopyalayan bir araç — tamamen senin bilgisayarında, hiçbir yere veri göndermeden.

📧**E-postanı ve hesaplarını kilitle.**

2FA nedir, nasıl kurulur, Passkey ne işe yarar, e-posta alias neden hayat kurtarır — bunların hepsini `mailProtect.md` içinde bulursun. Gmail, Outlook, ProtonMail için ayrı ayrı adımlar var.

💻**Cihazını sertleştir.**

`deviceHardening.md` telefon ve bilgisayar için disk şifreleme, tarayıcı eklentileri, parola yöneticisi kurulumu ve otomatik güncelleme ayarlarını anlatıyor. Bir kere yaparsın, yıllarca koruma sağlar.

🎣**Oltalama (phishing) tuzaklarını tanı.**

Sahte bankacılık SMS'i, kurumsal görünümlü e-posta, "hesabın askıya alındı" tehdidi — `phishingBilgilendirme.md` bunların nasıl göründüğünü, nasıl anlaşıldığını ve tıkladıktan sonra ne yapman gerektiğini adım adım açıklıyor.

📲**Sosyal medya hesaplarını gizli tut.**

Instagram, Twitter/X, LinkedIn, Facebook, TikTok ve WhatsApp için Türkçe arayüz üzerinden adım adım gizlilik ayarları — `socialMediaPrivacy.md` ile varsayılan ayarların seni nasıl ifşa ettiğini ve nasıl düzelteceğini öğren.

🔓**Bilgilerin sızdı mı? Ne yapacaksın?**

`dataBreachResponse.md` ile haveibeenpwned çıktısını nasıl okuyacağını, hangi sızıntı türünün ne anlama geldiğini ve Türkiye'de kimlik hırsızlığına karşı hangi adımları atacağını öğren.

📶**Kafede veya havalimanında güvende kal.**

`publicWifi.md` ortak Wi-Fi'de gerçek riskleri abartmadan anlatıyor — evil twin saldırısı nedir, VPN olmadan minimum ne yapmalısın, hangi işlemleri ertele.

👨‍👩‍👧**Çocuğunu internette koru.**

`parentalGuide.md` grooming, deepfake tehditler, siber zorbalık ve ebeveyn denetim araçlarını yaş gruplarına göre anlatıyor. "Çocuğumla bu konuyu nasıl konuşurum?" sorusuna da cevap var.

🎭**Seni tehdit eden kişinin elinde gerçekte ne var?**

`socialEngineeringGercekleri.md` ile "seni hackliyorum" diyenlerin büyük çoğunluğunun neden boş tehdit olduğunu, klasik taktiklerini ve bunu yapanların Türk hukukunda ne tür cezalarla karşılaştığını öğren.

🚨**Şantaj veya siber saldırıya uğrarsan ne yaparsın? (Acil Durum)**

`155_911.md` sadece acil numaraları değil, şantaj durumunda izlenecek dakika dakika yol haritasını ve BTK / Emniyet Siber Suç birimine nasıl ihbarda bulunacağını da kapsıyor. Paniklemeden, sırayla ne yapman gerektiğini bilmek zaman kazandırır.

---

### 📱 Telefon mu, Bilgisayar mı?

Her iki cihazda da çalışan adımlar açıkça işaretlenmiştir. Python scriptini çalıştırmak için bilgisayar gerekirken (telefon için olan adımlar da aşağıda anlatıldı), e-posta güvenliği, 2FA kurulumu, tarayıcı ayarları ve ihbar adımları tamamen telefondan da yapılabilir.

---

## 📋 İçindekiler - Tıkla Ulaş

### Önleyici Rehberler — Sırasıyla Uygula

| # | Dosya | Konu |
|---|-------|------|
| 1 | [🔑 passwordGenerator.py](passwordGenerator.py) | Güçlü parola üretici (script) |
| 2 | [📧 mailProtect.md](mailProtect.md) | E-posta & hesap güvenliği |
| 3 | [💻 deviceHardening.md](deviceHardening.md) | Cihaz sertleştirme & şifreleme |
| 4 | [🎣 phishingBilgilendirme.md](phishingBilgilendirme.md) | Oltalama saldırısı tanıma |
| 5 | [📲 socialMediaPrivacy.md](socialMediaPrivacy.md) | Sosyal medya gizlilik ayarları |
| 6 | [🔓 dataBreachResponse.md](dataBreachResponse.md) | Veri sızıntısı sonrası eylem planı |
| 7 | [📶 publicWifi.md](publicWifi.md) | Ortak Wi-Fi güvenliği |
| 8 | [👨‍👩‍👧 parentalGuide.md](parentalGuide.md) | Ebeveyn rehberi & çocuk güvenliği |

### Bilgi & Kriz Anı Rehberleri

| # | Dosya | Konu |
|---|-------|------|
| 9 | [🎭 socialEngineeringGercekleri.md](socialEngineeringGercekleri.md) | "Hacker" tehditleri, gerçekler ve yasal yaptırımlar |
| 10 | [🚨 155_911.md](155_911.md) | Acil durum protokolü: hack, hesap çalınması, şantaj |

---

## 🗂️ İçindekiler Rehber Kısa Özet Açıklamaları

### 🔑 [passwordGenerator.py](passwordGenerator.py)
Kriptografik olarak güvenli parola üretici: Her karakter grubundan minimum garanti, Shannon entropi skoru ve güç etiketi, otomatik pano kopyalama, tam CLI desteği.

> ⚠️ **ÖNEMLİ:** Kodu sadece [https://github.com/globaldefensive/PersonalSecurity-TR](https://github.com/globaldefensive/PersonalSecurity-TR) kaynağından indirdiğinizden emin olun. Üçüncü kişilerin dağıttığı veya attığı programlara asla güvenmeyin.

### 📧 [mailProtect.md](mailProtect.md)
E-posta hesabını korumanın adım adım rehberi: 2FA / Passkey kurulumu, e-posta alias kullanımı, piksel takipçi engelleme, oturum çerezi saldırıları ve kurtarma zinciri.

### 💻 [deviceHardening.md](deviceHardening.md)
Cihaz ve tarayıcı güvenliği: Windows / macOS / Linux disk şifreleme, tarayıcı eklentileri, parola yöneticisi kurulumu, VPN & DNS şifreleme, Wi-Fi güvenliği.

### 🎣 [phishingBilgilendirme.md](phishingBilgilendirme.md)
Oltalama saldırısı tanıma ve önleme: URL & e-posta adres analizi, spear phishing / smishing / vishing türleri, deepfake dolandırıcılıkları, gerçek dünya senaryoları.

### 📲 [socialMediaPrivacy.md](socialMediaPrivacy.md)
Instagram, Twitter/X, LinkedIn, Facebook, TikTok ve WhatsApp için Türkçe arayüz menü yollarıyla adım adım gizlilik ayarları. Varsayılan ayarlar seni değil, platformu korur.

### 🔓 [dataBreachResponse.md](dataBreachResponse.md)
Haveibeenpwned çıktısını anlama kılavuzu, sızıntı türüne göre öncelik sırası, Türkiye'de kimlik hırsızlığı kontrolü (e-Devlet, Findeks/KKB), credential stuffing nedir ve kalıcı koruma adımları.

### 📶 [publicWifi.md](publicWifi.md)
Ortak ağlarda gerçek risk analizi: Evil twin, MITM, ARP spoofing saldırıları — abartısız anlatım. VPN seçimi, bağlanmadan önce cihaz ayarları, havalimanı/otel/kafe risk karşılaştırması.

### 👨‍👩‍👧 [parentalGuide.md](parentalGuide.md)
Yaş gruplarına göre online riskler, grooming sürecinin uyarı işaretleri, deepfake sextortion tehdidi, siber zorbalık türleri ve ebeveyn denetim araçları. Çocuğunla bu konuları nasıl konuşacağına dair somut rehber.

### 🎭 [socialEngineeringGercekleri.md](socialEngineeringGercekleri.md)
"Seni hackliyorum" diyenlerin büyük çoğunluğunun "script kiddie" olduğunu, klasik taktiklerinin (IP tehdidi, kamera erişimi vb.) gerçekte neye karşılık geldiğini ve Türk hukukunda bu fiillerin (TCK 106, 107, 134, 136, 243, 244) hangi cezalarla karşılandığını anlatır. Yakalanma sonrası gerçek hayata etkileri.

### 🚨 [155_911.md](155_911.md)
Siber kriz protokolü: RAT/hack durumunda dakika dakika ne yapılır, hesap çalındıysa kurtarma adımları, şantaj ve tehdit mesajlarında eylem planı, BTK / Emniyet Siber Suç ihbar kılavuzu.

---

## ⚡ Hızlı Başlangıç - Sırasıyla Adımları Uygulamaya Başla

### 30 Dakikada Temel Koruma

```text
✅ 1. Güçlü parola üret                          → passwordGenerator.py
✅ 2. Parola yöneticisine geç                    → deviceHardening.md
✅ 3. Tüm önemli hesaplara 2FA ekle              → mailProtect.md
✅ 4. Tarayıcını sertleştir                      → deviceHardening.md
✅ 5. Phishing tuzaklarını tanımayı öğren        → phishingBilgilendirme.md
✅ 6. Sosyal medya gizlilik ayarlarını düzenle   → socialMediaPrivacy.md
✅ 7. E-postanın sızdırılıp sızdırılmadığını kontrol et → dataBreachResponse.md
```

> 📌 Yukarıdaki sıra "önce araçları edin, sonra hesapları kilitle, sonra farkındalık kazan" mantığıyla ilerler. `publicWifi.md`, `parentalGuide.md`, `socialEngineeringGercekleri.md` ve `155_911.md` durumsal rehberlerdir — ihtiyaç anında veya zaman bulduğunda okunabilir.

### Şimdi Güçlü Parolayı Üretelim - Parola Üreticisini Çalıştır

### 🔑 `passwordGenerator.py` İndirme tamamlandıktan sonra yapmanız gerekenler:

```
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

### 🔑 `passwordGenerator.py` İndirmek İstemiyorsanız Yapmanız Gerekenler:

Python dilini kullanarak oluşturulan bu şifre üreticisinde bizim için gerekli olan mobilde çalışacak bir Python derleyicisidir. Bu sebeple önce uygulamayı indirme adımına geçelim:

1. Mobil cihazınız **Apple (iOS)** ise **App Store**, diğer modeller (**Android**) için **Play Store** uygulama mağazanıza girin.
2. Arama kısmına **"Pydroid 3 - IDE for Python 3"** yazın ve indirin.
3. Kurulumu tamamladıktan sonra [🔑 passwordGenerator.py](passwordGenerator.py) dosyasına ilerleyin ve içindeki **kodu kopyalayın**.
4. İndirdiğiniz "Pydroid 3" uygulamasının içerisine bu kodu yapıştırın ve çalıştırın.

🎉 *Başarılı! Şifreniz tamamen yerel olarak üretildi.*

---

## 🚨 Acil Bir Durumla mı Karşı Karşıyasın?

Eğer şu anda hacklendiğini düşünüyorsan, hesabın çalındıysa veya birisi seni şantajla tehdit ediyorsa — yukarıdaki adımları okumayı bırak ve doğrudan şuraya git:

> 🚨 **[155_911.md](155_911.md)** — Dakika dakika acil durum protokolü

Tehdit eden kişinin elinde gerçekte ne olduğunu anlamak için → [socialEngineeringGercekleri.md](socialEngineeringGercekleri.md)

---

## 🔬 Cihazın Hakkında Daha Fazlasını Öğrenmek İster misin?

Cihazının **arka planda hangi uygulamaların çalıştığını**, **internete nasıl çıktığını**, hangi sunuculara bağlandığını veya sisteminde beklenmedik bir aktivite olup olmadığını merak ediyorsan — bunlar için bu repoda genel bir araç sunmak yerine kişiye özel çözüm geliştirmeyi tercih ediyorum.

Her cihazın yapılandırması, işletim sistemi ve ağ ortamı farklıdır. Bu nedenle **ağ izleme ve süreç analizi konularında doğrudan benimle iletişime geçebilirsin** — durumuna göre ne yapman gerektiğini birlikte değerlendiririz.

> 📬 **İletişim:** Detaylar **Online Çözümler ve Benimle İletişim** bölümünde yer almaktadır.

---

## 🌐 Online Çözümler ve Benimle İletişim

Kendi dijital güvenliğinizi sağlamak ve dijital hayatınızı kontrol altında tutabilmek adına aşağıdaki kanallardan benimle iletişime geçebilirsiniz:

*   **🛡️ Standart Destek (Ücretsiz):** Bu rehberdeki konularla ilgili bir sorunuz, takıldığınız bir adım veya teknik bir hata varsa GitHub üzerinden bir [Issue (Sorun)](../../issues) açabilirsiniz. Topluluk kuralları çerçevesinde, müsaitlik durumuma göre sorularınızı yanıtlamaktan memnuniyet duyarım.
*   **💎 Kişiye Özel Premium Danışmanlık (Ücretli Ek Paket):** Rehberin ötesine geçmek, kendi cihazlarınız (telefon/bilgisayar) ve dijital hesaplarınız için **birebir, size özel bir sertleştirme ve rutin kontrol planı** oluşturmak isterseniz benimle doğrudan iletişime geçebilirsiniz.
*   Bu ek paket kapsamında:
    *   Cihazlarınızın ve ağ trafiğinizin analizi,
    *   Kişisel tehdit modelinizin çıkarılması,
    *   Periyodik dijital güvenlik Check-Up'ları, rutin kontrolleri ve ek olarak size özel çözümler
    *   Danışmanlık sırasında gizliliğiniz yüksek öncelikli olarak yürütülür.

> 📬 **İletişim & Destek:** Birebir premium danışmanlık talepleri, iş birlikleri ve özel sorularınız için gizlilik odaklı **globaldefensive@proton.me** adresinden bana ulaşabilir veya projeyi [GitHub Sponsors](https://github.com/sponsors/globaldefensive) üzerinden ya da aşağıdaki kripto adresi üzerinden destekleyebilirsiniz.

---

## 🪙 Crypto Support (Kripto İle Ödeme&Destek)

Bu rehberin bağımsız kalmasını desteklemek, küresel ve sansürsüz bir şekilde bağışta bulunmak isterseniz aşağıdaki **USDT** adresini kullanabilirsiniz. Blockchain ağının doğası gereği yapacağınız destekler tamamen güvenli ve taraflar arası gizlilik prensibine uygundur:

*   **Coin:** USDT (Tether)
*   **Network (Ağ):** Tron (TRC20)  `<- Farklı bir ağdan gönderim yapmayınız.`
*   **Deposit Address:** `TDBvJvWGYsTUVpWPRPechbWRfVjZDcgCoi`

---

## 🤝 Katkı

Rehbere katkıda bulunmak ister misin? → [CONTRIBUTING.md](CONTRIBUTING.md)

Hata buldun veya eksik gördün? [Issue aç](../../issues) veya PR gönder.

---

## 📄 Lisans

[MIT License](LICENSE) © 2025 globaldefensive

> ⚠️ **Not:** Bu rehber bilgilendirme amaçlıdır. Hukuki veya resmi güvenlik danışmanlığının yerini tutmaz.
