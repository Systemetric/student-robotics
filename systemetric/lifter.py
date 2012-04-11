from mbed import MbedDevice
import time

class Lifter(MbedDevice):
	LIFT_WAIT = 2

	def __init__(self, mbed = None):
		super(Lifter, self).__init__('L', mbed)

	def up(self, wait=True):
		self.request('u')

		if wait:
			time.sleep(Lifter.LIFT_WAIT)

	def down(self, wait=True):
		self.request('d')

		if wait:
			time.sleep(Lifter.LIFT_WAIT)

	def wobble(self):
		self.up()
		self.down(wait=False)

def main():
	l = Lifter

	l.up()
	l.down()