import pandas as pd
import matplotlib.pyplot as plt
import os

output_klasoru = os.path.join("output", "standart_paket")
if not os.path.exists(output_klasoru):
    os.makedirs(output_klasoru)

df = pd.read_csv("ornek_veri.csv")
df["Tarih"] = pd.to_datetime(df["Tarih"])
df["Ay"] = df["Tarih"].dt.to_period("M")
df["Gün"] = df["Tarih"].dt.day_name()

# Grafikler
df.groupby("Ürün")["Tutar"].sum().sort_values(ascending=False).head(10).plot(
    kind="bar", title="Top 10 Ürün", color="dodgerblue"
)
plt.tight_layout()
plt.savefig(os.path.join(output_klasoru, "std_top10_urun.png"))
plt.clf()

df.groupby("Ay")["Tutar"].sum().plot(
    kind="line", marker="o", color="darkgreen", title="Aylık Satış Trendi"
)
plt.tight_layout()
plt.savefig(os.path.join(output_klasoru, "std_aylik_trend.png"))
plt.clf()

gunler = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df.groupby("Gün")["Tutar"].sum().reindex(gunler).plot(
    kind="bar", title="Günlük Satış", color="orange"
)
plt.tight_layout()
plt.savefig(os.path.join(output_klasoru, "std_gunluk_satis.png"))
plt.clf()

df.groupby("Şehir")["Tutar"].sum().sort_values(ascending=False).head(10).plot(
    kind="barh", title="Şehirlere Göre Satış", color="salmon"
)
plt.tight_layout()
plt.savefig(os.path.join(output_klasoru, "std_sehirler.png"))
plt.clf()

df.groupby("Müşteri")["Tutar"].sum().sort_values(ascending=False).head(10).plot(
    kind="bar", title="Top Müşteriler", color="mediumpurple"
)
plt.tight_layout()
plt.savefig(os.path.join(output_klasoru, "std_musteri_satis.png"))
plt.clf()

# Öneri
top_urun = df.groupby("Ürün")["Tutar"].sum().sort_values(ascending=False).idxmax()
en_zayif_gun = df.groupby("Gün")["Tutar"].sum().idxmin()

with open(os.path.join(output_klasoru, "std_kisa_oneri.txt"), "w", encoding="utf-8") as f:
    f.write(f"Top Ürün: {top_urun} - Bu ürün öne çıkarılmalı.\n")
    f.write(f"En düşük satış günü: {en_zayif_gun} - Bu gün için kampanya yapılabilir.\n")

print("✅ Standart analiz tamamlandı. 5 grafik ve öneri dosyası output klasöründe.")
