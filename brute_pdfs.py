import requests
import wget

url = "http://10.10.10.248/documents/"
wordlist = open("wordlist.txt")
for line in wordlist:
    line = line.replace("\n", "")
    print(url + line + "-upload.pdf")
    r = requests.get(url + line + "-upload.pdf")
    if int(r.status_code) == 200:
        print("Founded" + " " + str(url) + " " + "Status code:" + " ", int(r.status_code))
        wget.download(url + line + "-upload.pdf", out="pdfs")