import requests
response = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=Adelaide,SA&destination=Adelaide,SA&waypoints=optimize:true|Barossa+Valley,SA|Clare,SA|Connawarra,SA|McLaren+Vale,SA&key=AIzaSyBJzaXpxxw-EhzHW8jyQudUij3sgWbXM78')
print(response.json())


