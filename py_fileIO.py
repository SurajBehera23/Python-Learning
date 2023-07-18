#
# try:
#     mytxt = open("C:\\Users\\NBDPLN0021\\Desktop\\python\\vky.txt", "r")
#     print(mytxt.readlines())
#
# except:
#     print("File not available")
# else:
#     mytxt.close()
#     print("file closed")
#
# file copy
# try:
#     with open("C:\\Users\\NBDPLN0021\\Desktop\\python\\vky.txt") as a:
#         with open("C:\\Users\\NBDPLN0021\\Desktop\\python\\vky2.txt", "w") as b:
#             for i in a:
#                 b.write(i)
#
# except:
#     print("File not available")
# else:
#     a.close()
#     print("file closed")

# file delete
import os

if os.path.exists("C:\\Users\\NBDPLN0021\\Desktop\\python\\vkyh.txt"):
    os.remove("C:\\Users\\NBDPLN0021\\Desktop\\python\\vky.txt")
    print("File deleted")
else:
    print("File not avaialable")
