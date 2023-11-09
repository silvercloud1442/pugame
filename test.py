import player
import math

x = 10
y = 10
first_player = player.Player((x, y), math.pi * 2)

new_x, new_y, angle = first_player.get()
print(new_x, new_y, angle)