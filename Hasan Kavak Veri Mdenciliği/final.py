import pandas as pd
import matplotlib.pyplot as plt

# 1. VERİLERİ OKUMA
# Sigara ve Kanser verilerini yüklüyoruz.
sigara_verisi = pd.read_csv("sigara_kullanim.csv")
kanser_verisi = pd.read_csv("kanser_oranlari.csv")

# 2. SİGARA VERİSİNİ DÜZENLEME
# Sigara içenleri (1) ve içmeyenleri (0) ayırıyoruz.
icenler = sigara_verisi[sigara_verisi["SMOKING"] == 1]
icmeyenler = sigara_verisi[sigara_verisi["SMOKING"] == 0]

# Sigara içenlerin ve içmeyenlerin hastalık oranını buluyoruz (Ortalama alarak).
# YES = 1 (Hasta), NO = 0 (Sağlıklı)
icen_risk_orani = icenler["PULMONARY_DISEASE"].apply(lambda x: 1 if x == "YES" else 0).mean() * 100
icmeyen_risk_orani = icmeyenler["PULMONARY_DISEASE"].apply(lambda x: 1 if x == "YES" else 0).mean() * 100

# 3. KANSER VERİSİNİ DÜZENLEME
# Kanser verisindeki tüm hastalara ve sadece kötü huylu (M) olanlara bakıyoruz.
tum_hastalar = len(kanser_verisi)
kotu_huylu_olanlar = len(kanser_verisi[kanser_verisi["diagnosis"] == "M"])

# Genel kanser riskini hesaplıyoruz
genel_kanser_riski = (kotu_huylu_olanlar / tum_hastalar) * 100

# 4. TABLOYU OLUŞTURMA
# Sonuçları grafik çizmek için tablo haline getiriyoruz.
veri_seti = {
    "Durum": ["Sigara İçenlerde\nHastalık Riski", "İçmeyenlerde\nHastalık Riski", "Genel Kanser\n(Kötü Huylu)"],
    "Yuzde_Oran": [icen_risk_orani, icmeyen_risk_orani, genel_kanser_riski]
}
ozet_tablo = pd.DataFrame(veri_seti)

# 5. GRAFİK ÇİZME
# Çerçeve ve eksen oluşturuyoruz.
cerceve, eksen = plt.subplots(figsize=(11, 6))

# Renkler: Riskli (Kırmızı), Güvenli (Yeşil), Nötr/Diğer (Turuncu)
renkler = ['red', 'green', 'orange']

# Grafiği çiziyoruz
eksen.bar(ozet_tablo["Durum"], ozet_tablo["Yuzde_Oran"], color=renkler, width=0.6)

# Başlık ve eksen ayarları
eksen.set_ylabel('Görülme Oranı (%)', fontsize=12)
eksen.set_title("Karşılaştırma: Sigara Kullanımı ve Genel Kanser Riski", fontsize=14, fontweight='bold')
eksen.grid(axis='y', linestyle='--', alpha=0.5)

# Grafiği göster
plt.show()