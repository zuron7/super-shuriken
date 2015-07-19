try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random
import serial

#arduino = serial.Serial('COM1', 115200, timeout=.1)
arduino = serial.Serial('/dev/ttyACM0',115200,timeout=0)

#width=1180 and height=690
CANVAS_WIDTH = 1100
CANVAS_HEIGHT = 680

BALL_RADIUS = 50
GAP = 30
BALL_COLOUR = 'Black'
ball_pos = []
i=0
num_of_targets = 5
pos_of_disk = None
topArea = CANVAS_HEIGHT-(CANVAS_HEIGHT/3)
RESOLUTIONx = 103.484848485

def convert_to_cm(x):
    return x*0.026458333

def convert_to_pixels(x):
    return x*0.394*RESOLUTIONx
	#return x/0.026458333

def loop_to_remove(minX, maxX, minY, maxY):
	global ball_pos, i
	for j in ball_pos:
		if((minX <= j[0] <= maxX) and (minY <= j[1] <= maxY)):
			ball_pos.remove(j)
			i -= 1


def draw(canvas):
    global i, ball_pos
    i=i+1
    if i<num_of_targets+1:
        ball_pos.append((random.randint(GAP+BALL_RADIUS,CANVAS_WIDTH-BALL_RADIUS-GAP),random.randint(BALL_RADIUS,(topArea)-BALL_RADIUS)))
    for j in (ball_pos):
        canvas.draw_circle((j), BALL_RADIUS, 1, BALL_COLOUR, BALL_COLOUR)
    #print ball_pos
    data = arduino.readline()
    if data:
        print data
    	shuriken_data = []
    	shuriken_data = data.split()
    	#print "shur data: ",shuriken_data
    	#print "Shur data0: ",shuriken_data[0]
        #print "shur data twice :", shuriken_data
        if len(shuriken_data) == 2:
            shuriken_data[0] = float(convert_to_pixels(float(shuriken_data[0])))
            if int(shuriken_data[1]) == 1:
                loop_to_remove(CANVAS_WIDTH-shuriken_data[0]-BALL_RADIUS,CANVAS_WIDTH-shuriken_data[0]+BALL_RADIUS,0,topArea/3)
        	elif int(shuriken_data[1]) == 2:
                loop_to_remove(CANVAS_WIDTH-shuriken_data[0]-BALL_RADIUS,CANVAS_WIDTH-shuriken_data[0]+BALL_RADIUS,topArea/3,2*(topArea/3))
        	elif int(shuriken_data[1]) == 3:
                loop_to_remove(CANVAS_WIDTH-shuriken_data[0]-BALL_RADIUS,CANVAS_WIDTH-shuriken_data[0]+BALL_RADIUS,2*(topArea/3),topArea)
        else:
            print "Error, single value only"





frame = simplegui.create_frame("Shuriken Sport",CANVAS_WIDTH,CANVAS_HEIGHT)
frame.set_canvas_background('White')
frame.set_draw_handler(draw)

frame.start()
arduino.flush()
arduino.flushInput()
arduino.flushOutput()
arduino.close()

			