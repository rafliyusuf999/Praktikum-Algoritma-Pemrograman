import pandas as pd

df = pd.read_csv(r"D:\algopratikum\algopratikum\modul12\Negara.csv")

df.columns = df.columns.str.strip()
print("Nama kolom yang tersedia:")
print(df.columns)
if 'Benua' in df.columns:
    mean = df.groupby('Benua').mean(numeric_only=True)
    std = df.groupby('Benua').std(numeric_only=True)

    print("\nBerikut DataFrame nya:")
    print(df)

    print("\nBerikut Mean Benua nya:")
    print(mean)

    print("\nBerikut Standar Deviasi nya:")
    print(std)

    mean.to_csv("NegaraMean.csv", index=True)
    std.to_csv("NegaraStandarDeviasi.csv", index=True)

    print("\nFile CSV berhasil dibuat!")
else:
    print("\nKolom 'Benua' tidak ditemukan dalam DataFrame.")
