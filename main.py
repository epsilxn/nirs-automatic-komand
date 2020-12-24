from BusinessTravel import Travel
from flask import *


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/get_prices", methods=["GET", "POST"])
def get_prices():
    try:
        a = request.values
        print(a["originCity"], a["destinationCity"], a["originDate"], a["destinationDate"])
    except Exception as e:
        print(e)
    return json.dumps({"oshibka": "uspeh"})


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
