import pathlib
from map import Map

MAP_URL = f"{pathlib.Path().absolute()}/wayer/maps/map1.txt"

map = Map(MAP_URL)
map.show()
