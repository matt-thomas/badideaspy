import requests
import sys
from bs4 import BeautifulSoup
import re
VIDEO_RES = [
    'HLS_270',
    'DASH_9_6_M',
    'DASH_4_8_M',
    'DASH_2_4_M',
    'DASH_1_2_M',
    'DASH_600_K',
    'DASH_1080',
    'DASH_720',
    'DASH_480',
    'DASH_360',
    'DASH_240',
    'DASH_9_6_M.mp4',
    'DASH_4_8_M.mp4',
    'DASH_2_4_M.mp4',
    'DASH_1_2_M.mp4',
    'DASH_600_K.mp4',
    'DASH_1080.mp4',
    'DASH_720.mp4',
    'DASH_480.mp4',
    'DASH_360.mp4',
    'DASH_240.mp4'
    ]

# load up the provided link
url = sys.argv[1]
result = requests.get(url + ".mobile", headers = {'User-agent': "badideabot 0.1"})

if (result.status_code == 200):
    c = result.content
    soup = BeautifulSoup(c, features="html.parser")
    videos = soup.find(attrs={"href": re.compile("https://v.redd.it")})
    if videos and len(videos) > 0:
        href = videos['href']
        for res in VIDEO_RES:
            dash = href + '/' + res
            dashresult = requests.get(dash, allow_redirects=False, headers = {'User-agent': "badideabot 0.1"})
            if dashresult.status_code == 200:
                print(dash)
                break
    else:
        print("no video found")
else:
    print("sorry, something went wrong\n")
    print("error code " + result.status_code)
