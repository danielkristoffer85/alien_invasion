import pygame
pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.play(-1)
pygame.init()
pygame.display.set_mode(pygame.display.list_modes()[-1]) # smallest resolution available
pygame.mixer.init()
pygame.mixer.music.load("sounds/music.mp3")
pygame.mixer.music.play(5) # repeat 5 times
pygame.mixer.music.queue("sounds/music.mp3")   # queue test2.wav after test.wav plays 5 times
clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)
    
class Music(Sprite):
    """A class to manage bullets fired from the ship"""
    
    def __init__(self, ai_settings, screen, ship):
    
        super(Bullet,self).__init__()
        self.screen = screen
    
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
    
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
    
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
    
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y
    
    def draw_bullet(self):
    
        pygame.draw.rect(self.screen, self.color, self.rect)