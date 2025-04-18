#Gmail Checker
#Code by Lucky
gmail = input("Enter your G-Mail ID :").strip().lower()
if (gmail.endswith("@gmail.com")):
    print(gmail,"is valid G-Mail ID")
else:
    print(gmail,"is not a valid G-Mail ID")
