#!/usr/local/bin/python3

import datetime
import hashlib
import os
import uuid
from requests import get
import subprocess
import sys


def get_uni():
    fp = ".uni.txt"
    if not os.path.exists(fp):
        uni = input("Please enter your UNI: ").strip()
        with open(fp, "w+") as f:
            f.write(uni)
        return uni

    with open(fp) as f:
        return f.read(-1).strip()


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



def mark_attendance(class_code=None, recipient=None):
    uni = get_uni()
    ip = get_ip()
    mac = str(uuid.getnode())
    salt = get_salt()
    t = get_time()

    if not class_code:
        class_code = input("Please enter the classroom code: ")

    if not recipient:
        recipient = input("Please enter the UNI of the recipient: ")

    if not recipient.endswith("columbia.edu"):
        recipient += "@columbia.edu"

    sha1 = hashlib.sha1()
    specs = [uni, ip, mac, salt, t]
    sha1.update("".join(specs).encode("ascii"))
    hash = sha1.hexdigest()
    specs.append(hash)
    body = "_".join(specs)

    try:
        link = "mailto:%s?subject=Attendance&body=%s" % (recipient, body)
        subprocess.check_output("open '%s'" % link , shell=True)

    print("If it failed, please send an email with subject 'Attendance' and " +
          "this line in the body to %s@columbia.edu:" % recipient)
    print("-" * 10)
    print(body)
    print("-" * 10)                                


mark_attendance()

