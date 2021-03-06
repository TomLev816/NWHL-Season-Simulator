#NWHL 2018-2019

import random
import operator

class team_info(object):
  def __init__(self, teamname, wins, loses, ties, gf, ga):
    self.teamname = teamname
    self.gp = wins + loses + ties 
    self.wins = wins
    self.loses = loses
    self.ties = ties
    self.points = wins*2 + ties
    self.gf = gf
    self.ga = ga
    
    
RIV = team_info("Riveters", 0,0,0,0,0)
CTW = team_info("Whale   ", 0,0,0,0,0)
BUF = team_info("Beauts  ", 0,0,0,0,0)
BOS = team_info("Pride   ", 0,0,0,0,0)
MIN = team_info("Whitecaps", 0,0,0,0,0)


all_teams = (RIV, CTW, BUF, BOS, MIN)

class player_info(object):
  def __init__(self, team, name, pos, age, shot, off, dfnce, gtend, goals, saves):
    self.team = team
    self.name = name
    self.age = age
    self.pos = pos
    self.overall = shot + off + dfnce + gtend 
    self.shot = shot
    self.off = off
    self.dfnce = dfnce
    self.gtend = gtend
    self.goals = goals
    self.saves = saves
    


# team, name, pos, age, shot, off, defence, goalie, Goals, Saves
Riveters = [
player_info("Riveters", "Madison Packer", "C", 27,9,9,7,0,0,0),
player_info("Riveters", "Bray Ketchum", "C", 29,5,6,4,0,0,0),
player_info("Riveters", "Alexa Gruschow", "W", 24,8,6,6,0,0,0),
player_info("Riveters", "Amanda Kessel", "W", 26,5,8,8,0,0,0),
player_info("Riveters", "Rebecca Russo", "W", 24,8,4,3,0,0,0),
player_info("Riveters", "Miye D'Oench", "W", 24,8,7,3,0,0,0),
player_info("Riveters", "Courtney Burke", "D",23,3,8,8,0,0,0),
player_info("Riveters", "Jenny Ryan", "D",23,1,7,4,0,0,0),
player_info("Riveters", "Kiira Dosdall", "D",30,1,6,7,0,0,0),
player_info("Riveters", "Kelsey koelzer", "D", 23,6,5,9,0,0,0),
player_info("Riveters", "Katie Fitzgerald", "G", 24,0,0,0,25,0,0)]

Whale = [
player_info("Whale", "Emily Fluke", "C", 25,4,6,4,0,0,0),
player_info("Whale", "Sam Faber", "C", 31,3,5,6,0,0,0),
player_info("Whale", "Jamie Goldsmith", "W", 27,4,6,7,0,0,0),
player_info("Whale", "Kelly Babstock", "W", 25,4,7,4,0,0,0),
player_info("Whale", "Sam Donovan", "W", 25,4,7,4,0,0,0),
player_info("Whale", "Meghan Huertas", "W", 25,5,7,6,0,0,0),
player_info("Whale", "Amanda Boulier", "D", 25,4,6,7,0,0,0),
player_info("Whale", "Emma Greco", "D",22,1,4,5,0,0,0),
player_info("Whale", "Shannon Doyle", "D",22,1,5,7,0,0,0),
player_info("Whale", "Cydney Roesler", "D",22,2,3,8,0,0,0),
player_info("Whale", "Sydney Rossman", "G", 27,0,0,0,21,0,0)]

Beauts = [
player_info("Beauts", "Hayley Scamurra", "C", 24,7,7,5,0,0,0),
player_info("Beauts", "Jordan Juron", "C", 24,6,6,4,0,0,0),
player_info("Beauts", "Maddie Elia", "W", 29,1,7,5,0,0,0),
player_info("Beauts", "Kristin Lewicki", "W", 34,6,5,6,0,0,0),
player_info("Beauts", "Dani Cameranesi", "W", 23,3,8,7,0,0,0),
player_info("Beauts", "Kourtney Kunichika", "W", 26,5,9,3,0,0,0),
player_info("Beauts", "Lisa Chesson", "D", 27,2,4,7,0,0,0),
player_info("Beauts", "Sarah Casorso", "D",22,1,6,6,0,0,0),
player_info("Beauts", "Emily Pfalzer", "D",25,3,7,9,0,0,0),
player_info("Beauts", "Sarah Edney", "D",25,3,7,9,0,0,0),
player_info("Beauts", "Shannon Szabados", "G", 31,0,0,0,27,0,0)]

Pride = [
player_info("Pride", "Jillian Dempsey", "C", 25,7,7,4,0,0,0),
player_info("Pride", "Brianna Decker", "C", 27,9,9,5,0,0,0),
player_info("Pride", "Sydney Daniels", "W", 23,8,6,5,0,0,0),
player_info("Pride", "Emily Field", "W", 25,2,6,3,0,0,0),
player_info("Pride", "Haley Skarupa", "W", 24,7,8,3,0,0,0),
player_info("Pride", "Dana Trivigno", "W", 24,7,7,6,0,0,0),
player_info("Pride", "Alyssa Gagliardi", "D", 27,3,5,7,0,0,0),
player_info("Pride", "Kaleigh Fratkin", "D",25,1,5,6,0,0,0),
player_info("Pride", "Paige Harrington", "D",24,1,4,8,0,0,0),
player_info("Pride", "Meagan Mangene", "D",25,3,7,7,0,0,0),
player_info("Pride", "Brittany Ott", "G", 28,0,0,0,23,0,0)]

Whitecaps = [
player_info("Whitecaps", "Hannah Brandt", "C", 24,6,8,5,0,0,0),
player_info("Whitecaps", "Hillary Crowe", "C", 25,6,7,4,0,0,0),
player_info("Whitecaps", "Kendall Coyne", "W", 26,5,9,6,0,0,0),
player_info("Whitecaps", "Amy Menke", "W", 23,4,7,4,0,0,0),
player_info("Whitecaps", "Kathleen Frischmann", "W", 27,2,4,6,0,0,0),
player_info("Whitecaps", "Margo Lund", "W", 25,2,4,7,0,0,0),
player_info("Whitecaps", "Kelly Buchta", "D", 28,2,5,6,0,0,0),
player_info("Whitecaps", "Tanja Eisenschmid", "D",25,6,3,7,0,0,0),
player_info("Whitecaps", "Anna-Maria Fiegert", "D",24,2,4,5,0,0,0),
player_info("Whitecaps", "Emma Stauber", "D",25,3,7,8,0,0,0),
player_info("Whitecaps", "Julie Friend", "G", 25,0,0,0,19,0,0)]


allPlayers = Riveters + Whale + Beauts + Pride + Whitecaps

def game(teama,teamStatA, teamb,teamStatB):
    #defines teams Offence
    def team_off(player_list):
        team_off = 0
        for player in player_list:
            if player.pos == "W" :
                team_off += (player.off * 2)
            elif player.pos == "C" :
                team_off += (player.off * 1.5)
            else:
                team_off += player.off    
        return team_off

    # scores team defence
    def team_dfnce(player_list):
        team_dfnce = 0
        for player in player_list:
            if player.pos == "D" :
                team_dfnce += (player.dfnce * 2)
            elif player.pos == "C" :
                team_dfnce += (player.dfnce * 1.5)
            else:
                team_dfnce += player.dfnce    
        return team_dfnce

    # define team goalie scores
    def team_goalie(goalie):
        total_goalie = 0
        for lookforg in goalie:
            total_goalie += lookforg.gtend
        return total_goalie
        

    #team Goalie
    team_a_goalie = team_goalie(teama)
    team_b_goalie = team_goalie(teamb)
    # team Def
    team_dfnce_teama = team_dfnce(teama)
    team_dfnce_teamb = team_dfnce(teamb)
    #Team Off
    team_off_teama = team_off(teama)
    team_off_teamb = team_off(teamb)
    
    #Shot on Goal, determines if a goal is scored
    def shot_on_goal(sog,goalie):
        son = 0
        while son < 1:
            shooter = (random.choice(sog))
            if shooter.shot > 0:
                if shooter.shot > random.randint(0,(goalie * 2)):
                    shooter.goals += 1 
                    #print (shooter.team,"-", shooter.name)
                    return 1
                else:
                    return 0
                son += 1

    shots_teama = 0
    shots_teamb = 0
    goals_teamb = 0
    goals_teama = 0
    per = 0


    #Game, Per 1, 2 & 3
    while per < 3:
        per += 1
        #print ("Start of period", per )
        #print ("Goals by:")
        poss_in_per = random.randint(30,48)
        poss = 0
        while poss < poss_in_per:
            turnover = 0
            while turnover < 1:
                if random.randint(0,int(team_off_teama)) > random.randint(0,int(team_dfnce_teamb)):
                    if shot_on_goal(teama,team_b_goalie) == 0:
                        #print ("Shot team A")
                        shots_teama += 1
                        poss += 1
                    else: 
                        #print ("Goal Team A")
                        shots_teama += 1
                        goals_teama += 1
                        turnover += 1
                else:
                    #print ("Turnover team A")
                    poss += 1
                    turnover += 1
            while turnover < 2:
                if random.randint(0,int(team_off_teamb)) > random.randint(0,int(team_dfnce_teama)):
                    if shot_on_goal(teamb,team_a_goalie) == 0:
                        #print ("Shot team B")
                        shots_teamb += 1
                        poss += 1
                    else:
                        #print ("Goal Team B")
                        shots_teamb += 1
                        goals_teamb += 1
                        turnover += 1
                else:
                    #print ("Turnover team B")
                    poss += 1
                    turnover += 1

    #prints the final score of the game
    print()
    print ("Final Score")
    print (teamStatA, " Goals: ", goals_teama)
    print (teamStatB, " Goals: ", goals_teamb)

    #calculates the saves a goalie has made
    teama[10].saves +=  shots_teamb - goals_teamb
    teamb[10].saves += shots_teama - goals_teama

    #convert from strings to list to use in class
    teamStatB_eval = eval(teamStatB)
    teamStatA_eval = eval(teamStatA)
    
    #Adds game stats to the team class for standings
    teamStatA_eval.gf += goals_teama
    teamStatA_eval.ga += goals_teamb
    teamStatB_eval.gf += goals_teamb
    teamStatB_eval.ga += goals_teama

    if goals_teama > goals_teamb:
        teamStatA_eval.wins += 1
        teamStatB_eval.loses += 1
    elif goals_teamb > goals_teama:
        teamStatA_eval.loses += 1
        teamStatB_eval.wins += 1
    else:
        teamStatA_eval.ties += 1
        teamStatB_eval.ties += 1
    


def viewRoster():
    teams = ["[1] \t Riveters", "[2] \t Whale", "[3] \t Beauts","[4] \t Pride", "[5] \t Whitecaps"]
    for once in teams: 
      print (once)
    print ()  
    chosenTeam = input("Please choose number from above: ")
    if chosenTeam == '1':
        team = Riveters
    elif chosenTeam == '2':
        team = Whale
    elif chosenTeam == '3':
        team = Beauts
    elif chosenTeam == '4':
        team = Pride
    else:
        team = Whitecaps 
    print ("Name \t\t Age-Pos-Ovr-Goals-Saves")
    for players in team:
        print(players.name, '\t', players.age, '-', players.pos, '-', players.overall, '-', players.goals, '-', players.saves)
  

def standings():
    print()
    print ("Team Name \t GP \t Wins \t Loses \t Ties \t Points \t GF \t GA")
    rankedTeams = sorted(all_teams, key=lambda team: team.wins, reverse=True)
    for i in rankedTeams:
        i = team_info(i.teamname, i.wins,i.loses,i.ties,i.gf,i.ga)  
        print (i.teamname, "\t", i.gp,"\t", i.wins,"\t",i.loses,"\t",i.ties,"\t",i.points,"\t\t",i.gf,"\t",i.ga)
    print()
  
        
def leagueleaders():
    print ('[1] \t Goalies')
    print ('[2] \t Skaters')
    select = input('Please select Goalies or Skaters:  ')
    if select == '1':
        for players in allPlayers:
            if players.pos == "G":
                print (players.name, '---', players.team, '---', players.pos, '-', players.saves)
    else:
        show = input('How many players do you wish to see? ')
        num = eval(show)
        Scoring = sorted(allPlayers, key=lambda player: player.goals, reverse=True)
        for players in Scoring[:num]:
            print(players.name, '-', players.team, '-', players.pos, '-', players.goals)
        print()

def simWeek(gameList):
    for i in gameList[:2]:
        game(i[0],i[1],i[2],i[3])
    gameList.pop(0)
    gameList.pop(0)

allGames = [[Beauts, 'BUF', Whitecaps, 'MIN'],[Pride, 'BOS', Whale, 'CTW'],[Riveters, 'RIV', Beauts, 'BUF'],[Whitecaps, 'MIN', Pride, 'BOS'],
[Riveters, 'RIV', Pride, 'BOS'],[Whale, 'CTW', Whitecaps, 'MIN'],[Riveters, 'RIV', Whitecaps, 'MIN'],[Beauts, 'BUF', Whale, 'CTW'],
[Riveters, 'RIV', Whale, 'CTW'],[Beauts, 'BUF', Pride, 'BOS'],[Pride, 'BOS', Riveters, 'RIV'],[Whitecaps, 'MIN', Whale, 'CTW'],
[Beauts, 'BUF', Riveters, 'RIV'],[Pride, 'BOS', Whitecaps, 'MIN'],[Whitecaps, 'MIN', Riveters, 'RIV'],[Whale, 'CTW', Beauts, 'BUF'],
[Whale, 'CTW', Riveters, 'RIV'],[Pride, 'BOS', Beauts, 'BUF'],[Whitecaps, 'MIN', Beauts, 'BUF'],[Whale, 'CTW', Pride, 'BOS' ],
[Beauts, 'BUF', Whitecaps, 'MIN'],[Pride, 'BOS', Whale, 'CTW'],[Riveters, 'RIV', Beauts, 'BUF'],[Whitecaps, 'MIN', Pride, 'BOS'],
[Riveters, 'RIV', Pride, 'BOS'],[Whale, 'CTW', Whitecaps, 'MIN'],[Riveters, 'RIV', Whitecaps, 'MIN'],[Beauts, 'BUF', Whale, 'CTW'],
[Riveters, 'RIV', Whale, 'CTW'],[Beauts, 'BUF', Pride, 'BOS'],[Pride, 'BOS', Riveters, 'RIV'],[Whitecaps, 'MIN', Whale, 'CTW'],
[Beauts, 'BUF', Riveters, 'RIV'],[Pride, 'BOS', Whitecaps, 'MIN'],[Whitecaps, 'MIN', Riveters, 'RIV'],[Whale, 'CTW', Beauts, 'BUF'],
[Whale, 'CTW', Riveters, 'RIV'],[Pride, 'BOS', Beauts, 'BUF'],[Whitecaps, 'MIN', Beauts, 'BUF'],[Whale, 'CTW', Pride, 'BOS' ]]


def seasonMode():
    weekIn = 0
    while weekIn < 21:
        print ()
        print ('Welcome to the NWHL Season Simulator menu:')
        print ('[1] \t Standings')
        print ('[2] \t League Leaders')
        print ('[3] \t View Roster')
        print ('[4] \t Sim Week')
        print ('[5] \t Exit Game')
        print ()
        if weekIn != 20:
            print ('The games for week', (weekIn + 1), 'are:')
            print (allGames[0][1], ' vs ', allGames[0][3])
            print (allGames[1][1], ' vs ', allGames[1][3])
        print ()
        choice = input('Please select number 1-5: ')
        print ()
        if choice == '1':
            print ('Week' , (weekIn + 1) , 'Standings:')
            standings()
        elif choice == '2':
            print ('Week' , (weekIn + 1) , 'League Goal Leaders:')
            leagueleaders()
        elif choice == '3':
            viewRoster()
        elif choice == '5':
            break
        else:
            if weekIn == 20:
                break
            else:
                print ('Week' , (weekIn + 1) , 'Results')
                simWeek(allGames)
                weekIn +=1
    
     
        
#Opens and runs the game
seasonMode()







