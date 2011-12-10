import sr
from libs.pyeuclid import *
from pointset import PointSet

class VisionResult(list):

	def __init__(self, rawmarkers):
		self[:] = rawmarkers
		self.tokens = []
		self.arena = []
		self.robots = []
		self.buckets = []
		self.cameraMatrix = Matrix4()
		#self.cameraMatrix = Matrix4.new_rotate_euler(	# https://github.com/dov/pyeuclid/blob/master/euclid.txt (line 385)
		#	heading = 0,								 # rotation around the y axis
		#	attitude = -5,							  # rotation around the x axis
		#	bank = 0									 # rotation around the z axis
		#)
		self.__groupByType()

	def __groupByType(self):
		'''Get all the markers, grouped by id.
		For example, to get the token with id 1, use:
		
			markers = R.see().getMarkersById()
			
			# Check if token 0 is visible
			if 0 in markers.tokens:
				markersOnFirstToken = markers.tokens[0]
		'''		
		for marker in self:
			#id = marker.info.offset
			type = marker.info.marker_type
			
			# What type of marker is it?
			if type == sr.MARKER_TOKEN:
				list = self.tokens
			elif type == sr.MARKER_ARENA:
				list = self.arena
			elif type == sr.MARKER_ROBOT:
				list = self.robots
			else:
				list = self.buckets
			
			##Is this the first marker we've seen for this object?
			#if not id in list:
			#	list[id] = []
			

			#Add this marker to the list of markers for this object
			#list[id].append(marker)
			list.append(marker)

	def __convertPoint(self, point):
		return Point3(point.world.x, point.world.y, point.world.z)

	def __projectToFieldPlane(self, point):
		return Point2(*(self.cameraMatrix * point).xz)
	
	def visibleCubes(self):		
		tokens = []
		estimatedCentres = []

		# For each token
		for markerId, markers in self.tokens.iteritems():
			newmarkers = []
			# Convert all the markers to a nicer format, using pyeuclid
			for marker in markers:
			
				vertices = []
				# We only care about 3D coordinates - keep those
				for v in marker.vertices:
					vertices.append(Point3(
						v.world.x,
						v.world.y,
						v.world.z
					))
				
				# Calculate the normal vector of the surface
				edge1 = vertices[2] - vertices[1]
				edge2 = vertices[0] - vertices[1]
				normal = edge1.cross(edge2).normalize()
				
				# Keep the center position
				location = marker.centre.world

				newmarkers.append(Marker(
					location = Point3(location.x, location.y, location.z),
					normal = normal,
					vertices = vertices
				))
				
				estimatedCentres.append(location - normal * 0.05)
			
			token = Token(
				markers = newmarkers,
				timestamp = markers[0].timestamp,
				id = markerId,
				location = sum(estimatedCentres) / len(estimatedCentres)
			)
			# Take into account the position of the robot
			# token.location = self.robotMatrix * token.Location
			tokens.append(token)
		
		#sort by distance, for convenience
		tokens.sort(key=lambda m: m.location.magnitude())
		return tokens


	def arenaMarkerEdges(self):
		edges = []
		for marker in self.arena:

			corners = [self.__convertPoint(v) for v in marker.vertices]

			#Midpoints of edges
			edge1 = (corners[0] + corners[1]) / 2.0
			edge2 = (corners[1] + corners[2]) / 2.0
			edge3 = (corners[2] + corners[3]) / 2.0
			edge4 = (corners[3] + corners[0]) / 2.0

			#Horizontal distance between midpoints
			d1 = (edge1 - edge3).x
			d2 = (edge2 - edge4).x

			if abs(d1) >= abs(d2):
				if d1 > 0:
					edges += [edge1, edge3]
				else:
					edges += [edge3, edge1]
			else:
				if d2 > 0:
					edges += [edge2, edge4]
				else:
					edges += [edge4, edge2]
					
		return PointSet([self.__projectToFieldPlane(edge) for edge in edges])
