# This file is part of systemetric-student-robotics.

# systemetric-student-robotics is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# systemetric-student-robotics is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with systemetric-student-robotics.  If not, see <http://www.gnu.org/licenses/>.

from sr import *
import pygtk
import gtk, gobject, cairo
from gtk import gdk

R = Robot()

class Screen(gtk.DrawingArea):
	""" This class is a Drawing Area"""
	def __init__(self):
		super(Screen,self).__init__()
		## Old fashioned way to connect expose. I don't savvy the gobject stuff.
		self.connect("expose_event", self.do_expose_event)
		## This is what gives the animation life!
		gobject.timeout_add(50, self.tick) # Go call tick every 50 whatsits.

	def tick(self):
		## This invalidates the screen, causing the expose event to fire.
		self.alloc = self.get_allocation()
		rect = gtk.gdk.Rectangle(self.alloc.x, self.alloc.y, self.alloc.width, self.alloc.height)
		self.window.invalidate_rect(rect, True)        
		return True # Causes timeout to tick again.

	## When expose event fires, this is run
	def do_expose_event(self, widget, event):
		self.cr = self.window.cairo_create()
		## Call our draw function to do stuff.
		self.draw(*self.window.get_size())

class MyStuff(Screen):
	"""This class is also a Drawing Area, coming from Screen."""
	def __init__(self):
		Screen.__init__(self)
		## x,y is where I'm at
		self.x, self.y = 25, -25
		## rx,ry is point of rotation
		self.rx, self.ry = -10, -25
		## rot is angle counter
		self.rot = 0
		## sx,sy is to mess with scale
		self.sx, self.sy = 1, 1

	def draw(self, width, height):
		cr = self.cr
		markers = R.see()
		## A shortcut

		## First, let's shift 0,0 to be in the center of page
		## This means:
		##  -y | -y
		##  -x | +x
		## ----0------
		##  -x | +x
		##  +y | +y

		markers = R.see(res = (960, 720))

		matrix = cairo.Matrix(1, 0, 0, 1, width/2, height/2) ## translate matrix to centre of screen
		cr.transform(matrix) ## Make it so...
		
		## Now save that situation so that we can mess with it. This preserves the last context (the one at 0,0) and let's us do new stuff.
		cr.save()

		## Let's draw a crosshair so we can identify 0,0
		self.drawcross(cr) 

		for m in markers:

			## Now attempt to rotate something around a point. Use a matrix to change the shape's position and rotation.
			ThingMatrix = cairo.Matrix(1, 0, 0, 1, 0, 0)

			## Next, move the drawing to it's x,y
			cairo.Matrix.translate(ThingMatrix, m.centre.world.x * 100, -m.centre.world.y * 100)
			cr.transform(ThingMatrix) # Changes the context to reflect that

			## Now, whatever is draw is "under the influence" of the context and all that matrix magix we just did.
			self.drawCairoStuff(cr)

			## We restore to a clean context, to undo all that hocus-pocus
			cr.restore()        

	def drawCairoStuff(self, cr):
		## Thrillingly, we draw a red rectangle such that 0,0 is in it's center.
		cr.rectangle(-5, -5, 10, 10)
		cr.set_source_rgb(1, 0, 0) 
		cr.fill()
		## Now a visual indicator of the point of rotation
		## I have no idea (yet) how to keep this as a 
		## tiny dot when the entire thing scales.
		cr.set_source_rgb(1, 1, 1)
		cr.move_to(self.rx, self.ry)
		cr.line_to(self.rx+1, self.ry+1)
		cr.stroke()

	def drawcross(self, ctx):
		## Also drawn around 0,0 in the center
		ctx.set_source_rgb(0, 0, 0)
		ctx.move_to(0, 10)
		ctx.line_to(0, -10)
		ctx.move_to(-10, 0)
		ctx.line_to(10, 0)
		ctx.stroke()


def run(Widget):
	window = gtk.Window()
	window.connect("delete-event", gtk.main_quit)
	window.set_size_request(400, 400)
	widget = Widget()
	widget.show()
	window.add(widget)
	window.present()
	gtk.main()

run(MyStuff)
