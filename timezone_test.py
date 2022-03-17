#####################################################
# Timezone_test.py: Converts time from one timezone
#     to another (supports 16 time zones)
#
# Author: Bryson Goto, 2/21/2022
#####################################################

from click import argument
from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)

@app.route('/displayZones', methods=["POST"])
def displayZones():
    local_zone = request.form.get("local_zone")
    selected_zone = request.form.get("selected_zone")
    url = 'http://worldtimeapi.org/api/timezone/'
    local_url = url + local_zone
    selected_url = url + selected_zone
    r = requests.get(selected_url);
    rl = requests.get(local_url);
    local_zones = rl.json();
    time_zones = r.json();
    lzones = {
        'abbreviation': local_zones['abbreviation']
    }
    zones = {
        'abbreviation': time_zones['abbreviation'],
        'datetime': time_zones['datetime']
    }
    return render_template("displayZones.html", local_zone=local_zone, selected_zone=selected_zone, lzones=lzones, zones=zones)
