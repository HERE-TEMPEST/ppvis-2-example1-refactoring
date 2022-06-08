import pygame

from events import eventBus

pygame.init()

class View:
    def __init__(self):
        self.controller = None
        
        self.window = None
        self.padding = 5
        self.TILE = 100
        self.WIDTH = self.TILE * 3 + self.padding * 2
        self.HEIGHT = self.TILE * 4 + self.padding * 3
        self.clock = None

        self.sprites = {
          "zero": None,
          "zero_win": None,
          "cross": None,
          "cross_win": None,
          "gray": None,
          "btn_restart": None,
          "txt_restart": None,
          "rect_btn_restart": None,
          "rect_txt_restart": None
        }
        self.buttons = []
        

        eventBus.on("switch", self.event_switch)
        eventBus.on("win", self.event_win)
        eventBus.on("restart", self.event_restart)


    def event_restart(self):
        self.buttons = ["gray"] * 9
    
    def event_win(self, coor):
        self.buttons[coor[0]] = self.buttons[coor[0]] + "_win"
        self.buttons[coor[1]] = self.buttons[coor[1]] + "_win"
        self.buttons[coor[2]] = self.buttons[coor[2]] + "_win"

    def event_switch(self, x, y, char):
        if char == 'X':
          self.buttons[x * 3 + y] = "cross"
        if char == 'O':
          self.buttons[x * 3 + y] = "zero"

    def init_controller(self, controller):
        self.controller = controller

    def build(self):
        self.sprites["zero"] = pygame.transform.scale(pygame.image.load("./images/zero.png"), (self.TILE, self.TILE))
        self.sprites["cross"] = pygame.transform.scale(pygame.image.load("./images/cross.png"), (self.TILE, self.TILE))
        self.sprites["gray"] = pygame.transform.scale(pygame.image.load("./images/gray.jpg"), (self.TILE, self.TILE))
        self.sprites["zero_win"] = pygame.transform.scale(pygame.image.load("./images/win_zero.png"), (self.TILE, self.TILE))
        self.sprites["cross_win"] = pygame.transform.scale(pygame.image.load("./images/win_cross.png"), (self.TILE, self.TILE))
        
        self.sprites["btn_restart"] = pygame.transform.scale(pygame.image.load("./images/gray.jpg"), (self.TILE * 3 + self.padding * 2, self.TILE))
        self.sprites["txt_restart"] = pygame.font.Font(None, 70).render('restart', True, 'white')
        self.sprites["rect_btn_restart"] = pygame.Rect(0, self.TILE * 3 + self.padding * 3, self.TILE * 3 + self.padding * 3, self.TILE)
        self.sprites["rect_txt_restart"] = pygame.Rect(self.TILE * 0.75, (self.TILE + self.padding) * 3 + self.TILE * 0.2, (self.TILE + self.padding) * 3, self.TILE)

        self.buttons = ["gray"] * 9

        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        return self
    
    def draw(self):
      for index, value in enumerate(self.buttons):
        rect = pygame.Rect(self.TILE * (index // 3) + self.padding * (index // 3), self.TILE * (index % 3) + self.padding * (index % 3), self.TILE, self.TILE)
        self.window.blit(self.sprites[value], rect)
      self.window.blit(self.sprites["btn_restart"], self.sprites["rect_btn_restart"])
      self.window.blit(self.sprites["txt_restart"], self.sprites["rect_txt_restart"])

    
    def click(self, event: tuple):
      x = event[0] // self.TILE
      y = event[1] // self.TILE
      if event[0] - (x - 1) * self.TILE < 0: x += 1
      if event[1] - (y - 1) * self.TILE < 0: y += 1
      if self.sprites["rect_btn_restart"].collidepoint(event[0], event[1]):
        self.controller.restart()
      else:
        self.controller.click((x, y))      

    def run(self):
        play = True
        while play:
          self.window.fill('black')

          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

            if event.type == pygame.MOUSEBUTTONDOWN:
              self.click(event.pos)

          self.draw()
          pygame.display.update()
        pygame.quit()
