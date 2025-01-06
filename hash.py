import os
import hashlib
import base64
import json

def generatesalt(length=12):
    return os.urandom(length)


def hashing(password, salt):
    combined = salt + password.encode()
    hashed = hashlib.sha256(combined).hexdigest()
    return hashed


task = input("Enter 1 for login and 2 for signing up \n")

if task == "2":

    username = input("User name \n")
    password = input("Password\n")

    salt = generatesalt()
    hashed = hashing(password, salt)

    file_path = "data.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    salt_64 = base64.b64encode(salt).decode()

    data["userid"][username] = {
        "salt": salt_64,
        "hash": hashed
    }

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print("User " + username + " added successfully.")

if task == "1":
    username = input("Enter the username")
    password = input("enter password")

    file_path = "data.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    salted = data["userid"][username]["salt"]

    salt = base64.b64decode(salted)
    hashed = hashing(password, salt)

    if data["userid"][username]["hash"] == hashed:
        print("login succesfull")
    else:
        print("failed login")