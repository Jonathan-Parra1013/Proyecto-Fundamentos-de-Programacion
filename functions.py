import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from io import BytesIO
import base64


excel_path = os.path.join("data", "TABLAPREMIER.xlsx")


def obtener_equipos():
    """Lee la Hoja1 (equipos y logos)."""
    try:
        df = pd.read_excel(excel_path, sheet_name="Hoja1")
    except Exception as e:
        print(f"Error al leer Hoja1: {e}")
        return []

    if "EQUIPO" not in df.columns or "LOGO" not in df.columns:
        print("Error: Falta la columna EQUIPO o LOGO en Hoja1.")
        return []

    equipos = df["EQUIPO"].dropna().tolist()
    logos = df["LOGO"].fillna("default.png").tolist()

    return [{"nombre": e, "logo": l} for e, l in zip(equipos, logos)]


def obtener_jugadores_por_equipo(equipo):
   
    try:
        df = pd.read_excel(excel_path, sheet_name="Hoja2")
    except Exception as e:
        print(f"Error al leer Hoja2: {e}")
        return []

    if "EQUIPO" not in df.columns:
        print("Error: Falta la columna EQUIPO en Hoja2.")
        return []

    jugadores = df[df["EQUIPO"].str.strip().str.lower() == equipo.strip().lower()]
    return jugadores.to_dict(orient="records")


def obtener_datos_jugadores(nombres):
    try:
        df = pd.read_excel(excel_path, sheet_name="Hoja2")
    except Exception as e:
        print(f"Error al leer Hoja2: {e}")
        return pd.DataFrame()

    if "Nombre" not in df.columns:
        print("Error: Falta la columna Nombre en Hoja2.")
        return pd.DataFrame()

    df_filtrado = df[df["Nombre"].isin(nombres)]
    return df_filtrado


def generar_grafica_comparacion(df):
    columnas_comparables = ["Goles", "Asistencias", "Tiros a puerta", "Total de tiros", "Atajadas"]

    # Filtrar solo columnas numéricas presentes
    columnas_presentes = [col for col in columnas_comparables if col in df.columns]
    df_numerico = df[["Nombre"] + columnas_presentes]

    # Gráfico de barras
    plt.figure(figsize=(10, 6))
    df_numerico.set_index("Nombre").plot(kind="bar", ax=plt.gca())
    plt.title("Comparación de Rendimiento entre Jugadores", fontsize=14)
    plt.ylabel("Valor")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Convertir a imagen base64
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    grafica_base64 = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    return grafica_base64


def generar_mapa_calor(df):
    """Genera un mapa de calor con estadísticas de jugadores."""
    columnas_comparables = ["Goles", "Asistencias", "Tiros a puerta", "Total de tiros", "Atajadas"]
    columnas_presentes = [col for col in columnas_comparables if col in df.columns]
    df_matriz = df.set_index("Nombre")[columnas_presentes]

    plt.figure(figsize=(8, 5))
    sns.heatmap(df_matriz, annot=True, cmap="YlOrRd", linewidths=0.5)
    plt.title("Mapa de Calor de Rendimiento", fontsize=14)
    plt.tight_layout()

    # Convertir a imagen base64
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    mapa_base64 = base64.b64encode(buffer.getvalue()).decode()
    plt.close()

    return mapa_base64
