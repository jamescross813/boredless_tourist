destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]

def get_destination_index(destination):
    return destinations.index(destination)

def get_traveler_location(traveler):
    return traveler[1]

print(get_destination_index("Los Angeles, USA"))