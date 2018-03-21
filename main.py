from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from time import strftime

class ClockApp(App):

    seconds = 0

    started = False


    def update_time(self, nap):

        self.root.ids.time.text = strftime('[b]%H[/b]:%M:[sup]%S[/sup]')


    def update(self, nap):

        self.seconds += nap

        self.root.ids.time.text = strftime('[b]%H[/b]:%M:[sup]%S[/sup]')

        m, s = divmod(self.seconds, 60)

        self.root.ids.stopwatch.text = ('%02d:%02d.[size=40]%02d[/size]' %
        (int(m), int(s), int(s * 100 % 100)))

        if self.started:
            self.seconds += nap


    def on_start(self):

        Clock.schedule_interval(self.update_time, 0.016)


    def start_stop(self):
        self.root.ids.start_stop.text = 'Start' if self.started else 'Stop'
        self.started = not self.started


    def reset(self):
        if self.started:
            self.root.ids.start_stop = 'Start'
            self.started = False
                
        self.seconds = 0




if __name__ == '__main__':

    LabelBase.register(name = 'OpenSans',
    fn_regular = 'fonts/OpenSans-Regular.ttf')
    Window.clearcolor = get_color_from_hex('#8B008B')

    ClockApp().run()