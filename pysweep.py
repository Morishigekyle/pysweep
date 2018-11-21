#!/usr/bin/env python
import subprocess

the_response = []
the_ip_address = []
full_response = []
def main():
    ip_target = "10.0.2."
    for x in range(0, 257):
        ip = ip_target + str(x)
        print("Now Scanning: {}".format(ip))
        command = subprocess.Popen(["fping", "-a", "-C 5", "-q" , ip], stderr = subprocess.PIPE, stdout = subprocess.PIPE)
        output = command.stderr.read()
        print(output)
        the_ip_address = output.decode().split(" : ")[0]
        the_response = output.decode().split(" : ")[1]

if __name__ == "__main__":
    main()