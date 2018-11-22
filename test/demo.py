# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import signal
import sys

from neopixel import Color

from led_strip import *
from config import settings

# Main program logic follows:
if __name__ == '__main__':
	# Create LedStrip object with default configuration (as defined in config/settings.py
	led_strip = LedStrip()

    def handle_exit(sig, frame):
        led_strip.allOff()
        print('LED Strip Demo finished')
        sys.exit(0)

    # handle the exit signal
    signal.signal(signal.SIGINT, handle_exit)

    print('Running LED Strip Demo funtions')
	print('Press Ctrl-C to quit.')

	while True:
		# Color wipe animations.
		led_strip.colorWipe(Color(255, 0, 0))  # Red wipe
		led_strip.colorWipe(Color(0, 255, 0))  # Blue wipe
		led_strip.colorWipe(Color(0, 0, 255))  # Green wipe
		# Theater chase animations.
		led_strip.theaterChase(Color(127, 127, 127))  # White theater chase
		led_strip.theaterChase(Color(127,   0,   0))  # Red theater chase
		led_strip.theaterChase(Color(  0,   0, 127))  # Blue theater chase
		# Rainbow animations.
		led_strip.rainbow()
		led_strip.theaterChase(Color(127, 127, 127)) 
		led_strip.rainbowCycle()
		led_strip.theaterChase(Color(127, 127, 127)) 
		led_strip.theaterChaseRainbow()
