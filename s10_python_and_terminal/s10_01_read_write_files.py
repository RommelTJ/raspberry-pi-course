import os

if os.path.exists("/home/pi/Desktop/code/text_file"):
    print("FILE EXISTS")
else:
    print("FILE DOES NOT EXIST")

# with open("/home/pi/Desktop/code/text_file", "r") as f:
#     # print(f.read())
#     for line in f:
#         print(line)

# with open("/home/pi/Desktop/code/text_file", "w") as f:
#     f.write("Hello World!\n")

# with open("/home/pi/Desktop/code/text_file", "a") as f:
#     f.write("Hello World Again!\n")
