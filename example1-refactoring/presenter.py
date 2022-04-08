class Presenter:
  def __init__(self, service):
    self.viewer = None
    self.service = service

  def init_viewer(self, viewer):
    self.viewer = viewer

  def tic_tac_toe(self, arg):
    arg.disabled = True
    arg.text = self.service.text()
    self.checkWin()
        

  def checkWin(self):
    vector = list(map(lambda item: item.text, self.viewer.buttons))
    win = self.service.win(vector)
    if win != (-1, -1, -1):
      color = self.service.get_win_color()
      for i in win:
          self.viewer.buttons[i].color = color
      for button in self.viewer.buttons:
          button.disabled = True

  def restart(self, arg):
      for button in self.viewer.buttons:
          button.color = self.service.get_main_color()
          button.text = ""
          button.disabled = False