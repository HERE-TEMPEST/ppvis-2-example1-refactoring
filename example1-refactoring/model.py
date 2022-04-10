class Model:
  def __init__(self):
    self.switch = True
    self.coordinate = (
      (0, 1, 2), (3, 4, 5), (6, 7, 8),  # X
      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Y
      (0, 4, 8), (2, 4, 6),  # D
    )

  def text(self):
    self.switch = not self.switch
    return 'X' if not self.switch else 'O'


  def tic_tac_toe(self, button): 
    button.disabled = True
    button.text = self.text()

  def checkWin(self, vector):    
    for item in self.coordinate:
      if self.get_subvector(vector, item).count('X') == 3 or self.get_subvector(vector, item).count('O') == 3:
        return item
    return (-1, -1, -1)

  def reset_game(self, buttons):
    for button in buttons:
      button.color = self.get_main_color()
      button.text = ""
      button.disabled = False

  def disable_buttons(self, buttons):
    for button in buttons:
      button.disabled = True

  def finish_the_game(self, item, buttons):
    color = self.get_win_color()
    for i in item:
      buttons[i].color = color

  def extract_vector_of_text(self, buttons):
    return list(map(lambda item: item.text, buttons))

  def get_subvector(self, vector, item):
    return [vector[x] for x in item]

  def get_win_color(self):
    return [0, 1, 0, 1]

  def get_main_color(self):
    return [0, 0, 0, 1]
