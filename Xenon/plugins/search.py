import webbrowser as webb
from googlesearch import search as gsearch
import funcs

def search(user):
    toSearch = user[7:]
    link = f"https://www.google.com/search?q={toSearch}&rlz=1C1RXQR_enIN1036IN1036&oq=&aqs=chrome..69i57j69i60l3.900j0j7&sourceid=chrome&ie=UTF-8"
    webb.open(link)
    funcs.printAndSay("Showing top 5 results")
    cnt = 0
    for url in gsearch(toSearch,stop=5):
        funcs.printAndSay(f"[{cnt+1}]: {url}")
        webb.open(url)
        cnt += 1