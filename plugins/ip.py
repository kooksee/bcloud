# -*- coding:utf-8 -*-

import re
import getpass
import socket


class HostInfo():
    def __init__(self):
        pass

    def get_host(self):
        hostName = socket.getfqdn(socket.gethostname())
        localIP = socket.gethostbyname(hostName)
        username = getpass.getuser()

        return username, hostName, localIP

    # print get_host()


    def get_internet(self):
        import requests
        res = requests.get("http://ip.chinaz.com/getip.aspx")
        data = re.split(r"',address:'", res.content[5:-2])
        ip = data[0]
        addr, web = data[1].split(" ")

        return ip, addr, web

        # print get_internet()
