# Labyrinth

🤔 Recherche Bibliothèque PyGames : 
  - https://he-arc.github.io/livre-python/pygame/index.html
  - https://www.pygame.org/docs/
  - https://fr.wikibooks.org/wiki/Pygame

⁉ Forum création map avec PyGames : 
  - https://openclassrooms.com/forum/sujet/python-pygame-dk-labyrinthe

🖥 Idéé ChatGPT:
```
      import pygame

      # Constantes De Couleurs : #

      WHITE = (255, 255, 255)
      BLACK = (0, 0, 0)

      
      # Class De Map : #

      class Map:

        ### Création ###

        def __init__(self, width, height):
          self.width = width
          self.height = height
          self.cells = [[False] * width for _ in range(height)]

        ### Génaration ###

        def generate(self):
        # Ici, vous pouvez mettre votre logique de génération de labyrinthe
        pass

        ### Dessin ###

        def draw(self, screen, cell_size):
          for row in range(self.height):
          for col in range(self.width):
          if self.cells[row][col]:
          pygame.draw.rect(screen, BLACK, (col * cell_size, row * cell_size, cell_size, cell_size))

      # Class Joueur : #

      class Player:

        ### Initialisation ###
        def __init__(self, row, col):
          self.row = row
          self.col = col

        ### Mouvements ###

        def move(self, dx, dy):
          # Ici, vous pouvez mettre votre logique de déplacement du joueur
          pass

        ### Skin Du Joueur ###

        def draw(self, screen, cell_size):
          # Ici, vous pouvez dessiner le joueur
          pass

      # Loop qui fait tourner le jeu # / J'ai pas compris grand chose perso

      def main():
        pygame.init()
        cell_size = 20
        num_rows = 15
        num_cols = 15
        screen_width = cell_size * num_cols
        screen_height = cell_size * num_rows
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Labyrinthe")
        map = Map(num_cols, num_rows)
        map.generate()
        player = Player(0, 0)
        running = True

        while running:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              running = False
          # Ici, vous pouvez gérer les événements de déplacement du joueur
          screen.fill(WHITE)
          map.draw(screen, cell_size)
          player.draw(screen, cell_size)
          pygame.display.flip()
        pygame.quit()
      if __name__ == "__main__":
        main()
```
