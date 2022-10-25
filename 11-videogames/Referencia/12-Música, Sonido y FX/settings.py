# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 640   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 480  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

MAX_SPEED = 5

# map
TILESIZE = 42
KEY_COLOR = (94, 129, 162)

# player
PLAYER_SPEED = 4
PLAYER_SPRITE_AT = (28, 0)
PLAYER_HEALTH = 100

# walls, purplish
TOP_WALL_SPRITE_AT = (4, 23)
FRONT_WALL_SPRITE_AT = (4, 25)

# Bee
BEE_SPEED = 2
BEE_SPRITE_AT = (24, 11)
BEE_HEALTH = 10
BEE_KNOCKBACK = 2

# Bee Nest
BEE_NEST_SPRITE_AT = (24, 11)
BEE_NEST_SPAWN_FREQUENCY = 3000
BEE_NEST_MAX_HEALTH = 25
BEE_NEST_MAX_POPULATION = 5

# Basic gun
BASIC_GUN_SPEED = 0.5
BASIC_GUN_FIRING_RATE = 100
BASIC_GUN_COLOR = YELLOW
BASIC_GUN_TTL = 2000
BASIC_GUN_SPREAD = 0.1
BASIC_GUN_DAMAGE = 2

# Items
ITEM_HOVER_RANGE = 5
ITEM_HOVER_SPEED = 0.005
ITEMS = {
    'HEALTH': {
        'SPRITE_AT': (13, 12),
        'HEAL': 20,
        'FX': 'heal.wav'
    },
    'SPEEDUP': {
        'SPRITE_AT': (6, 29),
        'SPEED': 4,
        'DURATION': 3000,
        'FX': 'speedup.wav'
    }
}

# ADDED SOME SOUNDS AND MUSIC
BG_MUSIC = "DST-RailJet-LongSeamlessLoop.ogg"
CRITTER_DEAD_FX = ["splat.wav"]
BASIC_GUN_FX = ["pewpew.wav", "pewpew1.wav", "pewpew2.wav",
                "pewpew3.wav", "pewpew4.wav", "pewpew5.wav"]
