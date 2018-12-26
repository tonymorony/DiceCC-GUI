from lib import rpclib
from kivy.uix.screenmanager import Screen
from kivy.app import App


class TableCreationPage(Screen):

    def create_table(self):
        tablename = self.ids["tablename"].text
        tablefunds = self.ids["tablefunds"].text
        minbet = self.ids["minbet"].text
        maxbet = self.ids["maxbet"].text
        maxodds = self.ids["maxodds"].text
        timeoutblocks = self.ids["timeoutblocks"].text
        new_table = rpclib.dice_fund(App.get_running_app().rpc_connection, tablename, tablefunds, minbet, maxbet, maxodds, timeoutblocks)
        try:
            new_table_txid = rpclib.sendrawtransaction(App.get_running_app().rpc_connection, new_table["hex"])
        except Exception as e:
            self.ids["creationstatus"].text = str(new_table)
        else:
            self.ids["creationstatus"].text = "Table opening transaction [color=43c51a]" + new_table_txid + "[/color] succesfully broadcasted"
