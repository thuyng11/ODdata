import requests
import pandas as pd

# Define the API key and endpoint
api_key = 'AIzaSyDxTFxprFZHa80HJ8rcRAj8oN0BF8szLLs'  # Replace with your actual API key
directions_endpoint = 'https://maps.googleapis.com/maps/api/directions/json'

# Define the OD pairs as tuples of (start_lat, start_lng, end_lat, end_lng)
od_pairs = [
    (33.943007030415195, -118.40369108793467, 33.67543656602603, -117.86889893466338), #LAX to John Wayne Airport
    (33.943007030415195, -118.40369108793467, 32.734175981327624, -117.18970367329247), # LAX to San Diego International Airport
    (33.943007030415195, -118.40369108793467, 34.01988581745, -118.44723181081041), # LAX to Santa Monica Airport
    (34.04314164414001, -118.26989729468191, 34.258541047335626, -118.46632516987702), #LA Convention Center to Hickson Mission Hill
    (34.04314164414001, -118.26989729468191, 34.21617325050829, -118.48237507659199), # LA Covention Center to UCLA ECDC in Van Nuys
    (33.76475151942483, -118.1906326052472, 34.04314164414001, -118.26989729468191),  # Long Beach Convention Center to LA Convention Center
    (34.05235111873421, -118.15521487748612, 33.81656736762932, -118.18186601253025), # Monterey Park to Shopping store in Signal Hill
    (34.04230078052316, -118.2391036250401, 33.812015707748515, -117.8922274210929),  # Downtown LA (in the middle) to Anaheim
    (34.04230078052316, -118.2391036250401, 34.05245726642068, -117.80490833228933), # Downtown LA in the middle to Pomona
    (34.156037409769425, -118.15347659296648, 34.13499557264049, -117.5394997822741), # Pasadena to Rancho Cucamonga
    (37.76783013159205, -122.40723085073442, 37.312747708307356, -121.85498245607256), # San Francisco to San Jose
    (37.79774793940261, -122.2619612439802, 37.312747708307356, -121.85498245607256), # Oakland to San Jose
    (26.685584882003116, -80.0964319152403, 25.79074426760603, -80.27783010991321), # Palm beach IA to Miami IA
    (41.850100545682935, -87.61642847170353, 41.65540115954826, -88.13282584239305), # S King Dr Chicago to Bolingbrook
    (41.850100545682935, -87.61642847170353, 41.98156781410147, -87.89001529611065) # S king dr chicago to chicago dhale IA
]

# Function to get directions data
def get_directions_data(start_lat, start_lng, end_lat, end_lng, api_key):
    origin = f"{start_lat},{start_lng}"
    destination = f"{end_lat},{end_lng}"
    params = {
        'origin': origin,
        'destination': destination,
        'key': api_key
    }
    response = requests.get(directions_endpoint, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['routes']:
            route = data['routes'][0]
            leg = route['legs'][0]
            return {
                'start_address': leg['start_address'],
                'end_address': leg['end_address'],
                'distance': leg['distance']['text'],
                'duration': leg['duration']['text']
            }
    return None

# Collect data for all OD pairs
data = []
for start_lat, start_lng, end_lat, end_lng in od_pairs:
    result = get_directions_data(start_lat, start_lng, end_lat, end_lng, api_key)
    if result:
        data.append(result)

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('od_pairs_data.csv', index=False)

# Display the DataFrame
print(df)
