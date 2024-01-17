teamName = input("Please enter team name: ")

number_of_matches = int(input("Please enter the total number of matches played:"))

total_runs = 0
total_overs = 0
total_runs_conceded = 0
total_overs_bowled = 0

for i in range(number_of_matches):
    runs_scored_inmatch = int(input("Please enter runs scored in match " + str(i+1) + ":"))
    overs_played_inmatch = int(input("Please enter the overs played in match " + str(i+1) + ":"))

    total_runs = total_runs + runs_scored_inmatch
    total_overs = total_overs + overs_played_inmatch

    runs_conceded_inmatch = int(input("Please enter runs conceded in match " + str(i+1) + ":"))
    overs_bowled_inmatch = int(input("Please enter overs bowled in match " + str(i+1) + ":"))

    total_runs_conceded = total_runs_conceded + runs_conceded_inmatch
    total_overs_bowled = total_overs_bowled + overs_bowled_inmatch

    nrr = (total_runs/total_overs) - (total_runs_conceded/total_overs_bowled)

print("Net run rate of team " + teamName + " is:", nrr)
