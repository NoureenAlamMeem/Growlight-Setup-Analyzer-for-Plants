
import csv
from dataclasses import dataclass
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "plants.csv"

@dataclass
class Plant:
    name: str
    light_category: str
    recommended_hours: int
    min_watt: int
    max_watt: int
    min_lux: int
    max_lux: int
    note: str

def load_plants():
    with open(DATA_PATH, newline="", encoding="utf-8") as f:
        return [Plant(**{
            "name": r["plant"],
            "light_category": r["light_category"],
            "recommended_hours": int(r["recommended_hours"]),
            "min_watt": int(r["min_watt"]),
            "max_watt": int(r["max_watt"]),
            "min_lux": int(r["min_lux"]),
            "max_lux": int(r["max_lux"]),
            "note": r["note"]
        }) for r in csv.DictReader(f)]

def get_plant(name):
    for p in load_plants():
        if p.name == name.lower():
            return p
        
def display_plant_info(plant):
    print(f"🌱 Plant: {plant.name.capitalize()}")
    print(f"Light category: {plant.light_category}")
    print(f"Recommended lux range: {plant.min_lux} - {plant.max_lux}")
    print(f"Recommended wattage: {plant.min_watt} - {plant.max_watt}")
    print(f"Recommended hours: {plant.recommended_hours}")
    print(f"Additional notes: {plant.note if hasattr(plant,'note') else 'None'}")
