destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
def get_destination_index(destination):
  destination_index = 0
  for place in destinations:
    if destination == place:
      destination_index = destinations.index(place)
      return destination_index
    
print(get_destination_index('Hyderabad, India'))
  