import time
import pygame as pg

# Player Class
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Import Death animation
        death_1 = pg.image.load("png/death/death_1.png").convert_alpha()
        death_2 = pg.image.load("png/death/death_2.png").convert_alpha()
        death_3 = pg.image.load("png/death/death_3.png").convert_alpha()
        death_4 = pg.image.load("png/death/death_4.png").convert_alpha()
        death_5 = pg.image.load("png/death/death_5.png").convert_alpha()
        death_6 = pg.image.load("png/death/death_6.png").convert_alpha()
        death_7 = pg.image.load("png/death/death_7.png").convert_alpha()
        death_8 = pg.image.load("png/death/death_8.png").convert_alpha()
        death_9 = pg.image.load("png/death/death_9.png").convert_alpha()
        death_10 = pg.image.load("png/death/death_10.png").convert_alpha()
        death_11 = pg.image.load("png/death/death_11.png").convert_alpha()
        death_12 = pg.image.load("png/death/death_12.png").convert_alpha()
        death_13 = pg.image.load("png/death/death_13.png").convert_alpha()
        death_14 = pg.image.load("png/death/death_14.png").convert_alpha()
        death_15 = pg.image.load("png/death/death_15.png").convert_alpha()
        death_16 = pg.image.load("png/death/death_16.png").convert_alpha()
        death_17 = pg.image.load("png/death/death_17.png").convert_alpha()
        death_18 = pg.image.load("png/death/death_18.png").convert_alpha()
        death_19 = pg.image.load("png/death/death_19.png").convert_alpha()

        # Import idle sprites
        idle_1 = pg.image.load("png/idle/idle_1.png").convert_alpha()
        idle_2 = pg.image.load("png/idle/idle_2.png").convert_alpha()
        idle_3 = pg.image.load("png/idle/idle_3.png").convert_alpha()
        idle_4 = pg.image.load("png/idle/idle_4.png").convert_alpha()
        idle_5 = pg.image.load("png/idle/idle_5.png").convert_alpha()
        idle_6 = pg.image.load("png/idle/idle_6.png").convert_alpha()

        # Import defend sprites
        defend_1 = pg.image.load("png/defend/defend_1.png").convert_alpha()
        defend_2 = pg.image.load("png/defend/defend_2.png").convert_alpha()
        defend_3 = pg.image.load("png/defend/defend_3.png").convert_alpha()
        defend_4 = pg.image.load("png/defend/defend_4.png").convert_alpha()
        defend_5 = pg.image.load("png/defend/defend_5.png").convert_alpha()
        defend_6 = pg.image.load("png/defend/defend_6.png").convert_alpha()
        defend_7 = pg.image.load("png/defend/defend_7.png").convert_alpha()
        defend_8 = pg.image.load("png/defend/defend_8.png").convert_alpha()
        defend_9 = pg.image.load("png/defend/defend_9.png").convert_alpha()
        defend_10 = pg.image.load("png/defend/defend_10.png").convert_alpha()
        defend_11 = pg.image.load("png/defend/defend_11.png").convert_alpha()
        defend_12 = pg.image.load("png/defend/defend_12.png").convert_alpha()
        defend_13 = pg.image.load("png/defend/defend_13.png").convert_alpha()

        # Import running sprites
        run_1 = pg.image.load("png/run/run_1.png").convert_alpha()
        run_2 = pg.image.load("png/run/run_2.png").convert_alpha()
        run_3 = pg.image.load("png/run/run_3.png").convert_alpha()
        run_4 = pg.image.load("png/run/run_4.png").convert_alpha()
        run_5 = pg.image.load("png/run/run_5.png").convert_alpha()
        run_6 = pg.image.load("png/run/run_6.png").convert_alpha()
        run_7 = pg.image.load("png/run/run_7.png").convert_alpha()
        run_8 = pg.image.load("png/run/run_8.png").convert_alpha()

        # Import jumping sprites
        j_up_1 = pg.image.load("png/j_up/j_up_1.png").convert_alpha()
        j_up_2 = pg.image.load("png/j_up/j_up_2.png").convert_alpha()
        j_up_3 = pg.image.load("png/j_up/j_up_3.png").convert_alpha()

        # Import jump down sprites
        j_down_1 = pg.image.load("png/j_down/j_down_1.png").convert_alpha()
        j_down_2 = pg.image.load("png/j_down/j_down_2.png").convert_alpha()
        j_down_3 = pg.image.load("png/j_down/j_down_3.png").convert_alpha()

        # Import attack sprites
        atk_1 = pg.image.load("png/1_atk/1_atk_1.png").convert_alpha()
        atk_2 = pg.image.load("png/1_atk/1_atk_2.png").convert_alpha()
        atk_3 = pg.image.load("png/1_atk/1_atk_3.png").convert_alpha()
        atk_4 = pg.image.load("png/1_atk/1_atk_4.png").convert_alpha()
        atk_5 = pg.image.load("png/1_atk/1_atk_5.png").convert_alpha()
        atk_6 = pg.image.load("png/1_atk/1_atk_6.png").convert_alpha()

        # Import second attack sprites (2_atk)
        atk_2_1 = pg.image.load("png/2_atk/2_atk_1.png").convert_alpha()
        atk_2_2 = pg.image.load("png/2_atk/2_atk_2.png").convert_alpha()
        atk_2_3 = pg.image.load("png/2_atk/2_atk_3.png").convert_alpha()
        atk_2_4 = pg.image.load("png/2_atk/2_atk_4.png").convert_alpha()
        atk_2_5 = pg.image.load("png/2_atk/2_atk_5.png").convert_alpha()
        atk_2_6 = pg.image.load("png/2_atk/2_atk_6.png").convert_alpha()
        atk_2_7 = pg.image.load("png/2_atk/2_atk_7.png").convert_alpha()
        atk_2_8 = pg.image.load("png/2_atk/2_atk_8.png").convert_alpha()
        atk_2_9 = pg.image.load("png/2_atk/2_atk_9.png").convert_alpha()
        atk_2_10 = pg.image.load("png/2_atk/2_atk_10.png").convert_alpha()
        atk_2_11 = pg.image.load("png/2_atk/2_atk_11.png").convert_alpha()
        atk_2_12 = pg.image.load("png/2_atk/2_atk_12.png").convert_alpha()

        # Import third attack sprites (3_atk)
        atk_3_1 = pg.image.load("png/3_atk/3_atk_1.png").convert_alpha()
        atk_3_2 = pg.image.load("png/3_atk/3_atk_2.png").convert_alpha()
        atk_3_3 = pg.image.load("png/3_atk/3_atk_3.png").convert_alpha()
        atk_3_4 = pg.image.load("png/3_atk/3_atk_4.png").convert_alpha()
        atk_3_5 = pg.image.load("png/3_atk/3_atk_5.png").convert_alpha()
        atk_3_6 = pg.image.load("png/3_atk/3_atk_6.png").convert_alpha()
        atk_3_7 = pg.image.load("png/3_atk/3_atk_7.png").convert_alpha()
        atk_3_8 = pg.image.load("png/3_atk/3_atk_8.png").convert_alpha()
        atk_3_9 = pg.image.load("png/3_atk/3_atk_9.png").convert_alpha()
        atk_3_10 = pg.image.load("png/3_atk/3_atk_10.png").convert_alpha()
        atk_3_11 = pg.image.load("png/3_atk/3_atk_11.png").convert_alpha()
        atk_3_12 = pg.image.load("png/3_atk/3_atk_12.png").convert_alpha()
        atk_3_13 = pg.image.load("png/3_atk/3_atk_13.png").convert_alpha()
        atk_3_14 = pg.image.load("png/3_atk/3_atk_14.png").convert_alpha()
        atk_3_15 = pg.image.load("png/3_atk/3_atk_15.png").convert_alpha()
        atk_3_16 = pg.image.load("png/3_atk/3_atk_16.png").convert_alpha()
        atk_3_17 = pg.image.load("png/3_atk/3_atk_17.png").convert_alpha()
        atk_3_18 = pg.image.load("png/3_atk/3_atk_18.png").convert_alpha()
        atk_3_19 = pg.image.load("png/3_atk/3_atk_19.png").convert_alpha()
        atk_3_20 = pg.image.load("png/3_atk/3_atk_20.png").convert_alpha()
        atk_3_21 = pg.image.load("png/3_atk/3_atk_21.png").convert_alpha()
        atk_3_22 = pg.image.load("png/3_atk/3_atk_22.png").convert_alpha()
        atk_3_23 = pg.image.load("png/3_atk/3_atk_23.png").convert_alpha()

        # Import special attack
        sp_atk_1 = pg.image.load("png/sp_atk/sp_atk_1.png").convert_alpha()
        sp_atk_2 = pg.image.load("png/sp_atk/sp_atk_2.png").convert_alpha()
        sp_atk_3 = pg.image.load("png/sp_atk/sp_atk_3.png").convert_alpha()
        sp_atk_4 = pg.image.load("png/sp_atk/sp_atk_4.png").convert_alpha()
        sp_atk_5 = pg.image.load("png/sp_atk/sp_atk_5.png").convert_alpha()
        sp_atk_6 = pg.image.load("png/sp_atk/sp_atk_6.png").convert_alpha()
        sp_atk_7 = pg.image.load("png/sp_atk/sp_atk_7.png").convert_alpha()
        sp_atk_8 = pg.image.load("png/sp_atk/sp_atk_8.png").convert_alpha()
        sp_atk_9 = pg.image.load("png/sp_atk/sp_atk_9.png").convert_alpha()
        sp_atk_10 = pg.image.load("png/sp_atk/sp_atk_10.png").convert_alpha()
        sp_atk_11 = pg.image.load("png/sp_atk/sp_atk_11.png").convert_alpha()
        sp_atk_12 = pg.image.load("png/sp_atk/sp_atk_12.png").convert_alpha()
        sp_atk_13 = pg.image.load("png/sp_atk/sp_atk_13.png").convert_alpha()
        sp_atk_14 = pg.image.load("png/sp_atk/sp_atk_14.png").convert_alpha()
        sp_atk_15 = pg.image.load("png/sp_atk/sp_atk_15.png").convert_alpha()
        sp_atk_16 = pg.image.load("png/sp_atk/sp_atk_16.png").convert_alpha()
        sp_atk_17 = pg.image.load("png/sp_atk/sp_atk_17.png").convert_alpha()
        sp_atk_18 = pg.image.load("png/sp_atk/sp_atk_18.png").convert_alpha()
        sp_atk_19 = pg.image.load("png/sp_atk/sp_atk_19.png").convert_alpha()
        sp_atk_20 = pg.image.load("png/sp_atk/sp_atk_20.png").convert_alpha()
        sp_atk_21 = pg.image.load("png/sp_atk/sp_atk_21.png").convert_alpha()
        sp_atk_22 = pg.image.load("png/sp_atk/sp_atk_22.png").convert_alpha()
        sp_atk_23 = pg.image.load("png/sp_atk/sp_atk_23.png").convert_alpha()
        sp_atk_24 = pg.image.load("png/sp_atk/sp_atk_24.png").convert_alpha()
        sp_atk_25 = pg.image.load("png/sp_atk/sp_atk_25.png").convert_alpha()

        # Import roll
        roll_1 = pg.image.load("png/roll/roll_1.png").convert_alpha()
        roll_2 = pg.image.load("png/roll/roll_2.png").convert_alpha()
        roll_3 = pg.image.load("png/roll/roll_3.png").convert_alpha()
        roll_4 = pg.image.load("png/roll/roll_4.png").convert_alpha()
        roll_5 = pg.image.load("png/roll/roll_5.png").convert_alpha()

        # Import air attack
        air_atk_1 = pg.image.load("png/air_atk/air_atk_1.png").convert_alpha()
        air_atk_2 = pg.image.load("png/air_atk/air_atk_2.png").convert_alpha()
        air_atk_3 = pg.image.load("png/air_atk/air_atk_3.png").convert_alpha()
        air_atk_4 = pg.image.load("png/air_atk/air_atk_4.png").convert_alpha()
        air_atk_5 = pg.image.load("png/air_atk/air_atk_5.png").convert_alpha()
        air_atk_6 = pg.image.load("png/air_atk/air_atk_6.png").convert_alpha()
        air_atk_7 = pg.image.load("png/air_atk/air_atk_7.png").convert_alpha()

        # Import taking hit sprite
        take_hit_1 = pg.image.load("png/take_hit/take_hit_1.png").convert_alpha()
        take_hit_2 = pg.image.load("png/take_hit/take_hit_2.png").convert_alpha()
        take_hit_3 = pg.image.load("png/take_hit/take_hit_3.png").convert_alpha()
        take_hit_4 = pg.image.load("png/take_hit/take_hit_4.png").convert_alpha()
        take_hit_5 = pg.image.load("png/take_hit/take_hit_5.png").convert_alpha()
        take_hit_6 = pg.image.load("png/take_hit/take_hit_6.png").convert_alpha()

        # Import Health_bar png's
        Health_bar_1 = pg.image.load("Health_0.png").convert_alpha()
        Health_bar_2 = pg.image.load("Health_1.png").convert_alpha()
        Health_bar_3 = pg.image.load("Health_2.png").convert_alpha()
        Health_bar_4 = pg.image.load("Health_3.png").convert_alpha()
        Health_bar_5 = pg.image.load("Health_4.png").convert_alpha()
        Health_bar_6 = pg.image.load("Health_5.png").convert_alpha()
        Health_bar_7 = pg.image.load("Health_6.png").convert_alpha()
        Health_bar_8 = pg.image.load("Health_7.png").convert_alpha()
        Health_bar_9 = pg.image.load("Health_8.png").convert_alpha()

        # Import Power_up bar
        power_up_bar_1 = pg.image.load("Power_up/sprite_00.png").convert_alpha()
        power_up_bar_2 = pg.image.load("Power_up/sprite_01.png").convert_alpha()
        power_up_bar_3 = pg.image.load("Power_up/sprite_02.png").convert_alpha()
        power_up_bar_4 = pg.image.load("Power_up/sprite_03.png").convert_alpha()
        power_up_bar_5 = pg.image.load("Power_up/sprite_04.png").convert_alpha()
        power_up_bar_6 = pg.image.load("Power_up/sprite_05.png").convert_alpha()
        power_up_bar_7 = pg.image.load("Power_up/sprite_06.png").convert_alpha()
        power_up_bar_8 = pg.image.load("Power_up/sprite_07.png").convert_alpha()
        power_up_bar_9 = pg.image.load("Power_up/sprite_08.png").convert_alpha()
        power_up_bar_10 = pg.image.load("Power_up/sprite_09.png").convert_alpha()

        # Get a reference to pygame channel
        self.channel = pg.mixer.Channel(0)
        self.channel_2 = pg.mixer.Channel(1)
        self.channel_3 = pg.mixer.Channel(2)
        self.channel_4 = pg.mixer.Channel(4)

        #import sound
        self.sound_01 = pg.mixer.Sound("sfx\mixkit-war-field-explosion-1702.wav")
        self.sound_01.set_volume(0.3)
        self.sound_02 = pg.mixer.Sound("sfx\mixkit-impact-of-a-blow-2150.wav")
        self.sound_02.set_volume(0.3)#pygame/
        self.sound_03 = pg.mixer.Sound("sfx/mixkit-hard-and-quick-punch-2143.wav")
        self.sound_03.set_volume(0.3)
        self.man_scream = pg.mixer.Sound("sfx/mixkit-fighting-mans-voice-2171.wav")
        self.ground_rumbling = pg.mixer.Sound("sfx/ground rumbling.wav")
        self.attack_rumbling = pg.mixer.Sound("sfx/attack_2_rumble.wav")
        self.grunt = pg.mixer.Sound("sfx/angry-grunt-103204.mp3")#pygame/sfx/mixkit-metal-hit-woosh-1485.wav

        # Add Power_up bar frames to power_up_frames
        self.power_up_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                power_up_bar_1, power_up_bar_2, power_up_bar_3, power_up_bar_4, power_up_bar_5, power_up_bar_6, power_up_bar_7, power_up_bar_8, power_up_bar_9, power_up_bar_10 
            ]
        ]

        # Add take_hits into a list
        self.death_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                death_1, death_2, death_3, death_4, death_5, death_6, death_7, death_8, death_9, death_10, death_11, death_12, death_13, death_14, death_15, death_16, death_17, death_18, death_19 
            ]
        ]

        # Add them to the attack4_frames list
        self.jump__down_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                j_down_1, j_down_2, j_down_3
            ]
        ]

        # Add take_hits into a list
        self.take_hit_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                take_hit_1, take_hit_2, take_hit_3, take_hit_4, take_hit_5, take_hit_6
            ]
        ]

        # Add them to the attack4_frames list
        self.air_atk_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                air_atk_1, air_atk_2, air_atk_3, air_atk_4, air_atk_5, air_atk_6, air_atk_7
            ]
        ]

        # Add them to the roll_frames list
        self.roll_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                roll_1, roll_2, roll_3, roll_4, roll_5
            ]
        ]

        # Add them to the attack4_frames list
        self.attack4_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                sp_atk_1, sp_atk_2, sp_atk_3, sp_atk_4, sp_atk_5, sp_atk_6, sp_atk_7, sp_atk_8, sp_atk_9, sp_atk_10,
                sp_atk_11, sp_atk_12, sp_atk_13, sp_atk_14, sp_atk_15, sp_atk_16, sp_atk_17, sp_atk_18, sp_atk_19, sp_atk_20,
                sp_atk_21, sp_atk_22, sp_atk_23, sp_atk_24, sp_atk_25
            ]
        ]

        # Add them to the attack3_frames list
        self.attack3_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                atk_3_1, atk_3_2, atk_3_3, atk_3_4, atk_3_5, atk_3_6, atk_3_7, atk_3_8, atk_3_9, atk_3_10,
                atk_3_11, atk_3_12, atk_3_13, atk_3_14, atk_3_15, atk_3_16, atk_3_17, atk_3_18, atk_3_19, atk_3_20,
                atk_3_21, atk_3_22, atk_3_23
            ]
        ]

        # Add take_hits into a list
        self.health_bar_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                Health_bar_1, Health_bar_2, Health_bar_3, Health_bar_4, Health_bar_5, Health_bar_5, Health_bar_6, Health_bar_7, Health_bar_8, Health_bar_9
            ]
        ]

        # Scale all defend_frames sprites for higher resolution
        self.defend_frames = [
            pg.transform.scale2x(frame)
            for frame in [defend_1, defend_2, defend_3, defend_4, defend_5, defend_6, defend_7, defend_8, 
            defend_9, defend_10, defend_11, defend_12, defend_13]
        ]

        # Player Idle
        self.idle_frames = [
            pg.transform.scale2x(frame)
            for frame in [idle_1, idle_2, idle_3, idle_4, idle_5, idle_6]
        ]

        # Player running
        self.run_frames = [
            pg.transform.scale2x(frame)
            for frame in [run_1, run_2, run_3, run_4, run_5, run_6, run_7, run_8]
        ]

        # Player jumping
        self.jump_frames = [
            pg.transform.scale2x(frame)
            for frame in [j_up_1, j_up_2, j_up_3]
        ]

        # Player attacking
        self.attack_frames = [
            pg.transform.scale2x(frame)
            for frame in [atk_1, atk_2, atk_3, atk_4, atk_5, atk_6]
        ]

        # Player attacking 2
        self.attack2_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                atk_2_1, atk_2_2, atk_2_3, atk_2_4, atk_2_5, atk_2_6,
                atk_2_7, atk_2_8, atk_2_9, atk_2_10, atk_2_11, atk_2_12
            ]
        ]

        # Variable definitions
        self.frame_index = 0
        self.image = self.idle_frames[self.frame_index]
        width, height = self.image.get_size()
        self.image  = pg.transform.scale(self.image, (width * 2, height * 2))
        self.rect = self.image.get_rect(midbottom=(200, 570))
        self.gravity = 0
        self.speed = 5  # Player movement speed
        self.direction = 0  # Direction player is moving
        self.last_direction = 1  # Default to right direction
        self.jumping = False  # Flag to track if the player is jumping
        self.jumping_down = False  # Flag to track if the player is jumping
        self.attacking = False  # Flag to track if the player is attacking
        self.attacking_2 = False  # Flag for second attack
        self.attack_time = 0  # Timer to track the attack duration
        self.attack_complete = True  # Flag to track if the previous attack is complete
        self.attack_complete_2 = True  # Flag to track the second attack completion
        self.key_held = False  # Track if the J key is held down
        self.key_held_2 = False  # Track if the K key is held down
        self.attacking_3 = False  # Flag for third attack
        self.attack_complete_3 = True  # Flag to track if third attack is complete
        self.key_held_3 = False  # Track if the L key is held down (new key for third attack)
        self.key_held_4 = False
        self.defend = False
        self.defend_complete = True
        self.attacking_4 = False
        self.attack_complete_4 = True
        self.key_held_5 = False
        self.air_attack = False
        self.air_attack_complete = True
        self.key_held_6 = False
        self.take_hit = False
        self.take_hit_complete = True 
        self.health = 10
        self.health_index = 0
        self.power_up = True
        self.power_up_index = 8

    def stuff(self):
        collision_box = pg.Rect(
            self.rect.centerx - 8,  # 5 pixels to the left of centerx
            self.rect.y + 180,  # Start from the bottom and extend upwards by 7 pixels
            14,  # Width of the collision box
            self.rect.height - 210  # Height of the collision box
        )
        return collision_box.left, collision_box.top, collision_box.width, collision_box.height

    def player_input(self):
        keys = pg.key.get_pressed()
        self.direction = 0  # Reset direction

        # Jump input
        if (keys[pg.K_SPACE] or keys[pg.K_UP] or keys[pg.K_w]) and self.rect.bottom == 570 and not self.jumping:
            self.gravity = -15
            self.jumping = True 

        # Air attack
        if keys[pg.K_i] and self.rect.bottom < 570 and not self.air_attack:
            self.air_attack = True

        # Movement input (left/right)
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.direction = 1  # Move right
            self.last_direction = 1  # Update last direction to right
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.direction = -1  # Move left
            self.last_direction = -1  # Update last direction to left

        # Attack input - trigger only on key press if attack is complete
        if keys[pg.K_j] and not self.key_held and self.attack_complete:  # Trigger attack only if previous attack is complete
            self.attacking = True
            self.attack_time = 0
            self.attack_complete = False  # Mark attack as ongoing
            self.key_held = True  # Prevent further attacks while key is held down

        # Second attack input - trigger only on key press if second attack is complete
        if keys[pg.K_k] and not self.key_held_2 and self.attack_complete_2:
            self.attacking_2 = True
            self.attack_time = 0
            self.attack_complete_2 = False  # Mark second attack as ongoing
            self.key_held_2 = True  # Prevent further second attacks while key is held down

        # Reset attack condition if J or K key is released
        if not keys[pg.K_j] and self.key_held:
            self.key_held = False  # Allow the next attack once J is released
        if not keys[pg.K_k] and self.key_held_2:
            self.key_held_2 = False  # Allow the next second attack once K is released

        # Third attack input - trigger only on key press if third attack is complete
        if keys[pg.K_l] and not self.key_held_3 and self.attack_complete_3:
            self.attacking_3 = True
            self.attack_time = 0
            self.attack_complete_3 = False  # Mark third attack as ongoing
            self.key_held_3 = True  # Prevent further third attacks while key is held down

        # Reset third attack condition if L key is released
        if not keys[pg.K_l] and self.key_held_3:
            self.key_held_3 = False  # Allow the next third attack once L is released

        # Will only be available of power-up is true
        #if self.power_up:
        # Fourth attack input - trigger only on key press if third attack is complete
        if (keys[pg.K_b] and keys[pg.K_n]) and not self.key_held_5 and self.attack_complete_4:
            self.attacking_4 = True
            self.attack_time = 0
            self.attack_complete_4 = False  # Mark third attack as ongoing
            self.key_held_5 = True  # Prevent further third attacks while key is held down

        # Reset third attack condition if b & n key is released
        if not (keys[pg.K_b] and keys[pg.K_n]) and self.key_held_5:
            self.key_held_5 = False  # Allow the next third attack once L is released

        # Defend input - trigger only on key press if fourth attack is complete
        if keys[pg.K_m]:
            self.defend = True
           
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 570:
            self.rect.bottom = 570
            self.jumping = False  # Reset jumping flag when landing
    
    def draw(self, screen):
        # Draw the player image on the screen
        screen.blit(self.image, self.rect)
    
    def animation_state(self):
        if self.attacking:  # Attack animation
            self.frame_index += 0.2
            if self.frame_index >= len(self.attack_frames):
                self.frame_index = 0
                self.attacking = False  # Reset attack flag after animation
                self.attack_complete = True  # Mark attack as complete
            self.image = self.attack_frames[int(self.frame_index)]

            # Flip the attack frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)
            self.rect.x += 2 * self.direction  # Move player slightly forward while attacking

        elif self.attacking_2:  # Second attack animation
            self.frame_index += 0.2
            if self.frame_index >= len(self.attack2_frames):
                self.frame_index = 0
                self.attacking_2 = False  # Reset second attack flag after animation
                self.attack_complete_2 = True  # Mark second attack as complete
            self.image = self.attack2_frames[int(self.frame_index)]

            # Flip the attack frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)
            self.rect.x += 2 * self.direction  # Move player slightly forward while attacking

        elif self.attacking_3:  # Third attack animation
            self.frame_index += 0.2
            if int(self.frame_index) == 16:
                self.channel_3.play(self.attack_rumbling)
            if int(self.frame_index) == 3:
                self.channel.play(self.sound_03)
            if int(self.frame_index) == 6:
                self.channel.play(self.sound_03)
            if int(self.frame_index) == 9:
                self.channel.play(self.sound_03)
            if self.frame_index >= len(self.attack3_frames):
                self.frame_index = 0
                self.attacking_3 = False  # Reset third attack flag after animation
                self.attack_complete_3 = True  # Mark third attack as complete
            self.image = self.attack3_frames[int(self.frame_index)]

            # Flip the third attack frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)
            self.rect.x += 2 * self.direction  # Move player slightly forward while attacking

        elif self.attacking_4:  # Fourth attack animation
            self.frame_index += 0.17
            if int(self.frame_index) == 3:
                self.channel_2.play(self.ground_rumbling)
            if int(self.frame_index) == 17:
                self.channel_3.play(self.man_scream)
            if int(self.frame_index) == 18:
                self.channel_2.stop()
                self.channel.play(self.sound_01)
            if self.frame_index >= len(self.attack4_frames):
                self.frame_index = 0
                self.attacking_4 = False  # Reset third attack flag after animation
                self.attack_complete_4 = True  # Mark third attack as complete
                self.power_up = False
            self.image = self.attack4_frames[int(self.frame_index)]

            # Flip the Fourth attack frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)
            self.rect.x += 2 * self.direction  # Move player slightly forward while attacking

        elif self.air_attack:  # Air attack animation
            self.frame_index += 0.35
            if self.frame_index >= len(self.air_atk_frames):
                self.frame_index = 0
                self.air_attack = False  # Reset air attack flag after animation
                self.air_attack_complete = True  # Mark air attack as complete
            self.image = self.air_atk_frames[int(self.frame_index)]

            # Flip the Air attack frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)
            self.rect.x += 2 * self.direction  # Move player slightly forward while attacking
        
        elif self.defend:  # Defend animation
            self.frame_index += 0.2
            if self.frame_index >= len(self.defend_frames):
                self.frame_index = 7
                self.defend = False  # Reset defend flag after animation
                self.defend_complete= True  # defend as complete
            self.image = self.defend_frames[int(self.frame_index)]

            # Flip the defend frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)
            self.rect.x += 2 * self.direction  # Move player slightly forward while attacking


        elif self.jumping:  # Jumping animation
            self.frame_index += 0.2
            if self.frame_index >= len(self.jump_frames):
                self.frame_index = len(self.jump_frames) - 1  # Hold the last jump frame
            self.image = self.jump_frames[int(self.frame_index)]

            # Flip the jump frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)

        elif self.jumping_down:  # Jumping down animation
            self.frame_index += 0.2
            if self.frame_index >= len(self.jump__down_frames):
                self.frame_index = len(self.jump__down_frames) - 1  # Hold the last jump down frame
            self.image = self.jump__down_frames[int(self.frame_index)]

            # Flip the jump frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)

        elif self.direction != 0:  # Running animation
            self.frame_index += 0.2
            if self.frame_index >= len(self.run_frames):
                self.frame_index = 0
            self.image = self.run_frames[int(self.frame_index)]

            # Flip the running frame based on movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)
        
        elif self.take_hit:  # Take hit animation
            self.frame_index += 0.2
            if self.frame_index >= len(self.take_hit_frames):
                self.take_hit = False  # Reset the "take hit" flag after animation
                self.take_hit_complete = True  # Mark as complete if needed
                self.frame_index = 0  # Reset frame index to avoid looping
            else:
                self.image = self.take_hit_frames[int(self.frame_index)]

            # Flip the frame if necessary
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)


        else:  # Idle animation
            self.frame_index += 0.1
            if self.frame_index >= len(self.idle_frames):
                self.frame_index = 0
            self.image = self.idle_frames[int(self.frame_index)]

            # Flip the idle frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)

    def return_collision_box(self, enemy, screen):

        # Collision boxes for collision detecting
        count_1 = 0
        count_2 = 0
        count_3 = 0
        count_4 = 0

        #collision box definitions
        collision_box_atk3 = 0
        triangle_points = 0

        # Set the boxes according to the player animation
        if self.attacking_3:  # If the third attack animation is playing
            collision_box = pg.Rect(
                self.rect.centerx + 20,  # 5 pixels to the left of centerx
                self.rect.y + 190,  # Start from the bottom and extend upwards by 7 pixels
                50,  # Width of the collision box
                self.rect.height - 240  # Height of the collision box
            )
            # If player is facing left
            if self.last_direction == -1:
                # If player looks oppositee direction the box should change
                collision_box = pg.Rect(
                self.rect.centerx - 55,  # 5 pixels to the left of centerx
                self.rect.y + 190,  # Start from the bottom and extend upwards by 7 pixels
                60,  # Width of the collision box
                self.rect.height - 240  # Height of the collision box
                )
            # Hit animation for the enmy and drop blood levele for the enemy
            if int(self.frame_index) == 3:
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print(f"Collision detected!!")
                    if count_1 == 0:
                        enemy.take_hit = True
                        enemy.hit_taken()
                        count_1 += 1
                        enemy.take_hit = False
                    if count_1 >= 4:
                        count_1 = 0
            if int(self.frame_index) == 5:
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print("Collision detected!!")
                    if count_2 == 0:
                        enemy.take_hit = True
                        enemy.hit_taken()
                        count_2 += 1
                        enemy.take_hit = False
                    if count_2 >= 4:
                        count_2 = 0
            if int(self.frame_index) == 10:
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print("Collision detected!!")
                    if count_3 == 0:
                        enemy.take_hit = True
                        enemy.own_health()
                        enemy.hit_taken()
                        count_3 += 1
                        enemy.take_hit = False
                    if count_3 >= 4:
                        count_3 = 0
            if int(self.frame_index) == 18:
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print("Collision detected!!")
                    self.power_up_index -= 0.4
                    if count_4 == 0:
                        enemy.take_hit = True
                        enemy.hit_taken()
                        count_4 += 1
                        enemy.take_hit = False
                    if count_4 >= 4:
                        count_4 = 0
   
            if self.frame_index > 17 and (self.frame_index <= 21):
                    triangle_points = [
                        pg.Vector2(self.rect.centerx + 140, self.rect.top + 172),  # Top of the player (center x)
                        pg.Vector2(self.rect.centerx, self.rect.bottom- 15),  # Bottom left of the attack triangle
                        pg.Vector2(self.rect.centerx + 185, self.rect.bottom - 15),  # Bottom right of the attack triangle
                    ]
        # Attack 4 will trigger hit animation and blood drop for thee enemy
        elif self.attacking_4:  # If the fourth attack animation is playing
            collision_box = pg.Rect(
                self.rect.centerx + 54,  # 5 pixels to the left of centerx
                self.rect.y + 180,  # Start from the bottom and extend upwards by 7 pixels
                45,  # Width of the collision box
                self.rect.height - 190  # Height of the collision box
            )
            # Hit animation for the enmy and drop blood level for the enemy
            if int(self.frame_index) == 6:
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print("Collision detected!!")
                    if count_1 == 0:
                        enemy.take_hit = True
                        enemy.own_health()
                        enemy.hit_taken()
                        count_1 += 1
                        enemy.take_hit = False
                    if count_1 >= 4:
                        count_1 = 0
            # Frame 5
            if int(self.frame_index) == 9:
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print("Collision detected!!")
                    if count_2 == 0:
                        enemy.take_hit = True
                        # Reduce health more than normally
                        enemy.own_health()
                        enemy.hit_taken()
                        count_2 += 1
                        enemy.take_hit = False
                    if count_2 >= 4:
                        count_2 = 0
            # Frame 18
            if int(self.frame_index) == 18:
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print("Collision detected!!")
                    if count_4 == 0:
                        enemy.take_hit = True
                        # Reduce health more than normally
                        enemy.own_health_sp_atk()
                        enemy.hit_taken()
                        count_4 += 1
                        enemy.take_hit = False
                    if count_4 >= 4:
                        count_4 = 0
        # If there are no attack animations then collision box stays on the body
        else:
            collision_box = pg.Rect(
                self.rect.centerx - 8,  # 5 pixels to the left of centerx
                self.rect.y + 180,  # Start from the bottom and extend upwards by 7 pixels
                14,  # Width of the collision box
                self.rect.height - 210  # Height of the collision box
            )
    
    def own_health(self):
        self.health_index += 0.1
    
    def own_health_sp_atk(self):
        self.health_index += 0.4
       
    def hit_taken(self):
        if self.take_hit:  # Take hit animation
            self.frame_index += 0.2
            if self.frame_index >= len(self.take_hit_frames):
                self.frame_index = 0
                self.take_hit = False  # Reset take hit flag after animation
                self.take_hit_complete = True  # Mark hit animation as complete
            self.image = self.take_hit_frames[int(self.frame_index)]

            # Flip the take hit frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)
        else:
            self.take_hit = False
    
    def update(self, screen):
        # Player input for movement and actions
        self.player_input()

        # Apply gravity
        self.apply_gravity()

        #pg.draw.rect(screen, (0, 255, 0), collision_box)  # Red box for collision area
        
        # Update animation and movement
        self.animation_state()

        # Actual player movement (separate from attack logic)
        self.rect.x += self.direction * self.speed  

        # Display the health bar
        screen.blit(self.health_bar_frames[int(self.health_index)], (20, 20)) 
        
        # Display the power up bar
        #screen.blit(self.power_up_frames[int(self.power_up_index)], (20, 40))