from random import choice

class Player:
    def __init__(self):
        self.score = 0

class HumanPlayer(Player):
    def choose_method(self):
        while True:
            user_choice = input('Rock, paper or scissors [r/p/s]? ')
            if user_choice in ['r', 'p', 's']:
                return user_choice

class ComputerPlayer(Player):
    def choose_method(self):
        return choice('rps')

class Game():
    rounds = 0
    outcomes = {
        ('r', 'r'): 'tied',
        ('p', 'p'): 'tied',
        ('s', 's'): 'tied',
        ('r', 'p'): 'lost',
        ('r', 's'): 'won',
        ('p', 'r'): 'won',
        ('p', 's'): 'lost',
        ('s', 'r'): 'lost',
        ('s', 'p'): 'won',
    }

    def __init__(self):
        self.player_one = HumanPlayer()
        self.player_two = ComputerPlayer()

    def start_game(self):
        print('--- Rock Paper Scissors Game ---')
        while True:
            num_rounds = input('How many rounds would you like to play? ')
            if num_rounds.isnumeric():
                self.rounds = int(num_rounds)
                break

        for round in range(self.rounds):
            self.play_round()

    def end_game(self):
        human_score = self.player_one.score
        computer_score = self.player_two.score

        print('[Game Summary] Your points:', human_score, '| Computer points:', computer_score)

        if human_score > computer_score:
            print('Congratulations! You won!')
        elif computer_score > human_score:
            print('Sorry, you lost this time.')
        else:
            print('This game was a tie.')

    def play_round(self):
        user_choice = self.player_one.choose_method()
        computer_choice = self.player_two.choose_method()
        outcome = self.outcomes[(user_choice, computer_choice)]

        if outcome == 'won':
            self.player_one.score += 1
        elif outcome == 'lost':
            self.player_two.score += 1

        print('You:', user_choice, ' | Computer:', computer_choice)
        print('You', outcome, 'this round.')

def main():
    new_game = Game()
    new_game.start_game()
    new_game.end_game()

if __name__ == '__main__':
    main()