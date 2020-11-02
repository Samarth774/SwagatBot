import json
import requests


TOKEN = "1453960586:AAE3B-dCuotUK6hC_pmi2tAfAotlmsil7jE"
print("Testing..")
try:
    r = requests.get("https://api.telegram.org/bot"+TOKEN+"/getUpdates")

    s = json.loads(r.content)

    if s["ok"] == True:
        print("TEST OK")
    else:
        print("Error", s["description"])
except Exception as e:
    print("Failed")
    print("-"*25)
    print(e)
finally:
    input("Enter any key to continue...")
