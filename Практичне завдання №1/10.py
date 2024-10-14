import math

pekin = (39.9075000, 116.3972300)
kyiv = (50.4546600, 30.5238000)

lat1, lon1 = map(math.radians, pekin)
lat2, lon2 = map(math.radians, kyiv)

distance = 6371.032 * math.acos(math.sin(lat1) * math.sin(lat2) +
                                math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))

print(f"{distance:>10.3f} км")