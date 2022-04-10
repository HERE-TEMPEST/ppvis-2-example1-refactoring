class Presenter:
  def __init__(self, service):
    self.viewer = None
    self.service = service

  def init_viewer(self, viewer):
    self.viewer = viewer

  def tic_tac_toe(self, arg):
    self.service.tic_tac_toe(arg)
    self.checkWin()
        

  def checkWin(self):
    vector = self.service.extract_vector_of_text(self.viewer.buttons)
    item = self.service.checkWin(vector)
    if item != (-1, -1, -1):
      self.service.finish_the_game(item, self.viewer.buttons)
      self.service.disable_buttons(self.viewer.buttons)
      
  def restart(self, arg):
    self.service.reset_game(self.viewer.buttons)