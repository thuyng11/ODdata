import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Example data (the actual data should be loaded from your dataset)
data = [
    {"COUNTRY_CODE": "FR", "DATE": "2022-09-07", "VEH_SEGMT": "VAN", "START_COUNTY": "Lot-et-Garonne", "END_COUNTY": "Dordogne", "VEHICLE_COUNT": 5, "TRIP_COUNT": 6, "SUM_DISTANCE": 354.04, "DURATION": 274},
    {"COUNTRY_CODE": "FR", "DATE": "2022-09-05", "VEH_SEGMT": "TRUCK", "START_COUNTY": "Ille-et-Vilaine", "END_COUNTY": "Manche", "VEHICLE_COUNT": 15, "TRIP_COUNT": 16, "SUM_DISTANCE": 1802.16, "DURATION": 950},
    # Add more data as necessary
]

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Example coordinates for counties (in actual application, use geocoding to determine these)
county_coords = {
    "Lot-et-Garonne": (44.3667, 0.4667),
    "Dordogne": (45.1833, 0.7167),
    "Ille-et-Vilaine": (48.1667, -1.5833),
    "Manche": (49.0333, -1.3333),
}

# Map county names to coordinates
df['start_coords'] = df['START_COUNTY'].map(county_coords)
df['end_coords'] = df['END_COUNTY'].map(county_coords)

# Create a base map
map = folium.Map(location=[46.2276, 2.2137], zoom_start=6)

# Add lines and markers for each trip
for idx, row in df.iterrows():
    folium.PolyLine(locations=[row['start_coords'], row['end_coords']], weight=1, color='blue').add_to(map)
    folium.Marker(row['start_coords'], popup=f"{row['START_COUNTY']} (Start)").add_to(map)
    folium.Marker(row['end_coords'], popup=f"{row['END_COUNTY']} (End)").add_to(map)

# Save the map to an HTML file
map.save('Origin_Destination_Map.html')
