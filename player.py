import pygame
import math

class Player:
    def __init__(self, player_position, player_angle):
        self.x = player_position[0]
        self.y = player_position[1]
        self.angle = player_angle

    def get(self):
        return (self.x, self.y, self.angle)

    def move(self, keys, rays):
        if keys[pygame.K_LEFT]:
            self.angle -= 0.1
        if keys[pygame.K_RIGHT]:
            self.angle += 0.1
        if keys[pygame.K_UP]:
            if rays[int(len(rays) / 2)] > 6:
                self.x += -1 * math.sin(self.angle) * 5
                self.y += math.cos(self.angle) * 5
        if keys[pygame.K_DOWN]:
            if rays[-1] > 6:
                self.x -= -1 * math.sin(self.angle) * 5
                self.y -= math.cos(self.angle) * 5

        return (self.x, self.y, self.angle)

class Player_2:
    def __init__(self, player_position, player_angle):
        self.x = player_position[0]
        self.y = player_position[1]
        self.angle = player_angle

    def get(self):
        return (self.x, self.y, self.angle)

    def move(self, keys, rays):
        if keys[pygame.K_a]:
            self.angle -= 0.1
        if keys[pygame.K_d]:
            self.angle += 0.1
        if keys[pygame.K_w]:
            if rays[int(len(rays) / 2)] > 6:
                self.x += -1 * math.sin(self.angle) * 5
                self.y += math.cos(self.angle) * 5
        if keys[pygame.K_s]:
            if rays[-1] > 6:
                self.x -= -1 * math.sin(self.angle) * 5
                self.y -= math.cos(self.angle) * 5

        return (self.x, self.y, self.angle)