import pygame
import pages
import platform

pygame.init()
pygame.font.init()
# index.init()

screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_height, screen_width))
background = pygame.image.load("icons/background.jpg")
screen.blit(background, (0, 0))
clock = pygame.time.Clock()
pygame.display.set_caption("System Data")
end = False

########## INDEX PAGE ##########

system_icon = pygame.image.load("icons/system_icon.png").convert_alpha()
system_icon = pygame.transform.scale(system_icon, (80, 80))
network_icon = pygame.image.load("icons/network_icon.png").convert_alpha()
network_icon = pygame.transform.scale(network_icon, (80, 80))
cpu_icon = pygame.image.load("icons/cpu_icon.png").convert_alpha()
cpu_icon = pygame.transform.scale(cpu_icon, (80, 80))
memory_icon = pygame.image.load("icons/memory_icon.png").convert_alpha()
memory_icon = pygame.transform.scale(memory_icon, (80, 80))
back_icon = pygame.image.load("icons/back_icon.png").convert_alpha()
back_icon = pygame.transform.scale(back_icon, (40, 40))
disk_icon = pygame.image.load("icons/disk_icon.png")
disk_icon = pygame.transform.scale(disk_icon, (80, 80))
overview_icon = pygame.image.load("icons/overview_icon.png")
overview_icon = pygame.transform.scale(overview_icon, (80, 80))
font = pygame.font.SysFont('DS-DIGI.TFF', 24, False, False)

global back_button, system_button, network_button, disk_button, cpu_button, memory_button, overview_button
back_button = {'image': back_icon, 'rect': pygame.Rect(screen_width / 32, 20, 40, 40)}
system_button = {'image': system_icon, 'rect': pygame.Rect(screen_width / 4, 100, 80, 80)}
network_button = {'image': network_icon, 'rect': pygame.Rect(screen_width / 2, 100, 80, 80)}
disk_button = {'image': disk_icon, 'rect': pygame.Rect((screen_width / 4) * 3, 250, 80, 80)}
cpu_button = {'image': cpu_icon, 'rect': pygame.Rect((screen_width / 4) * 3, 100, 80, 80)}
memory_button = {'image': memory_icon, 'rect': pygame.Rect(screen_width, 100, 80, 80)}
overview_button = {'image': overview_icon, 'rect': pygame.Rect(screen_width / 2, 250, 80, 80)}


def index():
    screen.blit(system_button['image'], (screen_width / 4, 100))
    text = font.render("System info", True, (0, 220, 0))
    screen.blit(text, (screen_width / 4, 80))

    screen.blit(network_button['image'], (screen_width / 2, 100))
    text = font.render("Network info", True, (0, 220, 0))
    screen.blit(text, (screen_width / 2, 80))

    screen.blit(cpu_button['image'], ((screen_width / 4) * 3, 100))
    text = font.render("  CPU info", True, (0, 220, 0))
    screen.blit(text, ((screen_width / 4) * 3, 80))

    screen.blit(memory_button['image'], (screen_width, 100))
    text = font.render("Memory info", True, (0, 220, 0))
    screen.blit(text, (screen_width, 80))

    screen.blit(overview_button['image'], (screen_width / 2, 250))
    text = font.render("  Overview", True, (0, 220, 0))
    screen.blit(text, (screen_width / 2, 230))

    screen.blit(disk_button['image'], ((screen_width / 4) * 3, 250))
    text = font.render("   Disk info", True, (0, 220, 0))
    screen.blit(text, ((screen_width / 4) * 3, 230))


################################

index()
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()

            ### INDEX PAGE COLLISION ###

            if system_button['rect'].collidepoint(pos):
                screen.fill((255, 0, 0))
                screen.blit(background, (0, 0))
                screen.blit(back_button['image'], (screen_width / 32, 20))
                pages.system()
            elif network_button['rect'].collidepoint(pos):
                screen.fill((255, 0, 0))
                screen.blit(background, (0, 0))
                screen.blit(back_button['image'], (screen_width / 32, 20))
                pages.network()
            elif cpu_button['rect'].collidepoint(pos):
                screen.fill((255, 0, 0))
                screen.blit(background, (0, 0))
                screen.blit(back_button['image'], (screen_width / 32, 20))
                pages.cpu()
            elif disk_button['rect'].collidepoint(pos):
                screen.fill((255, 0, 0))
                screen.blit(background, (0, 0))
                screen.blit(back_button['image'], (screen_width / 32, 20))
                pages.disk()
            elif overview_button['rect'].collidepoint(pos):
                screen.fill((255, 0, 0))
                screen.blit(background, (0, 0))
                screen.blit(back_button['image'], (screen_width / 32, 20))
                pages.overview()
            elif memory_button['rect'].collidepoint(pos):
                screen.fill((255, 0, 0))
                screen.blit(background, (0, 0))
                screen.blit(back_button['image'], (screen_width / 32, 20))
                pages.memory()
            elif back_button['rect'].collidepoint(pos):
                screen.fill((255, 0, 0))
                screen.blit(background, (0, 0))
                index()

    pygame.display.update()
    clock.tick(60)
pygame.display.quit()
