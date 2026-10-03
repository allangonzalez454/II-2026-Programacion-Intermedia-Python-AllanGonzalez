import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width', 120)

# =========================================================
# 1) CARGAR EL DATASET
# =========================================================
df = pd.read_csv('estudiantes.csv')

print("=" * 60)
print("1) CONTENIDO ORIGINAL DEL DATASET")
print("=" * 60)
print(df.to_string())
print("\nTipos de datos:")
print(df.dtypes)

# =========================================================
# 2) LIMPIAR LOS DATOS
# =========================================================

# --- 2.1 Quitar espacios sobrantes y eliminar duplicados ---
df.columns = df.columns.str.strip()
df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))

duplicados = df.duplicated().sum()
df = df.drop_duplicates().reset_index(drop=True)
print(f"\nRegistros duplicados eliminados: {duplicados}")

# --- 2.2 Corregir formato incorrecto (texto -> numero) ---
PALABRAS = {
    'dieciocho': 18, 'diecinueve': 19, 'veinte': 20, 'veintiuno': 21,
    'veintidos': 22, 'veintidós': 22, 'veintitres': 23, 'veintitrés': 23,
    'veinticuatro': 24, 'veinticinco': 25, 'veintiseis': 26, 'veintiséis': 26,
}

def a_numero(serie):
    s = serie.astype(str).str.strip().str.lower().replace(PALABRAS)
    s = s.str.replace(',', '.', regex=False)        # 1,75 -> 1.75
    return pd.to_numeric(s, errors='coerce')        # lo que no se pueda -> NaN

columnas_num = ['Edad', 'Estatura', 'Peso', 'HorasEstudio', 'Calificacion']
for col in columnas_num:
    df[col] = a_numero(df[col])

# --- 2.3 Datos evidentemente erroneos -> NaN ---
# Estatura: 199 en vez de 1.99 (se divide entre 100); luego se valida el rango
df.loc[df['Estatura'] > 3, 'Estatura'] = df['Estatura'] / 100

# AJUSTE estos rangos segun lo que vea en su archivo
df.loc[~df['Edad'].between(15, 80), 'Edad'] = pd.NA
df.loc[~df['Estatura'].between(1.0, 2.3), 'Estatura'] = pd.NA
df.loc[~df['Peso'].between(30, 250), 'Peso'] = pd.NA
df.loc[~df['HorasEstudio'].between(0, 100), 'HorasEstudio'] = pd.NA
df.loc[~df['Calificacion'].between(0, 100), 'Calificacion'] = pd.NA  # use 0-10 si esa es su escala

# --- 2.4 Identificar vacios y reemplazar con la media ---
print("\nValores vacios por columna (antes de reemplazar):")
print(df[columnas_num].isnull().sum())

for col in columnas_num:
    df[col] = df[col].astype(float)
    df[col] = df[col].fillna(round(df[col].mean(), 2))

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
print(df[['Edad', 'Peso', 'HorasEstudio', 'Calificacion']].mean().round(2))

# =========================================================
# 4) CORRELACIONES
# =========================================================
print("\n" + "=" * 60)
print("4) MATRIZ DE CORRELACION")
print("=" * 60)
corr = df[columnas_num].corr()
print(corr.round(2))

print("\nHorasEstudio vs Calificacion:", round(corr.loc['HorasEstudio', 'Calificacion'], 2))
print("Estatura vs Peso:            ", round(corr.loc['Estatura', 'Peso'], 2))

# =========================================================
# 5) GRAFICACION (lineas: Estatura y Peso)
# =========================================================
fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.plot(df.index, df['Estatura'], color='tab:blue', marker='o', label='Estatura (m)')
ax1.set_xlabel('Estudiante (indice)')
ax1.set_ylabel('Estatura (m)', color='tab:blue')

ax2 = ax1.twinx()   # segundo eje Y porque las escalas son muy distintas
ax2.plot(df.index, df['Peso'], color='tab:red', marker='s', label='Peso (kg)')
ax2.set_ylabel('Peso (kg)', color='tab:red')

plt.title('Estatura y Peso de los estudiantes')
fig.tight_layout()
plt.savefig('estatura_peso.png', dpi=150)
plt.show()
