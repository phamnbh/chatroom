import server
import client

a = input("[C]reate or [J]oin chatroom?")

if a == 'c' or a =='C':
    b =server.Server(12345)
    b.run()
elif a== 'j' or a == 'J':
    b =client.Client("138.229.223.177", 12345)
    b.run()
