#Joseph Morris
#1840300

class Team:
    def __init__(self, team_name = 'none', team_wins = 0, team_losses = 0):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)

    def get_team_losses(self, team_losses):
        self.team_losses = team_losses

    def get_team_wins(self, team_wins):
        self.team_wins = team_wins

    def get_team_name(self, team_name):
        self.team_name = team_name


if __name__ == '__main__':

    professional_team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    professional_team.get_team_name(team_name)
    professional_team.get_team_wins(team_wins)
    professional_team.get_team_losses(team_losses)

    if professional_team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', professional_team.team_name, 'has a winning average!')
    else:
        print('Team', professional_team.team_name, 'has a losing average.')

