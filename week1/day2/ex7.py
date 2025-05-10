
import random

def get_random_temp(season):
    tmp_dict = {
        "winter": random.uniform(-10, 1),
        "spring": random.uniform(10, 24),
        "summer": random.uniform(20, 40),
        "autumn": random.uniform(5, 20),
        "fall": random.uniform(5, 20)
    }
    if season not in tmp_dict:
        temp = random.uniform(-10, 40)
    else:
        temp = tmp_dict[season]
    return round(temp, 1)

def month_to_season(month):
    seasons = {
        "winter": (12, 1, 2),
        "spring": (3, 4, 5),
        "summer": (6, 7, 8),
        "autumn": (9, 10, 11)
    }
    for season, months in seasons.items():
        if month in months:
            return season
    return None

def main():
    m = input("Enter a month (1-12): ")
    if not m.isdigit() or int(m) < 1 or int(m) > 12:
        print("Invalid month. Please enter a number between 1 and 12.")
        return
    m = int(m)
    season = month_to_season(m)
    temp = get_random_temp(season)
    print(f"The temperature in {season} is {temp}°C.")
    
    messages = [
        (lambda t: t < 0, "Brrr, that’s freezing! Wear some extra layers today."),
        (lambda t: t <= 16, "Quite chilly! Don’t forget your coat."),
        (lambda t: t <= 23, "Nice and cool. Maybe a light jacket would be good."),
        (lambda t: t <= 32, "Warm weather! Stay hydrated."),
        (lambda t: True, "It's hot! Make sure to drink plenty of water and avoid the sun."),
    ]
    for check, msg in messages:
        if check(temp):
            print(msg)
            break

main()