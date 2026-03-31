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
    info.add_argument("name")  
    args = parser.parse_args()

    if args.cmd == "list-plants":
        for pl in load_plants():
            print("-", pl.name)

    elif args.cmd == "plant-info":
        plant = get_plant(args.name)  
        if plant:
            display_plant_info(plant)
        else:
            print(f"❌ Plant '{args.name}' not found!")
    
    elif args.cmd == "check":
        pl = get_plant(args.plant)
        score, rating, msgs = evaluate(pl, args.watt, args.hours)
        cost = yearly_cost(args.watt, args.hours, args.price)

        print(f"Plant: {pl.name}")
        print(f"Score: {score} | Rating: {rating}")
        for m in msgs:
            print("-", m)
        print(f"Yearly cost: €{cost:.2f}")