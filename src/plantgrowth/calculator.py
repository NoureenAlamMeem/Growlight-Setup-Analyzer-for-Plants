
def energy_kwh(watt, hours):
    return (watt * hours) / 1000

def yearly_cost(watt, hours, price):
    return energy_kwh(watt, hours) * 365 * price

def lux(watt):
    return watt * 100

def evaluate(plant, watt, hours):
    score = 0
    msgs = []

    if hours >= plant.recommended_hours:
        score += 35
        msgs.append(f"Hours OK ({hours}h)")
    else:
        msgs.append("Low hours")

    if plant.min_watt <= watt <= plant.max_watt:
        score += 30
        msgs.append("Watt OK")
    else:
        msgs.append("Watt not ideal")

    lx = lux(watt)
    if plant.min_lux <= lx <= plant.max_lux:
        score += 35
        msgs.append(f"Lux OK ({lx})")
    else:
        msgs.append(f"Lux out of range ({lx})")

    rating = "Excellent" if score>=90 else "Good" if score>=70 else "Fair" if score>=50 else "Poor"
    return score, rating, msgs
