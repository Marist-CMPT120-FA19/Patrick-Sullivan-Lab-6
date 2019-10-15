from graphics import*
win = GraphWin()
def draw_light_body(x, y, length, width):
	body = Rectangle (Point(x, y), Point(length, width))
	body.setOutline("black")
	body.setFill("white")
	body.draw(win)

	
def draw_lamp(color, x2, y2, radius):
	lightcolor = Circle(Point(x2, y2), radius)
	lightcolor.setOutline("black")
	lightcolor.setFill(color)
	lightcolor.draw(win)

def draw_traffic_light(x, y):
	draw_light_body (x, y, 40, 100)
	draw_lamp("red", 20, 40, 8)
	draw_lamp("yellow", 20, 60, 8)
	draw_lamp("green", 20, 80, 8)

	
draw_traffic_light(2, 20)
