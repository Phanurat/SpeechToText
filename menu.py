import json
import os

menu = [
    {
        "name": "กระเพราไก่",
        "price": 50,
        "description": "ข้าวกระเพราไก่"
    },
    {
        "name": "ผัดซีอิ้วทะเล",
        "price": 80,
        "description": "ข้าวผัดซีอิ้วทะเล"
    },
    {
        "name": "ต้มยำกุ้ง",
        "price": 120,
        "description": "ต้มยำกุ้งน้ำข้น"
    }
]

# Create folder
folder_name = "Assets"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
else:
    print(f"The folder '{folder_name}' already exists.")

# Write data to JSON file
file_path = os.path.join(folder_name, "menu.json")
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(menu, file, ensure_ascii=False, indent=4)

# Read data from JSON file
with open(file_path, 'r', encoding='utf-8') as file:
    menu_data = json.load(file)

# Print the menu data
print(menu_data)
