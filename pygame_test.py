import pygame
import math
import random
# pygame setup
pygame.init()

awesomeWindowWidth=1000
awesomeWindowHeight=480

screen = pygame.display.set_mode((awesomeWindowWidth, awesomeWindowHeight))
clock = pygame.time.Clock()
running = True

buttonLeftImg=pygame.image.load('gui_resources\\button_left.png')
buttonMidImg=pygame.image.load('gui_resources\\button_middle.png')
buttonRightImg=pygame.image.load('gui_resources\\button_right.png')

ButtonFont = pygame.font.Font(r'C:\Windows\Fonts\msgothic.ttc', 14)
SmallFont = pygame.font.Font(r'C:\Windows\Fonts\msgothic.ttc', 12)

screenNWImg=pygame.image.load('gui_resources\\screen_NW.png')
screenNImg=pygame.image.load('gui_resources\\screen_N.png')
screenNEImg=pygame.image.load('gui_resources\\screen_NE.png')
screenEImg=pygame.image.load('gui_resources\\screen_E.png')
screenSEImg=pygame.image.load('gui_resources\\screen_SE.png')
screenSImg=pygame.image.load('gui_resources\\screen_S.png')
screenSWImg=pygame.image.load('gui_resources\\screen_SW.png')
screenWImg=pygame.image.load('gui_resources\\screen_W.png')

buttonNWImg=pygame.image.load('gui_resources\\button_NW.png')
buttonNImg=pygame.image.load('gui_resources\\button_N.png')
buttonNEImg=pygame.image.load('gui_resources\\button_NE.png')
buttonEImg=pygame.image.load('gui_resources\\button_E.png')
buttonSEImg=pygame.image.load('gui_resources\\button_SE.png')
buttonSImg=pygame.image.load('gui_resources\\button_S.png')
buttonSWImg=pygame.image.load('gui_resources\\button_SW.png')
buttonWImg=pygame.image.load('gui_resources\\button_W.png')

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

efxParams=[]

for i in range(20):
    efxParams.append(['EfxParam#'+(str(i).zfill(2)),0])
alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-=!@#$%^&*()_+~`{}|[]\\:";\'<>?,./ '

rolandFont=pygame.image.load('gui_resources\\RolandFontBG.png')

def renderRolandText(x,y,text):
    for _i in range(len(text)):
        chn=int(ord(text[_i]))
        char = pygame.Surface((5, 7))
        char.blit(rolandFont, (0, 0), (5*(chn % 16), 7*math.floor(chn/16), 5, 7))
        char=pygame.transform.scale(char,(10,14))
        screen.blit(char, (x+(11*_i),y))

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
    clicked=False
    if pygame.mouse.get_pressed()[0]:
        mousex,mousey=pygame.mouse.get_pos()
        if mousex>=x and mousex<=x+width:
            if mousey>=y and mousey<=y+28:
                clicked=True
    return clicked

def renderButtonBetter(x,y,width,height,text):
    pygame.draw.rect(screen, '#444444', (x+2,y+2,width-4,height-4))
    screen.blit(buttonNWImg, (x,y))
    
    for _i in range(round(width)-4):
        screen.blit(buttonNImg, (x+2+_i,y))
    screen.blit(buttonNEImg, (x+width-1,y))
    
    for _i in range(round(height)-5):
        screen.blit(buttonWImg, (x,y+2+_i))
        screen.blit(buttonEImg, (x+width-2,y+2+_i))

    screen.blit(buttonSWImg, (x,y+height-3))
    for _i in range(round(width)-6):
        screen.blit(buttonSImg, (x+3+_i,y+height-3))
    screen.blit(buttonSEImg, (x+width-3,y+height-3))

    
    clicked=False
    if pygame.mouse.get_pressed()[0]:
        mousex,mousey=pygame.mouse.get_pos()
        if mousex>=x and mousex<=x+width:
            if mousey>=y and mousey<=y+28:
                clicked=True
    return clicked

def renderScreen(x,y,width,height):
    pygame.draw.rect(screen, '#FF6A00', (x,y,width,height))
    screen.blit(screenNWImg, (x,y))
    
    for _i in range(round(width)-6):
        screen.blit(screenNImg, (x+3+_i,y))
    screen.blit(screenNEImg, (x+width-3,y))
    
    for _i in range(round(height)-6):
        screen.blit(screenWImg, (x,y+3+_i))
        screen.blit(screenEImg, (x+width-3,y+3+_i))

    screen.blit(screenSWImg, (x,y+height-3))
    for _i in range(round(width)-6):
        screen.blit(screenSImg, (x+3+_i,y+height-3))
    screen.blit(screenSEImg, (x+width-3,y+height-3))
    return False

screener='efxtype' #its only called screener because screen was taken idk
while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#333333")

    # RENDER YOUR GAME HERE
    #Render Main Menu at top
    buttoncolumns=3
    buttonwidth=150
    buttonpaddingx=8
    buttonpaddingy=4
    totalbuttonwidth=(buttonwidth+buttonpaddingx)*buttoncolumns
    totalbuttonheight=(28+buttonpaddingy)*math.ceil(len(buttons)/buttoncolumns)
    buttongroupx=(awesomeWindowWidth/2)-(totalbuttonwidth/2)
    buttongroupy=(awesomeWindowHeight/4)-(totalbuttonheight/2)
    
    for i in range(len(buttons)):
        buttonclicked=renderButton(buttongroupx+((buttonwidth+buttonpaddingx)*(i%buttoncolumns)),buttongroupy+((28+buttonpaddingy)*math.floor(i/buttoncolumns)),buttonwidth,buttons[i])
        if buttonclicked:
##         'Adjust global values',
##         'System Parameters',
##         'Reverb Settings',
##         'Delay Settings',
##         'Chorus Settings',
##         'Draw on the LCD',
##         'Write Text',
##         'Part Parameters',
##         'Scale Tuning']
            if i==0: screener='efx'
            if i==1: screener='efxtype'
            if i==2: screener='eq'
            if i==3: screener='sysreset'
            if i==4: screener='global'
            if i==5: screener='sysparam'
            if i==6: screener='reverb'
            if i==7: screener='delay'
            if i==8: screener='chorus'
            if i==9: screener='lcd'
            if i==10: screener='text'
            if i==11: screener='partparam'
            if i==12: screener='scaletuning'

    if screener=='mainmenu':
        pass #i dont need this if statemtn
    if screener=='efx':
        pass
    if screener=='efxtype':
        buttoncolumns=4
        buttonwidth=180
        buttonheight=20
        buttonpaddingx=64
        buttonpaddingy=4
        totalbuttonwidth=(buttonwidth+buttonpaddingx)*buttoncolumns
        totalbuttonheight=(28+buttonpaddingy)*math.ceil(len(buttons)/buttoncolumns)
        buttongroupx=(awesomeWindowWidth/2)-(totalbuttonwidth/2)
        buttongroupy=(awesomeWindowHeight/4)-(totalbuttonheight/2)+(awesomeWindowHeight/2)
        for i in range(len(efxParams)):
            _x=buttongroupx+((buttonwidth+buttonpaddingx)*(i%buttoncolumns))
            _y=buttongroupy+((buttonheight+buttonpaddingy)*math.floor(i/buttoncolumns))
            #renderButtonBetter(_x,_y,buttonwidth,buttonheight,'sacks')
            renderScreen(_x,_y,buttonwidth,buttonheight)
            renderScreen(_x+182,_y,40,buttonheight)
            renderButtonBetter(_x+184+40,_y,20,buttonheight/2,'sacks')
            renderButtonBetter(_x+184+40,_y+buttonheight/2+1,20,buttonheight/2,'sacks')
            text=efxParams[i][0]+':'+str(efxParams[i][1])
            renderRolandText(_x+3,_y+3,text)
            
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
