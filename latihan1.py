import pandas as pd

df = pd.read_csv(r"D:\algopratikum\algopratikum\modul12\Negara.csv")

print(df.columns)
print(df.head())

if 'Benua' in df.columns:
    mean = df.groupby('Benua').mean(numeric_only=True)
    std = df.groupby('Benua').std(numeric_only=True)

    print(mean)
    print(std)
else:
    print("Kolom 'Benua' tidak ditemukan.")
