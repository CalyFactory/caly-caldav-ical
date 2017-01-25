
XML_REQ_PRINCIPAL =(
                "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
                "<D:propfind xmlns:D=\"DAV:\">"
                "   <D:prop>"
                "       <D:current-user-principal/>"
                "   </D:prop>"
                "</D:propfind>"
)


XML_REQ_HOMESET =(
                "<?xml version=\"1.0\" encoding=\"utf-8\"?> "
                "<ns0:propfind xmlns:C=\"urn:ietf:params:xml:ns:caldav\" xmlns:D=\"DAV\" xmlns:ns0=\"DAV:\">"
                "   <ns0:prop>"
                "       <C:calendar-home-set/>"
                "   </ns0:prop>"
                "</ns0:propfind>"
)

XML_REQ_CALENDARCTAG =(
                "<?xml version=\"1.0\" encoding=\"utf-8\"?> "
                "<d:propfind xmlns:d=\"DAV:\" xmlns:cs=\"http://calendarserver.org/ns/\"> "
                "    <d:prop> "
                "        <d:displayname /> "
                "        <d:resourcetype/> "
                "        <cs:getctag /> "
                "    </d:prop> "
                "</d:propfind>"
)