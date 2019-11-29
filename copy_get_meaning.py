import pyperclip
import json
import requests
import notify2
import time


notify2.init("Your Meaning")

n = notify2.Notification(None, None)

n.set_urgency(notify2.URGENCY_NORMAL)

n.set_timeout(10000)

app_id = "290078f0"
app_key = "a972f82a0199d1d37ddb57d7b63eeaca"

word = ""
#url = "https://od-api.oxforddictionaries.com/api/v2/" + "entries"+"/"+"en-us"+"/"+s
#re = requests.get(url, headers={"app_id":app_id, "app_key":app_key})

while True:
    s = pyperclip.paste()
    if word == s:
        s =""
        time.sleep(5)
    if len(s)==0:
        time.sleep(5)
    else:
        word = s
        url = "https://od-api.oxforddictionaries.com/api/v2/" + "entries"+"/"+"en-us"+"/"+s
        re = requests.get(url, headers={"app_id":app_id, "app_key":app_key})
        print("code {}\n".format(re.status_code))
        j = json.dumps(re.json(), indent=2)
        data = json.loads(j)
        meaning = data["results"][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        example = data["results"][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['examples'][0]['text']



        n.update(str(meaning), str(example))
        n.show()
        time.sleep(10)







