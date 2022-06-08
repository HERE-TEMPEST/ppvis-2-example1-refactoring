from events import eventBus

class Controller:
    def __init__(self, view, model):
      self.model = model
      self.view = view

      self.stopped = False
      
      eventBus.on("restart", self.event_restart)
      eventBus.on("win", self.event_win)

    def event_restart(self):
      self.stopped = False

    def event_win(self, _):
      self.stopped = True

    def click(self, coor):
      if not self.stopped:
        self.model.click(coor)
        self.model.tic_tac_toe()
        
    def get_fields(self):
      return self.model.get_fields()

    def restart(self):
      self.model.restart()
