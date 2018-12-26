from kivy.app import App
from kivy.uix.slider import Slider
from lib import rpclib


class BetAmountSlider(Slider):

    application = App.get_running_app()

    def set_slider_values(self):
        table_info = rpclib.dice_info(self.application.rpc_connection, self.application.active_table_id)
        self.min = table_info["minbet"]
        self.max = table_info["maxbet"]
        # as a test step is a 1/100 of max min delta
        self.step = (self.max - self.min) / 100


