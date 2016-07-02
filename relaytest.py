from ioexpand import PCF8574
import smbus

def main():
    bus = smbus.SMBus(1)
    relays = PCF8574(bus, 0x27)
    relays.set_gpio(0, 0x01)

if __name__=="__main__":
    main()
