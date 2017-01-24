#!/usr/bin/python3
import requests 
import xml.sax
import xml.dom.minidom
from xml.etree.ElementTree import *

class CaldavClient:

    def __init__(self, hostname, id, pw):
        if(hostname == "iCal"):
            self.hostname = "https://caldav.icloud.com:443"
        else:
            self.hostname = "https://caldav.icloud.com:443"

        self.userId = id
        self.userPw = pw 
    
    def requestPROPFIND(self, host_url, req_data,req_depth=0):
        
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
        data = (
                "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
                "<D:propfind xmlns:D=\"DAV:\">"
                "   <D:prop>"
                "       <D:current-user-principal/>"
                "   </D:prop>"
                "</D:propfind>"
        )
        res=self.requestPROPFIND(self.hostname,data)

        prin_tree = ElementTree(fromstring(res.text)).getroot()
        self.prin_url=prin_tree[0][1][0][0][0].text

        """
        prin_tree = ElementTree(fromstring(response.text)).getroot()
        for child in prin_tree[0][1][0][0][0]:
            print(child.tag, child.attrib)
            print(prin_tree[0][1][0][0][0].text)
        """
        
    def getTopCalendarID(self):
        data = (
                "<?xml version=\"1.0\" encoding=\"utf-8\"?> "
                "<ns0:propfind xmlns:C=\"urn:ietf:params:xml:ns:caldav\" xmlns:D=\"DAV\" xmlns:ns0=\"DAV:\">"
                "   <ns0:prop>"
                "       <C:calendar-home-set/>"
                "   </ns0:prop>"
                "</ns0:propfind>"
            )
        #print("getTotalCalendarID")
        #print(self.hostname+self.prin_url)

        res=self.requestPROPFIND(self.hostname+self.prin_url,data)
        #print(res.text)
        top_cal_tree = ElementTree(fromstring(res.text)).getroot()

        self.top_cal_url=top_cal_tree[0][1][0][0][0].text
        #print(self.top_cal_url)

    def getAllCalendarID(self):
        data = (
                "<?xml version=\"1.0\" encoding=\"utf-8\"?> "
                "<ns0:propfind xmlns:C=\"urn:ietf:params:xml:ns:caldav\" xmlns:D=\"DAV\" xmlns:ns0=\"DAV:\"> "
                "    <ns0:prop> "
                "         <ns0:displayname/> "
                "        <ns0:resourcetype/> "
                "    </ns0:prop> "
                "</ns0:propfind> "
            )
        res = self.requestPROPFIND(self.top_cal_url,data,1)

        all_cal_tree = ElementTree(fromstring(res.text)).getroot()
        print(res.status_code)
        print(res.text)
        for child in all_cal_tree[0]:
            print(child.tag, child.attrib)
        print(all_cal_tree[0].text)