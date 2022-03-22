no_of_teams = int(input())
teams = {}
for i in range(no_of_teams):
    team = input()
    teams[team] = [0,0.0]

num_of_matches = int(input())

for i in range(num_of_matches):
    pointsA,pointsB = 0,0
    teamA,teamA_runrate, teamB,teamB_runrate = input().split(" ")
    teamA_runrate,teamB_runrate = float(teamA_runrate),float(teamB_runrate)
    if (teamA_runrate > teamB_runrate):
        pointsA += 2
    if (teamA_runrate < teamB_runrate):
        pointsB += 2
    if (teamA_runrate == teamB_runrate):
        pointsA += 1
        pointsB += 1

    teams[teamA][0] += pointsA
    teams[teamA][1] += teamA_runrate
    teams[teamB][0] += pointsB
    teams[teamB][1] += teamB_runrate

teams = sorted(teams.items(),key=lambda item:item[1][1],reverse=True)
for key,value in teams:
    print('{} {} {}'.format(key,value[0],format(value[1],'.2f')))
