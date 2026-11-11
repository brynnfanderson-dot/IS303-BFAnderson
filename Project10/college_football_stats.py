import pandas as pd


cfb_stats = pd.read_csv("cfb.csv")
valid_seasons = cfb_stats["Season"].unique()
season_valid = False


#ask user for input
while season_valid == False:
    try:
        season = int(input("What season would you like to analyze? "))
    #make sure input is a number
    except ValueError:
        print("Please enter a year as a whole number.")
        continue
    #make sure input is in the data
    if season not in valid_seasons:
        print("That season is not in the data, please try again.")
    else:
        season_valid = True
#filter based on user input
season_teams = cfb_stats.loc[cfb_stats['Season'] == season]
#form empty dictionary
win_groups = {
    "10 or more wins": [],
    "8-9 wins": [],
    "6-7 wins": [],
    "Fewer than 6 wins": []
}
#iterate through filter data and sort teams
for index, row in season_teams.iterrows():
    team_name = row["Team"]
    wins = row["Win"]
    if wins >= 10:
        win_groups["10 or more wins"].append(team_name)
    elif wins >= 8:
        win_groups["8-9 wins"].append(team_name)
    elif wins >= 6:
        win_groups["6-7 wins"].append(team_name)
    else:
        win_groups["Fewer than 6 wins"].append(team_name)

#print results
print(f"\nCollege Football Results for {season}")

for win_range, teams in win_groups.items():
    print(f"\n{win_range}:")
    for team in teams:
        print(f"  {team}")