from kivy.app import App
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
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
    count_enabled = BooleanProperty(False)
    my_text = StringProperty('1')
    text_input_str = StringProperty('SIVA')
    #slider_value_text = StringProperty('Value')
    def on_button_click(self):
        if self.count_enabled == True:
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            # OFF
            widget.text = "OFF"
            self.count_enabled = False
        else:
            # ON
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print("Switch " + str(widget.active))

    def on_slider_value(self, widget):
        print("Slider Value " + str(int(widget.value)))
        # self.slider_value_text = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text




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

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(700, 500, 150, 100), width=5)
            self.rec = Rectangle(pos=(700, 200), size=(150, 100))

    def on_button_a_click(self):
        x, y = self.rec.pos
        w, h = self.rec.size
        inc = dp(10)

        diff = self.width - (x+w)
        if diff < inc:
            inc = diff
        x += inc
        self.rec.pos= (x, y)



class MainWidget(Widget):
    pass




class TheLabApp(App):
    pass


TheLabApp().run()