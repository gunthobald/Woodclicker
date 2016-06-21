import pygame
from game_lib import *
pygame.init()


# Main program
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            resources.click()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                buymenu_activated = True

                while buymenu_activated:
                    for buy_event in pygame.event.get():
                        if buy_event.type == pygame.KEYDOWN:
                            if buy_event.key == pygame.K_TAB:
                                buymenu_activated = False

                        if buy_event.type == pygame.QUIT:
                            run = False
                            buymenu_activated = False

                        if buy_event.type == pygame.MOUSEMOTION:
                            collision = common.aabb(pygame.mouse.get_pos(), [0, 0], [960, 0], [135, 135])
                            if collision:
                                for i in range(2):
                                    resources.House.click(i)
                        common.screen.blit(buymenue.buymenue_overlay, [0, 0])
                        resources.House.draw_object()
                        resources.draw_house()
                        pygame.display.flip()

    common.screen.fill([255, 255, 255])
    resources.draw_resources()
    pygame.display.flip()
    common.clock.tick(60)

pygame.quit()
