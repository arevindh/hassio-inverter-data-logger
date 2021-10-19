#!/usr/bin/env python3

import json
import sys

OPTIONS_FILE_NAME = "/data/options.json"
CONFIG_FILE_NAME = "config.cfg"
BASE_CONFIG = """[general]
enabled_plugins = ConsoleOutput,PVoutputOutput
use_temperature = true
min_temp = 5
min_voltage = 0
min_freq = 30

[server]
listen_address = 0.0.0.0
listen_port = 10004

[log]
type = console
level = {log_level}
filename = inverter-export.log

[pvout]"""

with open(OPTIONS_FILE_NAME, "r", encoding="UTF-8") as fp:
    options = json.load(fp)

assert "inverters" in options

with open(CONFIG_FILE_NAME, "w", encoding="UTF-8") as fp:
    print(BASE_CONFIG.format(log_level=options.get("log_level", "info")), file=fp)

    for inverter in options["inverters"]:
        print("apikey-{} = {}".format(inverter["serialnumber"], inverter["pvout_apikey"]), file=fp)
        print("sysid-{} = {}".format(inverter["serialnumber"], inverter["pvout_sysid"]), file=fp)
        print("sysid-{} = {}".format(inverter["serialnumber"], inverter["pvout_sysid"]), file=fp)
        if "pvout_always_upload" in inverter:
            print("always-upload-{} = {}".format(inverter["serialnumber"],
                                                 inverter["pvout_always_upload"]), file=fp)
        print("[logger]", file=fp)
        print("gateways = {},{}".format(inverter["logger_ip"], inverter["logger_sn"]), file=fp)
        print("port = {},{}".format(inverter["logger_port"]), file=fp)
        print("timeout = 3", file=fp)
