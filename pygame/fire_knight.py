import time
import pygame as pg

# Player Class
class Fire_knight(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Sound effects
        self.channel_7 = pg.mixer.Channel(7)
        self.channel_8 = pg.mixer.Channel(6)
        self.slash = pg.mixer.Sound("sfx/mixkit-metal-hit-woosh-1485.wav")
        self.fire_slash = pg.mixer.Sound("fire_woosh.mp3")
        self.sword_swing = pg.mixer.Sound("sword swing.mp3")
        self.fire_slash.set_volume(10)


        # Import Death animation
        death_1 = pg.image.load("fire_knight/11_death/death_1.png").convert_alpha()
        death_2 = pg.image.load("fire_knight/11_death/death_2.png").convert_alpha()
        death_3 = pg.image.load("fire_knight/11_death/death_3.png").convert_alpha()
        death_4 = pg.image.load("fire_knight/11_death/death_4.png").convert_alpha()
        death_5 = pg.image.load("fire_knight/11_death/death_5.png").convert_alpha()
        death_6 = pg.image.load("fire_knight/11_death/death_6.png").convert_alpha()
        death_7 = pg.image.load("fire_knight/11_death/death_7.png").convert_alpha()
        death_8 = pg.image.load("fire_knight/11_death/death_8.png").convert_alpha()
        death_9 = pg.image.load("fire_knight/11_death/death_9.png").convert_alpha()
        death_10 = pg.image.load("fire_knight/11_death/death_10.png").convert_alpha()
        death_11 = pg.image.load("fire_knight/11_death/death_11.png").convert_alpha()
        death_12 = pg.image.load("fire_knight/11_death/death_12.png").convert_alpha()
        death_13 = pg.image.load("fire_knight/11_death/death_13.png").convert_alpha()

        # Import idle sprites
        idle_1 = pg.image.load("fire_knight/01_idle/idle_1.png").convert_alpha()
        idle_2 = pg.image.load("fire_knight/01_idle/idle_2.png").convert_alpha()
        idle_3 = pg.image.load("fire_knight/01_idle/idle_3.png").convert_alpha()
        idle_4 = pg.image.load("fire_knight/01_idle/idle_4.png").convert_alpha()
        idle_5 = pg.image.load("fire_knight/01_idle/idle_5.png").convert_alpha()
        idle_6 = pg.image.load("fire_knight/01_idle/idle_6.png").convert_alpha()
        idle_7 = pg.image.load("fire_knight/01_idle/idle_7.png").convert_alpha()
        idle_8 = pg.image.load("fire_knight/01_idle/idle_8.png").convert_alpha()

        # Import defend sprites
        defend_1 = pg.image.load("fire_knight/09_defend/defend_1.png").convert_alpha()
        defend_2 = pg.image.load("fire_knight/09_defend/defend_2.png").convert_alpha()
        defend_3 = pg.image.load("fire_knight/09_defend/defend_3.png").convert_alpha()
        defend_4 = pg.image.load("fire_knight/09_defend/defend_4.png").convert_alpha()
        defend_5 = pg.image.load("fire_knight/09_defend/defend_5.png").convert_alpha()
        defend_6 = pg.image.load("fire_knight/09_defend/defend_6.png").convert_alpha()
        defend_7 = pg.image.load("fire_knight/09_defend/defend_7.png").convert_alpha()
        defend_8 = pg.image.load("fire_knight/09_defend/defend_8.png").convert_alpha()
        defend_9 = pg.image.load("fire_knight/09_defend/defend_9.png").convert_alpha()
        defend_10 = pg.image.load("fire_knight/09_defend/defend_10.png").convert_alpha()

        # Import running sprites
        run_1 = pg.image.load("fire_knight/02_run/run_1.png").convert_alpha()
        run_2 = pg.image.load("fire_knight/02_run/run_2.png").convert_alpha()
        run_3 = pg.image.load("fire_knight/02_run/run_3.png").convert_alpha()
        run_4 = pg.image.load("fire_knight/02_run/run_4.png").convert_alpha()
        run_5 = pg.image.load("fire_knight/02_run/run_5.png").convert_alpha()
        run_6 = pg.image.load("fire_knight/02_run/run_6.png").convert_alpha()
        run_7 = pg.image.load("fire_knight/02_run/run_7.png").convert_alpha()
        run_8 = pg.image.load("fire_knight/02_run/run_8.png").convert_alpha()

        # Import jumping sprites
        j_up_1 = pg.image.load("fire_knight/03_jump/jump_1.png").convert_alpha()
        j_up_2 = pg.image.load("fire_knight/03_jump/jump_2.png").convert_alpha()
        j_up_3 = pg.image.load("fire_knight/03_jump/jump_3.png").convert_alpha()
        j_up_4 = pg.image.load("fire_knight/03_jump/jump_4.png").convert_alpha()
        j_up_5 = pg.image.load("fire_knight/03_jump/jump_5.png").convert_alpha()
        j_up_6 = pg.image.load("fire_knight/03_jump/jump_6.png").convert_alpha()
        j_up_7 = pg.image.load("fire_knight/03_jump/jump_7.png").convert_alpha()
        j_up_8 = pg.image.load("fire_knight/03_jump/jump_8.png").convert_alpha()
        j_up_9 = pg.image.load("fire_knight/03_jump/jump_9.png").convert_alpha()
        j_up_10 = pg.image.load("fire_knight/03_jump/jump_10.png").convert_alpha()
        j_up_11 = pg.image.load("fire_knight/03_jump/jump_11.png").convert_alpha()
        j_up_12 = pg.image.load("fire_knight/03_jump/jump_12.png").convert_alpha()
        j_up_13 = pg.image.load("fire_knight/03_jump/jump_13.png").convert_alpha()
        j_up_14 = pg.image.load("fire_knight/03_jump/jump_14.png").convert_alpha()
        j_up_15 = pg.image.load("fire_knight/03_jump/jump_15.png").convert_alpha()
        j_up_16 = pg.image.load("fire_knight/03_jump/jump_16.png").convert_alpha()
        j_up_17 = pg.image.load("fire_knight/03_jump/jump_17.png").convert_alpha()
        j_up_18 = pg.image.load("fire_knight/03_jump/jump_18.png").convert_alpha()
        j_up_19 = pg.image.load("fire_knight/03_jump/jump_19.png").convert_alpha()
        j_up_20 = pg.image.load("fire_knight/03_jump/jump_20.png").convert_alpha()

        # Import attack sprites
        atk_1 = pg.image.load("fire_knight/05_1_atk/1_atk_1.png").convert_alpha()
        atk_2 = pg.image.load("fire_knight/05_1_atk/1_atk_2.png").convert_alpha()
        atk_3 = pg.image.load("fire_knight/05_1_atk/1_atk_3.png").convert_alpha()
        atk_4 = pg.image.load("fire_knight/05_1_atk/1_atk_4.png").convert_alpha()
        atk_5 = pg.image.load("fire_knight/05_1_atk/1_atk_5.png").convert_alpha()
        atk_6 = pg.image.load("fire_knight/05_1_atk/1_atk_6.png").convert_alpha()
        atk_7 = pg.image.load("fire_knight/05_1_atk/1_atk_7.png").convert_alpha()
        atk_8 = pg.image.load("fire_knight/05_1_atk/1_atk_8.png").convert_alpha()
        atk_9 = pg.image.load("fire_knight/05_1_atk/1_atk_9.png").convert_alpha()
        atk_10 = pg.image.load("fire_knight/05_1_atk/1_atk_10.png").convert_alpha()
        atk_11 = pg.image.load("fire_knight/05_1_atk/1_atk_11.png").convert_alpha()

        # Import second attack sprites (2_atk)
        atk_2_1 = pg.image.load("fire_knight/06_2_atk/2_atk_1.png").convert_alpha()
        atk_2_2 = pg.image.load("fire_knight/06_2_atk/2_atk_2.png").convert_alpha()
        atk_2_3 = pg.image.load("fire_knight/06_2_atk/2_atk_3.png").convert_alpha()
        atk_2_4 = pg.image.load("fire_knight/06_2_atk/2_atk_4.png").convert_alpha()
        atk_2_5 = pg.image.load("fire_knight/06_2_atk/2_atk_5.png").convert_alpha()
        atk_2_6 = pg.image.load("fire_knight/06_2_atk/2_atk_6.png").convert_alpha()
        atk_2_7 = pg.image.load("fire_knight/06_2_atk/2_atk_7.png").convert_alpha()
        atk_2_8 = pg.image.load("fire_knight/06_2_atk/2_atk_8.png").convert_alpha()
        atk_2_9 = pg.image.load("fire_knight/06_2_atk/2_atk_9.png").convert_alpha()
        atk_2_10 = pg.image.load("fire_knight/06_2_atk/2_atk_10.png").convert_alpha()
        atk_2_11 = pg.image.load("fire_knight/06_2_atk/2_atk_11.png").convert_alpha()
        atk_2_12 = pg.image.load("fire_knight/06_2_atk/2_atk_12.png").convert_alpha()
        atk_2_13 = pg.image.load("fire_knight/06_2_atk/2_atk_13.png").convert_alpha()
        atk_2_14 = pg.image.load("fire_knight/06_2_atk/2_atk_14.png").convert_alpha()
        atk_2_15 = pg.image.load("fire_knight/06_2_atk/2_atk_15.png").convert_alpha()
        atk_2_16 = pg.image.load("fire_knight/06_2_atk/2_atk_16.png").convert_alpha()
        atk_2_17 = pg.image.load("fire_knight/06_2_atk/2_atk_17.png").convert_alpha()
        atk_2_18 = pg.image.load("fire_knight/06_2_atk/2_atk_18.png").convert_alpha()
        atk_2_19 = pg.image.load("fire_knight/06_2_atk/2_atk_19.png").convert_alpha()

        # Import third attack sprites (3_atk)
        atk_3_1 = pg.image.load("fire_knight/07_3_atk/3_atk_1.png").convert_alpha()
        atk_3_2 = pg.image.load("fire_knight/07_3_atk/3_atk_2.png").convert_alpha()
        atk_3_3 = pg.image.load("fire_knight/07_3_atk/3_atk_3.png").convert_alpha()
        atk_3_4 = pg.image.load("fire_knight/07_3_atk/3_atk_4.png").convert_alpha()
        atk_3_5 = pg.image.load("fire_knight/07_3_atk/3_atk_5.png").convert_alpha()
        atk_3_6 = pg.image.load("fire_knight/07_3_atk/3_atk_6.png").convert_alpha()
        atk_3_7 = pg.image.load("fire_knight/07_3_atk/3_atk_7.png").convert_alpha()
        atk_3_8 = pg.image.load("fire_knight/07_3_atk/3_atk_8.png").convert_alpha()
        atk_3_9 = pg.image.load("fire_knight/07_3_atk/3_atk_9.png").convert_alpha()
        atk_3_10 = pg.image.load("fire_knight/07_3_atk/3_atk_10.png").convert_alpha()
        atk_3_11 = pg.image.load("fire_knight/07_3_atk/3_atk_11.png").convert_alpha()
        atk_3_12 = pg.image.load("fire_knight/07_3_atk/3_atk_12.png").convert_alpha()
        atk_3_13 = pg.image.load("fire_knight/07_3_atk/3_atk_13.png").convert_alpha()
        atk_3_14 = pg.image.load("fire_knight/07_3_atk/3_atk_14.png").convert_alpha()
        atk_3_15 = pg.image.load("fire_knight/07_3_atk/3_atk_15.png").convert_alpha()
        atk_3_16 = pg.image.load("fire_knight/07_3_atk/3_atk_16.png").convert_alpha()
        atk_3_17 = pg.image.load("fire_knight/07_3_atk/3_atk_17.png").convert_alpha()
        atk_3_18 = pg.image.load("fire_knight/07_3_atk/3_atk_18.png").convert_alpha()
        atk_3_19 = pg.image.load("fire_knight/07_3_atk/3_atk_19.png").convert_alpha()
        atk_3_20 = pg.image.load("fire_knight/07_3_atk/3_atk_20.png").convert_alpha()
        atk_3_21 = pg.image.load("fire_knight/07_3_atk/3_atk_21.png").convert_alpha()
        atk_3_22 = pg.image.load("fire_knight/07_3_atk/3_atk_22.png").convert_alpha()
        atk_3_23 = pg.image.load("fire_knight/07_3_atk/3_atk_23.png").convert_alpha()
        atk_3_24 = pg.image.load("fire_knight/07_3_atk/3_atk_24.png").convert_alpha()
        atk_3_25 = pg.image.load("fire_knight/07_3_atk/3_atk_25.png").convert_alpha()
        atk_3_26 = pg.image.load("fire_knight/07_3_atk/3_atk_26.png").convert_alpha()
        atk_3_27 = pg.image.load("fire_knight/07_3_atk/3_atk_27.png").convert_alpha()
        atk_3_28 = pg.image.load("fire_knight/07_3_atk/3_atk_28.png").convert_alpha()

        # Import special attack
        sp_atk_1 = pg.image.load("fire_knight/08_sp_atk/sp_atk_1.png").convert_alpha()
        sp_atk_2 = pg.image.load("fire_knight/08_sp_atk/sp_atk_2.png").convert_alpha()
        sp_atk_3 = pg.image.load("fire_knight/08_sp_atk/sp_atk_3.png").convert_alpha()
        sp_atk_4 = pg.image.load("fire_knight/08_sp_atk/sp_atk_4.png").convert_alpha()
        sp_atk_5 = pg.image.load("fire_knight/08_sp_atk/sp_atk_5.png").convert_alpha()
        sp_atk_6 = pg.image.load("fire_knight/08_sp_atk/sp_atk_6.png").convert_alpha()
        sp_atk_7 = pg.image.load("fire_knight/08_sp_atk/sp_atk_7.png").convert_alpha()
        sp_atk_8 = pg.image.load("fire_knight/08_sp_atk/sp_atk_8.png").convert_alpha()
        sp_atk_9 = pg.image.load("fire_knight/08_sp_atk/sp_atk_9.png").convert_alpha()
        sp_atk_10 = pg.image.load("fire_knight/08_sp_atk/sp_atk_10.png").convert_alpha()
        sp_atk_11 = pg.image.load("fire_knight/08_sp_atk/sp_atk_11.png").convert_alpha()
        sp_atk_12 = pg.image.load("fire_knight/08_sp_atk/sp_atk_12.png").convert_alpha()
        sp_atk_13 = pg.image.load("fire_knight/08_sp_atk/sp_atk_13.png").convert_alpha()
        sp_atk_14 = pg.image.load("fire_knight/08_sp_atk/sp_atk_14.png").convert_alpha()
        sp_atk_15 = pg.image.load("fire_knight/08_sp_atk/sp_atk_15.png").convert_alpha()
        sp_atk_16 = pg.image.load("fire_knight/08_sp_atk/sp_atk_16.png").convert_alpha()
        sp_atk_17 = pg.image.load("fire_knight/08_sp_atk/sp_atk_17.png").convert_alpha()
        sp_atk_18 = pg.image.load("fire_knight/08_sp_atk/sp_atk_18.png").convert_alpha()

        # Import roll
        roll_1 = pg.image.load("fire_knight/04_roll/roll_1.png").convert_alpha()
        roll_2 = pg.image.load("fire_knight/04_roll/roll_2.png").convert_alpha()
        roll_3 = pg.image.load("fire_knight/04_roll/roll_3.png").convert_alpha()
        roll_4 = pg.image.load("fire_knight/04_roll/roll_4.png").convert_alpha()
        roll_5 = pg.image.load("fire_knight/04_roll/roll_5.png").convert_alpha()
        roll_6 = pg.image.load("fire_knight/04_roll/roll_6.png").convert_alpha()
        roll_7 = pg.image.load("fire_knight/04_roll/roll_7.png").convert_alpha()
        roll_8 = pg.image.load("fire_knight/04_roll/roll_8.png").convert_alpha()

        # Import air attack
        air_atk_1 = pg.image.load("fire_knight/air_atk/air_atk_1.png").convert_alpha()
        air_atk_2 = pg.image.load("fire_knight/air_atk/air_atk_2.png").convert_alpha()
        air_atk_3 = pg.image.load("fire_knight/air_atk/air_atk_3.png").convert_alpha()
        air_atk_4 = pg.image.load("fire_knight/air_atk/air_atk_4.png").convert_alpha()
        air_atk_5 = pg.image.load("fire_knight/air_atk/air_atk_5.png").convert_alpha()
        air_atk_6 = pg.image.load("fire_knight/air_atk/air_atk_6.png").convert_alpha()
        air_atk_7 = pg.image.load("fire_knight/air_atk/air_atk_7.png").convert_alpha()
        air_atk_8 = pg.image.load("fire_knight/air_atk/air_atk_8.png").convert_alpha()

        # Import taking hit sprite
        take_hit_1 = pg.image.load("fire_knight/10_take_hit/take_hit_1.png").convert_alpha()
        take_hit_2 = pg.image.load("fire_knight/10_take_hit/take_hit_2.png").convert_alpha()
        take_hit_3 = pg.image.load("fire_knight/10_take_hit/take_hit_3.png").convert_alpha()
        take_hit_4 = pg.image.load("fire_knight/10_take_hit/take_hit_4.png").convert_alpha()
        take_hit_5 = pg.image.load("fire_knight/10_take_hit/take_hit_5.png").convert_alpha()
        take_hit_6 = pg.image.load("fire_knight/10_take_hit/take_hit_6.png").convert_alpha()

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
        self.grunt = pg.mixer.Sound("sfx/angry-grunt-103204.mp3")

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
                death_1, death_2, death_3, death_4, death_5, death_6, death_7, death_8, death_9, death_10, death_11, death_12, death_13 
            ]
        ]

        # Add them to the attack4_frames list
        self.jump_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                j_up_1, j_up_2, j_up_3, j_up_4, j_up_5, j_up_6, j_up_7, j_up_8, j_up_9, j_up_10, j_up_11, j_up_12, j_up_13, j_up_14, j_up_15, j_up_16, j_up_17, j_up_18, j_up_19, j_up_20
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
                air_atk_1, air_atk_2, air_atk_3, air_atk_4, air_atk_5, air_atk_6, air_atk_7, air_atk_8
            ]
        ]

        # Add them to the roll_frames list
        self.roll_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                roll_1, roll_2, roll_3, roll_4, roll_5, roll_6, roll_7, roll_8
            ]
        ]

        # Add them to the attack4_frames list
        self.attack4_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                sp_atk_1, sp_atk_2, sp_atk_3, sp_atk_4, sp_atk_5, sp_atk_6, sp_atk_7, sp_atk_8, sp_atk_9, sp_atk_10,
                sp_atk_11, sp_atk_12, sp_atk_13, sp_atk_14, sp_atk_15, sp_atk_16, sp_atk_17, sp_atk_18
            ]
        ]

        # Add them to the attack3_frames list
        self.attack3_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                atk_3_1, atk_3_2, atk_3_3, atk_3_4, atk_3_5, atk_3_6, atk_3_7, atk_3_8, atk_3_9, atk_3_10,
                atk_3_11, atk_3_12, atk_3_13, atk_3_14, atk_3_15, atk_3_16, atk_3_17, atk_3_18, atk_3_19, atk_3_20,
                atk_3_21, atk_3_22, atk_3_23, atk_3_24, atk_3_25, atk_3_26, atk_3_27, atk_3_28
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
            defend_9, defend_10]
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

        # Player attacking
        self.attack_frames = [
            pg.transform.scale2x(frame)
            for frame in [atk_1, atk_2, atk_3, atk_4, atk_5, atk_6, atk_7, atk_8, atk_9, atk_10, atk_11]
        ]

        # Player attacking 2
        self.attack2_frames = [
            pg.transform.scale2x(frame)
            for frame in [
                atk_2_1, atk_2_2, atk_2_3, atk_2_4, atk_2_5, atk_2_6,
                atk_2_7, atk_2_8, atk_2_9, atk_2_10, atk_2_11, atk_2_12, atk_2_13,
                atk_2_14, atk_2_15, atk_2_16, atk_2_17, atk_2_18, atk_2_19
            ]
        ]

        # Variable definitions
        self.frame_index = 0
        self.image = self.idle_frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=(100, 100))
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
            self.rect.centerx + 270,  # 5 pixels to the left of centerx
            self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
            60,  # Width of the collision box
            self.rect.height - 150  # Height of the collision box
        )
        return collision_box.left, collision_box.top, collision_box.width, collision_box.height

    def player_input(self):
        keys = pg.key.get_pressed()
        self.direction = 0  # Reset direction

        # Jump input
        if (keys[pg.K_SPACE] or keys[pg.K_UP] or keys[pg.K_w]) and self.rect.bottom == 480 and not self.jumping:
            self.gravity = -20
            self.jumping = True 

        # Air attack
        if keys[pg.K_q] and self.rect.bottom < 480 and not self.air_attack:
            self.air_attack = True

        # Movement input (left/right)
        if keys[pg.K_d]:
            self.direction = 1  # Move right
            self.last_direction = 1  # Update last direction to right
        if keys[pg.K_a]:
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
        if self.rect.bottom >= 480:
            self.rect.bottom = 480
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
            self.image = pg.transform.scale2x(self.attack_frames[int(self.frame_index)]) 

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
            self.image = pg.transform.scale2x(self.attack2_frames[int(self.frame_index)])

            # Flip the attack frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)
            self.rect.x += 2 * self.direction  # Move player slightly forward while attacking

        elif self.attacking_3:  # Third attack animation
            self.frame_index += 0.2
            if self.frame_index >= len(self.attack3_frames):
                self.frame_index = 0
                self.attacking_3 = False  # Reset third attack flag after animation
                self.attack_complete_3 = True  # Mark third attack as complete
            self.image = pg.transform.scale2x(self.attack3_frames[int(self.frame_index)])

            # Flip the third attack frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)
            self.rect.x += 2 * self.direction  # Move player slightly forward while attacking

        elif self.attacking_4:  # Fourth attack animation
            self.frame_index += 0.17
            if self.frame_index >= len(self.attack4_frames):
                self.frame_index = 0
                self.attacking_4 = False  # Reset third attack flag after animation
                self.attack_complete_4 = True  # Mark third attack as complete
                self.power_up = False
            self.image = pg.transform.scale2x(self.attack4_frames[int(self.frame_index)])

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
            self.image = pg.transform.scale2x(self.air_atk_frames[int(self.frame_index)])

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
            self.image = pg.transform.scale2x(self.defend_frames[int(self.frame_index)])

            # Flip the defend frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)
            self.rect.x += 2 * self.direction  # Move player slightly forward while attacking


        elif self.jumping:  # Jumping animation
            self.frame_index += 0.2
            if self.frame_index >= len(self.jump_frames):
                self.frame_index = len(self.jump_frames) - 1  # Hold the last jump frame
            self.image = pg.transform.scale2x(self.jump_frames[int(self.frame_index)])

            # Flip the jump frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)

        elif self.jumping_down:  # Jumping down animation
            self.frame_index += 0.2
            if self.frame_index >= len(self.jump_frames):
                self.frame_index = len(self.jump_frames) - 1  # Hold the last jump down frame
            self.image = pg.transform.scale2x(self.jump_frames[int(self.frame_index)])

            # Flip the jump frame based on the last movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)

        elif self.direction != 0:  # Running animation
            self.frame_index += 0.2
            if self.frame_index >= len(self.run_frames):
                self.frame_index = 0
            self.image = pg.transform.scale2x(self.run_frames[int(self.frame_index)])

            # Flip the running frame based on movement direction
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)
        
        elif self.take_hit:  # Take hit animation
            self.frame_index += 0.2
            if self.frame_index >= len(self.take_hit_frames):
                self.take_hit = False  # Reset the "take hit" flag after animation
                self.take_hit_complete = True  # Mark as complete if needed
                self.frame_index = 0  # Reset frame index to avoid looping
            self.image = pg.transform.scale2x(self.take_hit_frames[int(self.frame_index)])

            # Flip the frame if necessary
            if self.last_direction == -1:
                self.image = pg.transform.flip(self.image, True, False)


        else:  # Idle animation
            self.frame_index += 0.1
            if self.frame_index >= len(self.idle_frames):
                self.frame_index = 0
            self.image = pg.transform.scale2x(self.idle_frames[int(self.frame_index)])

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
        if self.attacking:
            collision_box = pg.Rect(
                self.rect.centerx + 393,  # 5 pixels to the left of centerx
                self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
                150,  # Width of the collision box
                self.rect.height - 100  # Height of the collision box
            )
            # If player is facing left
            if self.last_direction == -1:
                # If player looks oppositee direction the box should change
                collision_box = pg.Rect(
                self.rect.centerx + 45,  # 5 pixels to the left of centerx
                self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
                147,  # Width of the collision box
                self.rect.height - 100  # Height of the collision box
                )
             # Hit animation for the enmy and drop blood levele for the enemy
            if int(self.frame_index) == 4:
                # Play slash sound effect
                self.channel_7.play(self.slash)
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print(f"Collision detected!!")
                    if count_1 == 0:
                        enemy.take_hit = True
                        enemy.hit_taken()
                        enemy.own_health()
                        count_1 += 1
                        enemy.take_hit = False
                    if count_1 >= 4:
                        count_1 = 0
        elif self.attacking_2:
            collision_box = pg.Rect(
                self.rect.centerx + 393,  # 5 pixels to the left of centerx
                self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
                150,  # Width of the collision box
                self.rect.height - 100  # Height of the collision box
            )
            
            # If player is facing left
            if self.last_direction == -1:
                # If player looks oppositee direction the box should change
                collision_box = pg.Rect(
                    self.rect.centerx + 45,  # 5 pixels to the left of centerx
                    self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
                    147,  # Width of the collision box
                    self.rect.height - 100  # Height of the collision box
                )
                
            # When the frame is at index and 10 to 15 the box should chnage
            if int(self.frame_index) >= 10 and int(self.frame_index) < 17:
                collision_box = pg.Rect(
                    self.rect.centerx + 140,  # 5 pixels to the left of centerx
                    self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
                    400,  # Width of the collision box
                    self.rect.height - 100  # Height of the collision box
                )
                if self.last_direction == -1:
                    collision_box = pg.Rect(
                        self.rect.centerx + 10,  # 5 pixels to the left of centerx
                        self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
                        430,  # Width of the collision box
                        self.rect.height - 100  # Height of the collision box
                    )

            # Hit animation for the enmy and drop blood levele for the enemy
            if int(self.frame_index) == 4:
                # Play slash sound effect
                self.channel_7.play(self.slash)
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print(f"Collision detected!!")
                    if count_1 == 0:
                        enemy.take_hit = True
                        enemy.hit_taken()
                        enemy.own_health()
                        count_1 += 1
                        enemy.take_hit = False
                    if count_1 >= 4:
                        count_1 = 0
            if int(self.frame_index) == 9:
                self.channel_8.play(self.sword_swing)
            if int(self.frame_index) == 12:
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print(f"Collision detected!!")
                    if count_1 == 0:
                        enemy.take_hit = True
                        enemy.hit_taken()
                        enemy.own_health()
                        count_1 += 1
                        enemy.take_hit = False
                    if count_1 >= 4:
                        count_1 = 0
            if int(self.frame_index) == 11:
                self.channel_8.play(self.sword_swing)
            if int(self.frame_index) == 14:
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print(f"Collision detected!!")
                    if count_1 == 0:
                        enemy.take_hit = True
                        enemy.hit_taken()
                        enemy.own_health()
                        count_1 += 1
                        enemy.take_hit = False
                    if count_1 >= 4:
                        count_1 = 0
        elif self.attacking_3:  # If the third attack animation is playing
            collision_box = pg.Rect(
                self.rect.centerx + 393,  # 5 pixels to the left of centerx
                self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
                150,  # Width of the collision box
                self.rect.height - 100  # Height of the collision box
            )
            # If player is facing left
            if self.last_direction == -1:
                # If player looks oppositee direction the box should change
                collision_box = pg.Rect(
                    self.rect.centerx + 45,  # 5 pixels to the left of centerx
                    self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
                    147,  # Width of the collision box
                    self.rect.height - 100  # Height of the collision box
                )
            # When the frame is at index and 10 to 15 the box should chnage
            if int(self.frame_index) >= 10 and int(self.frame_index) < 17:
                collision_box = pg.Rect(
                    self.rect.centerx + 140,  # 5 pixels to the left of centerx
                    self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
                    400,  # Width of the collision box
                    self.rect.height - 100  # Height of the collision box
                )
                if self.last_direction == -1:
                    collision_box = pg.Rect(
                        self.rect.centerx + 10,  # 5 pixels to the left of centerx
                        self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
                        430,  # Width of the collision box
                        self.rect.height - 100  # Height of the collision box
                    )
            # When the frame is at index and 10 to 15 the box should chnage
            if int(self.frame_index) >= 22 and int(self.frame_index) < 27:
                collision_box = pg.Rect(
                    self.rect.centerx + 393,  # 5 pixels to the left of centerx
                    self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
                    150,  # Width of the collision box
                    self.rect.height - 100  # Height of the collision box
                )
                if self.last_direction == -1:
                    collision_box = pg.Rect(
                        self.rect.centerx + 45,  # 5 pixels to the left of centerx
                        self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
                        147,  # Width of the collision box
                        self.rect.height - 100  # Height of the collision box
                    )
            
            # Hit animation for the enmy and drop blood levele for the enemy
            if int(self.frame_index) == 4:
                # Play slash sound effect
                self.channel_7.play(self.slash)
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print(f"Collision detected!!")
                    if count_1 == 0:
                        enemy.take_hit = True
                        enemy.hit_taken()
                        enemy.own_health()
                        count_1 += 1
                        enemy.take_hit = False
                    if count_1 >= 4:
                        count_1 = 0
            if int(self.frame_index) == 9:
                self.channel_8.play(self.sword_swing)
            if int(self.frame_index) == 12:
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print("Collision detected!!")
                    if count_2 == 0:
                        enemy.take_hit = True
                        enemy.hit_taken()
                        enemy.own_health()
                        count_2 += 1
                        enemy.take_hit = False
                    if count_2 >= 4:
                        count_2 = 0
            if int(self.frame_index) == 11:
                self.channel_8.play(self.sword_swing)
            if int(self.frame_index) == 14:
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
            if int(self.frame_index) == 20:
                self.channel_8.play(self.fire_slash)
            if int(self.frame_index) == 24:
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print("Collision detected!!")
                    self.power_up_index -= 0.4
                    if count_4 == 0:
                        enemy.take_hit = True
                        enemy.hit_taken()
                        enemy.own_health()
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
                self.rect.centerx + 393,  # 5 pixels to the left of centerx
                self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
                300,  # Width of the collision box
                self.rect.height - 100  # Height of the collision box
            )
            if self.last_direction == -1:
                # If player looks oppositee direction the box should change
                collision_box = pg.Rect(
                    self.rect.centerx - 100,  # 5 pixels to the left of centerx
                    self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
                    300,  # Width of the collision box
                    self.rect.height - 100  # Height of the collision box
                )
            # Hit animation for the enmy and drop blood level for the enemy
            if int(self.frame_index) == 0 or int(self.frame_index) == 1 or int(self.frame_index) == 2 or int(self.frame_index) == 3 or int(self.frame_index) == 4:
                self.channel_8.play(self.fire_slash)
            if int(self.frame_index) == 12:
                self.channel_7.play(self.slash)
                if collision_box.colliderect(pg.Rect(enemy.stuff())):
                    print("Collision detected!!")
                    if count_1 == 0:
                        enemy.take_hit = True
                        enemy.own_health_sp_atk()
                        enemy.own_health()
                        enemy.own_health()
                        enemy.hit_taken()
                        count_1 += 1
                        enemy.take_hit = False
                    if count_1 >= 4:
                        count_1 = 0
        # Else collisoon box stay focused on the body
        else:
            collision_box = pg.Rect(
            self.rect.centerx + 270,  # 5 pixels to the left of centerx
            self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
            60,  # Width of the collision box
            self.rect.height - 150  # Height of the collision box
        )
        #pg.draw.rect(screen, (0, 255, 255), collision_box)
    
    def own_health(self):
        self.health_index += 0.03
    
    def own_health_sp_atk(self):
        self.health_index += 0.4
       
    def hit_taken(self):
        if self.take_hit:  # Take hit animation
            self.frame_index += 0.2
            if self.frame_index >= len(self.take_hit_frames):
                self.frame_index = 0
                self.take_hit = False  # Reset take hit flag after animation
                self.take_hit_complete = True  # Mark hit animation as complete
            self.image = pg.transform.scale2x(self.take_hit_frames[int(self.frame_index)])

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

        #collision_box = pg.Rect(
            #self.rect.centerx + 270,  # 5 pixels to the left of centerx
            #self.rect.y + 350,  # Start from the bottom and extend upwards by 7 pixels
            #60,  # Width of the collision box
            #self.rect.height - 150  # Height of the collision box
        #)
        #pg.draw.rect(screen, (0, 255, 0), collision_box)
        
        # Update animation and movement
        self.animation_state()

        # Actual player movement (separate from attack logic)
        self.rect.x += self.direction * self.speed  

        # Display the health bar
        screen.blit(self.health_bar_frames[int(self.health_index)], (20, 20))

        # Print the bottom of the player
        #print(self.rect.bottom) 
        
        # Display the power up bar
        #screen.blit(self.power_up_frames[int(self.power_up_index)], (20, 40))