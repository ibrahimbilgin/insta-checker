import requests
import os
from bs4 import BeautifulSoup
kadi = [line.rstrip('\n') for line in open("accounts.txt", encoding="utf8")]
while True:
    for i in kadi:
        try:
            r = requests.get('https://www.instagram.com/{}/'.format(i))
            soup = BeautifulSoup(r.content, 'html.parser')
            m = soup.find("meta", {"property": "og:description"})
            user = m.get("content")
            f_pos = user.index('Followers')
            fol_pos = user.index("Following")
            b_pos = user.index('s,')
            p_pos = user.index("g,")
            p_post = user.index("Posts")
            print("")
            print(" User Name: {}".format(i))
            print(" Followers: {}".format(user[0:f_pos]))
            print(" Following: {}".format(user[b_pos + 2:fol_pos]))
            print(" Posts: {}".format(user[p_pos + 2:p_post]))
            print("")
            print(" ---------------")
        except AttributeError:
            print("")
            print(" This username is not used: {}".format(i))
            print("")
            print(" ---------------")
    soru = input(" Press E to repeat operation or press H to exit the program: ")
    if soru == "E" or "e":
        os.system("cls||clear")
    else:
        break
