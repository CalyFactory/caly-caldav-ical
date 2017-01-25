#!/usr/bin/python3
import requests 
import xml.sax
import xml.dom.minidom
import static
from xml.etree.ElementTree import *

"""
prin_tree = ElementTree(fromstring(response.text)).getroot()
for child in prin_tree[0][1][0][0][0]:
    print(child.tag, child.attrib)
    print(prin_tree[0][1][0][0][0].text)
"""

class CaldavClient:

    def __init__(self, hostname, id, pw):
        if(hostname == "iCal"):
            self.hostname = "https://caldav.icloud.com:443"
        else:
            self.hostname = "https://caldav.icloud.com:443"

        self.userId = id
        self.userPw = pw 
    
    def requestPROPFIND(self, host_url, req_data, req_depth=0):
        
        req = requests.request(
            "PROPFIND",
            host_url, 
            headers = {
                "Depth" : str(req_depth)
            },
            data = (
                req_data
            ),
            auth = (
                self.userId,
                self.userPw
            )
        )
        return req

    def getPrincipal(self):
        data = static.XML_REQ_PRINCIPAL
        res=self.requestPROPFIND(self.hostname,data)

        prin_tree = ElementTree(fromstring(res.text)).getroot()
        self.prin_url=prin_tree[0][1][0][0][0].text
        print(prin_tree[0][1][0][0][0].text)

        
    def getTopCalendarID(self):
        data = static.XML_REQ_HOMESET
        #print("getTotalCalendarID")
        #print(self.hostname+self.prin_url)

        res=self.requestPROPFIND(self.hostname+self.prin_url,data)
        #print(res.text)
        top_cal_tree = ElementTree(fromstring(res.text)).getroot()

        self.top_cal_url=top_cal_tree[0][1][0][0][0].text
        #print(self.top_cal_url)

    def getAllCalendarID(self):
        data = static.XML_REQ_CALENDARCTAG
        res = self.requestPROPFIND(self.top_cal_url,data,1)

        all_cal_tree = ElementTree(fromstring(res.text)).getroot()
        #print(res.status_code)
        #print(res.status_code)
        print(res.text)
        self.printAllCalendarName(all_cal_tree)
        #self.cal_url = "https://p62-caldav.icloud.com:443/10761962064/calendars/home/"

    def printAllCalendarName(self,trees):
        
        for tree in trees:
            for child in tree:
                if child.tag == "{DAV:}href":
                    print("HREF", child.text)
                    
                if child.tag == "{DAV:}propstat":
                    #print("PROPSTAT", child[0][0].tag, child[0][0].attrib)#, len(child[0]))
                    if "{DAV:}displayname" in child[0][0].tag:
                        print("DS ",child[0][0].text)
                    if len(child[0]) > 1:
                        #print("PROPSTAT", child[0][1].tag, child[0][1].attrib)
                        if "{http://calendarserver.org/ns/}getctag" in child[0][1].tag:
                            print("GC ",child[0][1].text)
                    if len(child[0]) > 2:
                        #print("PROPSTAT", child[0][2].tag, child[0][2].attrib)
                        if "{http://calendarserver.org/ns/}getctag" in child[0][2].tag:
                            print("GC ",child[0][2].text)

                    print()
                    

    def getCtagCurrentCalendar(self):
        data = (
                "<?xml version=\"1.0\" encoding=\"utf-8\"?> "
                "<d:propfind xmlns:d=\"DAV:\" xmlns:cs=\"http://calendarserver.org/ns/\"> "
                "    <d:prop> "
                "        <d:displayname /> "
                "        <cs:getctag /> "
                "    </d:prop> "
                "</d:propfind>"
            )
        res = self.requestPROPFIND(self.cal_url,data,1)

        ctag_tree = ElementTree(fromstring(res.text)).getroot()
        #print(res.status_code)
        #print(res.text)
        """
        for tree in ctag_tree:
            for child in tree:
                print(child.tag, child.attrib)
                """
        #self.printAllCalendarName(ctag_tree)