
# Imports
import pygame
import intersects
import time

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
screen_walls = pygame.Surface(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60
pop_up_speedup_timer = 0
master_timer = 60
times = 0

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (150, 0, 150)

#Music
route = pygame.mixer.music.load("menu.ogg")
boom = pygame.mixer.Sound('boom.ogg')
shot = pygame.mixer.Sound('shot.ogg')

# Make a player
player1 =  [25, 25, 25, 25]
player2 =  [25, 25, 25, 25]
vel1 = [0, 0]
vel2 = [0, 0]
player1_speed = 5
player2_speed = 5
score1 = 0

#stages
status = 0
start = 0
play = 1
end = 2
pause = 3
stage = 4
leaderboard = 5
choice = 0
ch_p1 = 0
ch_p2 = 1
check_name = False
brick_gone = False
is_bomb = True

# make walls
edge1 =  [0, 0, 375, 25]
edge2 =  [0, 0, 25, 600]
edge3 =  [775, 0, 25, 600]
edge4 =  [0, 575, 375, 25]
edge5 =  [425, 0, 375, 25]
edge6 =  [425, 575, 375, 25]
wall1 =  [25, 50, 200, 25]
wall2 =  [250, 50, 25, 100]
wall3 =  [175, 150, 100, 25]
wall4 =  [125, 125, 75, 25]
wall5 =  [125, 125, 25, 150]
wall6 =  [175, 100, 50, 25]
wall7 =  [50, 100, 25, 400]
wall8 =  [75, 100, 25, 25]
wall9 =  [100, 150, 25, 25]
wall10 =  [75, 200, 25, 25]
wall11 =  [100, 250, 25, 50]
wall12 =  [50, 525, 25, 50]
wall13 =  [75, 325, 100, 25]
wall14 =  [300, 50, 25, 125]
wall15 =  [150, 200, 75, 25]
wall16 =  [175, 250, 100, 25]
wall17 =  [150, 300, 125, 25]
wall18 =  [200, 350, 100, 25]
wall19 =  [100, 525, 200, 25]
wall20 =  [100, 475, 225, 25]
wall21 =  [100, 425, 175, 25]
wall22 =  [100, 350, 25, 100]
wall23 =  [300, 400, 25, 100]
wall24 =  [250, 375, 25, 25]
wall25 =  [200, 400, 25, 25]
wall26 =  [150, 375, 25, 25]
wall27 =  [300, 50, 150, 25]
wall28 =  [475, 50, 25, 250]
wall29 =  [300, 275, 150, 25]
wall30 =  [350, 100, 100, 25]
wall31 =  [350, 100, 25, 150]
wall32 =  [400, 225, 50, 25]
wall33 =  [425, 150, 25, 75]
wall34 =  [375, 150, 25, 25]
wall35 =  [300, 200, 25, 175]
wall36 =  [250, 200, 50, 25]
wall37 =  [350, 325, 150, 25]
wall38 =  [350, 375, 25, 25]
wall39 =  [400, 375, 25, 75]
wall40 =  [350, 425, 50, 25]
wall41 =  [350, 475, 25, 75]
wall42 =  [325, 525, 25, 25]
wall43 =  [400, 475, 100, 25]
wall44 =  [450, 375, 25, 75]
wall45 =  [450, 525, 300, 25]
wall46 =  [400, 525, 25, 25]
wall47 =  [525, 50, 25, 250]
wall48 =  [500, 325, 25, 100]
wall49 =  [500, 425, 50, 25]
wall50 =  [525, 450, 75, 25]
wall51 =  [525, 500, 25, 25]
wall52 =  [575, 475, 25, 25]
wall53 =  [625, 375, 25, 125]
wall54 =  [575, 375, 25, 50]
wall55 =  [550, 375, 25, 25]
wall56 =  [550, 325, 75, 25]
wall57 =  [575, 150, 25, 150]
wall58 =  [550, 50, 100, 25]
wall59 =  [575, 100, 50, 25]
wall60 =  [575, 150, 75, 25]
wall61 =  [650, 50, 25, 75]
wall62 =  [625, 200, 25, 100]
wall63 =  [700, 100, 50, 25]
wall64 =  [700, 25, 25, 50]
wall65 =  [750, 50, 25, 25]
wall66 =  [675, 150, 50, 25]
wall67 =  [750, 150, 25, 25]
wall68 =  [675, 200, 25, 25]
wall69 =  [725, 200, 25, 200]
wall70 =  [675, 250, 50, 25]
wall71 =  [675, 300, 25, 100]
wall72 =  [650, 325, 25, 25]
wall73 =  [675, 425, 75, 25]
wall74 =  [675, 475, 25, 25]
wall75 =  [725, 475, 25, 25]



walls = [edge1, edge2, edge3, edge4, edge5, edge6, wall1, wall2,
         wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10,
         wall11, wall12, wall13, wall14, wall15, wall16, wall17,
         wall18, wall19, wall20, wall21, wall22, wall23, wall24,
         wall25, wall26, wall27, wall28, wall29, wall30, wall31,
         wall32, wall33, wall34, wall35, wall36, wall37, wall38,
         wall39, wall40, wall41, wall42, wall43, wall44, wall45,
         wall46, wall47, wall48, wall49, wall50, wall51, wall52,
         wall53, wall54, wall55, wall56, wall57, wall58, wall59,
         wall60, wall61, wall62, wall63, wall64, wall65, wall66,
         wall67, wall68, wall69, wall70, wall71, wall72, wall73,
         wall74, wall75]

brick1 = [375, 0, 25, 25]
brick2 = [400, 0, 25, 25]
brick3 = [450, 50, 25, 25]
brick4 = [500, 125, 25, 25]
brick5 = [425, 125, 25, 25]
brick6 = [325, 200, 25, 25]
brick7 = [375, 575, 25, 25]
brick8 = [400, 575, 25, 25]
brick9 = [250, 175, 25, 25]
brick10 = [575, 125, 25, 25]
brick11 = [725, 25, 25, 25]
brick12 = [600, 175, 25, 25]
brick13 = [625, 300, 25, 25]
brick14 = [75, 400, 25, 25]
brick15 = [125, 500, 25, 25]
brick16 = [350, 350, 25, 25]
brick17 = [600, 500, 25, 25]
brick18 = [650, 450, 25, 25]

bricks = [brick1, brick2, brick3, brick4, brick5, brick6, brick7,
          brick8, brick9, brick10, brick11, brick12, brick13, brick14,
          brick15, brick16, brick17, brick18]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [275, 250, 25, 25]
coin4 = [600, 400, 25, 25]
coin5 = [750, 500, 25, 25]
coin6 = [475, 400, 25, 25]
coin7 = [25, 150, 25, 25]
coin8 = [25, 300, 25, 25]
coin9 = [25, 450, 25, 25]
coin10 = [150, 25, 25, 25]
coin11 = [300, 25, 25, 25]
coin12 = [450, 25, 25, 25]
coin13 = [600, 25, 25, 25]
coin14 = [125, 75, 25, 25]
coin15 = [75, 150, 25, 25]
coin16 = [75, 275, 25, 25]
coin17 = [150, 250, 25, 25]
coin18 = [225, 325, 25, 25]
coin19 = [125, 375, 25, 25]
coin20 = [200, 450, 25, 25]
coin21 = [200, 500, 25, 25]
coin22 = [200, 550, 25, 25]
coin23 = [275, 400, 25, 25]
coin24 = [350, 550, 25, 25]
coin25 = [500, 550, 25, 25]
coin26 = [650, 550, 25, 25]
coin27 = [550, 475, 25, 25]
coin28 = [700, 450, 25, 25]
coin29 = [750, 300, 25, 25]
coin30 = [725, 175, 25, 25]
coin31 = [650, 175, 25, 25]
coin32 = [700, 275, 25, 25]
coin33 = [700, 400, 25, 25]
coin34 = [575, 75, 25, 25]
coin35 = [500, 100, 25, 25]
coin36 = [500, 200, 25, 25]
coin37 = [500, 300, 25, 25]
coin38 = [275, 175, 25, 25]
coin39 = [375, 300, 25, 25]
coin40 = [375, 450, 25, 25]

coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8,
         coin9, coin10, coin11, coin12, coin13, coin14, coin15,
         coin16, coin17, coin18, coin19, coin20, coin21, coin22,
         coin23, coin24, coin25, coin26, coin27, coin28, coin29,
         coin30, coin31, coin32, coin33, coin34, coin35, coin36,
         coin37, coin38, coin39, coin40]

speed1 = [750, 25, 25, 25]
speed2 = [75, 350, 25, 25]

speed_ups = [speed1, speed2]

slow1 = [150, 150, 25, 25]
slow2 = [600, 250, 25, 25]

slow_time = [slow1, slow2]

bomb1 = [750, 550, 25, 25]

def check_collide(collidebles, player, vel):
    ''' resolve collisions horizontally '''
    for c in collidebles:
        if intersects.rect_rect(player, c):        
            if vel[0] > 0:
                player[0] = c[0] - player[2]
            elif vel[0] < 0:
                player[0] = c[0] + c[2]

    ''' move the player in vertical direction '''
    player[1] += vel[1]
    
    ''' resolve collisions vertically '''
    for c in collidebles:
        if intersects.rect_rect(player, c):                    
            if vel[1] > 0:
                player[1] = c[1] - player[3]
            if vel[1]< 0:
                player[1] = c[1] + c[3]

def load_leaderboards():
    with open('high_scores.txt', 'r') as f:
        leaders = f.read().splitlines()
    leaders.sort()
    return leaders

leaders = load_leaderboards()


for w in walls:
    wall = pygame.image.load('wall.png')
    for y in range(w[1], w[1]+w[3], 25):
        for x in range(w[0], w[0] + w[2], 25):
            loc = x, y
            screen_walls.blit(wall, loc)

# Game loop
pygame.mixer.music.play(0)

win = False
lose = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # timers    
    times += 1
    if times > 60:
        times = 0
        if status == play and not lose:
            master_timer -= 1
        pop_up_speedup_timer -= 1

    pressed = pygame.key.get_pressed()

    # inputs and checks for stages
    start_to_play = pressed[pygame.K_SPACE]
    rshift = pressed[pygame.K_RSHIFT]
    lshift = pressed[pygame.K_LSHIFT]
    pause_b = pressed[pygame.K_p]
    p1 = pressed[pygame.K_1]
    p2 = pressed[pygame.K_2]

    if status == start:
        if start_to_play:
            status = stage

    if status == stage:
        if p1:
            choice = ch_p1
            status = play
        elif p2:
            choice = ch_p2
            status = play

    if status == play:
        if master_timer == 0:
            lose = True
            status = end

    if brick_gone:
        bricks = []

    if status == end and win:
        while not check_name:
            name = input("What's your name?")
            if len(name) >= 1 and len(name) <= 8:
                check_name = True
            else:
                print('Put a name between 1 and 8 characters')
        if check_name:
            if start_to_play:
                win = False
                lose = False
                with open ('high_scores.txt', 'w') as f:
                    f.write(str(master_timer) + " - " + name + "\n")
                    for score in leaders:
                        f.write(str(score) + "\n")
                status = leaderboard
    elif status == end and lose:
        if start_to_play:
            lose = False
            win = False
            status = leaderboard

    if status == leaderboard:
        if rshift or lshift:
            coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8,
         coin9, coin10, coin11, coin12, coin13, coin14, coin15,
         coin16, coin17, coin18, coin19, coin20, coin21, coin22,
         coin23, coin24, coin25, coin26, coin27, coin28, coin29,
         coin30, coin31, coin32, coin33, coin34, coin35, coin36,
         coin37, coin38, coin39, coin40]
            speed_ups = [speed1, speed2]
            bricks = [brick1, brick2, brick3, brick4, brick5, brick6, brick7,
          brick8, brick9, brick10, brick11, brick12, brick13, brick14,
          brick15, brick16, brick17, brick18]
            slow_time = [slow1, slow2]
            is_bomb = True
            score1 = 0
            player1 = [25,25,25,25]
            player2 = [25,25,25,25]
            player1_speed = 5
            player2_speed = 5
            master_timer = 60
            choice = 0
            check_name = False
            brick_gone = False
            status = start

    #moving the player
    up = pressed[pygame.K_UP]
    down = pressed[pygame.K_DOWN]
    left = pressed[pygame.K_LEFT]
    right = pressed[pygame.K_RIGHT]

    if choice == ch_p2:
        up2 = pressed[pygame.K_w]
        down2 = pressed[pygame.K_s]
        left2 = pressed[pygame.K_a]
        right2 = pressed[pygame.K_d]

    if status == play:
        if left:
            vel1[0] = -player1_speed
        elif right:
            vel1[0] = player1_speed
        else:
            vel1[0] = 0
        if up:
            vel1[1] = -player1_speed
        elif down:
            vel1[1] = player1_speed
        else:
            vel1[1] = 0

        if choice == ch_p2:
            if left2:
                vel2[0] = -player2_speed
            elif right2:
                vel2[0] = player2_speed
            else:
                vel2[0] = 0

            if up2:
                vel2[1] = -player2_speed
            elif down2:
                vel2[1] = player2_speed
            else:
                vel2[1] = 0
        
        
    # Game logic (Check for collisions, update points, etc.)
    left = player1[0]
    right = player1[0] + player1[2]
    top = player1[1]
    bottom = player1[1] + player1[3]

    left2 = player2[0]
    right2 = player2[0] + player2[2]
    top2 = player2[1]
    bottom2 = player2[1] + player2[3]
    
    ''' move the player in horizontal direction '''
    player1[0] += vel1[0]
    if choice == ch_p2:
        player2[0] += vel2[0]

    #Boundaries
    if left > WIDTH:
        player1[0] = 0 - player1[2]
    elif right < 0:
        player1[0] = WIDTH
        
    if bottom < 0:
        player1[1] = HEIGHT
    elif top > HEIGHT:
        player1[1] = 0 - player1[3]

    if choice == ch_p2:
        if left2 > WIDTH:
            player2[0] = 0 - player2[2]
        elif right2 < 0:
            player2[0] = WIDTH
            
        if bottom2 < 0:
            player2[1] = HEIGHT
        elif top2 > HEIGHT:
            player2[1] = 0 - player2[3]

    #Checks for collsions via (Check_collide) methods
    collidebles = walls + bricks
    check_collide(collidebles, player1, vel1)
    check_collide(collidebles, player2, vel2)
    
    '''checks to see if the players have touched coins'''
    hit_list = []

    for c in coins:
        if intersects.rect_rect(player1, c):
            hit_list.append(c)
     
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]

    for hit in hit_list:
        coins.remove(hit)
        shot.play()
        score1 += 1

    for c in coins:
        if intersects.rect_rect(player2, c):
            hit_list.append(c)
     
    hit_list = [c for c in coins if intersects.rect_rect(player2, c)]

    for hit in hit_list:
        coins.remove(hit)
        shot.play()
        score1 += 1

    if status == play:
        if len(coins) == 0:
            win = True
            status = end

    '''checks for contact with the speed up power ups.'''
    for s in speed_ups:
        if intersects.rect_rect(player1, s):
            speed_ups.remove(s)
            if player1_speed == 5:
                pop_up_speedup_timer = 2
                player1_speed = 6.25
            else:
                player1_speed = 6.25

    for s in speed_ups:
        if intersects.rect_rect(player2, s):
            speed_ups.remove(s)
            if player2_speed == 5:
                pop_up_speedup_timer = 1
                player2_speed = 6.25
            else:
                player2_speed = 6.25

    '''checks for contact with the slow_down powerups'''
    for sl in slow_time:
        if intersects.rect_rect(player1, sl):
            slow_time.remove(sl)
            master_timer += 5
        elif intersects.rect_rect(player2, sl):
            slow_time.remove(sl)
            master_timer += 5

    #checks for contact with the bomb powerups
    if intersects.rect_rect(player1, bomb1):
        bricks = []
        is_bomb = False
        boom.play()
    elif intersects.rect_rect(player2, bomb1):
        bricks = []
        is_bomb = False
        boom.play()
    
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    if status == start:
        title = pygame.image.load('title.jpg')
        screen.blit(title, [-50,-100])

        pygame.draw.rect(screen, WHITE, [150, 150, 500, 45])
        pygame.draw.rect(screen, WHITE, [150, 250, 500, 45])
        pygame.draw.rect(screen, WHITE, [150, 350, 500, 45])
        pygame.draw.rect(screen, WHITE, [150, 450, 500, 45])

        font_coin_desp = pygame.font.Font(None, 50)
        text_coin_desp = font_coin_desp.render("Collect all 40 Golden Scars", 1, RED)
        screen.blit(text_coin_desp, [150, 150])

        font_coin_desp = pygame.font.Font(None, 45)
        text_coin_desp = font_coin_desp.render("Launch Pads Speed You Up", 1, RED)
        screen.blit(text_coin_desp, [150, 250])

        font_coin_desp = pygame.font.Font(None, 35)
        text_coin_desp = font_coin_desp.render("Shield Potions add 5 sec. to the timer", 1, RED)
        screen.blit(text_coin_desp, [150, 350])

        font_coin_desp = pygame.font.Font(None, 35)
        text_coin_desp = font_coin_desp.render("Grab the bomb to blow up bricks", 1, RED)
        screen.blit(text_coin_desp, [150, 450])

        font_coin_desp = pygame.font.Font(None, 45)
        text_coin_desp = font_coin_desp.render("Press Space To Play", 1, RED)
        screen.blit(text_coin_desp, [150, 525])

        scar = pygame.image.load('scar.png')
        screen.blit(scar, [600, 150])
        pad = pygame.image.load('pad.png')
        screen.blit(pad, [600, 250])
        shield = pygame.image.load('shield.png')
        screen.blit(shield, [600, 350])
        C4 = pygame.image.load('nitro.png')
        screen.blit(C4, [573, 450])
        block = pygame.image.load('brick.png')
        screen.blit(block, [600, 450])

    elif status == play:
        screen.blit(screen_walls, [0,0])
        
        dork = pygame.image.load('dork.png')
        loc = player1[:2]
        screen.blit(dork, loc)

        if choice == ch_p2:
            hound = pygame.image.load('hound.png')
            loc = player2[:2]
            screen.blit(hound, loc)

        for c in coins:
            scar = pygame.image.load('scar.png')
            loc = c[:2]
            screen.blit(scar, loc)
        
        for s in speed_ups:
            pad = pygame.image.load('pad.png')
            loc = s[:2]
            screen.blit(pad, loc)

        for sl in slow_time:
            shield = pygame.image.load('shield.png')
            loc = sl[:2]
            screen.blit(shield, loc)

        for b in bricks:
            block = pygame.image.load('brick.png')
            loc = b[:2]
            screen.blit(block, loc)

        if is_bomb:
            C4 = pygame.image.load('nitro.png')
            loc = bomb1[:2]
            screen.blit(C4, loc)

        if pop_up_speedup_timer > 0:
            font_speed_up = pygame.font.Font(None, 150)
            text_speed_up = font_speed_up.render("Speed Up!", 1, GREEN)
            screen.blit(text_speed_up, [100, 200])

        
        font_s = pygame.font.Font(None, 30)
        text_s = font_s.render("Scars = " + str(score1), 1, YELLOW)
        screen.blit(text_s, [700, 0])

        font_t = pygame.font.Font(None, 30)
        text_t = font_t.render("Time limit = " + str(master_timer), 1, YELLOW)
        screen.blit(text_t, [0, 0])

    elif status == end and win:      
        vic = pygame.image.load('vic.png')
        loc = (0, -200)
        screen.blit(vic, loc)

        if check_name:
            font_space = pygame.font.Font(None, 45)
            text_space = font_space.render("Press Space To Play", 1, WHITE)
            screen.blit(text_space, [150, 525])

        elif not check_name:
            font_space = pygame.font.Font(None, 45)
            text_space = font_space.render("Please enter your name in the shell!", 1, WHITE)
            screen.blit(text_space, [10, 525])

    elif status == end and lose:
        gav = pygame.image.load('gav.png')
        loc = (0,0)
        screen.blit(gav, loc)

        font_space = pygame.font.Font(None, 45)
        text_space = font_space.render("Press Space To Play", 1, WHITE)
        screen.blit(text_space, [150, 525])

    elif status == stage:
        select = pygame.image.load('select.png')
        screen.blit(select, [0,0])

        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("Press 1 for solos.", 1, WHITE)
        screen.blit(text_title, [50, 50])

        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("Press 2 for duos.", 1, WHITE)
        screen.blit(text_title, [450 , 50])

    elif status == leaderboard:
        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("The Best Gamers EVARRRRRR!!!!", 1, WHITE)
        screen.blit(text_title, [10 , 10])

        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("1.)" + str(leaders[-1]), 1, WHITE)
        screen.blit(text_title, [25 , 100])

        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("2.)" + str(leaders[-2]), 1, WHITE)
        screen.blit(text_title, [25 , 175])
        
        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("3.)" + str(leaders[-3]), 1, WHITE)
        screen.blit(text_title, [25 , 250])
        
        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("4.)" + str(leaders[-4]), 1, WHITE)
        screen.blit(text_title, [25 , 325])
        
        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("5.)" + str(leaders[-5]), 1, WHITE)
        screen.blit(text_title, [25 , 400])
        
        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("6.)" + str(leaders[-6]), 1, WHITE)
        screen.blit(text_title, [325 , 100])
        
        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("7.)" + str(leaders[-7]), 1, WHITE)
        screen.blit(text_title, [325 , 175])
        
        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("8.)" + str(leaders[-8]), 1, WHITE)
        screen.blit(text_title, [325 , 250])
        
        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("9.)" + str(leaders[-9]), 1, WHITE)
        screen.blit(text_title, [325 , 325])
        
        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("10.)" + str(leaders[-10]), 1, WHITE)
        screen.blit(text_title, [325 , 400])

        font_space = pygame.font.Font(None, 45)
        text_space = font_space.render("Press Shift To Play", 1, WHITE)
        screen.blit(text_space, [25, 500])

        font_title = pygame.font.Font(None, 50)
        text_title = font_title.render("Your Score: " + str(master_timer), 1, WHITE)
        screen.blit(text_title, [425 , 500])
        
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
