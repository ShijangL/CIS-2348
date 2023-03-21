# Shijang Lin PSID: 2018904

# zyLab 10.15

class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


if __name__ == "__main__":
    name = input()
    wins = int(input())
    losses = int(input())

    Team_Results = Team()
    Team_Results.team_name = name
    Team_Results.team_wins = wins
    Team_Results.team_losses = losses

    average = Team_Results.get_win_percentage()
    if average > .5:
        print(f'Congratulations, Team {name} has a winning average!')
    else:
        print(f'Team {name} has a losing average.')
