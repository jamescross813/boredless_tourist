destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]
attractions = []

def get_destination_index(destination):
    return destinations.index(destination)

def get_traveler_location(traveler):
    return traveler[1]

def get_attractions():
    for dest in destinations:
        attractions.append([])

# print(get_destination_index("Los Angeles, USA"))
# print(get_traveler_location(test_traveler))
test_destination_index = get_destination_index(get_traveler_location(test_traveler))
print(test_destionation_index)
