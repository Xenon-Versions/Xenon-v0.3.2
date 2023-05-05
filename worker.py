import pickle
import os
import inspect
import help


def newPath(path, fileName):
    path = os.path.join(path, fileName)
    return path


pathX = newPath("C:/Users", str(os.getlogin()))
itsXenonPath = inspect.getfile(help)
itsXenonPath = os.path.join(pathX, itsXenonPath)

xenonPath = itsXenonPath.replace("help.py", "")
dataBasePath = os.path.join(xenonPath, "xenonData")


def varset():
    global noPas, user_pass
    name = input("Enter your name:")
    title = input("Enter window title: ")
    speech = input("Enetr speech status[on/off]: ")
    city = input("Enetr your city name: ")
    wantq = input("Want to set password?[yes/no]: ")
    if wantq == "yes":
        user_pass = input("Enter password: ")
        while True:
            confirm_pass = input("Confirm your password[enter 'e' to exit]: ")
            if user_pass == confirm_pass:
                noPas = True
                break
            if confirm_pass == "e":
                noPas = False
                break
    else:
        noPas = False
    data = {}
    data["name"] = name
    data["title"] = title
    data["speech"] = speech
    data["city"] = city
    if noPas:
        data["user_password"] = user_pass
    else:
        try:
            data.pop("user_password")
        except:
            pass
    file = open(newPath(dataBasePath, "xenonConfig.XE"), "wb")
    pickle.dump(data, file)
    file.close()
    try:
        file = open(newPath(dataBasePath, "records.XE"), "rb")
    except:
        record = {}
        file = open(newPath(dataBasePath, "records.XE"), "wb")
        pickle.dump(record, file)
