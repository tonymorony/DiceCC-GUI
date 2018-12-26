from kivy.uix.button import Button
from kivy.app import App
from lib import rpclib


class PlaceBetButton(Button):

    def place_bet(self):
        application = App.get_running_app()
        table = application.active_table_id
        table_name = rpclib.dice_info(application.rpc_connection, table)["name"]
        bet_sum = application.root.ids.betplacepage.ids.betamount.text
        bet_odds = application.root.ids.betplacepage.ids.oddsamount.text
        try:
            bet_hex = rpclib.dice_bet(application.rpc_connection, table_name, table, bet_sum, bet_odds)
        except Exception as e:
            application.root.ids.betplacepage.ids.betstatus.text = str(e) + " " + str(bet_hex)
        else:
            try:
                bet_txid = rpclib.sendrawtransaction(application.rpc_connection, bet_hex["hex"])
            except Exception as e:
                application.root.ids.betplacepage.ids.betstatus.text = str(e) + " " + str(bet_hex)
            else:
                print(bet_txid)
                application.root.ids.betplacepage.ids.betstatus.text = "Bet transaction sent. TXID: " + str(bet_txid)
