import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty, ObjectProperty, StringProperty,NumericProperty
from kivy.uix.popup import Popup
from kivy.config import Config

from othello import Othello as Ot
from othello import Stone as St

Config.set("graphics","width","800")
Config.set("graphics","height","800")

class Blank(Button):
    index = ListProperty([0, 0])


class White(Button):
    index = ListProperty([0, 0])


class Black(Button):
    index = ListProperty([0, 0])

class Result(Popup):
    white=NumericProperty()
    black=NumericProperty()
    winner=StringProperty()


class RootWidget(Widget):
    board = Ot()  # make boards(already set initial four stones)
    turn = ObjectProperty(St.BLACK)  # St.BLACK or St.WHITE

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.draw_board()

    def draw_board(self):  # draw board
        self.grid = self.ids.grid
        for x in range(Ot.SIZE):
            for y in range(Ot.SIZE):
                if self.board.__getitem__(x, y) == St.BLANK:
                    self.grid.add_widget(Blank(index=[x, y]))
                elif self.board.__getitem__(x, y) == St.WHITE:
                    self.grid.add_widget(White(index=[x, y]))
                elif self.board.__getitem__(x, y) == St.BLACK:
                    self.grid.add_widget(Black(index=[x, y]))

    def put(self, x, y):  # x,y is location of clicked button(Blank)
        if self.board.put(x, y, self.turn):  # cannot put
            self.__init__()
            self.change_turn()
            self.check_pass()

    def change_turn(self):
        if self.turn == St.BLACK:
            self.turn = St.WHITE
        else:
            self.turn = St.BLACK

    def check_pass(self):
        if self.board.alljudge(self.turn)==[]:
            self.change_turn()
            if self.board.alljudge(self.turn)==[]:#WHITE and BLACK cannot put
                self.finish()

    def finish(self):
        result=Result()
        result.white,result.black=self.board.count_stone()
        if result.white==result.black:
            result.winner="DRAW"
        elif result.white>result.black:
            result.winner="WINNER:WHITE"
        else:
            result.winner="WINNER:BLACK"

        result.open()

class OthelloApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    OthelloApp().run()
