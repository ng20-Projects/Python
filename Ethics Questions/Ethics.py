import json

jsonfile = open('ethics.json', 'r')
jsondata = jsonfile.read()

obj = json.loads(jsondata)

list = obj['Ethics']
Ans = open("Your_Answers.txt", "w")
try:
    for i in range(203):
        print("\n", list[i].get("sawal"))
        usr_input = input("--> ")
        Ans.write(f"Q{i+1} - {usr_input}\n")
except KeyboardInterrupt as e:
    print("\n\nTest Ended!!")

Ans.close()
