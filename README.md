Overview
## Overview

This project is part of my research with Professor Jacqueline Huynh at the University of California, Irvine. It focuses on exploring the potential integration of Urban Air Mobility by analyzing origin-destination (OD) data. The project leverages the Google API and Python tools to process and visualize the data. Using Folium, we create an interactive map displaying OD pairs, highlighting potential travel routes and connectivity between airports and other significant locations.
Repository Structure
lua

Copy code
|-- visualize_od_pair.py
|-- google_api.py
|-- od_pairs_data.csv
|-- od_pairs_map.html
|-- README.md

Files
visualize_od_pair.py: Main script for processing OD pairs and generating the visualization map.
google_api.py: Handles interactions with the Google API for data retrieval.
od_pairs_data.csv: Contains the OD pairs data used for the visualization.
od_pairs_map.html: The generated HTML file displaying the interactive map.
README.md: This file.
Requirements
Python 3.x
Folium
pandas
googlemaps
Install the required Python libraries using:


bash
Copy code
pip install folium pandas googlemaps
Usage


Step 1: Data Preparation
Ensure the od_pairs_data.csv file is properly formatted with the necessary data for the OD pairs.


Step 2: API Key
Ensure you have a valid Google API key and set it up in the google_api.py file.


Step 3: Run the Visualization Script
Execute the visualize_od_pair.py script to process the data and generate the od_pairs_map.html file.

bash
Copy code
python visualize_od_pair.py


Step 4: View the Map
Open the od_pairs_map.html file in a web browser to view the interactive map with OD pairs visualized.

Example
The od_pairs_map.html will display a map with markers for each origin and destination. Polylines will connect the pairs, allowing users to visualize the travel routes.
