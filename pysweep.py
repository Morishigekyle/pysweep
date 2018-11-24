#!/usr/bin/env python
import subprocess
import time

ip_address = []
def main():
        start = time.time()
        ip_target = "10.0.2."
        for x in range(0, 257):
                ip = ip_target + str(x)
                # print("Now Scanning: {}".format(ip))
                command = subprocess.Popen(["fping", "-a", "-C 5", "-q" , ip], stderr = subprocess.PIPE, stdout = subprocess.PIPE)
                output = command.stderr.read()
                # print(output)
                the_ip_address = output.decode().split(" : ")[0]
                the_response = output.decode().split(" : ")[1]
                if "- - - - -" in the_response:
                        continue
                else:
                        
                        print("Host: " + the_ip_address + " is detected online. Response time(s) were: " + the_response)
                        ip_address.append(ip)
        print("The following hosts were found to be online and responding to pring requests: \nDetected Hosts:\n==============")
        for x in ip_address:
                print(x)
        the_time = time.time() - start
        scan_time = the_time * 1000
        print("\nTotal time to scan took: " + str(scan_time) + "ms")

if __name__ == "__main__":
    main()