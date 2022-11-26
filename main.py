import pygame as pg
import sys


class Game(object):

    def __init__(self):

        # Variables
        self.game_window_height = 720
        self.game_window_width = 1080
        self.menu_was_shown = False
        self.yellow_color = (255, 255, 0)  # first line of X and O
        self.pink_color = (255, 0, 255)  # second line of X
        self.which_sign_turn = "X"
        self.board = [[0, 0, 0] * 3]  # 0 - empty, 1 - X, 2 - O
        self.successful_moves_count = 0
        self.started = False
        self.wins_count_X_O = [0, 0]
        self.first_player_in_current_round = "X"
        self.x_first_line_draw_positions = [[(55, 45), (226, 212)], [(285, 45), (456, 212)], [(525, 45), (696, 212)],
                                            [(55, 277), (226, 442)], [(285, 277), (456, 442)], [(525, 277), (696, 442)],
                                            [(55, 509), (226, 672)], [(285, 509), (456, 672)], [(525, 509), (696, 672)]]
        self.x_second_line_draw_positions = [[(223, 45), (62, 212)], [(453, 45), (292, 212)], [(693, 45), (532, 212)],
                                             [(223, 277), (62, 436)], [(453, 277), (292, 436)], [(693, 277), (532, 436)],
                                             [(223, 509), (62, 660)], [(453, 509), (292, 660)], [(693, 509), (532, 660)]]
        self.o_draw_positions = [[(140, 130)], [(375, 130)], [(610, 130)],
                                 [(140, 360)], [(375, 360)], [(610, 360)],
                                 [(140, 590)], [(375, 590)], [(610, 590)]]
        self.win_x = False
        self.win_o = False
        self.tie_xo = False
        self.not_swap = True

        # Initialization
        pg.init()
        self.game_window = pg.display.set_mode((self.game_window_width, self.game_window_height))
        pg.display.set_caption("Tic Tac Toe")

        # Fields
        self.first_row_first_field = pg.draw.rect(self.game_window, (220, 220, 220), (40, 30, 200, 200))
        self.first_row_second_field = pg.draw.rect(self.game_window, (220, 220, 220), (275, 30, 200, 200))
        self.first_row_third_field = pg.draw.rect(self.game_window, (220, 220, 220), (510, 30, 200, 200))
        self.second_row_first_field = pg.draw.rect(self.game_window, (220, 220, 220), (40, 260, 200, 200))
        self.second_row_second_field = pg.draw.rect(self.game_window, (220, 220, 220), (275, 260, 200, 200))
        self.second_row_third_field = pg.draw.rect(self.game_window, (220, 220, 220), (510, 260, 200, 200))
        self.third_row_first_field = pg.draw.rect(self.game_window, (220, 220, 220), (40, 490, 200, 200))
        self.third_row_second_field = pg.draw.rect(self.game_window, (220, 220, 220), (275, 490, 200, 200))
        self.third_row_third_field = pg.draw.rect(self.game_window, (220, 220, 220), (510, 490, 200, 200))

        # Fonts
        self.verdana_80_bold = pg.font.SysFont("Verdana", 80, bold=True)
        self.verdana_55_bold = pg.font.SysFont("Verdana", 55, bold=True)
        self.verdana_40_bold = pg.font.SysFont("Verdana", 40, bold=True)
        self.verdana_30_bold = pg.font.SysFont("Verdana", 30, bold=True)
        self.verdana_25_bold = pg.font.SysFont("Verdana", 25, bold=True)

        # Texts for menu
        self.render_games_name = self.verdana_80_bold.render("Tic Tac Toe", True, self.yellow_color)
        # self.authors_name = self.author_font.render("made by Mateusz", True, self.xy_color_2)
        self.render_X_O_choice = self.verdana_30_bold.render(f"Press Q to choice between O and X "
                                                             f"(first player={self.first_player_in_current_round})",
                                                             True, self.pink_color)
        self.render_start_game_instruction = self.verdana_30_bold.render("Press space to start a game",
                                                                         True, self.pink_color)

        # Texts for results
        self.render_x_wins = self.verdana_40_bold.render("X wins!", True, self.yellow_color)
        self.render_o_wins = self.verdana_40_bold.render("O wins", True, self.yellow_color)
        self.render_restart_game_instruction = self.verdana_25_bold.render("Press space to restart.",
                                                                           True, self.pink_color)
        self.render_tie = self.verdana_40_bold.render("Tie!", True, self.yellow_color)
        self.render_scores = self.verdana_30_bold.render("Scores:", True, self.yellow_color)
        self.render_x_wins_count = self.verdana_25_bold.render(f"X: {self.wins_count_X_O[0]}", True, self.yellow_color)
        self.render_o_wins_count = self.verdana_25_bold.render(f"O: {self.wins_count_X_O[1]}", True, self.yellow_color)

        # Run game in a loop
        pg.time.delay(60)
        while True:
            if self.menu_was_shown is True:
                self.display_gameplay()
                self.not_swap = False
            else:
                self.display_menu()

            # Handle events
            for event in pg.event.get():
                # Makes exit possible
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_q and self.menu_was_shown is False:
                        self.swap_signs()
                    elif event.key == pg.K_SPACE:
                        self.new_game()

                # Display moves
                if event.type == pg.MOUSEBUTTONUP and self.started is True:
                    mouse_position = pg.mouse.get_pos()

                    # For first row
                    if self.first_row_first_field.collidepoint(mouse_position) and self.board[0][0] == 0:
                        if self.which_sign_turn == "X":
                            self.which_sign_turn = "O"
                            self.board[0][0] = 1
                        else:
                            self.which_sign_turn = "X"
                            self.board[0][0] = 2
                        self.successful_moves_count += 1
                    elif self.first_row_second_field.collidepoint(mouse_position) and self.board[0][1] == 0:
                        if self.which_sign_turn == "X":
                            self.which_sign_turn = "O"
                            self.board[0][1] = 1
                        else:
                            self.which_sign_turn = "X"
                            self.board[0][1] = 2
                        self.successful_moves_count += 1
                    elif self.first_row_third_field.collidepoint(mouse_position) and self.board[0][2] == 0:
                        if self.which_sign_turn == "X":
                            self.which_sign_turn = "O"
                            self.board[0][2] = 1
                        else:
                            self.which_sign_turn = "X"
                            self.board[0][2] = 2
                        self.successful_moves_count += 1
                    # For second row
                    elif self.second_row_first_field.collidepoint(mouse_position) and self.board[1][0] == 0:
                        if self.which_sign_turn == "X":
                            self.which_sign_turn = "O"
                            self.board[1][0] = 1
                        else:
                            self.which_sign_turn = "X"
                            self.board[1][0] = 2
                        self.successful_moves_count += 1
                    elif self.second_row_second_field.collidepoint(mouse_position) and self.board[1][1] == 0:
                        if self.which_sign_turn == "X":
                            self.which_sign_turn = "O"
                            self.board[1][1] = 1
                        else:
                            self.which_sign_turn = "X"
                            self.board[1][1] = 2
                        self.successful_moves_count += 1
                    elif self.second_row_third_field.collidepoint(mouse_position) and self.board[1][2] == 0:
                        if self.which_sign_turn == "X":
                            self.which_sign_turn = "O"
                            self.board[1][2] = 1
                        else:
                            self.which_sign_turn = "X"
                            self.board[1][2] = 2
                        self.successful_moves_count += 1
                    # For third row
                    elif self.third_row_first_field.collidepoint(mouse_position) and self.board[2][0] == 0:
                        if self.which_sign_turn == "X":
                            self.which_sign_turn = "O"
                            self.board[2][0] = 1
                        else:
                            self.which_sign_turn = "X"
                            self.board[2][0] = 2
                        self.successful_moves_count += 1
                    elif self.third_row_second_field.collidepoint(mouse_position) and self.board[2][1] == 0:
                        if self.which_sign_turn == "X":
                            self.which_sign_turn = "O"
                            self.board[2][1] = 1
                        else:
                            self.which_sign_turn = "X"
                            self.board[2][1] = 2
                        self.successful_moves_count += 1
                    elif self.third_row_third_field.collidepoint(mouse_position) and self.board[2][2] == 0:
                        if self.which_sign_turn == "X":
                            self.which_sign_turn = "O"
                            self.board[2][2] = 1
                        else:
                            self.which_sign_turn = "X"
                            self.board[2][2] = 2
                        self.successful_moves_count += 1

            if self.check_is_winner(1) is True and self.win_x is False:
                self.win_x = True
                self.started = False
                self.wins_count_X_O[0] += 1
                self.successful_moves_count = 0
            elif self.check_is_winner(2) is True and self.win_o is False:
                self.win_o = True
                self.started = False
                self.wins_count_X_O[1] += 1
                self.successful_moves_count = 0
            elif self.check_is_tie() is True and self.tie_xo is False:
                self.tie_xo = True
                self.started = False
                self.successful_moves_count = 0

            pg.display.update()

    def check_is_winner(self, player):

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

    def check_is_tie(self):
        if self.successful_moves_count == 9:
            return True
        return False

    def display_menu(self):
        self.game_window.fill((0, 0, 0))
        self.game_window.blit(self.render_games_name, (330, 60))
        # self.window.blit(self.authors_name, (267, 150))
        self.game_window.blit(self.render_X_O_choice, (150, 300))
        self.game_window.blit(self.render_start_game_instruction, (335, 370))

    def display_result(self):
        self.render_x_wins_count = self.verdana_25_bold.render(f"X: {self.wins_count_X_O[0]}", True, self.yellow_color)
        self.render_o_wins_count = self.verdana_25_bold.render(f"O: {self.wins_count_X_O[1]}", True, self.yellow_color)
        self.game_window.blit(self.render_scores, (810, 400))
        self.game_window.blit(self.render_x_wins_count, (810, 450))
        self.game_window.blit(self.render_o_wins_count, (810, 500))

    def display_fields(self):
        self.first_row_first_field = pg.draw.rect(self.game_window, (220, 220, 220), (40, 30, 200, 200))
        self.first_row_second_field = pg.draw.rect(self.game_window, (220, 220, 220), (275, 30, 200, 200))
        self.first_row_third_field = pg.draw.rect(self.game_window, (220, 220, 220), (510, 30, 200, 200))
        self.second_row_first_field = pg.draw.rect(self.game_window, (220, 220, 220), (40, 260, 200, 200))
        self.second_row_second_field = pg.draw.rect(self.game_window, (220, 220, 220), (275, 260, 200, 200))
        self.second_row_third_field = pg.draw.rect(self.game_window, (220, 220, 220), (510, 260, 200, 200))
        self.third_row_first_field = pg.draw.rect(self.game_window, (220, 220, 220), (40, 490, 200, 200))
        self.third_row_second_field = pg.draw.rect(self.game_window, (220, 220, 220), (275, 490, 200, 200))
        self.third_row_third_field = pg.draw.rect(self.game_window, (220, 220, 220), (510, 490, 200, 200))

    def display_gameplay(self):
        self.game_window.fill((0, 0, 0))

        self.display_fields()

        # Signs
        i = 0
        for row in self.board:
            for field in row:
                if field == 1:
                    pg.draw.line(self.game_window, self.pink_color, self.x_first_line_draw_positions[i][0],
                                 self.x_first_line_draw_positions[i][1], 15)
                    pg.draw.line(self.game_window, self.pink_color, self.x_second_line_draw_positions[i][0],
                                 self.x_second_line_draw_positions[i][1], 15)
                elif field == 2:
                    pg.draw.circle(self.game_window, self.yellow_color, self.o_draw_positions[i][0], 85, 10)
                i += 1

        self.display_result()
        if self.win_x:
            self.game_window.blit(self.render_x_wins, (830, 100))
            self.game_window.blit(self.render_restart_game_instruction, (755, 160))
        elif self.win_o:
            self.game_window.blit(self.render_o_wins, (830, 100))
            self.game_window.blit(self.render_restart_game_instruction, (755, 160))
        elif self.tie_xo:
            self.game_window.blit(self.render_tie, (870, 100))
            self.game_window.blit(self.render_restart_game_instruction, (755, 160))

    def swap_signs(self):
        if self.first_player_in_current_round == "X":
            self.first_player_in_current_round = "O"
        else:
            self.first_player_in_current_round = "X"
        self.which_sign_turn = self.first_player_in_current_round
        self.render_X_O_choice = self.verdana_30_bold.render(
            f"Press Q to choice between O and X (first player={self.first_player_in_current_round})",
            True, self.pink_color)

    def new_game(self):
        self.game_window.fill((0, 0, 0))
        self.menu_was_shown = True

        self.display_fields()

        self.display_result()

        # Variables reset
        self.successful_moves_count = 0
        self.started = True
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.win_x = False
        self.win_o = False
        self.tie_xo = False

        # Swap players in all new rounds
        if self.not_swap is False:
            self.swap_signs()

    def run_game(self):
        pass


if __name__ == "__main__":
    Game()
