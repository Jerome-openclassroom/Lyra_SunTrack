
import math

def calcul_15deg_km(lat_deg, lon_deg):
    """
    Calcule la longueur en km de 15° en longitude et 15° en latitude
    pour une position donnée sur le disque de Stonyhurst.

    :param lat_deg: Latitude solaire (°)
    :param lon_deg: Longitude solaire (°)
    :return: Tuple (distance_lat_km, distance_lon_km)
    """
    R = 696_000  # rayon moyen du Soleil en km

    # 15 degrés en radians
    delta_angle_rad = math.radians(15)

    # Distance latitudinale (le long d'un méridien) : simple arc de cercle
    d_lat_km = R * delta_angle_rad

    # Distance longitudinale (le long d'un parallèle) : dépend de la latitude
    # Attention : longitude géographique => angle de parallèle = latitude
    d_lon_km = R * math.cos(math.radians(lat_deg)) * delta_angle_rad

    return d_lat_km, d_lon_km

# Exemple d'utilisation :
if __name__ == "__main__":
    latitude = float(input("Entrez la latitude (en degrés) : "))
    longitude = float(input("Entrez la longitude (en degrés) : "))

    d_lat, d_lon = calcul_15deg_km(latitude, longitude)

    print(f"\nPour la position Lat: {latitude}°, Lon: {longitude}° :")
    print(f"15° en latitude = {d_lat:.1f} km")
    print(f"15° en longitude = {d_lon:.1f} km")
