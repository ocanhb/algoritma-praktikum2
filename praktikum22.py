import math

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    a = math.sin(delta_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c

    return distance

print ("masukkan lintang dan bujur titik pertama")
lat1 = float(input("lintang : "))
lon1 = float(input("bujur : "))

print ("masukkan lintang dan bujur titik kedua")
lat2 = float(input("lintang : "))
lon2 = float(input("bujur : "))

jarak = haversine_distance(lat1, lon1, lat2, lon2)

print (f"jarak antara kedua titik tersebut adalah {jarak} kilometer")
