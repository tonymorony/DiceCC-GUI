from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder

Config.set('kivy', 'window_icon', 'gui/img/favicon.ico')
Config.set('graphics', 'width', '1300')
Config.set('graphics', 'height', '680')


class DiceCCApp(App):

    title = "DiceCC GUI"

    is_connected = False

    rpc_connection = None

    active_table_id = ""


    def build(self):
        gui = Builder.load_file("gui/kv/channelscc.kv")
        return gui


if __name__ == "__main__":
    DiceCCApp().run()
