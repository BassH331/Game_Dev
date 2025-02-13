import pygame as pg
from player import Player  # Ensure player.py contains the Player class
from enemy import Enemy  # Ensure enemy.py contains the Enemy class
from fire_knight import Fire_knight

# Initialize Pygame
pg.init()

# Set up the screen
screen = pg.display.set_mode((1600, 830))
pg.display.set_caption("Fight Club")

# Import sound for menu buttons
button_press = pg.mixer.Sound("sfx/button_press.wav")
button_press.set_volume(0.17)

# Import sound for Next scene sfx
next_scene = pg.mixer.Sound("sfx/Next_scene.wav")
next_scene.set_volume(0.17)

# Play button press function
def butto_press_sfx():
    button_press.play()

# Play Next scene sfx function
def next_scene_sfx():
    next_scene.play()

# Import menu images of players 
Knight_image = pg.image.load('Fire knight.png').convert_alpha()
Wind_storm_image = pg.image.load('Wind Storm.png').convert_alpha()
# First image
box_x, box_y = 195, 200
box_size = 70
# Second image
box_x2, box_y2 = 550, 200
box_size2 = 70

#create font
test_font = pg.font.Font('Resources/font/Pixeltype.ttf', 50)#Font(font type, size)

# Border around selected or hovered character image
border = pg.Rect(195, 195, Knight_image.get_width() + 10, Knight_image.get_height() + 10)
border_2 = pg.Rect(545, 195, Wind_storm_image.get_width() + 10, Wind_storm_image.get_height() + 10)

# Text for game menu
pick_player_text = test_font.render('Pick your champion', False, (157, 0, 255))
pick_player_text_rect = pick_player_text.get_rect(center = (400, 80)) 
pick_battleground_text = test_font.render('Pick a battleground', False, (157, 0, 255))# Render(text, Anti-Aliazing, color)
pick_battleground_text_rect = pick_battleground_text.get_rect(center = (400, 350))

# Game active state so that we can check for when the user wants to either restart the game or quit
game_active = False

# Import battleground images (for game menu)
battleground_1 = pg.image.load('Old forest(night).jpg').convert_alpha()# Replace with your image file
battleground_1 = pg.transform.scale(battleground_1, (400, 230))  # Scale to fit placement
battleground_chosen = pg.image.load('Old forest(night).jpg').convert_alpha()
battleground_chosen = pg.transform.scale(battleground_chosen, (1600, 830))
battleground_2 = pg.image.load('Battleground_2/gif_frames/frame_000.png').convert_alpha()
battleground_2 = pg.transform.scale(battleground_2, (400, 230))
battleground_3 = pg.image.load('Battleground_4/frame_00.png')
battleground_3 = pg.transform.scale(battleground_3, (400, 230))

# Border for battleground menu image 
battleground_border_1 = pg.Rect(145, 455, battleground_1.get_width() + 10, battleground_1.get_height() + 10)
battleground_border_2 = pg.Rect(595, 455, battleground_2.get_width() + 10, battleground_2.get_height() + 10)
battleground_border_3 = pg.Rect(1045, 455, battleground_3.get_width() + 10, battleground_3.get_height() + 10)

# Box-x and Box-y for battground border
battleground_box1_x = 145
battleground_box1_y = 455
battleground_box2_x = 595
battleground_box2_y = 455
battleground_box3_x = 1045
battleground_box3_y = 455
battleground_box_size = 400

# Battleground selected flags
battleground_1_selected = False
battleground_2_selected = False
battleground_3_selected = False

# Import battleground images for game (game_active)
background_1 = pg.image.load('Battleground_2/gif_frames/frame_000.png').convert_alpha()# Replace with your image file
background_2 = pg.image.load('Battleground_2/gif_frames/frame_001.png').convert_alpha()
background_3 = pg.image.load('Battleground_2/gif_frames/frame_002.png').convert_alpha()
background_4 = pg.image.load('Battleground_2/gif_frames/frame_003.png').convert_alpha()
background_5 = pg.image.load('Battleground_2/gif_frames/frame_004.png').convert_alpha()
background_6 = pg.image.load('Battleground_2/gif_frames/frame_005.png').convert_alpha()
background_7 = pg.image.load('Battleground_2/gif_frames/frame_006.png').convert_alpha()
background_8 = pg.image.load('Battleground_2/gif_frames/frame_007.png').convert_alpha()
background_9 = pg.image.load('Battleground_2/gif_frames/frame_008.png').convert_alpha()
background_10 = pg.image.load('Battleground_2/gif_frames/frame_009.png').convert_alpha()
background_11 = pg.image.load('Battleground_2/gif_frames/frame_010.png').convert_alpha()
background_12 = pg.image.load('Battleground_2/gif_frames/frame_011.png').convert_alpha()
background_13 = pg.image.load('Battleground_2/gif_frames/frame_012.png').convert_alpha()
background_14 = pg.image.load('Battleground_2/gif_frames/frame_013.png').convert_alpha()
background_15 = pg.image.load('Battleground_2/gif_frames/frame_014.png').convert_alpha()
background_16 = pg.image.load('Battleground_2/gif_frames/frame_015.png').convert_alpha()
background_17 = pg.image.load('Battleground_2/gif_frames/frame_016.png').convert_alpha()
background_18 = pg.image.load('Battleground_2/gif_frames/frame_017.png').convert_alpha()
background_19 = pg.image.load('Battleground_2/gif_frames/frame_018.png').convert_alpha()

# Import battleground_2 images for game 
background02_1 = pg.image.load('Battleground_3/frame_0000.jpg').convert_alpha()# Replace with your image file
background02_2 = pg.image.load('Battleground_3/frame_0001.jpg').convert_alpha()
background02_3 = pg.image.load('Battleground_3/frame_0002.jpg').convert_alpha()
background02_4 = pg.image.load('Battleground_3/frame_0003.jpg').convert_alpha()
background02_5 = pg.image.load('Battleground_3/frame_0004.jpg').convert_alpha()
background02_6 = pg.image.load('Battleground_3/frame_0005.jpg').convert_alpha()
background02_7 = pg.image.load('Battleground_3/frame_0006.jpg').convert_alpha()
background02_8 = pg.image.load('Battleground_3/frame_0007.jpg').convert_alpha()
background02_9 = pg.image.load('Battleground_3/frame_0008.jpg').convert_alpha()
background02_10 = pg.image.load('Battleground_3/frame_0009.jpg').convert_alpha()
background02_11 = pg.image.load('Battleground_3/frame_0010.jpg').convert_alpha()
background02_12 = pg.image.load('Battleground_3/frame_0011.jpg').convert_alpha()
background02_13 = pg.image.load('Battleground_3/frame_0012.jpg').convert_alpha()
background02_14 = pg.image.load('Battleground_3/frame_0013.jpg').convert_alpha()
background02_15 = pg.image.load('Battleground_3/frame_0014.jpg').convert_alpha()
background02_16 = pg.image.load('Battleground_3/frame_0015.jpg').convert_alpha()
background02_17 = pg.image.load('Battleground_3/frame_0016.jpg').convert_alpha()
background02_18 = pg.image.load('Battleground_3/frame_0017.jpg').convert_alpha()
background02_19 = pg.image.load('Battleground_3/frame_0018.jpg').convert_alpha()
background02_20 = pg.image.load('Battleground_3/frame_0019.jpg').convert_alpha()
background02_21 = pg.image.load('Battleground_3/frame_0020.jpg').convert_alpha()
background02_22 = pg.image.load('Battleground_3/frame_0021.jpg').convert_alpha()
background02_23 = pg.image.load('Battleground_3/frame_0022.jpg').convert_alpha()
background02_24 = pg.image.load('Battleground_3/frame_0023.jpg').convert_alpha()

# Import battleground_3 images for game 
background03_1 = pg.image.load('Battleground_4/frame_00.png').convert_alpha()# Replace with your image file
background03_2 = pg.image.load('Battleground_4/frame_01.png').convert_alpha()
background03_3 = pg.image.load('Battleground_4/frame_02.png').convert_alpha()
background03_4 = pg.image.load('Battleground_4/frame_03.png').convert_alpha()
background03_5 = pg.image.load('Battleground_4/frame_04.png').convert_alpha()
background03_6 = pg.image.load('Battleground_4/frame_05.png').convert_alpha()
background03_7 = pg.image.load('Battleground_4/frame_06.png').convert_alpha()
background03_8 = pg.image.load('Battleground_4/frame_07.png').convert_alpha()
background03_9 = pg.image.load('Battleground_4/frame_08.png').convert_alpha()
background03_10 = pg.image.load('Battleground_4/frame_09.png').convert_alpha()
background03_11 = pg.image.load('Battleground_4/frame_10.png').convert_alpha()
background03_12 = pg.image.load('Battleground_4/frame_11.png').convert_alpha()
background03_13 = pg.image.load('Battleground_4/frame_12.png').convert_alpha()
background03_14 = pg.image.load('Battleground_4/frame_13.png').convert_alpha()
background03_15 = pg.image.load('Battleground_4/frame_14.png').convert_alpha()
background03_16 = pg.image.load('Battleground_4/frame_15.png').convert_alpha()
background03_17 = pg.image.load('Battleground_4/frame_16.png').convert_alpha()
background03_18 = pg.image.load('Battleground_4/frame_17.png').convert_alpha()
background03_19 = pg.image.load('Battleground_4/frame_18.png').convert_alpha()
background03_20 = pg.image.load('Battleground_4/frame_19.png').convert_alpha()
background03_21 = pg.image.load('Battleground_4/frame_20.png').convert_alpha()
background03_22 = pg.image.load('Battleground_4/frame_21.png').convert_alpha()
background03_23 = pg.image.load('Battleground_4/frame_22.png').convert_alpha()
background03_24 = pg.image.load('Battleground_4/frame_23.png').convert_alpha()
background03_25 = pg.image.load('Battleground_4/frame_24.png').convert_alpha()
background03_26 = pg.image.load('Battleground_4/frame_25.png').convert_alpha()
background03_27 = pg.image.load('Battleground_4/frame_26.png').convert_alpha()
background03_28 = pg.image.load('Battleground_4/frame_27.png').convert_alpha()
background03_29 = pg.image.load('Battleground_4/frame_28.png').convert_alpha()
background03_30 = pg.image.load('Battleground_4/frame_29.png').convert_alpha()
background03_31 = pg.image.load('Battleground_4/frame_30.png').convert_alpha()
background03_31 = pg.image.load('Battleground_4/frame_31.png').convert_alpha()

# Set index 
battleground_frame_index = 0

# List for battlefield images 
background_frames = [
    pg.transform.scale(frame, (1600, 830))
        for frame in [
            background_1, background_2, background_3, background_4, background_5, background_6, background_7, background_8, background_9, background_10, background_11, background_13, background_14, background_15, background_16, background_17, background_18, background_19
        ]
]
background_frames_2 = [
    pg.transform.scale(frame, (1600, 830))
        for frame in [
            background02_1, background02_2, background02_3, background02_4, background02_5, background02_6, background02_7, background02_8, background02_9, background02_10, background02_11, background02_13, background02_14, background02_15, background02_16, background02_17, background02_18, background02_19, background02_20, background02_21, background02_22, background02_23, background02_24
        ]
]
background_frames_3 = [
    pg.transform.scale(frame, (1600, 830))
        for frame in [
            background03_1, background03_2, background03_3, background03_4, background03_5, background03_6, background03_7, background03_8, background03_9, background03_10, background03_11, background03_13, background03_14, background03_15, background03_16, background03_17, background03_18, background03_19, background03_20, background03_21, background03_22, background03_23, background03_24, background03_25, background03_26, background03_27, background03_28, background03_29, background03_30, background03_31
        ]
]
    
# Import game intro background
intro_image = pg.image.load('Sunset.jpg').convert_alpha() 
intro_image = pg.transform.scale(intro_image, (1600 ,830))  # Scale to fit screen

# Import menu images of players 
Knight_image = pg.image.load('Fire knight.png').convert_alpha()
Wind_storm_image = pg.image.load('Wind Storm.png').convert_alpha()

# Import Start button
start_button = pg.image.load('Start button/start_0.png').convert_alpha() 
start_button_hover = pg.image.load('Start button/start_1.png').convert_alpha() 
#intro_image = pg.transform.scale(intro_image, (1600 ,830))
# Instantiate the player
player = Player()

# Initiate player 2
fire_knight = Fire_knight()

# Initialize enemy
enemy = Enemy(fire_knight)

# Clock for controlling the frame rate
clock = pg.time.Clock()

# Get a reference to pygame channel
channel = pg.mixer.Channel(0)

# import background music
channel_00 = pg.mixer.Channel(5)
channel_01 = pg.mixer.Channel(6)
bg_music_1 = pg.mixer.Sound("wind_background_music.mp3")
bg_music_1.set_volume(0.2)
bg_music_2 = pg.mixer.Sound("MP3/13- Full Strength Unleashed.mp3")
bg_music_2.set_volume(0.3)
bg_music_3 = pg.mixer.Sound("MP3/7- Nerve Monster.mp3")
bg_music_3.set_volume(0.3)
#bg_music.play(loops = -1)# loops = [how many times you want to loop the music] (-1 means forever)
#channel_00.play(bg_music_1, 0)
channel_00.queue(bg_music_2)

def play_background_music(sound):
    channel_00.play(sound, 0)

def play_background_music_1(sound):
    channel_01.play(sound, 0)

def stop_music():
    channel_00.stop()

def stop_music_1():
    channel_00.stop()

# Import attack sprites
Enter_01 = pg.image.load("PRESS ENTER\sprite_3.png").convert_alpha()
Enter_02 = pg.image.load("PRESS ENTER\sprite_4.png").convert_alpha()
Enter_03 = pg.image.load("PRESS ENTER\sprite_5.png").convert_alpha()
Press_01 = pg.image.load("PRESS ENTER\sprite_0.png").convert_alpha()
Press_02 = pg.image.load("PRESS ENTER\sprite_1.png").convert_alpha()
Press_03 = pg.image.load("PRESS ENTER\sprite_2.png").convert_alpha()

# Frame inde for press and enter 
press_frame_index = 0
enter_frame_index = 0

# Add them to the attack4_frames list
Press_frames = [
        Press_01, Press_02, Press_03
]

Enter_frames = [
        Enter_01, Enter_02, Enter_03
]

# Function to display press enter
def display_press_enter(press_frame_index, enter_frame_index):
    Press_image = Press_frames[int(press_frame_index)]
    Enter_image = Enter_frames[int(enter_frame_index)]
    screen.blit(Press_image, ((1600 / 2) - 120, 430))
    screen.blit(Enter_image, ((1600 / 2) - 120, 500))

# Determine wether player ot enemy has lost and declare the game as over
Game_over = False

#Flag to indicate game should move to the menu scene
game_menu = False
battleground_selected = False
Player_selected = False

# Border around image(mouse hovering)
Knight_selected =  False
Wind_storm_selected = False

# Game loop
running = True
play_music = True
while running:

    # Get the position of the mouse everytime it moves 
    mouse_pos = pg.mouse.get_pos()
    #print(mouse_pos)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if game_active:
        if play_music:
            next_scene_sfx()
            play_background_music(bg_music_1)
            play_music = False
        # Draw the background
        if battleground_2_selected:
            if battleground_frame_index >= len(background_frames) -1:
                battleground_frame_index = 0
            else:
                battleground_frame_index += 0.18
            screen.blit(background_frames[int(battleground_frame_index)], (0, 0))
        elif battleground_3_selected:
            if battleground_frame_index >= len(background_frames_3) -1:
                battleground_frame_index = 0
            else:
                battleground_frame_index += 0.18
            screen.blit(background_frames_3[int(battleground_frame_index)], (0, 0))
        else:
            screen.blit(battleground_chosen, (0, 0))


        # Inside the game loop
        enemy.draw(screen)
        enemy.update(screen)  # Update the enemy

        # Update and draw the player
        fire_knight.draw(screen) # Draw player on the screen
        fire_knight.update(screen) # Update player position and animations
        # Check if the player’s attack hits the enemy
        fire_knight.return_collision_box(enemy, screen)
        enemy.return_collision_box(fire_knight, screen)
        
        #print(player.collision_box.left == enemy.collision_box.right)
        #hit = player.enemy_hit(enemy)

        # If the enemy is hit, trigger the take-hit animation in the enemy class
        #enemy.hit_taken(hit)
        if enemy.health_index >= len(enemy.health_bar_frames) -1:
            Game_over = True
            game_active = False
            stop_music()
            channel_00.queue(bg_music_3)
    else:
        if Game_over:
            # Display "Game Over" message
            outro_image = pg.image.load('city_bg.webp')
            screen.blit(outro_image, (0, 0))
            game_over_text = pg.font.Font(None, 64).render("Game Over", True, (255, 0, 0))
            screen.blit(game_over_text, (300, 250))
            enemy.health_index == 0
        else:
            #if play_music:
                #play_background_music(bg_music_2)
                #play_music = False
            # Display intro image, user must press enter ti start the game
            screen.blit(intro_image, (0, 0))

            # Display press enter to play
            display_press_enter(press_frame_index, enter_frame_index)

            # Chnage frames for the press enter list of frames
            press_frame_index += 0.2
            enter_frame_index += 0.2
            if press_frame_index >= len(Press_frames) and enter_frame_index >= len(Enter_frames):
                press_frame_index = 0
                enter_frame_index = 0

            # Check for user input to start the game
            keys = pg.key.get_pressed()
            if keys[pg.K_RETURN]:
                next_scene_sfx()
                game_menu = True 
            if game_menu:
                screen.fill((0, 0, 0))
                # Hover over character
                if box_x <= mouse_pos[0] <= box_x + box_size and box_y <= mouse_pos[1] <= box_y + box_size:
                    pg.draw.rect(screen, (255, 255, 255), border)
                    if event.type == pg.MOUSEBUTTONDOWN:
                        # Button press sfx
                        butto_press_sfx()
                        Knight_selected = True
                        Wind_storm_selected = False
                if box_x2 <= mouse_pos[0] <= box_x2 + box_size2 and box_y2 <= mouse_pos[1] <= box_y2 + box_size2:
                    pg.draw.rect(screen, (255, 255, 255), border_2)
                    if event.type == pg.MOUSEBUTTONDOWN:
                        # Button press sfx
                        butto_press_sfx()
                        Wind_storm_selected = True
                        Knight_selected = False
                
                # Wind storm selected
                if Wind_storm_selected:
                    Player_selected = True
                    pg.draw.rect(screen, (0, 50, 157), border_2)
                # Knight selected
                if Knight_selected:
                    Player_selected = True
                    pg.draw.rect(screen, (0, 50, 157), border)
        
                # Display the images ontop of the border
                screen.blit(Knight_image, (200, 200))
                screen.blit(Wind_storm_image, (550, 200))
                # Display pick player text
                screen.blit(pick_player_text, pick_player_text_rect)
                # Display pick battleground text
                screen.blit(pick_battleground_text, pick_battleground_text_rect)

                # Hover over battleground 
                if battleground_box1_x <= mouse_pos[0] <= battleground_box1_x + battleground_box_size and battleground_box1_y <= mouse_pos[1] <= battleground_box1_y + battleground_box_size:
                    pg.draw.rect(screen, (255, 255, 255), battleground_border_1)
                    if event.type == pg.MOUSEBUTTONDOWN:
                        # Button press sfx
                        butto_press_sfx()
                        battleground_1_selected = True
                        battleground_2_selected = False
                        battleground_3_selected = False
                elif battleground_box2_x <= mouse_pos[0] <= battleground_box2_x + battleground_box_size and battleground_box2_y <= mouse_pos[1] <= battleground_box2_y + battleground_box_size:
                    pg.draw.rect(screen, (255, 255, 255), battleground_border_2)
                    if event.type == pg.MOUSEBUTTONDOWN:
                        # Button press sfx
                        butto_press_sfx()
                        battleground_2_selected = True
                        battleground_3_selected = False
                        battleground_1_selected = False
                elif battleground_box3_x <= mouse_pos[0] <= battleground_box3_x + battleground_box_size and battleground_box3_y <= mouse_pos[1] <= battleground_box3_y + battleground_box_size:
                    pg.draw.rect(screen, (255, 255, 255), battleground_border_3)
                    if event.type == pg.MOUSEBUTTONDOWN:
                        # Button press sfx
                        butto_press_sfx()
                        battleground_3_selected = True
                        battleground_2_selected = False
                        battleground_1_selected = False
                
                # Battleground selected
                if battleground_1_selected:
                    battleground_selected = True
                    pg.draw.rect(screen, (0, 50, 157), battleground_border_1)
                if battleground_2_selected:
                    battleground_selected = True
                    pg.draw.rect(screen, (0, 50, 157), battleground_border_2)
                if battleground_3_selected:
                    battleground_selected = True
                    pg.draw.rect(screen, (0, 50, 157), battleground_border_3)
                pg.draw.rect
        
                # Display battlegrounds for user to select
                screen.blit(battleground_1, (150, 460))
                screen.blit(battleground_2, (600, 460))
                screen.blit(battleground_3, (1050, 460))
                if 1145 >= mouse_pos[0] >= 900 and 285 >= mouse_pos[1] >= 165:
                   screen.blit(start_button_hover, (900,165))
                   # Start game when the player presses space or start button
                   if event.type == pg.MOUSEBUTTONDOWN or keys[pg.K_SPACE]:
                       screen.blit(start_button, (900,165))
                       if Player_selected and battleground_selected:
                            next_scene_sfx()
                            game_menu = False
                            game_active = True
                else: 
                    screen.blit(start_button, (900,165))
                #stop_music()
                

    # Update the display
    pg.display.flip()

    # Cap the frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pg.quit()