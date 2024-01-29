from flask import Flask, render_template , request
from flask import url_for ,jsonify

name = ""

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def base():
    return jsonify("Server running no params passed")

@app.route('/getinfo', methods=['GET'])
def query_records():
    name = request.args.get('name')
    print(name)
    return jsonify(name)


if __name__ == '__main__':
   app.run(debug=True)





# import requests

# url = "https://instagram130.p.rapidapi.com/account-info"

# querystring = {"username":"vishishtkapoor"}

# headers = {
# 	"X-RapidAPI-Key": "56abdaa66fmsh267e7ef1727851cp172e9bjsn56fe161e539f",
# 	"X-RapidAPI-Host": "instagram130.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())