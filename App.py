from flask import Flask ,render_template
from datetime import datetime,date
from config import Config
from database import init_db
from queryplayer import get_players
from api_request import *



app = Flask(__name__)
app.config.from_object(Config)
init_db(app)

@app.route("/")
def Home():  
    return render_template("results.html",hello=data_matches() , datetime=datetime ,date =date)


@app.route("/squad")
def Squad():  
    return render_template("squad.html",data_player=get_players())

@app.route("/standing")
def Standing():  
    return render_template("standing.html",standing=data_standing_liga(),standing_cl=data_standing_ucl())


if __name__ == "__main__":
    app.run(debug=True) 