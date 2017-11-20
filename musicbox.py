# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
import time

import Adafruit_MPR121.MPR121 as MPR121
import pygame.mixer

print('Starting Music Box')

# Create MPR121 instance.
cap = MPR121.MPR121()

# Initialize communication with MPR121 using default I2C bus of device, and
# default I2C address (0x5A).  On BeagleBone Black will default to I2C bus 0.
if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

#setup pygame to play sounds
pygame.mixer.init()

#set up mapping of pin numbers to actual numbers where pin numbers are array index
pinMapping = [7,8,9,10,11,6,5,0,1,2,3,4]

masterlist = []
counter = 0
gameSwitchPin = 4

drumlist = []
drumlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/drums/clap.wav")) 	#0
drumlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/drums/crash.wav"))	#1	
drumlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/drums/hat.wav"))	#2
drumlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/drums/hit.wav"))	#3
drumlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/drums/rim.wav"))	#4
drumlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/drums/smash.wav"))	#5
drumlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/drums/thud.wav"))	#6
drumlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/drums/ting.wav"))	#7

pianolist = []
pianolist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/piano/39172__jobro__piano-ff-025.wav"))    #0
pianolist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/piano/39173__jobro__piano-ff-026.wav"))    #1
pianolist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/piano/39174__jobro__piano-ff-027.wav"))    #2
pianolist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/piano/39175__jobro__piano-ff-028.wav"))    #3
pianolist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/piano/39176__jobro__piano-ff-029.wav"))    #4
pianolist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/piano/39177__jobro__piano-ff-030.wav"))    #5
pianolist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/piano/39178__jobro__piano-ff-031.wav"))    #6
pianolist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/piano/39179__jobro__piano-ff-032.wav"))    #7
pianolist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/piano/39180__jobro__piano-ff-033.wav"))    #8
pianolist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/piano/39181__jobro__piano-ff-034.wav"))    #9
pianolist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/piano/39182__jobro__piano-ff-035.wav"))    #10
pianolist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/piano/39183__jobro__piano-ff-036.wav"))    #11


farmlist = []
farmlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/farm/chicken.wav"))  #0
farmlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/farm/cow.wav"))      #1
farmlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/farm/dog.wav"))      #2
farmlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/farm/duck.wav"))   	#3
farmlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/farm/frog.wav"))    	#4
farmlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/farm/geese.wav"))   	#5
farmlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/farm/goat.wav"))    	#6
farmlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/farm/horse.wav"))    #7
farmlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/farm/pig.wav"))    	#8
farmlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/farm/sheep.wav"))    #9
farmlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/farm/cat.wav"))      #10

numberlist = []
numberlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/numbers/1.wav"))  #0
numberlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/numbers/2.wav"))  #1
numberlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/numbers/3.wav"))  #2
numberlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/numbers/4.wav"))  #3
numberlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/numbers/5.wav"))  #4
numberlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/numbers/6.wav"))  #5
numberlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/numbers/7.wav"))  #6
numberlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/numbers/8.wav"))  #7
numberlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/numbers/9.wav"))  #8
numberlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/numbers/10.wav"))  #9

laughlist = []
laughlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/laughs/laugh1.wav"))  #0
laughlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/laughs/laugh2.wav"))  #1
laughlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/laughs/laugh3.wav"))  #2
laughlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/laughs/laugh4.wav"))  #3
laughlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/laughs/laugh5.wav"))  #4
laughlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/laughs/laugh6.wav"))  #5
laughlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/laughs/laugh7.wav"))  #6
laughlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/laughs/laugh8.wav"))  #7
laughlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/laughs/laugh9.wav"))  #8
laughlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/laughs/laugh10.wav"))  #9
laughlist.append(pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/laughs/laugh11.wav"))  #10

masterlist.append(drumlist)
masterlist.append(pianolist)
masterlist.append(farmlist)
masterlist.append(numberlist)
masterlist.append(laughlist)

print('Music Box Ready')
pygame.mixer.Sound("/home/pi/Desktop/dev/python/musicbox/sounds/ready.wav").play()


# Main loop to print a message every time a pin is touched.
print('Press Ctrl-C to quit.')
last_touched = cap.touched()
while True:
    current_touched = cap.touched()
    # Check each pin's last and current state to see if it was pressed or released.
    for i in range(12):
        # Each pin is represented by a bit in the touched value.  A value of 1
        # means the pin is being touched, and 0 means it is not being touched.
        pin_bit = 1 << i
        
        # First check if transitioned from not touched to touched.
        if current_touched & pin_bit and not last_touched & pin_bit:
            print('{0} touched!'.format(i))
            if i == gameSwitchPin:
                if counter < (len(masterlist) - 1):
                    counter = counter + 1
                else:
                    counter = 0
                print('game counter is now {0}'.format(counter))
                masterlist[counter][0].play()
            
            else:
                #work with number from pinMapping as real world order not same as pin order
                if len(masterlist[counter]) > pinMapping[i]:
                    masterlist[counter][pinMapping[i]].play()
                else:
                    print("no sound defined for {0} do nothing".format(pinMapping[i]))
            
        # Next check if transitioned from touched to not touched.
        if not current_touched & pin_bit and last_touched & pin_bit:
            print('{0} released!'.format(i))
            
    # Update last state and wait a short period before repeating.
    last_touched = current_touched
    time.sleep(0.05)


