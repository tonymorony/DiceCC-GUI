from kivy.app import App
from kivy.uix.slider import Slider
from lib import rpclib


class OddsSlider(Slider):

    application = App.get_running_app()

    def set_slider_values(self):

        table_info = rpclib.dice_info(self.application.rpc_connection, self.application.active_table_id)
        self.min = 2
        self.max = table_info["maxodds"]
        self.step = 1
