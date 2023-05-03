import webbrowser as webb
def web(user):
    link = user[4:]
    superLink = f"https://{link}"
    webb.open(superLink)
