import socket
import sys

RECEIVER_IP="198.0.0.238"

def syntax():
    print "syntax: relaycontrol NUM [ON | OFF]"
    sys.exit(-1)

if len(sys.argv)!=3:
   syntax()

relay_num = int(sys.argv[1])
on_off = sys.argv[2]

msg = "%d %s" % (relay_num, on_off)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(msg, (RECEIVER_IP, 1234))

