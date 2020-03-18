destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = 0
  for place in destinations:
    if destination == place:
      destination_index = destinations.index(place)
      return destination_index
    
print(get_destination_index('Hyderabad, India'))
  
def get_traveler_location(traveler):
  name,traveler_destination,like = traveler
  return traveler_destination

test_destination_index = get_destination_index(get_traveler_location(test_traveler))

print(test_destination_index)