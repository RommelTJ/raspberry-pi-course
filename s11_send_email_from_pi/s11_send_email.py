import yagmail

password = ""
with open("/home/pi/Desktop/code/gmail_password.txt", "r") as f:
    password = f.read().rstrip()

email = "[REDACTED]@gmail.com"
yag = yagmail.SMTP(user=email, password=password)
yag.send(to="[REDACTED]@gmail.com", subject="Hello from Raspberry Pi", contents="Hello World", attachments="/home/pi/Desktop/code/file_to_join.txt")
