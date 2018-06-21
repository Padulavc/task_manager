import psutil
import platform
import cpuinfo
import pygame



screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.font.init()
font = pygame.font.SysFont('DS-DIGI.TFF', 24, False, False)

def use_bar(total, text, height):
    pygame.font.init()
    width = screen_width - 40
    pygame.draw.rect(screen, (0, 20, 0), (20, height, width, 40))
    width = width * total / 100
    pygame.draw.rect(screen, (0, 220, 0), (20, height, width, 40))
    text = font.render(text, False, (0, 220, 0))
    screen.blit(text, (20, (height - 20)))


def memory():
    mem = psutil.virtual_memory()
    mem_total_human = round(mem.total / (1024 * 1024 * 1024), 2)
    text = 'Total Memory : %  GB' % mem_total_human
    mem_using = mem.used
    text1 = font.render('Total Memory:', True, (0, 220, 0))
    screen.blit(text1, (screen_width / 32, 80))
    text2 = font.render('Used Memory:', True, (0, 220, 0))
    screen.blit(text2, (screen_width / 32, 100))
    use_bar(mem_using, text, 200)


def cpu():
    info_cpu = cpuinfo.get_cpu_info()
    brand = info_cpu['brand']
    word = str(info_cpu['bits'])
    cores_all = psutil.cpu_count()
    cores_physical = psutil.cpu_count(logical=False)
    cores_logical = cores_all - cores_physical
    cores_all = str(cores_all)
    cores_logical = str(cores_logical)
    cores_physical = str(cores_physical)
    freq = psutil.cpu_freq()
    freq_str = str(freq)
    freq_current = psutil.cpu_freq().current
    arch = info_cpu['arch']
    cpu_use = psutil.cpu_percent()
    text1 = font.render('Brand:', True, (0, 220, 0))
    text2 = font.render('Architecture:', True, (0, 220, 0))
    text3 = font.render('CPU word:', True, (0, 220, 0))
    text4 = font.render('Cores:', True, (0, 220, 0))
    text5 = font.render('Cores(logical):', True, (0, 220, 0))
    text6 = font.render('Frequency:', True, (0, 220, 0))
    info1 = font.render(brand, False, (0, 220, 0))
    info2 = font.render(arch, False, (0, 220, 0))
    info3 = font.render(word, False, (0, 220, 0))
    info4 = font.render(cores_all, False, (0, 220, 0))
    info5 = font.render(cores_logical, False, (0, 220, 0))
    info6 = font.render(freq_str, False, (0, 220, 0))
    screen.blit(text1, (screen_width / 32, 80))
    screen.blit(text2, (screen_width / 32, 100))
    screen.blit(text3, (screen_width / 32, 120))
    screen.blit(text4, (screen_width / 32, 140))
    screen.blit(text5, (screen_width / 32, 160))
    screen.blit(text6, (screen_width / 32, 180))
    screen.blit(info1, (screen_width / 4, 80))
    screen.blit(info2, (screen_width / 4, 100))
    screen.blit(info3, (screen_width / 4, 120))
    screen.blit(info4, (screen_width / 4, 140))
    screen.blit(info5, (screen_width / 4, 160))
    screen.blit(info6, (screen_width / 4, 180))
    use_bar(cpu_use, 'CPU use', 250)


def disk():
    disk = psutil.disk_usage('.')
    disk_total =  str(round(disk.total/(1024*1024*1024), 2))
    disk_use = str(round(disk.used/(1024*1024*1024), 2))
    disk_free = str(round(disk.free/(1024*1024*1024), 2))
    text1 = font.render('Total Disk space:', True, (0, 220, 0))
    text2 = font.render('Disk using:', True, (0, 220, 0))
    text3 = font.render('Free space:', True, (0, 220, 0))
    text4 = font.render(disk_total, True, (0, 220, 0))
    text5 = font.render(disk_use, True, (0, 220, 0))
    text6 = font.render(disk_free, True, (0, 220, 0))
    screen.blit(text1, (screen_width / 32, 80))
    screen.blit(text2, (screen_width / 32, 100))
    screen.blit(text3, (screen_width / 32, 120))
    screen.blit(text4, (screen_width / 4, 80))
    screen.blit(text5, (screen_width / 4, 100))
    screen.blit(text6, (screen_width / 4, 120))

def overview():
    text1 = font.render('OVERVIEW PAGE UNDER CONSTRUCTION', True, (0, 220, 0))
    screen.blit(text1, (screen_width / 32, 80))


def system():
    text1 = font.render('SYSTEM PAGE UNDER CONSTRUCTION', True, (0, 220, 0))
    screen.blit(text1, (screen_width / 32, 80))


def network():
    text1 = font.render('NETWORK PAGE UNDER CONSTRUCTION', True, (0, 220, 0))
    screen.blit(text1, (screen_width / 32, 80))