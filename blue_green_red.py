from machine import Pin, ADC
from utime import sleep
from neopixel import NeoPixel

ledNum = 16 #represent 16 leds in ring light

ring = NeoPixel(Pin(18), ledNum) #read from Pin18 of ESP32 connected to ring light
pot = ADC(Pin(32)) # read ADC value from the pin 32 of ESP32 connected to pot
off = (0, 0, 0) #condition for Off

while True:
    # Read potentiometer value and map it to delay time
    pot_value = pot.read()
    delay_time = int((pot_value / 4095) * 50)  #ADC range is 0 to 4095

    # Calculate color based on the mapped potentiometer value
    mapped_color_value = int(pot_value / 4096 * 255)  # / 4095) 
    blue_component = (255,0,0) #updating to blue colour at first index
    green_component = (0,255,0) #updating to green colour at first index
    red_component = (0,0,255) #updating to red colour at first index

    color = (red_component, green_component, blue_component) #RGB value for color

    # Update each LED with a variable delay
    for colors in (color): #iterating for 3 color values(RGB) for 16 leds
      for i in range(ledNum): #iterating for 16 leds in ring light
          ring[i] = colors #assigning colour value
          ring.write() #writing to the ring light
          sleep(delay_time / 1000.0)  # Convert delay_time to seconds
