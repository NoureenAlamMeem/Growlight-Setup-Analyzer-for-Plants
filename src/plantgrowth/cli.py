import argparse
from .plants import load_plants, get_plant, display_plant_info
from .calculator import yearly_cost, evaluate

def main():
    parser = argparse.ArgumentParser()
    sp = parser.add_subparsers(dest="cmd")

    # list-plants
    sp.add_parser("list-plants")

    # plant-info
    info = sp.add_parser("plant-info")
    info.add_argument("name")  # positional argument


    if args.cmd == "list-plants":
        for pl in load_plants():
            print("-", pl.name)

    elif args.cmd == "plant-info":
        plant = get_plant(args.name)  # <-- use args.name
        if plant:
            display_plant_info(plant)
        else:
            print(f"❌ Plant '{args.name}' not found!")