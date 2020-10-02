import pygame
import time
import random
import shelve

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
bright_red = (255,0,0)
red = (200,0,0)
bright_green = (0,255,0) 
green = (0, 200, 0)
blue = (0,0,255)
purple = (255, 0, 255) 
random_colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))


tom = []


y_background = -600

One_or_Zero = ['How...'] 
Bad = ['My God!', 'Revolting', 'Pray for you Soul', 'Get Out!']
Ok = ['You Suck!', 'Game Over!', 'Wow You Trash!', 'My Eyes Bleed!', "I Can't Even"]
Decent = ['Decent','Not Bad', 'There may be Hope']
Good = ['... Well Played']

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A Bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png') 
backgroundImg = pygame.image.load('back1.png')
# car_backImg = pygame.image.load('Thom.jpg')
car_back1Img = pygame.image.load('images.png')
thingsImg = pygame.image.load('Thigns.png') 
thingw = 50
thingh = 100

pygame.display.set_icon(carImg) 
car_width = 54 
car_height = 81

def score (points):
    pygame.draw.rect(gameDisplay, white, [0,0,75,25])
    Font = pygame.font.SysFont(None,25)
    tom = 'Score: ' +str(points)
    text = Font.render(tom, True, black)
    gameDisplay.blit(text, (0,0))

def thing (himesha, thingy):    
    for hamesha in himesha: #Added this
        if thingy == -100:
            thingy = 0-random.randrange(100,500)
        gameDisplay.blit(thingsImg, (hamesha, thingy))         

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def background (changing):
    gameDisplay.blit(backgroundImg,(0,changing))

# def Car_Back ():
    # gameDisplay.blit(car_backImg,(0,0))

def Car_Back1 ():
    gameDisplay.blit(car_back1Img, (0,0))

def message_display(text, duration_sleep): 
    Text_Font = pygame.font.Font('Bubblegum.ttf',115)
    TextSurf = Text_Font.render(text, True, black)
    TextRect = TextSurf.get_rect()
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(duration_sleep)   
    


def gameover(points):
    global tom 
    tom.append(points) 
    d = shelve.open('highscore.txt')
    highscore = d['highscore']
    if highscore < max(tom):
        d['highscore'] = max(tom)
        d.close()
        highscore = max(tom) 
    
    Text_Font = pygame.font.Font('Bubblegum.ttf',75)
    if points == 0 or points == 1:
        TextSurf = Text_Font.render(random.choice(One_or_Zero), True, black)  
    elif points < 10:
        TextSurf = Text_Font.render(random.choice(Bad), True, black)
    elif points < 30:
        TextSurf = Text_Font.render(random.choice(Ok), True, black)
    elif points< 50:
        TextSurf = Text_Font.render(random.choice(Decent), True, black)
    else:
        TextSurf = Text_Font.render(random.choice(Good), True, black)
        
    TextRect = TextSurf.get_rect()
    TextRect.center = ((display_width/2),(200))
    gameDisplay.blit(TextSurf, TextRect)

    # Highscore                
    HighscoreFont = pygame.font.SysFont('Bubblegum.ttf',55)
    HighscoreSurf = HighscoreFont.render('HS: ' +str(highscore), True, black)
    HighscoreRect = HighscoreSurf.get_rect()
    HighscoreRect.center = (400,275)
    gameDisplay.blit(HighscoreSurf, HighscoreRect)

    # Points                  
    PointsFont = pygame.font.SysFont('Bubblegum.ttf',55)
    PointsSurf = PointsFont.render('Score: ' +str(points), True, black)
    PointsRect = PointsSurf.get_rect()
    PointsRect.center = (400,325)
    gameDisplay.blit(PointsSurf, PointsRect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        # Continue Button:
        button('Play Again?', 150,350, 120, 50, green, bright_green, game_loop, 20)  
        
        # Quit Button:
        button('Quit', 500,350,100,50, red, bright_red, Quit, 25)       
      

        pygame.display.update()

def Quit(): 
    pygame.quit()
    quit()
    
def button(msg, x, y, w, h, inactive_colour, active_colour, function, font_size):   

    pygame.draw.rect(gameDisplay, inactive_colour, [x,y,w,h])
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed() 
    if x < mouse[0] < x + w and y < mouse[1] < y + h:
        pygame.draw.rect(gameDisplay, active_colour, [x,y,w,h])
        if click[0] == 1:
            pygame.draw.rect(gameDisplay, white, [x,y,w,h])   
            function()
                        
    
    Button_Font = pygame.font.SysFont('comicsansms',font_size)
    ButtonSurf = Button_Font.render(msg, True, black)
    ButtonRect = ButtonSurf.get_rect()
    ButtonRect.center = ((x + (w/2)),(y + (h/2)))
    gameDisplay.blit(ButtonSurf, ButtonRect)

    
def unpause (): 
    global Pause
    Pause = False
    
def pause():    
    global Pause
    Pause = True

    Text_Font = pygame.font.Font('Bubblegum.ttf',115)    
    TextSurf = Text_Font.render('Paused', True, black)
    TextRect = TextSurf.get_rect()
    TextRect.center = ((display_width/2),(200))
    gameDisplay.blit(TextSurf, TextRect)
    while Pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:      
                if event.key == pygame.K_SPACE:
                    unpause()               
                
 
        # Continue Button:
        button('Continue', 150,350, 100, 50, green, bright_green, unpause, 20)  
        
        # Quit Button:
        button('Quit', 500,350,100,50, red, bright_red, Quit, 25)       
      

        pygame.display.update()
        



    

def game_title():
        Text_Font = pygame.font.Font('Sketch 3D.otf',115)
        TextSurf = Text_Font.render('A Bit Racey', True, black)
        TextRect = TextSurf.get_rect()
        TextRect.center = ((display_width/2),(300))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
    
def game_intro():   
    intro_intro = True
    intro = True

    while intro_intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        gameDisplay.fill(white)
        message_display('Pundir', 1)
        time.sleep(1)
        gameDisplay.fill(white)
        message_display('Presents', 1)
        time.sleep(1)
        gameDisplay.fill(white)
        game_title()
        time.sleep(1)
        intro_intro = False
    # Car_Back()
    Car_Back1()
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        game_title()
        game_title()

        # Green Button:
        button('GO!', 150,450, 100, 50, green, bright_green, game_loop, 25) 
        
        # Red Button:
        button('Quit',500,450,100,50, red, bright_red, Quit, 25)
        
        pygame.display.update()




def game_loop(): 
    global y_background
    x = int(display_width * 0.45)
    y = int(display_height * 0.8)


    thing_startx = random.randrange(0, display_width - thingw)
    x_list = [thing_startx] # Added this
    thing_starty = -600
    thing_speed = 13

    x_change = 0
    block_count = 1 # Added this

    points = 0  
    move_faster = 0


    game_Exit = False   
    while not game_Exit:
        # Events
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                message_display('Thank You', 1) 
                Quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -10 - move_faster 
                    
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = 10 + move_faster
                            
                if event.key == pygame.K_SPACE:   
                    pause()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
        

        x += x_change
    
        
        background(y_background)
        if y_background < 0:
            y_background += 9 
        else:
            y_background = -600
        # gameDisplay.fill(white)
        car(x,y)
        score(points) 



        thing(x_list, thing_starty)
        
        button('Pause', 730, 10, 50, 30, random_colour, purple, pause, 15) 
            
    
        thing_starty += thing_speed
        
        # Logics
        if x < 0 or x > (display_width - car_width): 
            gameover(points)   

        if thing_starty > display_height:   
            thing_starty = 0 - thingh
            x_list = []  # Added this
            
            for i in range(0,block_count):  # Added this
                thing_startx = random.randrange(0, display_width - thingw)
                x_list.append(thing_startx)
            
            points += 1   
            print('Ha missed me bitch')
            
            if points > 0:
                if points % 5 == 0:
                    thing_speed += 5
                    move_faster += 2

            if points > 0:  # Added this
                if points % 10 == 0:
                    if block_count < 10:
                        block_count += 1

        if thing_starty >= y - car_height: # Changed this
            for humesha in x_list:
                if humesha + thingw > x and humesha < x:
                    gameover(points)  
                elif humesha + thingw > x + car_width and humesha < x + car_width:
                    gameover(points)  

            
        pygame.display.update()
        clock.tick(30)

game_intro()  
Quit()
