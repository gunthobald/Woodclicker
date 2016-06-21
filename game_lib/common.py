import pygame
pygame.init()

screen = pygame.display.set_mode([1920, 1080], pygame.RESIZABLE)
screen.fill([255, 255, 255])
pygame.display.set_caption("Rohstoffe")
clock = pygame.time.Clock()


def aabb(pos1, size1, pos2, size2):
    collision = False
    if pos1[0] > pos2[0] and pos1[0] + size1[0] < pos2[0] + size2[0]:
        if pos1[1] > pos2[1] and pos1[1] + size1[1] < pos2[1] + size2[1]:
            collision = True
    return collision
