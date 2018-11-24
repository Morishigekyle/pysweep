#!/usr/bin/env python
import subprocess

def main():
        ip_target = "10.0.2."
        detected_hosts = []
        for x in range(0, 256):
                ip = ip_target + str(x)
                command = "fping -a -C 5 -q" + ip
                # print("Now Scanning: {}".format(ip))
                try:
                        output = subprocess.check_output(command,stderr = subprocess.STDOUT,shell = True)
                        split_output = output.split(" : ")
                        ip_address = split_output[0]
                        response = split_output[1]
                        print(ip_address + " is detected online. Response time(s) were: " + response)
                        detected_hosts.append(ip_address)
                except subprocess.CalledProcessError as error:
                        e = error.output
        print(detected_hosts)
        # the_ip_address = output.decode().split(" : ")[0]
        # the_response = output.decode().split(" : ")[1]
        # if the_ip_address == "":
        #         response = ""
        # elif the_ip_address != "":
        #         response = the_response
        #         print(the_ip_address + " is detected online. Response time(s) were: " + response)

if __name__ == "__main__":
    main()