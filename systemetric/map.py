from libs.pyeuclid import *
from copy import copy
from time import time
class Map(object):
	"""Stores a map of the arena"""
	class Entity(object):
		def __init__(self, position = None, timestamp = 0):
			self.position = position
			self.timestamp = timestamp

		def reliability(self):
			HALF_LIFE = 10 #Time in seconds for an item to become half as likely
			dt = time() - self.timestamp

			return 2.0**(-dt/HALF_LIFE)

	def __init__(self, arena):
		self.arena = arena
		self.tokens    = [Map.Entity() for i in range(20)]
		self.buckets   = [Map.Entity() for i in range(4)]
		self.opponents = [Map.Entity() for i in range(4)]
		self.robot = None

	def fakeUpdateEntities(self, transform, tokens):
		"""Used for vision-less testing"""
		t = time()
		for id, position in tokens.iteritems():
			self.tokens[id].timestamp = t
			self.tokens[id].position = position

		self.robot = transform

	def updateEntityLocations(self, vision):
		"""Update the map with the new set of vision information"""

		#TODO: Maybe keep a timestamp on tokens, and "forget" them after a while?
		locInfo = self.arena.getLocationInfoFrom(vision)
		if locInfo:
			self.robot = locInfo.transform.inverse()
			for token in vision.tokens:
				self.tokens[token.id].position  = locInfo.transform * token.center
				self.tokens[token.id].timestamp = vision.timestamp