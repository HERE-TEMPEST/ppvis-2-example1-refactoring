from view import TicTackToe
from presenter import Presenter
from model import Model

if __name__ == "__main__":
    controller = Presenter(Model())
    TicTackToe(controller).run()