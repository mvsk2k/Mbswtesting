from kivy.app import App
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
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



class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(3)
        with self.canvas:
            #Ellipse(pos=(100, 100), size=(self.ball_size, self.ball_size))
            #Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        #Clock.schedule_interval(self.update, 0.5)
        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        #print("on size " + str(self.width) + ", " + str(self.height))
        #self.ball.pos = self.center
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)


    def update(self, dt):
        #print("Up")
        x, y = self.ball.pos

        x += self.vx
        y += self.vy

        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = - self.vy

        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = - self.vx

        if y < 0:
            y = 0
            self.vy = - self.vy

        if x < 0:
            x = 0
            self.vx = - self.vx

        self.ball.pos = (x, y)


class CanvasExample6(Widget):   # Relative Layout
    pass

class CanvasExample7(BoxLayout):   # Relative Layout
   pass





class MainWidget(Widget):
    pass




class TheLabApp(App):
    pass


TheLabApp().run()