import os
from bs4 import BeautifulSoup as bs
import requests

year = 2022

arr = []
with open(os.path.join(os.path.join(os.getcwd(),"Names and Codes"),f"{year}.csv")) as file:
    l = list(map(lambda x: x.split(","),file.readlines()))
    
    for pro in range(1,len(l)):

        codse = l[pro][1].strip("\t").strip("\n").replace(" ","")
        req = requests.get(f"https://www.congressionalappchallenge.us/22-{codse}/",headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"})
        
        s = bs(req.text,"html.parser")
        do = s.select("span[style='font-weight: 400;']")
        print(codse)
        del do[0]
        comp = ""
        for d in do:
            if d.text == "\n" or d.text == " ":
                continue
            comp += d.text
        arr.append([l[pro][0].strip("\t").strip("\n"),comp])


with open ("shanker.txt" , "a") as sh:
    for n,t in arr:
        sh.write(f"{n}:{t}\n")