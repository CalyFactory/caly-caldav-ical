#-*- coding: euc-kr -*-
#!/usr/bin/python3

import requests 
import xml.sax
import xml.dom.minidom
import static
from xml.etree.ElementTree import *
import pprint

class CaldavClient:

    def __init__(self, hostname, id, pw):
        if(hostname == "iCal"):
            self.hostname = "https://caldav.icloud.com:443"
        else:
            self.hostname = "https://caldav.icloud.com:443"

        self.userId = id
        self.userPw = pw 
        self.calCtagDict = {}
        self.calEtagDict = {}
        self.getPrincipal()
    
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
        self.getHomeSetCalendarID()

        
    def getHomeSetCalendarID(self):
        data = static.XML_REQ_HOMESET
        #print("getTotalCalendarID")
        #print(self.hostname+self.prin_url)

        res=self.requestPROPFIND(self.hostname+self.prin_url,data)
        print(res.text)
        top_cal_tree = ElementTree(fromstring(res.text)).getroot()

        self.top_cal_url=top_cal_tree[0][1][0][0][0].text
        #self.top_cal_url=top_cal_tree.find(".//{DAV:}")
        #print(self.top_cal_url)
        self.getAllCalendarID()

    def getAllCalendarID(self):
        data = static.XML_REQ_CALENDARCTAG
        res = self.requestPROPFIND(self.top_cal_url,data,1)

        all_cal_tree = ElementTree(fromstring(res.text)).getroot()
        #print(res.status_code)
        #print(res.status_code)
        #print(res.text)
        #print(str(res.text,'euc-kr'))
        #print(type(res.text))
        self.generateAllCalDict(all_cal_tree)
        #self.cal_url = "https://p62-caldav.icloud.com:443/10761962064/calendars/home/"

    def generateAllCalDict(self,trees):    
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

        #pp = pprint.PrettyPrinter(width=100, compact=True)
        #print("self.calDict =====")
        #pp.pprint(self.calDict)
        #return self.calDict

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
            self.calCtagDict[current_url]=[display_name,c_tag]            
            #print(self.calDict)

    def getCalSet(self):
        #pp = pprint.PrettyPrinter(width=100, compact=True)
        #print("self.calDict =====")
        #pp.pprint(self.calDict)
        return [self.calCtagDict,self.calEtagDict]

    def getAllCalendarEvent(self):
        data = static.XML_REQ_CALENDARETAG
        key_tokenizer = self.top_cal_url
        #key_tokenizer.i
        for key, value in self.calCtagDict.items():
            res = self.requestPROPFIND(key,data,1)
            evt_list=[]
            each_evt_tree = ElementTree(fromstring(res.text)).getroot()
            
            for tree in each_evt_tree:
                evt_list.append(tree[0].text)

            #dummy, key_tail = key.split(key_tokenizer)
            #self.calEtagDict[key_tail]=evt_list
            self.calEtagDict[key]=evt_list
            #print(res.text)

    def testsampleEtag(self):
        data = static.XML_REQ_CALENDARETAG
        for key, value in self.calCtagDict.items():
            res = self.requestPROPFIND(key,data,1)
        
            evts_tree = ElementTree(fromstring(res.text)).getroot()
            
            for tree in evts_tree:
                print(tree[0].tag, tree[0].text)
            print(res.text)