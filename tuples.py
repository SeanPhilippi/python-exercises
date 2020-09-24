airports = [
    ("O'Hare Internal Airport", "ORD"),
    ("Los Angeles International Airport", "LAX"),
    ("Dallas/Fort Worth International Airport", "DFW"),
    ("Denver International Airport", "DEN"),
]

def print_airports(ports):
    for (name, code) in ports:
        print(f"The code for {name} is {code}.")

print_airports(airports)
