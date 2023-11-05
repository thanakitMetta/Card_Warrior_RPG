import pygame
from src.Util import SpriteManager, Animation
import src.Util as Util
from src.StateMachine import StateMachine

sprite_collection = SpriteManager().spriteCollection

gRogue_animation_list = {"down": sprite_collection["rogue_walk_down"].animation,
                         "right": sprite_collection["rogue_walk_right"].animation,
                         "up": sprite_collection["rogue_walk_up"].animation,
                         "left": sprite_collection["rogue_walk_left"].animation
                         }


gRogue_image_list = [sprite_collection["rogue_1"].image, sprite_collection["rogue_2"].image,
                     sprite_collection["rogue_3"].image, sprite_collection["rogue_4"].image,
                     sprite_collection["rogue_5"].image, sprite_collection["rogue_6"].image,
                     sprite_collection["rogue_7"].image, sprite_collection["rogue_8"].image,
                     sprite_collection["rogue_9"].image, sprite_collection["rogue_10"].image,
                     sprite_collection["rogue_11"].image, sprite_collection["rogue_12"].image]

gWarrior_image_list = [sprite_collection["warrior_1"].image, sprite_collection["warrior_2"].image,
                    sprite_collection["warrior_3"].image, sprite_collection["warrior_4"].image,
                    sprite_collection["warrior_5"].image,sprite_collection["warrior_6"].image,
                    sprite_collection["warrior_7"].image]

gWizard_image_list = [sprite_collection["wizard_1"].image, sprite_collection["wizard_2"].image,
                    sprite_collection["wizard_3"].image, sprite_collection["wizard_4"].image,
                    sprite_collection["wizard_5"].image, sprite_collection["wizard_6"].image,
                    sprite_collection["wizard_7"].image, sprite_collection["wizard_8"].image]

gWitch_image_list = [sprite_collection["witch_charge_1"].image, sprite_collection["witch_charge_2"].image,
                    sprite_collection["witch_charge_3"].image, sprite_collection["witch_charge_4"].image,
                    sprite_collection["witch_charge_5"].image]

gWitch2_image_list = [sprite_collection["witch_idle_1"].image, sprite_collection["witch_idle_2"].image,
                    sprite_collection["witch_idle_3"].image, sprite_collection["witch_idle_4"].image,
                    sprite_collection["witch_idle_5"].image, sprite_collection["witch_idle_6"].image]

gDice_image_list = [sprite_collection["dice_face_1"].image, sprite_collection["dice_face_2"].image,
                    sprite_collection["dice_face_3"].image, sprite_collection["dice_face_4"].image,
                    sprite_collection["dice_face_5"].image,sprite_collection["dice_face_6"].image]
#rogue battle sprite
gRogueBattleIdle_image_list = [sprite_collection["rogue_1_BI"].image, sprite_collection["rogue_2_BI"].image,
                    sprite_collection["rogue_3_BI"].image, sprite_collection["rogue_4_BI"].image]

gRogueBattleAttack_image_list = [sprite_collection["rogue_1_BA"].image, sprite_collection["rogue_2_BA"].image,
                    sprite_collection["rogue_3_BA"].image, sprite_collection["rogue_4_BA"].image,
                    sprite_collection["rogue_5_BA"].image, sprite_collection["rogue_6_BA"].image,
                    sprite_collection["rogue_7_BA"].image, sprite_collection["rogue_8_BA"].image,
                    sprite_collection["rogue_9_BA"].image, sprite_collection["rogue_10_BA"].image]

gRogueBattleDead_image_list = [sprite_collection["rogue_1_BD"].image, sprite_collection["rogue_2_BD"].image,
                    sprite_collection["rogue_3_BD"].image, sprite_collection["rogue_4_BD"].image,
                    sprite_collection["rogue_5_BD"].image, sprite_collection["rogue_6_BD"].image,
                    sprite_collection["rogue_7_BD"].image]

gRogueBattleSkill_image_list = [sprite_collection["rogue_1_BS"].image, sprite_collection["rogue_2_BS"].image,
                    sprite_collection["rogue_3_BS"].image, sprite_collection["rogue_4_BS"].image,
                    sprite_collection["rogue_5_BS"].image, sprite_collection["rogue_6_BS"].image,
                    sprite_collection["rogue_7_BS"].image, sprite_collection["rogue_8_BS"].image,
                    sprite_collection["rogue_9_BS"].image]
gRogueBattleHurt_image_list = [sprite_collection["rogue_1_Hurt"].image, sprite_collection["rogue_2_Hurt"].image,
                    sprite_collection["rogue_3_Hurt"].image, sprite_collection["rogue_4_Hurt"].image,
                    sprite_collection["rogue_5_Hurt"].image]

gRogueBattle_image_list = [gRogueBattleIdle_image_list, gRogueBattleAttack_image_list, gRogueBattleHurt_image_list, gRogueBattleDead_image_list,
                           gRogueBattleDead_image_list, gRogueBattleSkill_image_list]
# end of rogue battle sprite

gKnightBattleAttack_image_list = [sprite_collection["knight_1_BA"].image, sprite_collection["knight_2_BA"].image, 
                                  sprite_collection["knight_3_BA"].image, sprite_collection["knight_4_BA"].image,
                                  sprite_collection["knight_5_BA"].image]
gKnightBattleHurt_image_list = [sprite_collection["knight_1_Hurt"].image, sprite_collection["knight_2_Hurt"].image]
gKnightBattleIdle_image_list = [sprite_collection["knight_1_Idle"].image, sprite_collection["knight_2_Idle"].image]
gKnightBattleDead_image_list = [sprite_collection["knight_1_dead"].image, sprite_collection["knight_2_dead"].image,
                                sprite_collection["knight_3_dead"].image, sprite_collection["knight_4_dead"].image,
                                sprite_collection["knight_5_dead"].image, sprite_collection["knight_6_dead"].image]
gKnightBattleDeadIdle_image_list = [sprite_collection["knight_1_deadidle"].image,sprite_collection["knight_2_deadidle"].image]

gKnightBattle_image_list = [gKnightBattleIdle_image_list, gKnightBattleAttack_image_list, gKnightBattleHurt_image_list, 
                            gKnightBattleDead_image_list, gKnightBattleDeadIdle_image_list]



gSounds = {
    'music': pygame.mixer.Sound('sounds/music.wav'),
    #extra
    'Retro_Single_v6': pygame.mixer.Sound('sounds/Retro_Single_v6.wav'),
    'late-hours': pygame.mixer.Sound('sounds/late-hours.wav'),
    'campfire_fireplace': pygame.mixer.Sound('sounds/campfire_fireplace.wav'),
    'no-select': pygame.mixer.Sound('sounds/no-select.wav'),
    'select': pygame.mixer.Sound('sounds/select.wav'),
    'confirm': pygame.mixer.Sound('sounds/confirm.wav'),
    'wall_hit': pygame.mixer.Sound('sounds/wall_hit.wav')
}

gFonts = {
    'small': pygame.font.Font('fonts/font.ttf', 24),
    'medium': pygame.font.Font('fonts/font.ttf', 48),
    'large': pygame.font.Font('fonts/font.ttf', 96),
    'zelda_small': pygame.font.Font('fonts/zelda.otf', 96),
    'zelda': pygame.font.Font('fonts/zelda.otf', 192),
    'gothic_medium': pygame.font.Font('fonts/GothicPixels.ttf', 48),
    'gothic_large': pygame.font.Font('fonts/GothicPixels.ttf', 96),

}


from src.states.game.StartState import StartState
from src.states.game.CharacterSelectState import CharacterSelectState
from src.states.game.RollDiceState import RollDiceState
from src.StateMachine import StateMachine
from src.states.game.BattleState import BattleState
