DEVELOPMENT
---
	- python 3.6.0

	- macOS Sierra (10.12.2) 

SET DEV
---

~~~
	source caly-ical/bin/activate
	pip install -r requirements.txt
~~~


CURRENT FLOW
---
	BASIC

	- Get User's principal url

	- Get Home-set Calendar ID
	
	- Get Each Calendar ID (from here, header depth=1)
	
	- Get C-tag about All Calendar (Problem:XML encoding)
	
	- Get E-tag about All Calendar Event (V)

	WEB UPLOAD

	- Upload web server with virtualenv & flask

	- Display Current Data for localhost:5000 (V)