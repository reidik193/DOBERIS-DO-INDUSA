import pygame
from random import *
import time
pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill((38, 128, 184))
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
elov = 25555, 44354, 30
krasniu = (255, 0, 0)
green = (0, 255, 0)
start_time = time.time()
cur_time = start_time
class area():
    def __init__(self, x=0, y=0, width = 10, height= 50, color=(2555, 1241, 2345)):
        self.rect = pygame.Rect(x, y, width, height) 
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def outlane(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)
    def point(self, x, y):
        return self.rect.collidepoint(x, y)
class label(area):
    def set_text(self, text, fsize = 12, text_color=BLACK):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shift_x = 0, shift_y = 0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
kapTochki = list()
num_kapTochki = 4
x = 70
for i in range(num_kapTochki):
    new_kapTochka = label(x, 170, 70, 100, (255, 255, 30))
    new_kapTochka.outlane((255, 255, 255), 10)
    new_kapTochka.set_text('KICK ME', 25)
    kapTochki.append(new_kapTochka)
    x += 100
wait = 0
c7676767chetchik76767667 = label(-10, -20, 190, 70, krasniu)
c7676767chetchik76767667.set_text('BpeMec', 67, BLACK)

da_tbl_shuesh = label(300, -10, 170, 50, krasniu)
da_tbl_shuesh.set_text('CcheT', 67, BLACK)
#Самойло Александр,
#19:24
timer = label(50,55,50,40, (38, 128, 184))
timer.set_text('0', 40, BLACK)
timer.draw(0,0)

score = label(430,55,50, 40, (38, 128, 184))
score.set_text('0', 40, BLACK)
score.draw(0,0)

Tbi_npoNgpal = label(150,25,50, 40, krasniu)
Tbi_npoNgpal.set_text('ТЫ ПРОИГРАЛ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', 67, BLACK)
points = 0
mne_len_pisat = label(250,25,50, 40, krasniu)
mne_len_pisat.set_text('ТЫ ВЫИГРАЛ.', 67, BLACK)

while True:
    window.fill((38, 128, 184))
    if wait == 0:
        wait = 30
        click = randint(1, num_kapTochki)
    else:
        wait -= 1
    for i in range(num_kapTochki):
        kapTochki[i].color(elov)
        if (i + 1) == click:
            kapTochki[i].draw(0.7, 40)
            
        else:
            kapTochki[i].fill()    
        kapTochki[i].outlane((255, 255, 255), 5)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i in range(num_kapTochki):
                if kapTochki[i].point(x, y):
                    if i + 1 == click:
                        kapTochki[i].color(green)
                        points += 1
                    else:
                        kapTochki[i].color(krasniu) 
                        points -= 1
                    kapTochki[i].fill()
    new_time = time.time()
    if new_time - cur_time >= 1:
        timer.set_text(str(int(new_time - start_time)), 40, BLACK)
    score.set_text(str(points), 40, BLACK)
    c7676767chetchik76767667.draw(20, 20)
    da_tbl_shuesh.draw(5, 10)
    score.draw(0, 0)
    timer.draw(0, 0)
    if new_time - start_time >= 11 or points <= -1:
        window.fill((255, 0, 0))
        Tbi_npoNgpal.draw(-150, 250)
    if points >= 5:      
        window.fill((0, 255, 0))
        mne_len_pisat.draw(-150, 250)
        mne_len_pisat2 = label(150,267,50, 40, krasniu)
        mne_len_pisat2.set_text('время прох.' + str(int(new_time - start_time)), 67, BLACK)
        mne_len_pisat2.draw(0, 0)
    pygame.display.update()
    clock.tick(60)
