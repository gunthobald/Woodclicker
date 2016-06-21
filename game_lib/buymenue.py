import pygame
import common
pygame.init()

buymenue_overlay = pygame.image.load("./bilder/buymenu.png")
houseImg = pygame.image.load("./bilder/haus.png")


class Object:
    def __init__(self, pos, size, image, cost, textpos, amounts):
        self.pos = pos
        self.textpos = textpos
        self.size = size
        self.image = image
        self.cost = cost
        self.amount = 0
        self.resources_amount = amounts
        self.color = [[255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]]
        self.string = ["Wood: ", "Stone: ", "Tools: ", "People: "]

    def draw_object(self):
        common.screen.blit(self.image, self.pos)

    def draw_color(self, n):
        if self.resources_amount[n].amount >= self.cost[n]:
            self.color[n] = [0, 255, 0]

    def draw_text(self, n):
        font = pygame.font.Font(None, 22)
        text = font.render(self.string[n], 100, self.color[n])
        common.screen.blit(text, self.textpos[n])
        text2 = font.render(str(self.resources_amount[n].amount), 100, self.color[n])
        common.screen.blit(text2, [self.textpos[n][0] + 60, self.textpos[n][1]])

    def click(self, n):
        collision = common.aabb(pygame.mouse.get_pos(), [0, 0], self.pos, self.size)
        if collision:
            resources = self.resources_amount
            resources[n] -= self.cost[n]
            self.resources_amount = resources

