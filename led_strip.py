
import time

from neopixel import *

from config import settings
from config import colors

class LedStrip:
    def __init__(self, led_count = settings.LED_COUNT, pin = settings.LED_PIN, frequency = settings.LED_FREQ_HZ, dma = settings.LED_DMA, invert = settings.LED_INVERT, brightness = settings.LED_BRIGHTNESS, pwm_channel = settings.LED_PWM_CHANNEL, strip_type = settings.LED_STRIP_TYPE):
        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(led_count, pin, frequency, dma, invert, brightness, pwm_channel, strip_type)

        # Intialize the library (must be called once before other functions).
        self.strip.begin()

    def allOn(self, color=colors.WHITE):
        """
        Sets all pixels to the provided color.
        """
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)

        self.strip.show()

    def allOff(self):
        """
        Turns off all the LEDS.
        """
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, colors.OFF)

        self.strip.show()

    def blinkNumTimes(self, color=colors.WHITE, numberOfBlinks=1, wait_ms=1000):
        """
        Blinks the strip for the specified number of times.
        Can specify the color and delay between blinks.
        """
        for num in range(0, numberOfBlinks):
            self.allOn(color)

            time.sleep(wait_ms/1000.0)

            self.allOff()

            time.sleep(wait_ms/1000.0)
        
    def colorWipe(self, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)

            self.strip.show()

            time.sleep(wait_ms/1000.0)

    def theaterChase(self, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, color)

                self.strip.show()

                time.sleep(wait_ms/1000.0)

                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, 0)

    def _wheel(pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    def rainbow(self, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256*iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, self._wheel((i+j) & 255))

            self.strip.show()

            time.sleep(wait_ms/1000.0)

    def rainbowCycle(self, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, self._wheel(((i * 256 / self.strip.numPixels()) + j) & 255))

            self.strip.show()

            time.sleep(wait_ms/1000.0)

    def theaterChaseRainbow(self, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, self._wheel((i+j) % 255))

                self.strip.show()

                time.sleep(wait_ms/1000.0)

                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, 0)