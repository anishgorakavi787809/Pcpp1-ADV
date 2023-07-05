# sourcery skip: convert-to-enumerate, for-append-to-extend
import requests
from bs4 import BeautifulSoup as bs
import csv
import os

#This is between 2019 to 22
year = "2020"
r = requests.get(f"https://www.congressionalappchallenge.us/{year}-winners/",headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"})

parse_it = bs(r.text,"html.parser")
arr = []
with open(os.path.join(os.path.join(os.getcwd(),"Reps and Codes"),f"{year}.csv")) as file:
    l = list(map(lambda x: x.split(","),file.readlines()))
    print(l)
    c = 1
    for i in parse_it.select("h3.image-title"):
        try:
            arr.append([i.text.strip("\n").strip("\t"),l[c][1].strip("\n")])
        except IndexError:
            break
        else:
            c += 1

with open(os.path.join(os.path.join(os.getcwd(),"Names and Codes"),f"{year}.csv"),"w") as file:
    do = csv.writer(file)
    do.writerow(["App Title","Rep Code"])
    do.writerows(arr)