import threading as thr
from BusinessTravel import Travel
from flask import *


app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/get_prices", methods=["GET", "POST"])
def get_prices():
    a = request.values
    print(f'Получены данные: {a["originCity"]}, {a["destinationCity"]}, {a["originDate"]}, {a["destinationDate"]}')
    search = Travel(a["originCity"], a["destinationCity"],
                    a["originDate"], a["destinationDate"])
    th = thr.Thread(target=search.search_aviatickets)
    th2 = thr.Thread(target=search.search_hostels)
    th.start()
    th2.start()
    th.join()
    th2.join()
    return json.dumps({"tickets": search.tickets, "hotels": search.hotels})


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
