#!/usr/bin/env python3

import json
import sys
import os

OPTIONS_FILE_NAME = "/data/options.json"
CONFIG_FILE_NAME = "config.cfg"
BASE_CONFIG = """[general]
[log]
type = console
level = {log_level}
filename = inverter-export.log

"""

with open(OPTIONS_FILE_NAME, "r", encoding="UTF-8") as fp:
    options = json.load(fp)

assert "inverters" in options

with open(CONFIG_FILE_NAME, "w", encoding="UTF-8") as fp:
    print(BASE_CONFIG.format(log_level=options.get("log_level", "info")), file=fp)

    for inverter in options["inverters"]:
        print("[logger]", file=fp)
        print("logger_ip = {},{}".format(inverter["logger_ip"]), file=fp)
        print("logger_sn = {},{}".format(inverter["logger_sn"]), file=fp)
        print("logger_port = {}".format(inverter["logger_port"]), file=fp)
        print("timeout = 3", file=fp)
        print("inverter_brand = {}".format(inverter["inverter_brand"]), file=fp)
        print("inverter_model = {}".format(inverter["inverter_model"]), file=fp)

        print("[mqtt]", file=fp)
        print("host = {}".format(inverter["mqtt_server"]), file=fp)
        print("port = {}".format(inverter["mqtt_port"]), file=fp)
        print("user = {}".format(inverter["mqtt_user"]), file=fp)
        print("password = {}".format(inverter["mqtt_password"]), file=fp)
