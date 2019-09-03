import pygame
from pygame.sprite import Group
from pygame import mixer
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    mixer.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Sound effects
    explosion = pygame.mixer.Sound('explosion.wav')
    laser = pygame.mixer.Sound('laser.wav')
    # Turn on cool music
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)
    
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make a ship, a group of bullets and a group of aliens.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()
    # Make an alien.
    aliens = Group()
    #alien = Alien(ai_settings, screen)
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, explosion)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            
        # Get rid of bullets that have disappeared.
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
run_game()