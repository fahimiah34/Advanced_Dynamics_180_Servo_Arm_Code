from machine import Pin,PWM

class Servo:
    ''' A simple servo library with defaults going from -90 degrees to 90 degrees
    '''
    def __init__(self,pin,min_us=544.0,max_us=2400.0,min_deg=-90.0,max_deg=90.0,freq=50):
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(freq)
        self.current_us = 0.0
        self.slope = (min_us-max_us)/(min_deg-max_deg)
        self.offset = min_us
        self.max = max_us
        self.min_deg = min_deg
        self.max_deg = max_deg
        
    def write_us(self,us):
        us = max(self.offset, min(self.max, us))
        self.current_us=us
        self.pwm.duty_ns(int(self.current_us*1000.0))

    def write(self,deg):
        deg = max(self.min_deg, min(deg,self.max_deg))
        self.write_us((deg-self.min_deg)*self.slope+self.offset)

    def read(self):
        return (self.current_us-self.offset)/self.slope + self.min_deg

    def off(self):
        self.pwm.duty_ns(0)
