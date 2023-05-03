"""import requests
import os
import vars_setup
import pyautogui as gui
import shutil


class netErrors(Exception):
    def __int__(self, message):
        self.message = message
        super.__init__(self.message)


url = requests.get("https://github.com")
if url.ok:
    pass
else:
    print("Please connect to network")
    raise netErrors("Please connect to network")



def install_repo():
    org_name = "Xenon-Versions"
    url = f"https://api.github.com/orgs/{org_name}/repos"
    response = requests.get(url)
    repos = response.json()
    list_repos = []
    for repo in repos:
        if repo["name"] == ".github":
            pass
        else:
            list_repos.append(repo["name"])
    for i in list_repos:
        print(f"[Index number-{list_repos.index(i)}]:{i}")
    user_version = int(input("Enter your desired index number: "))
    os.mkdir(f"C:/Users/{os.getlogin()}/temp")
    file = open(f"C:/Users/{os.getlogin()}/temp/update_on.py","w")
    codes = f"""

'''import git
import os
import pyautogui as gui
import time
import shutil

os.system("title XEN0N UPDATER")
print("Updating")
print("Please wait...")

time.sleep(10)

shutil.rmtree("C:/Users/{os.getlogin()}")
git.Repo.clone_from(
        "https://github.com/Xenon-Versions/{list_repos[user_version]}",
        "C:/Users/{os.getlogin()}"
    )
wins = gui.getWindowsWithTitle("XEN0N UPDATER")
wins[0].close()
'''"""
    file.write(codes)
    file.close()
    user = vars_setup.Personal()
    wins = gui.getWindowsWithTitle(user.title())
    os.system(f"start cmd /K python C:/Users/{os.getlogin()}/temp/update_on.py")
    wins[0].close()"""