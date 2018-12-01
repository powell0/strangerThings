from neopixel import ws 

# LED strip configuration:
LED_COUNT       = 50                   # Number of LED pixels.
LED_PIN         = 18                   # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ     = 800000               # LED signal frequency in hertz (usually 800khz)
LED_DMA         = 5                    # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS  = 255                  # Set to 0 for darkest and 255 for brightest
LED_INVERT      = False                # True to invert the signal (when using NPN transistor level shift)
LED_PWM_CHANNEL = 0                    # PWM channel to use for generating signal (typically 0)
LED_STRIP_TYPE  = ws.WS2811_STRIP_RGB  # The LED Strip type

# Stranger Things display configuration:
MIN_IDLE_TIMEOUT = 15  # Minimum amount of time in seconds before randomly displaying a message
MAX_IDLE_TIMEOUT = 30  # Maximum amount of time in seconds before randomly displaying a message
MESSAGE_DELAY    = 10  # Amount of time in seconds between displaying messages
FLICKER_CYCLES   = 3   # The number of times to flicker the lights

# Letter to LED Mapping
LETTER_TO_LED_MAP = {
    "a": 49,
    "b": 48,
    "c": 46,
    "d": 45,
    "e": 43,
    "f": 33,
    "g": 34,
    "h": 36,
    "i": 37,
    "j": 39,
    "k": 40,
    "l": 30,
    "m": 29,
    "n": 27,
    "o": 26,
    "p": 24,
    "q": 14,
    "r": 15,
    "s": 17,
    "t": 18,
    "u": 20,
    "v": 21,
    "w": 11,
    "x": 10,
    "y": 8,
    "z": 7
}
