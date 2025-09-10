import math
from supabase import create_client, Client

# Set your Supabase credentials
SUPABASE_URL = 'https://sngznbesdrkksldtwmvw.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNuZ3puYmVzZHJra3NsZHR3bXZ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTc0NzU2ODYsImV4cCI6MjA3MzA1MTY4Nn0.mGwIjcdTUiI73Vn_MxiEn3ngWXEOvsNvlOWiK-ukbWc'
TABLE_NAME = 'location_table'

# Earth's radius in kilometers
R = 6378.1

def bounding_box(lat, lon, area_ha):
    # Convert area: hectare to km^2
    area_km2 = area_ha * 0.01
    half_side_km = math.sqrt(area_km2) / 2

    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    rad_dist = half_side_km / R

    min_lat = lat_rad - rad_dist
    max_lat = lat_rad + rad_dist

    delta_lon = math.asin(math.sin(rad_dist) / math.cos(lat_rad))
    min_lon = lon_rad - delta_lon
    max_lon = lon_rad + delta_lon

    # Convert back to degrees
    return (
        math.degrees(min_lat), math.degrees(max_lat),
        math.degrees(min_lon), math.degrees(max_lon)
    )

# Connect to Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Fetch all rows (customize as needed for larger tables)
rows = supabase.table(TABLE_NAME).select("*").execute().data

for row in rows:
    lat = row['lat']
    lon = row['lon']
    area = row['area']  # Area in hectares

    min_lat, max_lat, min_lon, max_lon = bounding_box(lat, lon, area)

    # Update the row in Supabase (assuming primary key 'id')
    supabase.table(TABLE_NAME).update({
        'min_lat': min_lat,
        'max_lat': max_lat,
        'min_lon': min_lon,
        'max_lon': max_lon
    }).eq('id', row['id']).execute()
