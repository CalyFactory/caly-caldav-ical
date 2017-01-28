from flask import Flask, render_template
import caly_client
import caly_loader

app = Flask(__name__)

@app.route("/")
def start():
	ctag_dict, etag_dict = caly_loader.tmp_login()
	
	return render_template('calendar_list.html',ctag_result = ctag_dict, etag_result = etag_dict)
	#return render_template('index.html')

@app.route("/current_calendar")
def cur_cal():
	dict = caly_loader.tmp_login()
	print(type(dict))
	return render_template('calendar_list.html',result = dict)

if __name__ == "__main__":
	app.run()