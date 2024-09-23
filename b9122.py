import datetime
import hashlib
import os
import uuid
from requests import get
import subprocess
import sys


RECIPIENT = "mm3509"


MACOS = "macOS"
WINDOWS = "windows"
LINUX = "linux"
OS = MACOS

if "darwin" == sys.platform:
    OS = MACOS
elif sys.platform in ["linux", "linux2"]:
    OS = LINUX
elif sys.platform.startswith("win"):
    OS = WINDOWS
else:
    print("Unknown Operating System, defaulting to macOS")


def get_uni():
    fp = ".uni.txt"
    
    if os.path.exists(fp):
        with open(fp) as f:
            uni = f.read(-1).strip()

        if uni:
            return uni
        
    uni = ""
    while not uni:
        uni = input("Please enter your UNI: ").strip()
        if "" == uni:
            print("You didn't enter anything. Please enter your UNI.")
        
    with open(fp, "w+") as f:
        f.write(uni)
    return uni


def get_ip():
    return get('https://api.ipify.org').content.decode('utf8')


def get_salt():
    fp = ".salt.txt"
    if not os.path.exists(fp):
        salt = str(uuid.uuid4()).split("-")[0]
        with open(fp, "w+") as f:
            f.write(salt)
        return salt

    with open(fp) as f:
        return f.read(-1).strip()


def get_time():
    return datetime.datetime.now().strftime("%H:%M:%y%m%d")


def generate_hashcode(fields):
    sha1 = hashlib.sha1()
    sha1.update("".join(fields).encode("ascii"))
    return sha1.hexdigest()
    

def mark_attendance(class_code=None):
    uni = get_uni()
    ip_address = get_ip()
    mac_address = str(uuid.getnode())
    salt = get_salt()
    timestamp = get_time()

    while not class_code:
        class_code = input("Please enter the classroom code: ")
        if 4 == len(class_code):
            break
        print("Class code should be 4 characters, please try again")

    specs = [uni, ip_address, mac_address, salt, timestamp, class_code]
    hashcode = generate_hashcode(specs)
    specs.append(hashcode)
    body = "_".join(specs)

    link = ("mailto:%s@columbia.edu?" +
            "subject=Attendance&body=%s") % (RECIPIENT, body)
    print(link)

    if MACOS == OS:
        cmd = "open '%s'"
    elif WINDOWS == OS:
        cmd = 'start "" "%s"'
    elif LINUX == OS:
        cmd = "xdg-open '%s'"
    else:
        assert False, "Unknown OS!"
        
    subprocess.check_output(cmd % link, shell=True)
        
    print("If it failed, please send an email with subject 'Attendance'" +
          " and a single line in the body of the email " +
          " to %s@columbia.edu:" % RECIPIENT)
    print("-" * 10)
    print(body)
    print("-" * 10)                                


if "__main__" == __name__:
    mark_attendance()

