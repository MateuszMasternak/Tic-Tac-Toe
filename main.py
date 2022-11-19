import pygame as pg
import sys


class Game(object):

    def __init__(self):

        # Variables
        self.height = 720
        self.width = 1080
        self.menu = False
        self.xy_color_1 = (255, 0, 255)  # first line of X and O
        self.xy_color_2 = (255, 255, 0)  # second line of X
        self.opened = [False] * 9
        self.turn = "X"
        self.board = [[0, 0, 0] * 3]
        self.moves = 0
        self.started = False
        self.wins = [0, 0]
        self.first_player = "X"
        self.x_first_line = [[(55, 45), (226, 212)], [(285, 45), (456, 212)], [(525, 45), (696, 212)],
                             [(55, 277), (226, 442)], [(285, 277), (456, 442)], [(525, 277), (696, 442)],
                             [(55, 509), (226, 672)], [(285, 509), (456, 672)], [(525, 509), (696, 672)]]
        self.x_second_line = [[(223, 45), (62, 212)], [(453, 45), (292, 212)], [(693, 45), (532, 212)],
                              [(223, 277), (62, 436)], [(453, 277), (292, 436)], [(693, 277), (532, 436)],
                              [(223, 509), (62, 660)], [(453, 509), (292, 660)], [(693, 509), (532, 660)]]
        self.o = [[(140, 130)], [(375, 130)], [(610, 130)], [(140, 360)], [(375, 360)], [(610, 360)], [(140, 590)],
                  [(375, 590)], [(610, 590)]]
        self.win_x = False
        self.win_o = False
        self.tie_xo = False
        self.not_swap = True

        # Initialization
        pg.init()
        self.window = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Tic Tac Toe")

        # Fields
        self.first = pg.draw.rect(self.window, (220, 220, 220), (40, 30, 200, 200))
        self.second = pg.draw.rect(self.window, (220, 220, 220), (275, 30, 200, 200))
        self.third = pg.draw.rect(self.window, (220, 220, 220), (510, 30, 200, 200))
        self.fourth = pg.draw.rect(self.window, (220, 220, 220), (40, 260, 200, 200))
        self.fifth = pg.draw.rect(self.window, (220, 220, 220), (275, 260, 200, 200))
        self.sixth = pg.draw.rect(self.window, (220, 220, 220), (510, 260, 200, 200))
        self.seventh = pg.draw.rect(self.window, (220, 220, 220), (40, 490, 200, 200))
        self.eighth = pg.draw.rect(self.window, (220, 220, 220), (275, 490, 200, 200))
        self.ninth = pg.draw.rect(self.window, (220, 220, 220), (510, 490, 200, 200))

        # Fonts
        self.name_font = pg.font.SysFont("Verdana", 80, bold=True)
        self.author_font = pg.font.SysFont("Verdana", 55, bold=True)
        self.menu_font = pg.font.SysFont("Verdana", 30, bold=True)
        self.win_font = pg.font.SysFont("Verdana", 40, bold=True)
        self.res_font = pg.font.SysFont("Verdana", 25, bold=True)

        # Texts for menu
        self.games_name = self.name_font.render("Tic Tac Toe", True, self.xy_color_2)
        # self.authors_name = self.author_font.render("made by Mateusz", True, self.xy_color_2)
        self.menu_1 = self.menu_font.render(f"Press Q to choice between O and X (first player={self.first_player})",
                                            True, self.xy_color_1)
        self.menu_2 = self.menu_font.render("Press space to start a game", True, self.xy_color_1)

        # Texts for results
        self.x_win = self.win_font.render("X wins!", True, self.xy_color_2)
        self.o_win = self.win_font.render("O wins", True, self.xy_color_2)
        self.res = self.res_font.render("Press space to restart.", True, self.xy_color_1)
        self.tie = self.win_font.render("Tie!", True, self.xy_color_2)
        self.scores = self.menu_font.render("Scores:", True, self.xy_color_2)
        self.player_x = self.res_font.render(f"X: {self.wins[0]}", True, self.xy_color_1)
        self.player_o = self.res_font.render(f"O: {self.wins[1]}", True, self.xy_color_1)

        # Run game in a loop
        pg.time.delay(60)
        while True:
            if self.menu is False:
                self.display_menu()
            elif self.menu is True:
                self.display_gameplay()
                self.not_swap = False

            # Handle events
            for event in pg.event.get():
                # Makes exit possible
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_q and self.menu is False:
                        self.swap_signs()
                    elif event.key == pg.K_SPACE:
                        self.new_game()

                # Display moves
                if event.type == pg.MOUSEBUTTONUP and self.started is True:
                    mouse_pos = pg.mouse.get_pos()

                    # For first row
                    if self.first.collidepoint(mouse_pos) and self.opened[0] is False:
                        if self.turn == "X":
                            self.turn = "O"
                            self.board[0][0] = 1
                        else:
                            self.turn = "X"
                            self.board[0][0] = 2
                        self.opened[0] = True
                        self.moves += 1
                    elif self.second.collidepoint(mouse_pos) and self.opened[1] is False:
                        if self.turn == "X":
                            self.turn = "O"
                            self.board[0][1] = 1
                        else:
                            self.turn = "X"
                            self.board[0][1] = 2
                        self.opened[1] = True
                        self.moves += 1
                    elif self.third.collidepoint(mouse_pos) and self.opened[2] is False:
                        if self.turn == "X":
                            self.turn = "O"
                            self.board[0][2] = 1
                        else:
                            self.turn = "X"
                            self.board[0][2] = 2
                        self.opened[2] = True
                        self.moves += 1
                    # For second row
                    elif self.fourth.collidepoint(mouse_pos) and self.opened[3] is False:
                        if self.turn == "X":
                            self.turn = "O"
                            self.board[1][0] = 1
                        else:
                            self.turn = "X"
                            self.board[1][0] = 2
                        self.opened[3] = True
                        self.moves += 1
                    elif self.fifth.collidepoint(mouse_pos) and self.opened[4] is False:
                        if self.turn == "X":
                            self.turn = "O"
                            self.board[1][1] = 1
                        else:
                            self.turn = "X"
                            self.board[1][1] = 2
                        self.opened[4] = True
                        self.moves += 1
                    elif self.sixth.collidepoint(mouse_pos) and self.opened[5] is False:
                        if self.turn == "X":
                            self.turn = "O"
                            self.board[1][2] = 1
                        else:
                            self.turn = "X"
                            self.board[1][2] = 2
                        self.opened[5] = True
                        self.moves += 1
                    # For third row
                    elif self.seventh.collidepoint(mouse_pos) and self.opened[6] is False:
                        if self.turn == "X":
                            self.turn = "O"
                            self.board[2][0] = 1
                        else:
                            self.turn = "X"
                            self.board[2][0] = 2
                        self.opened[6] = True
                        self.moves += 1
                    elif self.eighth.collidepoint(mouse_pos) and self.opened[7] is False:
                        if self.turn == "X":
                            self.turn = "O"
                            self.board[2][1] = 1
                        else:
                            self.turn = "X"
                            self.board[2][1] = 2
                        self.opened[7] = True
                        self.moves += 1
                    elif self.ninth.collidepoint(mouse_pos) and self.opened[8] is False:
                        if self.turn == "X":
                            self.turn = "O"
                            self.board[2][2] = 1
                        else:
                            self.turn = "X"
                            self.board[2][2] = 2
                        self.opened[8] = True
                        self.moves += 1

            if self.check_win(1) is True and self.win_x is False:
                self.win_x = True
                self.started = False
                self.wins[0] += 1
                self.moves = 0
            elif self.check_win(2) is True and self.win_o is False:
                self.win_o = True
                self.started = False
                self.wins[1] += 1
                self.moves = 0
            elif self.check_tie() is True and self.tie_xo is False:
                self.tie_xo = True
                self.started = False
                self.moves = 0

            pg.display.update()

    def check_win(self, player):

        for row in self.board:
            for tile in row:
                if tile == player:
                    continue
                else:
                    break
            else:
                return True

        for column in range(3):
            for row in self.board:
                if row[column] == player:
                    continue
                else:
                    break
            else:
                return True

        for tile in range(3):
            if self.board[tile][tile] == player:
                continue
            else:
                break
        else:
            return True

        for tile in range(3):
            if self.board[tile][2-tile] == player:
                continue
            else:
                break
        else:
            return True

    def check_tie(self):
        if self.moves == 9:
            return True
        return False

    def display_menu(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.games_name, (290, 60))
        # self.window.blit(self.authors_name, (267, 150))
        self.window.blit(self.menu_1, (100, 300))
        self.window.blit(self.menu_2, (305, 370))

    def display_result(self):
        self.player_x = self.res_font.render(f"X: {self.wins[0]}", True, self.xy_color_1)
        self.player_o = self.res_font.render(f"O: {self.wins[1]}", True, self.xy_color_1)
        self.window.blit(self.scores, (810, 400))
        self.window.blit(self.player_x, (810, 450))
        self.window.blit(self.player_o, (810, 500))

    def display_fields(self):
        self.first = pg.draw.rect(self.window, (220, 220, 220), (40, 30, 200, 200))
        self.second = pg.draw.rect(self.window, (220, 220, 220), (275, 30, 200, 200))
        self.third = pg.draw.rect(self.window, (220, 220, 220), (510, 30, 200, 200))
        self.fourth = pg.draw.rect(self.window, (220, 220, 220), (40, 260, 200, 200))
        self.fifth = pg.draw.rect(self.window, (220, 220, 220), (275, 260, 200, 200))
        self.sixth = pg.draw.rect(self.window, (220, 220, 220), (510, 260, 200, 200))
        self.seventh = pg.draw.rect(self.window, (220, 220, 220), (40, 490, 200, 200))
        self.eighth = pg.draw.rect(self.window, (220, 220, 220), (275, 490, 200, 200))
        self.ninth = pg.draw.rect(self.window, (220, 220, 220), (510, 490, 200, 200))

    def display_gameplay(self):
        self.window.fill((0, 0, 0))

        self.display_fields()

        # Signs
        i = 0
        for row in self.board:
            for field in row:
                if field == 1:
                    pg.draw.line(self.window, self.xy_color_1, self.x_first_line[i][0],
                                 self.x_first_line[i][1], 15)
                    pg.draw.line(self.window, self.xy_color_2, self.x_second_line[i][0],
                                 self.x_second_line[i][1], 15)
                elif field == 2:
                    pg.draw.circle(self.window, self.xy_color_2, self.o[i][0], 85, 10)
                i += 1

        self.display_result()
        if self.win_x:
            self.window.blit(self.x_win, (810, 100))
            self.window.blit(self.res, (737, 160))
        elif self.win_o:
            self.window.blit(self.o_win, (810, 100))
            self.window.blit(self.res, (737, 160))
        elif self.tie_xo:
            self.window.blit(self.tie, (855, 100))
            self.window.blit(self.res, (737, 160))

    def swap_signs(self):
        if self.first_player == "X":
            self.first_player = "O"
        else:
            self.first_player = "X"
        self.turn = self.first_player
        self.menu_1 = self.menu_font.render(
            f"Press Q to choice between O and X (first player={self.first_player})",
            True, self.xy_color_1)

    def new_game(self):
        self.window.fill((0, 0, 0))
        self.menu = True

        self.display_fields()

        self.display_result()

        # Variables reset
        self.opened = [False] * 9
        self.moves = 0
        self.started = True
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.win_x = False
        self.win_o = False
        self.tie_xo = False

        # Swap players in all new rounds
        if self.not_swap is False:
            self.swap_signs()


if __name__ == "__main__":
    Game()
