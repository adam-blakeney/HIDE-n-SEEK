import random

intro_instructions = """ xxxxx """

class GameArea:
    """ this sets the area in which the player and computer will play.
    """
    def __init__(self, name):
        self.name = name
        # Code credit on self.board layout # https://github.com/Damianjacob/MS3-Battleship-Game
        self.board = [
            [" ",  " A", "  B", "  C", "  D", "  E"],
            ["1", "| |", "| |", "| |", "| |", "| |"],
            ["2", "| |", "| |", "| |", "| |", "| |"],
            ["3", "| |", "| |", "| |", "| |", "| |"],
            ["4", "| |", "| |", "| |", "| |", "| |"],
            ["5", "| |", "| |", "| |", "| |", "| |"],
        ]
        self.board_array = np.array(self.board)
        self.computer_displayed_board = np.array(self.board)
        self.user_score = 0
        self.computer_score = 0
        self.column_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}

def user_choose_ship_placement(self):
        """
        This function allows the user to place their 3 ships 
        it verfies all the data input by user is correct and if not then sends error message
        it will loop to allow for a re input
        """
        print("Time to place your ships!")
        user_board.display_board()
        added_ship_count = 0
        while added_ship_count < 3:
            while True:
                while True:
                    try:
                        y_input = input("Choose letter (A to E):\n").upper()
                        print('')
                        y_list = ['A', 'B', 'C', 'D', 'E']
                        if y_input not in y_list:
                            raise ValueError(
                                "You must select a letter from A to E!")
                    except ValueError as a:
                        print(f"Invalid data: {a}, please try again.\n")
                        continue
                    else:
                        break
                while True:
                    try:
                        x_input = input("Choose number (1 to 5):\n")
                        print('')
                        x_list = ['1', '2', '3', '4', '5']
                        if x_input not in x_list:
                            raise ValueError(
                                "You must select a number from 1 to 5!")
                    except ValueError as a:
                        print(f"Invalid data: {a}, please try again.\n")
                        continue
                    else:
                        break
                y_input = self.column_map[y_input]
                x_input = int(x_input)
                if self.board_array[x_input, y_input] == '|O|':
                    print("You already have a ship here! Try again!")
                    print('')
                else:
                    break
            self.board_array[x_input, y_input] = '|O|'
            added_ship_count += 1
            user_board.display_board()
            if added_ship_count == 3:
                print('')
                print("Great job placing the ships! Let's start the game!")
                print('')
                computer_board.randomize_ship_coordinates()
                self.display_board()
                self.display_computer_board()
                coin_flip(user_board, computer_board)
    
    def user_turn_place_hit(self):
         """
        Function will allow user to type in coordinates
        to hit.
        it will display if it is a hit or miss.
        it will also verify input is correct
        """
        while True:
            print('')
            print("Time to take your shot!")
            print('')
            self.display_computer_board()
            y_coord = self.column_map[self.validate_y_coordinate()]
            x_coord = int(self.validate_x_coordinate())
            if self.board_array[x_coord, y_coord] == '|O|':
                self.computer_displayed_board[x_coord, y_coord] = '|X|'
                self.board_array[x_coord, y_coord] = '|X|'
                print('')
                print('That was a hit! Good job, we can beat them!')
                print('')
                self.user_score += 1
                break
            elif self.computer_displayed_board[x_coord, y_coord] == '|X|':
                print('')
                print("This place has already been hit! Try another..")
            elif self.computer_displayed_board[x_coord, y_coord] == '|-|':
                print('')
                print("This place has already been hit! Try another..")
            else:
                self.computer_displayed_board[x_coord, y_coord] = '|-|'
                print('')
                print("SPLASH... thats a miss.")
                print('')
                break
        self.display_computer_board()
        if self.user_score < 3:
            user_board.computer_turn_place_hit()


    def computer_turn_place_hit(self):

    def computer_turn_place_hit(self):

    def user_wins(self):

    def computer_wins(self):

    def coin_flip(user_board, computer_board):

    def start_game():

    def introduction():

    def ask_user_ready():

    def end_game():

    def main():


