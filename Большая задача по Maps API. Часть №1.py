import sys
import requests
import pygame
import os


# пример ввода данных:
# 55.005021, 73.296302
# 0.01


pygame.init()
spn1, spn2 = "0.01", "0.01"
coords1, coords2 = map(str, input().split(", "))
l = "map"


def search():
    maps_server = 'http://static-maps.yandex.ru/1.x/'
    map_params = {
        'll': coords2 + ',' + coords1,
        'spn': spn1 + ',' + spn2,
        'l': l}
    response = requests.get(maps_server, params=map_params)
    with open('map.png', 'wb') as f:
        f.write(response.content)
    image = pygame.image.load('map.png')
    os.remove('map.png')
    return image


def terminate():
    pygame.quit()
    sys.exit()


pygame.display.set_caption('YL-MAP')
img = search()
size = width, height = img.get_width(), img.get_height() + 50
screen = pygame.display.set_mode(size)
running = True
img = search()
FPS = 50
clock = pygame.time.Clock()
while running:
    screen.blit(img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()