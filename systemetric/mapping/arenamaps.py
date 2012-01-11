from arenamap import ArenaMap
from libs.pyeuclid import Point2

class CompetitionArenaMap(ArenaMap):
	"""A class representing the layout of the actual competition arena"""
	def __init__(self):
		ArenaMap.__init__(self, {
			0:  ArenaMap.Marker(Point2(1, 0), 0),
			1:  ArenaMap.Marker(Point2(2, 0), 0),
			2:  ArenaMap.Marker(Point2(3, 0), 0),
			3:  ArenaMap.Marker(Point2(4, 0), 0),
			4:  ArenaMap.Marker(Point2(5, 0), 0),
			5:  ArenaMap.Marker(Point2(6, 0), 0),
			6:  ArenaMap.Marker(Point2(7, 0), 0),

			7:  ArenaMap.Marker(Point2(8, 1), 1),
			8:  ArenaMap.Marker(Point2(8, 2), 1),
			9:  ArenaMap.Marker(Point2(8, 3), 1),
			10: ArenaMap.Marker(Point2(8, 4), 1),
			11: ArenaMap.Marker(Point2(8, 5), 1),
			12: ArenaMap.Marker(Point2(8, 6), 1),
			13: ArenaMap.Marker(Point2(8, 7), 1),

			14: ArenaMap.Marker(Point2(7, 8), 2),
			15: ArenaMap.Marker(Point2(6, 8), 2),
			16: ArenaMap.Marker(Point2(5, 8), 2),
			17: ArenaMap.Marker(Point2(4, 8), 2),
			18: ArenaMap.Marker(Point2(3, 8), 2),
			19: ArenaMap.Marker(Point2(2, 8), 2),
			20: ArenaMap.Marker(Point2(1, 8), 2),

			21: ArenaMap.Marker(Point2(0, 7), 3),
			22: ArenaMap.Marker(Point2(0, 6), 3),
			23: ArenaMap.Marker(Point2(0, 5), 3),
			24: ArenaMap.Marker(Point2(0, 4), 3),
			25: ArenaMap.Marker(Point2(0, 3), 3),
			26: ArenaMap.Marker(Point2(0, 2), 3),
			27: ArenaMap.Marker(Point2(0, 1), 3)
		})

class S007ArenaMapSingleWall(ArenaMap):
	"""A class representing the layout of the S007 arena"""
	def __init__(self):
		ArenaMap.__init__(self, {
			0: ArenaMap.Marker(Point2(0, 0), 0),
			4: ArenaMap.Marker(Point2(1, 0), 0),
			9: ArenaMap.Marker(Point2(2, 0), 0)
		})

class S007SmallArenaMapSingleWall(ArenaMap):
	"""A class representing the layout of the S007 arena"""
	def __init__(self):
		ArenaMap.__init__(self, {
			0: ArenaMap.Marker(Point2(0, 0), 0),
			4: ArenaMap.Marker(Point2(0.5, 0), 0),
			9: ArenaMap.Marker(Point2(1, 0), 0)
		})

class S007SmallArenaMapSingleWall(ArenaMap):
	"""A class representing the layout of the S007 arena. The width is 3.5m, length is 2.75m
	^ Y
	|
    +---0---1---2---3---4---5---+--> X
    |                           |
    27                          6
    |                           |
    26                          7
    |                           |
    25                          8
    |                           |
    24                          9
    |                           |
    23 (origin)                 10



	"""
	def __init__(self):
		ArenaMap.__init__(self, {
			23: ArenaMap.Marker(Point2(0, 0), 3),
			24: ArenaMap.Marker(Point2(0, 0.5), 3),
			25: ArenaMap.Marker(Point2(0, 1), 3),
			26: ArenaMap.Marker(Point2(0, 1.5), 3),
			27: ArenaMap.Marker(Point2(0, 2), 3),

			0: ArenaMap.Marker(Point2(0.5, 2.5), 2),
			1: ArenaMap.Marker(Point2(1, 2.5, 2),
			2: ArenaMap.Marker(Point2(1.5, 2.5), 2),
			3: ArenaMap.Marker(Point2(2, 2.5), 2),
			4: ArenaMap.Marker(Point2(2.5, 2.5), 2),
			5: ArenaMap.Marker(Point2(3, 2.5), 2),

			6: ArenaMap.Marker(Point2(3.5, 2), 1),
			7: ArenaMap.Marker(Point2(3.5, 1.5), 1),
			8: ArenaMap.Marker(Point2(3.5, 1), 1),
			9: ArenaMap.Marker(Point2(3.5, 0.5), 1),
			10: ArenaMap.Marker(Point2(3.5, 0), 1),
		})