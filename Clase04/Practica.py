import pandas as pd
import matplotlib.pyplot as plt
# use a non-interactive backend suitable for scripts/environments without a display
plt.switch_backend('Agg')

pd.set_option('display.width', 120)

# =========================================================
# 1) CARGAR EL DATASET
# =========================================================
df = pd.read_csv('estudiantes.csv')

print("=" * 60)
print("1) CONTENIDO ORIGINAL DEL DATASET")
print("=" * 60)
print(df.to_string())
print("\nInfo:")
print(df.dtypes)

# =========================================================
# 2) LIMPIAR LOS DATOS
# =========================================================

# --- 2.1 Eliminar registros duplicados ---
duplicados = df.duplicated().sum()
df = df.drop_duplicates()
print(f"\nRegistros duplicados eliminados: {duplicados}")

# --- 2.2 Corregir formato incorrecto ---
# La columna Edad debe ser numerica; "veintidos" esta en formato incorrecto (texto)
df['Edad'] = df['Edad'].replace('veintidós', 22)
df['Edad'] = pd.to_numeric(df['Edad'])

# --- 2.3 Corregir datos evidentemente erroneos ---
# Una edad de 150 anios es imposible para un estudiante: es un dato erroneo
# (similar al ejemplo "199" en vez de "1,99"). Se marca como vacio para
# poder corregirlo con la media de la columna, igual que las celdas vacias.
df.loc[df['Edad'] > 100, 'Edad'] = pd.NA
df['Edad'] = pd.to_numeric(df['Edad'])

# --- 2.4 Identificar valores vacios y reemplazarlos con la media ---
print("\nValores vacios por columna (antes de reemplazar):")
print(df.isnull().sum())

for col in ['Edad', 'Estatura', 'Peso', 'HorasEstudio']:
    media_col = df[col].mean()
    df[col] = df[col].fillna(round(media_col, 2))

print("\n" + "=" * 60)
print("2) DATASET LIMPIO")
print("=" * 60)
print(df.to_string())

# =========================================================
# 3) ANALIZAR LOS DATOS
# =========================================================
print("\n" + "=" * 60)
print("3) PROMEDIOS")
print("=" * 60)
promedios = df[['Edad', 'Peso', 'HorasEstudio', 'Calificacion']].mean()
print(promedios.round(2))

# =========================================================
# 4) CALCULAR CORRELACIONES
# =========================================================
print("\n" + "=" * 60)
print("4) MATRIZ DE CORRELACION")
print("=" * 60)
corr = df.corr(numeric_only=True)
print(corr.round(2))

print("\nHorasEstudio vs Calificacion:", round(corr.loc['HorasEstudio', 'Calificacion'], 2))
print("Estatura vs Peso:            ", round(corr.loc['Estatura', 'Peso'], 2))

