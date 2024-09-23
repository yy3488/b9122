import datetime
import hashlib
import os
import uuid
from requests import get
import subprocess
import sys


RECIPIENT = "mm3509"


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
    now = datetime.datetime.now()
    return str(now.time()).split(".")[0]



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

    if not class_code:
        class_code = input("Please enter the classroom code: ")

    specs = [uni, ip_address, mac_address, salt, timestamp, class_code]
    hashcode = generate_hashcode(specs)
    specs.append(hashcode)
    body = "_".join(specs)

    try:
        link = ("mailto:%s@columbia.edu? " +
                "subject=Attendance&body=%s") % (RECIPIENT, body)
        subprocess.check_output("open '%s'" % link , shell=True)
    except:  # TODO fix this on Windows.
        pass
        
    print("If it failed, please send an email with subject 'Attendance'" +
          " and a single line in the body of the email " +
          " to %s@columbia.edu:" % RECIPIENT)
    print("-" * 10)
    print(body)
    print("-" * 10)                                


if "__main__" == __name__:
    mark_attendance()

