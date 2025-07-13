import pandas as pd
import matplotlib.pyplot as plt
import os

# Output klasörü oluştur
paket_klasoru = os.path.join("output", "temel_paket")
if not os.path.exists(paket_klasoru):
    os.makedirs(paket_klasoru)

# Veri oku
df = pd.read_csv("ornek_veri.csv")
df["Tarih"] = pd.to_datetime(df["Tarih"])
df["Ay"] = df["Tarih"].dt.to_period("M")

# Grafik 1 – En çok satan 5 ürün
df.groupby("Ürün")["Tutar"].sum().sort_values(ascending=False).head(5).plot(
    kind="barh", color="skyblue", title="Top 5 Ürün"
)
plt.tight_layout()
plt.savefig(os.path.join(paket_klasoru, "top5_urun.png"))
plt.clf()

# Grafik 2 – Aylık satış trendi
df.groupby("Ay")["Tutar"].sum().plot(
    kind="line", marker="o", color="green", title="Aylık Satış Trendi"
)
plt.tight_layout()
plt.savefig(os.path.join(paket_klasoru, "aylik_trend.png"))
plt.clf()

print("✅ Temel analiz tamamlandı. Grafikler 'output' klasörüne kaydedildi.")
