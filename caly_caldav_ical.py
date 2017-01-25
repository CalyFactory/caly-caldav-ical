#!/usr/bin/python3
import requests 
import xml.sax
import xml.dom.minidom
import static
from xml.etree.ElementTree import *
import pprint
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
        self.calDict = {}
    
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
        #print(prin_tree[0][1][0][0][0].text)

        
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
        #print(res.text)
        self.printAllCalendarName(all_cal_tree)
        #self.cal_url = "https://p62-caldav.icloud.com:443/10761962064/calendars/home/"

    def printAllCalendarName(self,trees):    
        org_url, dummy = self.top_cal_url.split(":443/")
        current_url=None
        for tree in trees:
            for child in tree:
                if child.tag == "{DAV:}href":
                    current_url=org_url+child.text
                    
                if child.tag == "{DAV:}propstat":
                    #print("PROPSTAT", child[0][0].tag, child[0][0].attrib)#, len(child[0]))
                    #if "{DAV:}displayname" in child[0][0].tag:
                    #    print("DS ",child[0][0].text)
                    if len(child[0]) > 1:
                        #print("PROPSTAT", child[0][1].tag, child[0][1].attrib)
                        if "{http://calendarserver.org/ns/}getctag" in child[0][1].tag:
                            display_name = child[0][0].text
                            c_tag = child[0][1].text
                            self.filterCal(current_url,display_name, c_tag, 1)
                            
                    if len(child[0]) > 2:
                        #print("PROPSTAT", child[0][2].tag, child[0][2].attrib)
                        if "{http://calendarserver.org/ns/}getctag" in child[0][2].tag:
                            display_name = child[0][0].text
                            c_tag = child[0][2].text
                            self.filterCal(current_url,display_name, c_tag, 2)

        pp = pprint.PrettyPrinter(width=41, compact=True)
        pp.pprint(self.calDict)

    def filterCal (self, current_url, display_name, c_tag, where):
        #print("where",where)
        if(display_name is None or c_tag is None):
            return

        if(type(display_name) == "<class 'str'>" and type(display_name) == "<class 'str'>"):
            display_name = display_name.replace(" ","")
            c_tag = c_tag.replace(" ","")
        
        if(display_name is not "" and (c_tag is not "" or c_tag is not "None")):
            #print("DS ",display_name)
            #print("GC ",c_tag, "[0][1]")
            self.calDict[current_url]=[display_name,c_tag]            
            #print(self.calDict)

