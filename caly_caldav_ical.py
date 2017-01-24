import requests 

class CaldavClient:

    def __init__(self, hostname, id, pw):
        if(hostname == "iCal"):
            self.hostname = "https://caldav.icloud.com:443"
        else:
            self.hostname = "https://caldav.icloud.com:443"

        self.userId = id
        self.userPw = pw 
    
    def requestPROPFIND(self, req_data):
        ret = requests.request(
            "PROPFIND",
            self.hostname, 
            data = (
                req_data
            ),
            auth = (
                self.userId,
                self.userPw
            )
        )
        return ret

    def getPrincipal(self):
        data = (
                "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
                "<D:propfind xmlns:D=\"DAV:\">"
                "   <D:prop>"
                "       <D:current-user-principal/>"
                "   </D:prop>"
                "</D:propfind>"
        )
        res=self.requestPROPFIND(data)
        print("PRINCIPAL PROBE TEST")
        print(res.status_code)
        print(res.text)