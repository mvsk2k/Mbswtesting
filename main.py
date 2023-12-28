from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    count = 1
    my_text = StringProperty('1')
    def on_button_click(self):
        self.count += 1
        self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            # OFF
            widget.text = "OFF"
        else:
            # ON
            widget.text = "ON"





class PageLayoutExample(PageLayout):
    pass

class ScrollViewExample(ScrollView):
    pass

class StackLayoutExample(StackLayout):
    pass

class GridLayoutExample(GridLayout):
    pass
class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass




class TheLabApp(App):
    pass


TheLabApp().run()