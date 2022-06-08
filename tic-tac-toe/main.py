from controller import Controller
from model import Model
from view import View

if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(view, model)
    view.init_controller(controller)

    view.build().run()