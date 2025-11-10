class Jugador:
    def __init__(self, datos):
        self.nombre = datos.get('Nombre', '')
        self.equipo = datos.get('EQUIPO', '')
        self.edad = datos.get('Edad', 0)
        self.ta = datos.get('TA', 0)
        self.tr = datos.get('TR', 0)
        self.asistencias = datos.get('Asistencias', 0)
        self.tiros_puerta = datos.get('Tiros a puerta', 0)
        self.total_tiros = datos.get('Total de tiros', 0)
        self.total_goles = datos.get('Total de goles', 0)
        self.goles = datos.get('Goles', 0)
        self.atajadas = datos.get('Atajadas', 0)
    
    def calcular_efectividad_tiros(self):
        """Calcula el porcentaje de efectividad en tiros a puerta"""
        if self.total_tiros == 0:
            return 0
        return (self.tiros_puerta / self.total_tiros) * 100
    
    def calcular_efectividad_goles(self):
        """Calcula el porcentaje de efectividad en goles"""
        if self.tiros_puerta == 0:
            return 0
        return (self.goles / self.tiros_puerta) * 100
    
    def obtener_estadisticas(self):
        """Retorna un diccionario con todas las estadísticas calculadas"""
        return {
            'Nombre': self.nombre,
            'Equipo': self.equipo,
            'Edad': self.edad,
            'Tarjetas Amarillas': self.ta,
            'Tarjetas Rojas': self.tr,
            'Asistencias': self.asistencias,
            'Tiros a Puerta': self.tiros_puerta,
            'Total de Tiros': self.total_tiros,
            'Efectividad Tiros (%)': round(self.calcular_efectividad_tiros(), 2),
            'Goles': self.goles,
            'Efectividad Goles (%)': round(self.calcular_efectividad_goles(), 2),
            'Atajadas': self.atajadas
        }