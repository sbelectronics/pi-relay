from ioexpand import PCF8574
import smbus
import socket
import sys
import traceback

def main():
    bus = smbus.SMBus(1)
    relays = PCF8574(bus, 0x27)

    relay_bits = 0
    relays.set_gpio(0, relay_bits)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 1234))

    while True:
        try:
            data, addr = sock.recvfrom(1024)
            parts=data.split(" ",1)
            relay_num = int(parts[0])
            relay_mask = 1 << relay_num
            if parts[1].lower()=="on":
                relay_bits = relay_bits | relay_mask
            else:
                relay_bits = relay_bits & (~relay_mask)

            print "recv: %d %s" % (relay_num, parts[1])

            relays.set_gpio(0, relay_bits)
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            traceback.print_exc("exc in main loop")

if __name__=="__main__":
    main()
