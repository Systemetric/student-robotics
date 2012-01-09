from libs.pyeuclid import *
from systemetric.bearing import Bearing
from pointset import PointSet

class ArenaMap(dict):
	class Marker(object):
		WIDTH = 0.25 * 10/12
		def __init__(self, center, zone):
			self.center = center
			self.zone = zone

			if zone == 0:
				side = Vector2(self.WIDTH/2, 0) #right
			elif zone == 1:
				side = Vector2(0, self.WIDTH/2) #up
			elif zone == 2:
				side = Vector2(-self.WIDTH/2, 0) #left
			elif zone == 3:
				side = Vector2(0, -self.WIDTH/2) #down

			self.left, self.right = center + side, center - side

	def __init__(self, arenaMarkers):
		self.update(arenaMarkers)

	def nearestMarkerTo(self, point):
		"""Find the marker with the minimum distance to the given point, and return its id"""
		return min(self, key = lambda i: abs(point - self[i].center))

	def positionsFromCodes(self, visionResult):
		codes = [marker.id for marker in visionResult.arena]
		positions = []
		for code in codes:
			pos = self[code]
			positions += [pos.right, pos.left]

		return PointSet(positions), codes

	def estimateTransformFrom(self, visionResult):
		if visionResult.arena:
			apparent = visionResult.arenaMarkerEnds()
			actual, codes = self.positionsFromCodes(visionResult)
			theta, transform, error = apparent.bestTransformTo(actual)
			return transform

	def estimatePositionFrom(self, visionResult):
		"""Calculate the robot position given what it can see"""
		#commonMarkerIds = set(visionResult.keys()) & set(self.keys())
		apparent = visionResult.arenaMarkerEnds()
		actual, codes = self.positionsFromCodes(visionResult)

		#Translation is the amount the origin is transformed
		theta, transform, error = apparent.bestTransformTo(actual)
		return Bearing(radians=theta), transform * Point2(0, 0), error