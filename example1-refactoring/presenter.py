class Presenter:
  def __init__(self, service):
    self.viewer = None
    self.service = service

  def init_viewer(self, viewer):
      self.viewer = viewer

  def tic_tac_toe(self, arg):
        arg.disabled = True
        arg.text = self.service.text()

        vector = list(map(lambda item: item.text, self.viewer.buttons))
        
        win = self.service.win(vector)
        if win != (-1, -1, -1):
          color = [0, 1, 0, 1]
          for i in win:
              self.viewer.buttons[i].color = color
          for button in self.viewer.buttons:
              button.disabled = True

  def restart(self, arg):
      self.switch = True

      for button in self.viewer.buttons:
          button.color = [0, 0, 0, 1]
          button.text = ""
          button.disabled = False