import pygame.locals


class HomeBase(pygame.sprite.Sprite):
    def __init__(self, img, spawnX, spawnY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.spawn = {'x': spawnX, 'y': spawnY}
        self.rect.x, self.rect.y = self.spawn['x'], self.spawn['y']  # setting the spawn

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # drawing the homebases to the screen


class BlueHomeBase(HomeBase):
    def __init__(self):
        HomeBase.__init__(self, 'Sprites/HomeBases/BlueHomeBase.png', 0, 0)


class RedHomeBase(HomeBase):
    def __init__(self):
        HomeBase.__init__(self, 'Sprites/HomeBases/RedHomeBase.png', 736, 736)
