import pygame
import sys
import math
import player

def draw_map(WINDOW, TILE_SIZE, MAP):
    wall_color = (190, 190, 190)
    space_color = (65, 65, 65)

    for i in range(MAP_SIZE):
        for j in range(MAP_SIZE):
            square = i * MAP_SIZE + j

            pygame.draw.rect(WINDOW,
                             wall_color if MAP[square] == '#' else space_color,
                             (TILE_SIZE * j, TILE_SIZE * i, TILE_SIZE - 1, TILE_SIZE - 1))

def draw_player(window, scale, player):
    player_x, player_y, _ = player

    pygame.draw.circle(window, (162, 0, 255), (player_x, player_y), 12 / scale)
    pygame.draw.circle(window, (162, 0, 255), (player_x, player_y), 12 / scale)

def ray_cast(window, player, target_player, num):
    player_x, player_y, player_angle = player
    start_angle = player_angle - HALF_FOV
    depths = []
    back = False
    for ray in range(CASTED_RAYS):
        for depth in range(MAX_DEPTH):
            if ray == CASTED_RAYS - 1:
                back = True
                start_angle = player_angle + math.pi

            target_x = player_x - math.sin(start_angle) * depth
            target_y = player_y + math.cos(start_angle) * depth

            col = int(target_x / TILE_SIZE)
            row = int(target_y / TILE_SIZE)

            square = row * MAP_SIZE + col
            color = 255 / (1 + depth * depth * 0.0001)
            if num == 1:
                ray_color = (236, 162, 49)
                player_color = (162, 49, 236)
            else:
                ray_color = (162, 49, 236)
                player_color = (236, 162, 49)

            prop_scale = 25
            if MAP[square] == '#':
                if not back:
                    pygame.draw.rect(window,
                                     (color, color, color),
                                     (SCALE * ray, (SCREEN_HEIGHT / 2) * (1 - prop_scale / (depth + 0.00000000001)),
                                      SCALE + 1, ((SCREEN_HEIGHT / 2) * (1 + prop_scale / (depth + 0.00000000001))) - (
                                              SCREEN_HEIGHT / 2) * (1 - prop_scale / (depth + 0.00000000001))
                                      ))
                    pygame.draw.rect(MAP_WINDOW,
                                     ray_color,
                                     (TILE_SIZE * col, TILE_SIZE * row, TILE_SIZE, TILE_SIZE))
                    pygame.draw.line(MAP_WINDOW,
                                     ray_color,
                                     (player_x, player_y),
                                     (target_x, target_y))
                else:
                    pygame.draw.line(MAP_WINDOW,
                                     (255, 255, 255),
                                     (player_x, player_y),
                                     (target_x, target_y))

                depths.append(depth)
                break

            player_par = 5
            target_x = int(target_x)
            target_y = int(target_y)

            if int(target_player[0]) in range(int(target_x - player_par), int(target_x + player_par)) and\
               int(target_player[1]) in range(int(target_y - player_par), int(target_y + player_par)) and\
               (player_x, player_y, player_angle) != (target_x, target_y):
                pygame.draw.rect(window,
                                 player_color,
                                 (SCALE * ray, (SCREEN_HEIGHT / 2) * (1 - prop_scale / (depth + 0.00000000001)),
                                  SCALE + 1, ((SCREEN_HEIGHT / 2) * (1 + prop_scale / (depth + 0.00000000001))) - (
                                          SCREEN_HEIGHT / 2) * (1 - prop_scale / (depth + 0.00000000001))
                                  ))
                depths.append(depth)
                break

            if int(target_player[0]) in range(int(target_x - player_par), int(target_x + player_par)) and\
               int(target_player[1]) in range(int(target_y - player_par), int(target_y + player_par)) and\
               (player_x, player_y, player_angle) != (target_x, target_y):
                pygame.draw.rect(window,
                                 player_color,
                                 (SCALE * ray, (SCREEN_HEIGHT / 2) * (1 - prop_scale / (depth + 0.00000000001)),
                                  SCALE + 1, ((SCREEN_HEIGHT / 2) * (1 + prop_scale / (depth + 0.00000000001))) - (
                                          SCREEN_HEIGHT / 2) * (1 - prop_scale / (depth + 0.00000000001))
                                  ))
                depths.append(depth)
                break

        start_angle += STEP_ANGLE
    return depths


SCREEN_HEIGHT: int = 960
SCREEN_WIDTH = SCREEN_HEIGHT

map_scale = 3
MAP_SIZE = 28
TILE_SIZE = int((SCREEN_HEIGHT / map_scale) / MAP_SIZE)
MAX_DEPTH = int(MAP_SIZE * TILE_SIZE) * 2
CASTED_RAYS = 90

FOV = math.pi / 3
HALF_FOV = FOV / 2
SCALE = SCREEN_WIDTH / (CASTED_RAYS - 1)
STEP_ANGLE = FOV / (CASTED_RAYS - 1)


x = ((SCREEN_WIDTH / 2) / map_scale) + (SCREEN_WIDTH / 10)
y = ((SCREEN_HEIGHT / 2) / map_scale) - (SCREEN_HEIGHT / 10)
first_player = player.Player((x, y), math.pi * 2)

x = ((SCREEN_WIDTH / 2) / map_scale) - (SCREEN_WIDTH / 10)
y = ((SCREEN_HEIGHT / 2) / map_scale) - (SCREEN_HEIGHT / 10)
second_player = player.Player_2((x, y), math.pi * 2)

MAP = ('############################'
       '#      ##            ##    #'
       '#      ##            ##    #'
       '#      ##            ##    #'
       '#      ##            ##    #'
       '#      ##            ##    #'
       '#      ##            ##    #'
       '#      ##            ##    #'
       '#      ##            ##    #'
       '#      ##            ##    #'
       '#                          #'
       '#                          #'
       '#                          #'
       '#                          #'
       '#                          #'
       '#                          #'
       '#                          #'
       '#                          #'
       '#                          #'
       '#                          #'
       '#                          #'
       '#                          #'
       '#                          #'
       '#######               ######'
       '#######               ######'
       '#                          #'
       '#                          #'
       '############################')

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH * 2, SCREEN_HEIGHT))
WINDOW_f = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
WINDOW_s = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
MAP_WINDOW = pygame.surface.Surface((SCREEN_WIDTH / map_scale, SCREEN_HEIGHT / map_scale))
clock = pygame.time.Clock()
depths = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    pygame.draw.rect(WINDOW_f, (0, 0, 0), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(WINDOW_f, (0, 150, 150), (0, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.draw.rect(WINDOW_s, (0, 0, 0), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(WINDOW_s, (0, 150, 150), (0, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT))


    pygame.draw.rect(MAP_WINDOW, (0, 0, 0), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    draw_map(MAP_WINDOW, TILE_SIZE, MAP)
    keys = pygame.key.get_pressed()
    #FIRST PLAYER
    rays = ray_cast(WINDOW_f, first_player.get(), second_player.get(), 2)
    draw_player(MAP_WINDOW, map_scale, first_player.get())
    first_player.move(keys, rays)

    #SECOND PLAYER
    rays = ray_cast(WINDOW_s, second_player.get(), first_player.get(), 1)
    draw_player(MAP_WINDOW, map_scale, second_player.get())
    second_player.move(keys, rays)

    pygame.draw.rect(WINDOW_s, (255, 0, 0), (SCREEN_WIDTH - 5, 0, 5, SCREEN_HEIGHT))
    pygame.draw.rect(WINDOW_f, (255, 0, 0), (0, 0, 5, SCREEN_HEIGHT))


    screen.blit(WINDOW_s, (0, 0))
    screen.blit(WINDOW_f, (SCREEN_WIDTH, 0))
    screen.blit(MAP_WINDOW, (SCREEN_WIDTH - (SCREEN_WIDTH / map_scale) / 2, 0))

    pygame.display.flip()
    clock.tick(60)