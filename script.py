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
    return attractions
get_attractions()

def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    if destination_index >= 0:
        attractions_for_destination = attractions[destination_index]
        attractions_for_destination.append(attraction)
    return attractions_for_destination

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest =[]
    for attrac in attractions_in_city:
        attraction_tag=attrac[1]
        # print(attrac[1])
        for attrac_tag in attraction_tag:
            for int in interests:
                if int == attrac_tag:
                    attractions_with_interest.append(attrac[0])
    return attractions_with_interest

def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
    for i in traveler_attractions:
        interests_string = interests_string + i
    return interests_string

test_traveler = ['Derek Smill', 'Paris, France', ["monument"]]
print(get_attractions_for_traveler(test_traveler))
# print(get_destination_index("Los Angeles, USA"))
# print(get_traveler_location(test_traveler))
# test_destination_index = get_destination_index(get_traveler_location(test_traveler))
# print(test_destination_index)
# print(attractions)

# additional attractions


# print(attractions)