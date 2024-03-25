e_sport_teams = [ "Dragons", "Wolves", "Elves", "Goblins"]

for team in e_sport_teams:
    for team1 in e_sport_teams: 
        for team2 in e_sport_teams:
            if team1 != team2:
                print(f"{team1} vs {team2}")

# This code will print all possible matchups 
# between the teams in the esport_teams list.
# Each team will be matched against every other team exactly once,
# ensuring no team plays against itself.


