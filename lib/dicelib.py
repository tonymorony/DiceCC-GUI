from lib import rpclib
from kivy.app import App
import os.path
import json


def get_tables_list(rpc_connection):

    if App.get_running_app().is_connected:
        tables_list = rpclib.dice_list(rpc_connection)
    else:
        tables_list = ""

    return tables_list


def get_balance(rpc_connection):
    if App.get_running_app().is_connected:
        balance = str(rpclib.getbalance(rpc_connection))
        ticker = rpclib.getinfo(rpc_connection)["name"]
        balance_reflection = balance + " " + ticker
    # to not crash in some cases when not connected or losing connection
    else:
        balance_reflection = ""
    return balance_reflection


class ConfigReader:

    def __init__(self):
        if os.path.isfile("connection.json"):
            with open("connection.json", "r") as file:
                connection_json = json.load(file)
                self.rpc_server = connection_json["rpc_server"]
                self.rpc_user = connection_json["rpc_user"]
                self.rpc_password = connection_json["rpc_password"]
                self.rpc_port = connection_json["rpc_port"]
        else:
            self.rpc_server = ''
            self.rpc_user = ''
            self.rpc_password = ''
            self.rpc_port = ''
