import yagmail

password = ""
with open("/home/pi/Desktop/code/gmail_password.txt", "r") as f:
    password = f.read().rstrip()

