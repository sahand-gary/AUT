import os
import pandas as pd
from shapely.geometry import Polygon, Point

folder_path = r"C:\Users\Asus\Desktop\regions"

regions = {}

for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        region_name = os.path.splitext(filename)[0]
        file_path = os.path.join(folder_path, filename)

        df = pd.read_excel(file_path, skiprows=1)
        df.columns = ['X', 'Y']

        coords = list(zip(df['X'], df['Y']))
        regions[region_name] = Polygon(coords)



def get_region_label(x, y, regions_dict):
    point = Point(x, y)
    for label, polygon in regions_dict.items():
        if polygon.contains(point):
            return label
    return "Outside all regions"

x_input = 300
y_input = 40
region = get_region_label(x_input, y_input, regions)
print(f"Point ({x_input}, {y_input}) is in region: {region}")
