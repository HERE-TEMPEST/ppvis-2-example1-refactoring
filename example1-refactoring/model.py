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

  def get_subvector(self, vector, item):
    return [vector[x] for x in item]

  def win(self, vector):
    for item in self.coordinate:
      if self.get_subvector(vector, item).count('X') == 3 or self.get_subvector(vector, item).count('O') == 3:
        return item
    return (-1, -1, -1)
