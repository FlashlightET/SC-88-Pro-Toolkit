import pygame
import math
import random
# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

buttonLeftImg=pygame.image.load('gui_resources\\button_left.png')
buttonMidImg=pygame.image.load('gui_resources\\button_middle.png')
buttonRightImg=pygame.image.load('gui_resources\\button_right.png')
ButtonFont = pygame.font.Font(r'C:\Windows\Fonts\msgothic.ttc', 14)

buttons=['Turn on EFX',
         'Set the EFX type',
         'EQ Settings',
         'Send a System Reset',
         'Adjust global values',
         'System Parameters',
         'Reverb Settings',
         'Delay Settings',
         'Chorus Settings',
         'Draw on the LCD',
         'Write Text',
         'Part Parameters',
         'Scale Tuning']

alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-=!@#$%^&*()_+~`{}|[]\\:";\'<>?,./ '

def renderButton(x,y,width,text):
    screen.blit(buttonLeftImg, (x,y))
    for _i in range(width-6):
        screen.blit(buttonMidImg, (x+3+_i,y))
    screen.blit(buttonRightImg, (x+width-3,y))
    img = ButtonFont.render(text, False, '#ffffff')
    #textSize=len(text)*7
    textSize=0
    for _i in text:
        if _i in alphabet:
            textSize+=7
        else:
            textSize+=14
    screen.blit(img, (x+(width/2)-(textSize/2)+1, y+5))
    return False
while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#333333")

    # RENDER YOUR GAME HERE
    buttoncolumns=3
    buttonwidth=150
    buttonpaddingx=8
    buttonpaddingy=4
    totalbuttonwidth=(buttonwidth+buttonpaddingx)*buttoncolumns
    totalbuttonheight=(28+buttonpaddingy)*math.ceil(len(buttons)/buttoncolumns)
    buttongroupx=320-(totalbuttonwidth/2)
    buttongroupy=240-(totalbuttonheight/2)
    
    for i in range(len(buttons)):
        buttonclicked=renderButton(buttongroupx+((buttonwidth+buttonpaddingx)*(i%buttoncolumns)),buttongroupy+((28+buttonpaddingy)*math.floor(i/buttoncolumns)),buttonwidth,buttons[i])

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
