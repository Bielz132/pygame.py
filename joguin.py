import pygame, os, sys,random

pygame.init()
tela = pygame.display.set_mode((500,500))
teste = True
while teste:
  for event in pygame.event.get():
    if event.type == pygame.quit:
      #pygame.quit()
      pass