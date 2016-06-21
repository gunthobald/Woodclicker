import pygame
import common
import buymenue
# Define Images
woodImg = pygame.image.load("./bilder/Wood.png")
stoneImg = pygame.image.load("./bilder/Stone.png")
pickImg = pygame.image.load("./bilder/Pickaxe.png")
VillagerImg = pygame.image.load("./bilder/The_Player_Icon.png")


# Objects
class Material:
    def __init__(self, pos, textpos, size, image, cooldown):
        self.pos = pos
        self.textpos = textpos
        self.size = size
        self.image = image
        self.amount = 0
        self.cooldown = cooldown
        self.cooldown2 = 1
        self.color = [0, 255, 0]

    def color_percent(self):
        color_percent = float(self.cooldown2) / self.cooldown
        red = 255 * color_percent
        green = 255 - red
        self.color = [int(red), int(green), 0]

    def draw_resource(self):
        common.screen.blit(self.image, self.pos)
        font = pygame.font.Font(None, 44)
        text = font.render(str(self.amount), 100, self.color)
        common.screen.blit(text, self.textpos)
        self.cooldown2 -= 1
        if self.cooldown2 <= 1:
            self.cooldown2 = 1

    def click(self):
        collision = common.aabb(pygame.mouse.get_pos(), [0, 0], self.pos, self.size)
        if collision:
            if self.cooldown2 <= 1:
                self.amount += 1
                self.cooldown2 = self.cooldown

# define resources
Wood = Material([350, 150], [400, 150], [48, 48], woodImg, 20)
Stone = Material([350, 225], [400, 225], [48, 48], stoneImg, 100)
Tool = Material([350, 300], [400, 300], [48, 48], pickImg, 200)
People = Material([350, 375], [400, 375], [48, 48], VillagerImg, 500)

House = buymenue.Object([1000, 30], [500, 120], buymenue.houseImg, [40, 20, 10, 0], [[1115, 30], [1115, 60], [1115, 90]
                                                                                     ], [Wood, Stone, Tool, People])


def draw_resources():
    Wood.color_percent()
    Stone.color_percent()
    Tool.color_percent()
    Wood.draw_resource()
    Stone.draw_resource()
    Tool.draw_resource()
    People.draw_resource()


def click():
    Wood.click()
    Stone.click()
    Tool.click()


def draw_house():
    for n in range(3):
        House.draw_color(n)
        House.draw_text(n)
