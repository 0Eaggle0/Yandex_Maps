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


def change_spn(flag):
    global spn1, spn2
    if flag:
        preres = float(spn1) * 2, float(spn2) * 2
    else:
        preres = float(spn1) / 2, float(spn2) / 2
    if 0.0001 < preres[0] < 0.1 and 0.0001 < preres[1] < 0.05:
        spn1, spn2 = [str(i) for i in preres]


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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEDOWN:
                change_spn(True)
            elif event.key == pygame.K_PAGEUP:
                change_spn(False)
            img = search()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()