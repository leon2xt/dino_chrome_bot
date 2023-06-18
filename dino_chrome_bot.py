#!/usr/bin/python

'''
Dino Chrome Game Bot - Guilherme Junqueira

Python Basico Solyd
https://solyd.com.br/treinamentos
'''

import time

from PIL import ImageGrab
import pyautogui


# Região de coordenadas
# Coordenadas para a resolução 1600x900
X = 655.0  # X2 = X + 15
Y1 = 215
Y2 = 250


# Tira um printscreen da tela usando o  PIL lib
def capture_screen():
    screen = ImageGrab.grab()
    return screen


# Detecta o inimigo por diferença na cor do pixel na região de detecções
def detect_enemy(screen):
    aux_color = screen.getpixel((int(X), Y1))
    for x in range(int(X), int(X+15)):
        for y in range(Y1, Y2):
            color = screen.getpixel((x, y))
            if color != aux_color:
                return True # Return True for a detected enemy
            else:
                aux_color = color


# Dino Pulo
def jump():
    global X
    pyautogui.press("up")
    X += 0.4  # Increment in detection region for increase speed of game


print("Start in 3 seconds...")
time.sleep(3)

# Loop infinito do bot
while True:
    screen = capture_screen()
    if detect_enemy(screen):
        jump()

