class Map():

    map: list
    size: dict
    point_a: dict
    point_b: dict

    def __init__(self, URL) -> None:

        try:
            raw_map = open(URL, "r").readlines()
        except Exception:
            raise FileNotFoundError
        
        self.map = [
                list(line.replace('\n', '')) for line 
                in raw_map
        ]
        self.size = {
            "length": len(self.map[0]), 
            "width":len(self.map)
        }
        self.point_a = self.dot_coordinates("A")
        self.point_b = self.dot_coordinates("B")

    def dot_coordinates(self, dot):

        for line in self.map:
            for symbol in line:
                if symbol == dot:
                    return {
                        "x": line.index(symbol), 
                        "y": self.map.index(line)
                    }
        return None
    
    def dot_value(self, coordinates: dict):

        return self.map[coordinates.get('y')][coordinates.get('x')]

    def show(self):
        
        for line in self.map:
            print(''.join(line))
