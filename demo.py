#!/usr/bin/env python
import subprocess

def main():
    print("Im in main")

    malware_list = ["virus", "worm", "trojan", "ransomware", "Nothing"] 

    for malware in malware_list:
        if malware == "worm":
            print("We found a worm!")
        elif malware == "trojan":
            print("We found a trojan")
        elif malware == "ransomware":
            print("We found a ransomware")
        elif malware == "virus":
            print("We found a ransomware")
        else:
            print("I don't know what we found?")

    for letter in "cyber":
        print(letter)

    for x in range (0,10):
        print("The current number is {} and my name is {}".format(x, "Kyle"))

    subprocess.call(["cat", "/etc/passwd"])

if __name__ == "__main__":
    # print(__name__)
    main()

