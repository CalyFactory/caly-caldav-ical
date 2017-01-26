DEVELOPMENT
---
	- python 3.6.0

	- macOS Sierra (10.12.2) 

SET DEV
---
	- source caly-ical/bin/activate
	- pip install -r requirements.txt


CURRENT FLOW
---
	BASIC

	- Get User's principal url

	- Get Top Calendar ID
	
	- Get Each Calendar ID (from here, header depth=1)
	
	- Get C-tag about All Calendar (V, Problem:XML encoding)
	
	- Get E-tag about All Calendar Event

	WEB UPLOAD

	- Upload web server with virtualenv & flask (V)