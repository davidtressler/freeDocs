
################################ FIND YOUTUBE LINKS FROM CHANNEL###################################
import os
import pafy
import requests
import json
mylist2 = []

def links_from_channel(links_url):

    url = links_url #"https://www.youtube.com/channel/UC3XTzVzaHQEd30rQbuvCtTQ"
    #url = "https://www.youtube.com/user/ragnarlothbrokk/videos"
    #url = "https://www.youtube.com/user/LastWeekTonight/videos"
    page = requests.get(url).content
    str_page =  str(page) ; data = str(page).split(' ') ; data = str(data)

    f = open("data.txt", "w+")
    f.write(data)
    f.close()

    with open('data.txt', 'rb') as file_in:
        with open("data_output.txt", "wb") as file_out:
            file_out.writelines(filter(lambda line: b'watch?v=' in line, file_in))
    x = 0
    mylist = []
    with open('data_output.txt') as fp:
        #LOOP OVER LINES
        #while x < len(fp):
        while x < 5000:
            try:
                x = x + 1
                line = fp.readline(x)
                #print("lines from loop", line)
                result = line.find('watch?v=')
                second_char = line[result:result+19]
                mylist.append(second_char)

            except:
                break


    global mylist2
    for i in mylist:
        if i != '' and len(i) > 4:
            myurl = "https://www.youtube.com/" + i
            mylist2.append(myurl)

    #print("Videos:", mylist2)


links_from_channel("https://www.youtube.com/c/RealCrime/videos")
links_from_channel("https://www.youtube.com/c/RealCrime/videos?view=0&sort=p&flow=grid")

links_from_channel("https://www.youtube.com/c/RealStories/videos")
links_from_channel("https://www.youtube.com/c/RealStories/videos?view=0&sort=p&flow=grid")

links_from_channel("https://www.youtube.com/c/TimelineChannel/videos")
links_from_channel("https://www.youtube.com/c/TimelineChannel/videos?view=0&sort=p&flow=grid")

links_from_channel("https://www.youtube.com/channel/UC_0r3EheCnp-wVvndYDGviQ/videos")
links_from_channel("https://www.youtube.com/channel/UC_0r3EheCnp-wVvndYDGviQ/videos?view=0&sort=p&flow=grid")


links_from_channel("https://www.youtube.com/channel/UCwxod2w5NT4qMWfMgZivCYQ/videos")
links_from_channel("https://www.youtube.com/channel/UCwxod2w5NT4qMWfMgZivCYQ/videos?view=0&sort=p&flow=grid")

links_from_channel("https://www.youtube.com/channel/UCW39zufHfsuGgpLviKh297Q/videos")
links_from_channel("https://www.youtube.com/channel/UCW39zufHfsuGgpLviKh297Q/videos?view=0&sort=p&flow=grid")
#
links_from_channel("https://www.youtube.com/c/HISTORY/videos")
links_from_channel("https://www.youtube.com/c/HISTORY/videos?view=0&sort=p&flow=grid")
#
#
links_from_channel("https://www.youtube.com/channel/UCb7xZQi7F3RW7BNtR57cNnA/videos")
links_from_channel("https://www.youtube.com/channel/UCb7xZQi7F3RW7BNtR57cNnA/videos?view=0&sort=p&flow=grid")

links_from_channel("https://www.youtube.com/channel/UCZSE95RmyMUgJWmfra9Yx1A/videos")
links_from_channel("https://www.youtube.com/channel/UCZSE95RmyMUgJWmfra9Yx1A/videos?view=0&sort=p&flow=grid")

links_from_channel("https://www.youtube.com/c/TimelineChannel/videos")
links_from_channel("https://www.youtube.com/c/TimelineChannel/videos?view=0&sort=p&flow=grid")

#links_from_channel("https://www.youtube.com/c/SparkDocs/videos")
#links_from_channel("https://www.youtube.com/c/SparkDocs/videos?view=0&sort=p&flow=grid")
#links_from_channel("https://www.youtube.com/channel/UCkRmoZiR_SOssKA89m1eYJg/videos?view=0&sort=p&flow=grid")

links_from_channel("https://www.youtube.com/c/TRACKSTravelChannel/videos")
links_from_channel("https://www.youtube.com/c/TRACKSTravelChannel/videos?view=0&sort=p&flow=grid")


links_from_channel("https://www.youtube.com/c/ShiverChannel/videos")
links_from_channel("https://www.youtube.com/c/ShiverChannel/videos?view=0&sort=p&flow=grid")

# links_from_channel("https://www.youtube.com/channel/UCkRmoZiR_SOssKA89m1eYJg/videos")

links_from_channel("https://www.youtube.com/channel/UCr5qeBG9g7bGtMGyHG2GzbQ/videos?view=0&sort=p&flow=grid")
links_from_channel("https://www.youtube.com/channel/UCr5qeBG9g7bGtMGyHG2GzbQ/videos")

links_from_channel("https://www.youtube.com/c/FreeDocumentary/videos")
links_from_channel("https://www.youtube.com/c/FreeDocumentary/videos?view=0&sort=p&flow=grid")

links_from_channel("https://www.youtube.com/c/wocomodocs/videos")
links_from_channel("https://www.youtube.com/c/wocomodocs/videos?view=0&sort=p&flow=grid")

links_from_channel("https://www.youtube.com/c/DocumentaryBase/videos")
links_from_channel("https://www.youtube.com/c/DocumentaryBase/videos?view=0&sort=p&flow=grid")

links_from_channel("https://www.youtube.com/c/WildThingsChannel/videos")
links_from_channel("https://www.youtube.com/c/WildThingsChannel/videos?view=0&sort=p&flow=grid")

links_from_channel("https://www.youtube.com/channel/UCwLtUyoh8cm3eXfM3FXRR_g/videos?view=0&sort=p&flow=grid")

links_from_channel("https://www.youtube.com/channel/UClBquUeMeLEhASVfz7GtlZw/videos")
links_from_channel("https://www.youtube.com/channel/UClBquUeMeLEhASVfz7GtlZw/videos?view=0&sort=p&flow=grid")

links_from_channel("https://www.youtube.com/user/secretosdenaturaleza/videos")
links_from_channel("https://www.youtube.com/user/secretosdenaturaleza/videos?view=0&sort=p&flow=grid")

links_from_channel("https://www.youtube.com/c/DarkCrimesTV/videos")
links_from_channel("https://www.youtube.com/user/secretosdenaturaleza/videos?view=0&sort=p&flow=grid")


def stream_url(usr_video):
    """TURNS A YT LINK INTO A STREAM LINK
        TO ACCESS THIS USE best.url
        """

    usr_video = usr_video.replace('"', " ")
    global best
    video = pafy.new(usr_video)
    best = video.getbest()




jsondata = {"Free Documentaries":[]}


#for i in range(0, len()):
count = 0
for i in range(0, len(mylist2)):
    try:
        count +=1
        try:
            stream_url(mylist2[i])
            video = pafy.new(mylist2[i])
        except:
            print("Error With Steam URL")


        print("Adding:",video.title)
        #print("thumb:",video.thumb)
        #print("video:",best.url)
        #print("genre:","Free Docs")

        new_genredata = jsondata["Free Documentaries"]
        new_genredata.append({"name":video.title})
        #new_genredata[i]["name"] = video.title
        new_genredata[i]["thumb"] = video.thumb
        new_genredata[i]["video"] = best.url
        new_genredata[i]["genre"] = "Free Documentaries"



    except KeyboardInterrupt:
        break
    except:
        print ("General Error... Quitting...")
        break
        #print("error loading", video.title)
        #break

with open('mydata.json', 'w+') as dataFile:
    jsondata = json.dump(jsondata, dataFile, indent=4)

os.system('git add mydata.json')
os.system('git commit -m "rpiupload" ')
os.system('git push --force -u origin master')

import urllib.request
url = "https://maker.ifttt.com/trigger/rpifd/with/key/cXxn_pXWyCoapUgTMvP-nHaPgckOI_6ueJm1W_mCV8K?value1=" + str(count)
page = urllib.request.urlopen(url)
page.read()


#if os.name == "posix":
#    count = str(count)
#    output = f"echo 'Finished with {count}, Videos'  | terminal-notifier -sound default"
#    os.system (output)


print("DONE | DOCS FOUND", count)

def maintw():
    try:
        import tweepy
        twitter_auth_keys = {
            "consumer_key"        : "nZqO0pY3SxnB7oWrnwyphfTNs",
            "consumer_secret"     : "hzXeQy5odMlbYVvDEmCse6QFULJSrTWDcpsfXpSwZxRRy2dHuz",
            "access_token"        : "1281282073865715718-FMaBpQ9gvwC39QKqjmTVRPlnkWs2qH",
            "access_token_secret" : "zF6wZN6NPKbBickSrEhSftCji5Z6awg6sJF79ZXzxwLPH"
        }
        auth = tweepy.OAuthHandler(
                twitter_auth_keys['consumer_key'],
                twitter_auth_keys['consumer_secret']
                )
        auth.set_access_token(
                twitter_auth_keys['access_token'],
                twitter_auth_keys['access_token_secret']
                )
        api = tweepy.API(auth)
        # Upload image
        #media = api.media_upload("/Users/david/dropbox/picam/current.jpg")
        # Post tweet with image
        tweet = f"Just updated #KodiFreeDocs with {count} #FreeDocumentary #Films #Kodi #KodiAddon #Free #WhattoWatch"
        post_result = api.update_status(status=tweet)
    except:
        print("Twitter Error")
#if __name__ == "__main__":
maintw()

#os.system('cd /Users/david/freeDocs/3/i/')
#os.system('')

#os.system('cd /Users/david/freeDocs/3/i/')
#os.system('python3.8 /Users/david/freeDocs/3/i/i.py')

