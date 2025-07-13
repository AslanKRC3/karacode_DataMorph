import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

output_klasoru = os.path.join("output", "pro_paket")
if not os.path.exists(output_klasoru):
    os.makedirs(output_klasoru)
df = pd.read_csv("ornek_veri.csv")
df["Tarih"] = pd.to_datetime(df["Tarih"])
df["Ay"] = df["Tarih"].dt.to_period("M")
df["Gün"] = df["Tarih"].dt.day_name()
df["Saat"] = df["Tarih"].dt.hour

# Grafik 1 – Top 10 ürün
df.groupby("Ürün")["Tutar"].sum().sort_values(ascending=False).head(10).plot(
    kind="bar", color="skyblue", title="Top 10 Ürün"
)
plt.tight_layout()
plt.savefig(os.path.join(output_klasoru, "grafik1_top10_urun.png"))
plt.clf()

# Grafik 2 – Aylık satış trendi
df.groupby("Ay")["Tutar"].sum().plot(
    kind="line", marker="o", title="Aylık Satış Trendi", color="green"
)
plt.tight_layout()
plt.savefig(os.path.join(output_klasoru, "grafik2_aylik_satis.png"))
plt.clf()

# Grafik 3 – Günlük dağılım
gunler = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df.groupby("Gün")["Tutar"].sum().reindex(gunler).plot(
    kind="bar", title="Günlük Satış Dağılımı", color="orange"
)
plt.tight_layout()
plt.savefig(os.path.join(output_klasoru, "grafik3_gun_satis.png"))
plt.clf()

# Grafik 4 – Şehir satışları
df.groupby("Şehir")["Tutar"].sum().sort_values(ascending=False).head(10).plot(
    kind="barh", title="Şehir Satışları", color="coral"
)
plt.tight_layout()
plt.savefig(os.path.join(output_klasoru, "grafik4_sehir_satis.png"))
plt.clf()

# Grafik 5 – Ortalama ürün satışları
df.groupby("Ürün")["Tutar"].mean().sort_values(ascending=False).head(10).plot(
    kind="bar", title="Ürün Başına Ortalama Satış", color="purple"
)
plt.tight_layout()
plt.savefig(os.path.join(output_klasoru, "grafik5_urun_ortalama.png"))
plt.clf()

# Grafik 6 – Müşteri satışları
df.groupby("Müşteri")["Tutar"].sum().sort_values(ascending=False).head(10).plot(
    kind="bar", title="Top Müşteriler", color="teal"
)
plt.tight_layout()
plt.savefig(os.path.join(output_klasoru, "grafik6_musteri_satis.png"))
plt.clf()

# Grafik 7 – Isı haritası
pivot = df.pivot_table(index="Gün", columns="Saat", values="Tutar", aggfunc="sum")
sns.heatmap(pivot, cmap="YlGnBu")
plt.title("Zaman Bazlı Satış Yoğunluğu")
plt.tight_layout()
plt.savefig(os.path.join(output_klasoru, "grafik7_heatmap.png"))
plt.clf()

# Grafik 8 – Satış tutarı dağılımı
df["Tutar"].plot(kind="hist", bins=20, title="Satış Tutarı Dağılımı", color="gray")
plt.tight_layout()
plt.savefig(os.path.join(output_klasoru, "grafik8_tutar_histogram.png"))
plt.clf()

# Grafik 9 – Kategori (varsa)
if "Kategori" in df.columns:
    df.groupby("Kategori")["Tutar"].sum().plot(
        kind="pie", autopct="%1.1f%%", title="Kategori Satışları"
    )
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(os.path.join(output_klasoru, "grafik9_kategori_pie.png"))
    plt.clf()

# Grafik 10 – Müşteri ortalama
df.groupby("Müşteri")["Tutar"].mean().sort_values(ascending=False).head(10).plot(
    kind="bar", title="Müşteri Başına Ortalama Harcama", color="darkred"
)
plt.tight_layout()
plt.savefig(os.path.join(output_klasoru, "grafik10_musteri_ortalama.png"))
plt.clf()

# Öneriler
top_urun = df.groupby("Ürün")["Tutar"].sum().sort_values(ascending=False).idxmax()
zayif_gun = df.groupby("Gün")["Tutar"].sum().idxmin()
top_sehir = df.groupby("Şehir")["Tutar"].sum().sort_values(ascending=False).idxmax()

oneriler = f"""
📊 Otomatik Öneriler:
- En çok satan ürün: {top_urun} → Bu ürüne reklam yatırımı yapılmalı.
- En zayıf satış günü: {zayif_gun} → Bu gün için kampanya önerilir.
- En çok satış yapılan şehir: {top_sehir} → Bölgeye özel strateji planlanabilir.
"""

with open(os.path.join(output_klasoru, "pro_oneriler.txt"), "w", encoding="utf-8") as f:
    f.write(oneriler)

print("✅ PRO analiz tamamlandı. 10+ grafik ve öneriler output klasöründe.")

