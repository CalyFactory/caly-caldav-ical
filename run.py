from flask import Flask, render_template
import caly_client
import caly_loader

app = Flask(__name__)

@app.route("/")
def start():
	dict = caly_loader.tmp_login()
	print(type(dict))
	return render_template('calendar_list.html',result = dict)

@app.route("/current_calendar")
def cur_cal():
	return render_template('calendar_list.html')

if __name__ == "__main__":
	app.run()