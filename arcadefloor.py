import pyray as pr

import utils
import gamestate

arcadefloortexture = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 5, 5, 1, 1, 1, 1, 1, 1, 2],
    [2, 1, 5, 1, 1, 1, 1, 1, 1, 3],
    [2, 10, 6, 1, 1, 1, 1, 1, 1, 3],
    [2, 5, 5, 1, 1, 1, 1, 1, 1, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 8, 2],
    [2, 2, 2, 7, 2, 2, 2, 2, 2, 2],
    [2, 4, 4, 4, 4, 4, 4, 4, 4, 2],
    [2, 4, 4, 4, 4, 4, 4, 4, 4, 2],
    [2, 4, 4, 4, 4, 4, 4, 4, 9, 2],
    [2, 4, 4, 4, 4, 4, 4, 4, 4, 2],
    [2, 4, 4, 4, 4, 4, 4, 4, 4, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
]
dialogs = [{'text': 'uhh', 'character': 1}, {'text': 'hi', 'character': 1},
           {'text': 'welcome to the white void arcade', 'character': 1},
           {'text': 'that number in the top right corner is your balance.', 'character': 1},
           {'text': 'you get more money by playing video games', 'character': 1},
           {'text': 'Isn\'t that, like, gambling?', 'character': 2},
           {'text': 'HOW DARE YOU SPEAK OF GAMBLING', 'character': 3},
           {
               'text': 'nope, we literally just pay you to play video games. not sure what\nwe\'re gonna do once we run out of subsidy money, but fortunately\nthat\'s not my problem',
               'character': 1}, {'text': 'have fun!', 'character': 1},
           {'text': '(exclamation point?!?!?!?!? what are you thinking bob ahhhhhhhhhh)', 'character': 1},
           {'text': '...', 'character': 2}, {'text': 'uh', 'character': 1},
           {'text': 'HELLO THERE. I AM A WALL.', 'character': 4},
           {'text': 'EVEN IF I WERE A DOOR, I WOULD NOT BE HEAVILY INCLINED TO\nLET YOUR BROKE ASS IN.', 'character': 4},
           {'text': 'YOU\'RE SMART. YOU CAN FIGURE OUT HOW MUCH.', 'character': 4},
           {'text': '1000 COINS IF YOU WOULD LIKE TO GAMBLE', 'character': 4},
           {'text': 'you technically have enough money for this, but we don\'t really sell\nit unless you have at least 1000 coins. not sure why, just company\npolicy', 'character': 1},
           {'text': 'you don\'t really have enough money to buy this. sorry.', 'character': 1},
           {'text': 'BING BONG', 'character': 5},
           {'text': 'I MAY NOT BE FULLY IMPLEMENTED, BUT IN MY HEART I AM A\nWHOLESOME GAME THAT DOES NOT INVOLVE GAMBLING', 'character': 6},
           {'text': 'ANYWAY, HERE\'S 20 BILLION DOLLARS', 'character': 6},
           {'text': 'SHEESH. I GET THAT I INSULTED YOU EARLIER, BUT AT THIS\nPOINT YOU\'RE JUST COMPENSATING FOR SOMETHING. COME ON\nIN, YOUR HIGHNESS.', 'character': 4},
           {'text': 'YOU REALLY EXPECTED YOU\'D BE ABLE TO GAMBLE HERE? HOW\nDARE YOU. GOODBYE.', 'character': 3},
           {'text': 'wait... this is for me? i.......', 'character': 1}]


class ArcadeFloor:
    def __init__(self, game_state):
        self.current_total_time = 0.0
        self.game_state = game_state
        self.charx = 4
        self.chary = 9
        self.ctcopen = False
        self.doorsopen = False
        self.currentnumcharacters = 0.0
        self.dialogstage = -1
        self.storeopen = False
        self.balance = 10
        self.temp_ctt = 9999.0
        self.showhiddenarea = False

        self.arcadetile = pr.load_image(utils.resource_path("arcadetile.png"))
        self.arcadetiletexture = pr.load_texture_from_image(self.arcadetile)
        self.bricktile = pr.load_image(utils.resource_path("brickwall.png"))
        self.bricktiletexture = pr.load_texture_from_image(self.bricktile)
        self.doortile = pr.load_image(utils.resource_path("door.png"))
        self.doortiletexture = pr.load_texture_from_image(self.doortile)
        self.uktile = pr.load_image(utils.resource_path("unknown.png"))
        self.uktiletexture = pr.load_texture_from_image(self.uktile)
        self.wptile = pr.load_image(utils.resource_path("woodplanks.png"))
        self.wptiletexture = pr.load_texture_from_image(self.wptile)
        self.crtile = pr.load_image(utils.resource_path("cashregister.png"))
        self.crtiletexture = pr.load_texture_from_image(self.crtile)
        self.uchar = pr.load_image(utils.resource_path("avatar.png"))
        self.uchartexture = pr.load_texture_from_image(self.uchar)
        self.bobava = pr.load_image(utils.resource_path("bob-avatar.png"))
        self.bobavatexture = pr.load_texture_from_image(self.bobava)
        self.bobeva = pr.load_image(utils.resource_path("evilbob.png"))
        self.bobevatexture = pr.load_texture_from_image(self.bobeva)
        self.dbox = pr.load_image(utils.resource_path("dialogbox.png"))
        self.dboxtexture = pr.load_texture_from_image(self.dbox)
        self.avadoor = pr.load_image(utils.resource_path("doorava.png"))
        self.avadoortexture = pr.load_texture_from_image(self.avadoor)
        self.avayour = pr.load_image(utils.resource_path("yourava.png"))
        self.youravatexture = pr.load_texture_from_image(self.avayour)
        self.sadstore = pr.load_image(utils.resource_path("sadstore.png"))
        self.sadstoretexture = pr.load_texture_from_image(self.sadstore)
        self.casinotile = pr.load_image(utils.resource_path("casinotile.png"))
        self.casinotiletexture = pr.load_texture_from_image(self.casinotile)
        self.gtron = pr.load_image(utils.resource_path("gablotron.png"))
        self.gtrontexture = pr.load_texture_from_image(self.gtron)
        self.ctc = pr.load_image(utils.resource_path("arcade.png"))
        self.ctctexture = pr.load_texture_from_image(self.ctc)
        self.regbob = pr.load_image(utils.resource_path("regularbob.png"))
        self.regbobtexture = pr.load_texture_from_image(self.regbob)
        self.romancend = False
        self.fin = pr.load_image(utils.resource_path("fin.png"))
        self.fintexture = pr.load_texture_from_image(self.fin)
        self.store_exit_box = pr.Rectangle(22*4, 72*4, (66-22)*4, (84-72)*4)
        self.store_bingbong_box = pr.Rectangle(23*4, 26*4, (180-23)*4, (46-26)*4)
        self.store_flower_box = pr.Rectangle(22*4, 49*4, (201-22)*4, (69-49)*4)
        # self.playbuttonbounds = pr.Rectangle(1024/2 - self.playbuttontexture.width / 2, 640/2 + 200 - self.playbuttontexture.height/2, self.playbuttontexture.width, self.playbuttontexture.height)

    def get_floor_texture(self):
        temp = arcadefloortexture.copy()
        if self.doorsopen:
            temp[3][9] = 1
            temp[4][9] = 1
        else:
            temp[3][9] = 3
            temp[4][9] = 3

        if self.dialogstage == 30:
            temp[9][3] = 4
        else:
            temp[9][3] = 7
        return temp

    def mup(self):
        self.chary -= 1

    def mdown(self):
        self.chary += 1

    def mleft(self):
        self.charx -= 1

    def mright(self):
        self.charx += 1

    def domove(self, perform, reverse):
        perform()
        match self.get_floor_texture()[self.charx][self.chary]:
            case 2:
                reverse()
            case 3:
                reverse()
            case 5:
                reverse()
            case 6:
                reverse()
                self.storeopen = True
            case 8:
                reverse()
                self.ctcopen = True
                self.dialogstage = 26
            case 7:
                reverse()
                if self.balance > 1000:
                    self.dialogstage = 29
                else:
                    if self.dialogstage < 20:
                        self.dialogstage += 1
                    else:
                        self.dialogstage = 19
            case 9:
                reverse()
                self.dialogstage = 31

    def draw_dialog(self, dialog):
        pr.draw_texture(self.dboxtexture, 32, 640 - 32 - 128, pr.RAYWHITE)
        match dialog['character']:
            case 1:
                pr.draw_texture(self.bobavatexture, 32 + 12, 640 - 32 - 128 + 12, pr.RAYWHITE)
            case 2:
                pr.draw_texture(self.youravatexture, 32 + 12, 640 - 32 - 128 + 12, pr.RAYWHITE)
            case 3:
                pr.draw_texture(self.bobevatexture, 32 + 12, 640 - 32 - 128 + 12, pr.RAYWHITE)
            case 4:
                pr.draw_texture(self.avadoortexture, 32 + 12, 640 - 32 - 128 + 12, pr.RAYWHITE)

        pr.draw_text(dialog['text'][0:int(self.currentnumcharacters)], 32 + 12 + 64 + 32 + 32, 640 - 32 - 128 + 12, 24, pr.RAYWHITE) # todo: font
    def dialogcheck(self, current_dialog):
        if pr.is_key_pressed(pr.KeyboardKey.KEY_SPACE) or pr.is_key_pressed(pr.KeyboardKey.KEY_ENTER):

            if self.currentnumcharacters < len(current_dialog['text']) - 1:
                self.currentnumcharacters = 9000
            else:
                self.currentnumcharacters = 0
                self.dialogstage += 1
                if self.dialogstage == 28:
                    self.balance += 20000000000
                if self.dialogstage == 32:
                    self.dialogstage = 25
                    self.currentnumcharacters = 11
                if self.dialogstage == 34:
                    self.romancend = True

        else:
            self.currentnumcharacters += 0.5
    def draw_frame(self):
        self.current_total_time += pr.get_frame_time()

        temptext = self.get_floor_texture()
        for i in range(16):
            layer = temptext[i]
            for j in range(10):
                tile = layer[j]
                match tile:
                    case 1:
                        pr.draw_texture(self.arcadetiletexture, i * 64, j * 64, pr.RAYWHITE)
                    case 2:
                        pr.draw_texture(self.bricktiletexture, i * 64, j * 64, pr.RAYWHITE)
                    case 3:
                        pr.draw_texture(self.doortiletexture, i * 64, j * 64, pr.RAYWHITE)
                    case 4:
                        if self.dialogstage == 30 or self.showhiddenarea:
                            pr.draw_texture(self.casinotiletexture, i * 64, j * 64, pr.RAYWHITE)
                        else:
                            pr.draw_texture(self.uktiletexture, i * 64, j * 64, pr.RAYWHITE)
                    case 5:
                        pr.draw_texture(self.wptiletexture, i * 64, j * 64, pr.RAYWHITE)
                    case 6:
                        pr.draw_texture(self.crtiletexture, i * 64, j * 64, pr.RAYWHITE)
                    case 7:
                        pr.draw_texture(self.doortiletexture, i * 64, j * 64, pr.RAYWHITE)
                    case 8:
                        pr.draw_texture(self.arcadetiletexture, i * 64, j * 64, pr.RAYWHITE)
                        pr.draw_texture(self.ctctexture, i * 64, j * 64, pr.RAYWHITE)
                    case 9:
                        if self.dialogstage == 30 or self.showhiddenarea:
                            pr.draw_texture(self.casinotiletexture, i * 64, j * 64, pr.RAYWHITE)
                            pr.draw_texture(self.gtrontexture, i * 64, j * 64, pr.RAYWHITE)
                        else:
                            pr.draw_texture(self.uktiletexture, i * 64, j * 64, pr.RAYWHITE)
                    case 10:
                        pr.draw_texture(self.arcadetiletexture, i * 64, j * 64, pr.RAYWHITE)
                        pr.draw_texture(self.regbobtexture, i * 64, j * 64, pr.RAYWHITE)
        if 1.0 < self.current_total_time < 1.6:
            self.doorsopen = True
        if self.current_total_time > 1.6:
            pr.draw_texture(self.uchartexture, self.charx * 64, self.chary * 64, pr.RAYWHITE)
            if self.current_total_time < 4.8:
                temptime = self.current_total_time - 1.6
                temptime = temptime * 2
                if temptime > 3:
                    self.doorsopen = False
                advance = int(temptime)
                self.chary = 9 - advance
            elif self.dialogstage == -1:
                self.dialogstage = 0
        if -1 < self.dialogstage < 12:
            current_dialog = dialogs[self.dialogstage]
            self.draw_dialog(current_dialog)
            self.dialogcheck(current_dialog)
            if self.dialogstage == 6 and self.currentnumcharacters >= 26:
                self.dialogstage += 1
        if self.dialogstage == 13:
            current_dialog = dialogs[self.dialogstage - 1]
            self.draw_dialog(current_dialog)
            self.dialogcheck(current_dialog)
        if self.dialogstage == 15:
            current_dialog = dialogs[self.dialogstage - 2]
            self.draw_dialog(current_dialog)
            self.dialogcheck(current_dialog)
        if self.dialogstage == 17:
            current_dialog = dialogs[self.dialogstage - 3]
            self.draw_dialog(current_dialog)
            self.dialogcheck(current_dialog)
        if self.dialogstage == 19:
            current_dialog = dialogs[self.dialogstage - 4]
            self.draw_dialog(current_dialog)
            self.dialogcheck(current_dialog)
        if self.dialogstage == 21:
            current_dialog = dialogs[self.dialogstage - 5]
            self.draw_dialog(current_dialog)
            self.dialogcheck(current_dialog)
        if self.dialogstage == 23:
            current_dialog = dialogs[self.dialogstage - 6]
            self.draw_dialog(current_dialog)
            self.dialogcheck(current_dialog)
        if self.dialogstage == 25:
            self.currentnumcharacters += 0.04
            if self.currentnumcharacters <= 11:
                current_dialog = dialogs[self.dialogstage - 7]
                self.draw_dialog(current_dialog)

            if self.currentnumcharacters > 11:
                csize = self.currentnumcharacters - 11
                pr.draw_circle(297, 189, csize * 800, pr.RAYWHITE)
            if self.currentnumcharacters > 15:
                utils.draw_text_centered("boom.", 1024/2, 640/2, 120, pr.RED)
            if self.currentnumcharacters > 18.4:
                i = 1337/0
        if self.dialogstage == 26 or self.dialogstage == 27:
            current_dialog = dialogs[self.dialogstage - 7]
            self.draw_dialog(current_dialog)
            self.dialogcheck(current_dialog)
        if self.dialogstage == 29:
            current_dialog = dialogs[21]
            self.draw_dialog(current_dialog)
            self.dialogcheck(current_dialog)
        if self.dialogstage == 31:
            self.showhiddenarea = True
            current_dialog = dialogs[22]
            self.draw_dialog(current_dialog)
            self.dialogcheck(current_dialog)
        if self.dialogstage == 33:
            current_dialog = dialogs[23]
            self.draw_dialog(current_dialog)
            self.dialogcheck(current_dialog)

        if self.storeopen:
            pr.draw_texture(self.sadstoretexture, 0, 0, pr.RAYWHITE)
            if pr.is_mouse_button_down(pr.MouseButton.MOUSE_BUTTON_LEFT):
                if pr.check_collision_point_rec(pr.get_mouse_position(), self.store_exit_box):
                    self.storeopen = False
                if pr.check_collision_point_rec(pr.get_mouse_position(), self.store_bingbong_box):
                    if self.balance < 10:
                        self.storeopen = False
                        self.dialogstage = 23
                    else:
                        self.storeopen = False
                        self.dialogstage = 25
                if pr.check_collision_point_rec(pr.get_mouse_position(), self.store_flower_box):
                    self.storeopen = False
                    if self.balance < 10:

                        self.dialogstage = 23
                    elif self.balance < 1000:

                        self.dialogstage = 21
                    else:
                        self.dialogstage = 33
        if self.romancend:
            pr.draw_texture(self.fintexture, 0, 0, pr.RAYWHITE)


        pr.draw_text(f"Balance: {self.balance} C", 1024 - pr.measure_text(f"Balance: {self.balance} C", 24) - 16, 0, 24, pr.WHITE)

        if (self.dialogstage == 12 or self.dialogstage == 14 or self.dialogstage == 16 or self.dialogstage == 18 or self.dialogstage == 20 or self.dialogstage == 22 or self.dialogstage == 24 or self.dialogstage == 26 or self.dialogstage == 28 or self.dialogstage == 30) and self.storeopen is False:
            if pr.is_key_pressed(pr.KeyboardKey.KEY_W) or pr.is_key_pressed(pr.KeyboardKey.KEY_UP):
                self.domove(self.mup, self.mdown)
            if pr.is_key_pressed(pr.KeyboardKey.KEY_A) or pr.is_key_pressed(pr.KeyboardKey.KEY_LEFT):
                self.domove(self.mleft, self.mright)
            if pr.is_key_pressed(pr.KeyboardKey.KEY_S) or pr.is_key_pressed(pr.KeyboardKey.KEY_DOWN):
                self.domove(self.mdown, self.mup)
            if pr.is_key_pressed(pr.KeyboardKey.KEY_D) or pr.is_key_pressed(pr.KeyboardKey.KEY_RIGHT):
                self.domove(self.mright, self.mleft)
