#NWHL 2018-2019

import random
import pandas as pd
import numpy as np
import operator

class team_stats(object):
  def __init__(self, teamname, wins, loses, ties, gf, ga):
    self.teamname = teamname
    self.gp = wins + loses + ties 
    self.wins = wins
    self.loses = loses
    self.ties = ties
    self.points = wins*2 + ties
    self.gf = gf
    self.ga = ga
    
    
RIV = team_stats("Riveters", 0,0,0,0,0)
CTW = team_stats("Whale   ", 0,0,0,0,0)
BUF = team_stats("Beauts  ", 0,0,0,0,0)
BOS = team_stats("Pride   ", 0,0,0,0,0)
MIN = team_stats("Whitecaps", 0,0,0,0,0)


all_teams = (RIV, CTW, BUF, BOS, MIN)

class player_stats(object):
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

player101 = player_stats("Riveters", "Madison Packer", "C", 27,9,9,7,0,0,0)
player102 = player_stats("Riveters", "Bray Ketchum", "C", 29,5,6,4,0,0,0)
player103 = player_stats("Riveters", "Alexa Gruschow", "W", 24,8,6,6,0,0,0)
player104 = player_stats("Riveters", "Amanda Kessel", "W", 26,5,8,8,0,0,0)
player105 = player_stats("Riveters", "Rebecca Russo", "W", 24,8,4,3,0,0,0)
player106 = player_stats("Riveters", "Miye D'Oench", "W", 24,8,7,3,0,0,0)
player107 = player_stats("Riveters", "Courtney Burke", "D",23,3,8,8,0,0,0)
player108 = player_stats("Riveters", "Jenny Ryan", "D",23,1,7,4,0,0,0)
player109 = player_stats("Riveters", "Kiira Dosdall", "D",30,1,6,7,0,0,0)
player110 = player_stats("Riveters", "Kelsey koelzer", "D", 23,6,5,9,0,0,0)
player111 = player_stats("Riveters", "Katie Fitzgerald", "G", 24,0,0,0,23,0,0)

player201 = player_stats("Whale", "Emily Fluke", "C", 25,4,6,4,0,0,0)
player202 = player_stats("Whale", "Sam Faber", "C", 31,3,5,6,0,0,0)
player203 = player_stats("Whale", "Jamie Goldsmith", "W", 27,4,6,7,0,0,0)
player204 = player_stats("Whale", "Kelly Babstock", "W", 25,4,7,4,0,0,0)
player205 = player_stats("Whale", "Sam Donovan", "W", 25,4,7,4,0,0,0)
player206 = player_stats("Whale", "Meghan Huertas", "W", 25,5,7,6,0,0,0)
player207 = player_stats("Whale", "Amanda Boulier", "D", 25,4,6,7,0,0,0)
player208 = player_stats("Whale", "Emma Greco", "D",22,1,4,5,0,0,0)
player209 = player_stats("Whale", "Shannon Doyle", "D",22,1,5,7,0,0,0)
player210 = player_stats("Whale", "Cydney Roesler", "D",22,2,3,8,0,0,0)
player211 = player_stats("Whale", "Sydney Rossman", "G", 27,0,0,0,19,0,0)

player301 = player_stats("Beauts", "Hayley Scamurra", "C", 24,7,7,5,0,0,0)
player302 = player_stats("Beauts", "Jordan Juron", "C", 24,6,6,4,0,0,0)
player303 = player_stats("Beauts", "Maddie Elia", "W", 29,1,7,5,0,0,0)
player304 = player_stats("Beauts", "Kristin Lewicki", "W", 34,6,5,6,0,0,0)
player305 = player_stats("Beauts", "Dani Cameranesi", "W", 23,3,8,7,0,0,0)
player306 = player_stats("Beauts", "Kourtney Kunichika", "W", 26,5,9,3,0,0,0)
player307 = player_stats("Beauts", "Lisa Chesson", "D", 27,2,4,7,0,0,0)
player308 = player_stats("Beauts", "Sarah Casorso", "D",22,1,6,6,0,0,0)
player309 = player_stats("Beauts", "Emily Pfalzer", "D",25,3,7,9,0,0,0)
player310 = player_stats("Beauts", "Sarah Edney", "D",25,3,7,9,0,0,0)
player311 = player_stats("Beauts", "Shannon Szabados", "G", 31,0,0,0,25,0,0)

player401 = player_stats("Pride", "Jillian Dempsey", "C", 25,7,7,4,0,0,0)
player402 = player_stats("Pride", "Brianna Decker", "C", 27,9,9,5,0,0,0)
player403 = player_stats("Pride", "Sydney Daniels", "W", 23,8,6,5,0,0,0)
player404 = player_stats("Pride", "Emily Field", "W", 25,2,6,3,0,0,0)
player405 = player_stats("Pride", "Haley Skarupa", "W", 24,7,8,3,0,0,0)
player406 = player_stats("Pride", "Dana Trivigno", "W", 24,7,7,6,0,0,0)
player407 = player_stats("Pride", "Alyssa Gagliardi", "D", 27,3,5,7,0,0,0)
player408 = player_stats("Pride", "Kaleigh Fratkin", "D",25,1,5,6,0,0,0)
player409 = player_stats("Pride", "Paige Harrington", "D",24,1,4,8,0,0,0)
player410 = player_stats("Pride", "Meagan Mangene", "D",25,3,7,7,0,0,0)
player411 = player_stats("Pride", "Brittany Ott", "G", 28,0,0,0,21,0,0)

player501 = player_stats("Whitecaps", "Hannah Brandt", "C", 24,6,8,5,0,0,0)
player502 = player_stats("Whitecaps", "Hillary Crowe", "C", 25,6,7,4,0,0,0)
player503 = player_stats("Whitecaps", "Kendall Coyne", "W", 26,5,9,6,0,0,0)
player504 = player_stats("Whitecaps", "Amy Menke", "W", 23,4,7,4,0,0,0)
player505 = player_stats("Whitecaps", "Kathleen Frischmann", "W", 27,2,4,6,0,0,0)
player506 = player_stats("Whitecaps", "Margo Lund", "W", 25,2,4,7,0,0,0)
player507 = player_stats("Whitecaps", "Kelly Buchta", "D", 28,2,5,6,0,0,0)
player508 = player_stats("Whitecaps", "Tanja Eisenschmid", "D",25,6,3,7,0,0,0)
player509 = player_stats("Whitecaps", "Anna-Maria Fiegert", "D",24,2,4,5,0,0,0)
player510 = player_stats("Whitecaps", "Emma Stauber", "D",25,3,7,8,0,0,0)
player511 = player_stats("Whitecaps", "Julie Friend", "G", 25,0,0,0,17,0,0)


Riveters = [player101, player102, player103, player104, player105, player106, player107, player108, player109, player110, player111]
Whale = [player201, player202, player203, player204, player205, player206, player207, player208, player209, player210, player211]
Beauts = [player301, player302, player303, player304, player305, player306, player307, player308, player309, player310, player311]
Pride = [player401, player402, player403, player404, player405, player406, player407, player408, player409, player410, player411]
Whitecaps = [player501, player502, player503, player504, player505, player506, player507, player508, player509, player510, player511]

allPlayers = Riveters + Whale + Beauts + Pride + Whitecaps

'''
games = 0
while games < 100:
  #Choosing teams
  loop = True
  while loop:
    teams = ["RIV", "CTW", "BUF","BOS", "MIN"]
    for once in teams: 
      print (once)
    print
    userteam = input("Please choose team from above: ").upper()
    print()
    print()
    
    if userteam == "RIV" or "CTW" or "BUF" or "BOS" or "MIN":
      break
    else:
      print ("Follow the instructions")
      

  loop = True
  while loop:
    teamscomp = ["RIV", "CTW", "BUF","BOS", "MIN"]
    teamscomp.remove(userteam)
    for once in teamscomp: 
      print (once)
    print
    teamcomp = input("Please choose another team from above: ").upper()
    print()
    print()
    
    if teamcomp == "RIV" or "CTW" or "BUF" or "BOS" or "MIN":
      break
    else:
      print ("Follow the instructions")

  the_team = userteam
  if the_team == "RIV":
    teama = team_01
  elif the_team == "CTW":
    teama = team_02
  elif the_team == "BUF":
    teama = team_03
  elif the_team == "BOS":
    teama = team_04
  elif the_team == "MIN":
    teama = team_05
          
  the_team = teamcomp
  if the_team == "RIV":
    teamb = team_01
  elif the_team == "CTW":
    teamb = team_02
  elif the_team == "BUF":
    teamb = team_03
  elif the_team == "BOS":
    teamb = team_04
  elif the_team == "MIN":
    teamb = team_05
    
  # scores teams off
  '''

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
        poss_in_per = random.randint(30,50)
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
        '''
        print ("Stats thru", per)
        print (teamStatA, " Shots: ", shots_teama)
        print (teamStatB, "Shots: ", shots_teamb)
        print ()
        print (teamStatA, " Goals: ", goals_teama)
        print (teamStatB, " Goals: ", goals_teamb)
        print ()
        '''

    print()
    print ("Final Score")
    print (teamStatA, " Goals: ", goals_teama)
    print (teamStatB, " Goals: ", goals_teamb)

    
    teama[10].saves +=  shots_teamb - goals_teamb
    teamb[10].saves += shots_teama - goals_teama

    #convert from strings to list
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
    
    
  
    

def standings():
    print()
    print ("Team Name \t GP \t Wins \t Loses \t Ties \t Points \t GF \t GA")
    for i in all_teams:
        i = team_stats(i.teamname, i.wins,i.loses,i.ties,i.gf,i.ga)  
        print (i.teamname, "\t", i.gp,"\t", i.wins,"\t",i.loses,"\t",i.ties,"\t",i.points,"\t\t",i.gf,"\t",i.ga)
    print()


  
        
def leagueleaders():
    print('Leading Goal Scorers:')
    Scoring = sorted(allPlayers, key=lambda player: player.goals, reverse=True)
    for players in Scoring[:10]:
        print(players.name, '-', players.team, '-', players.pos, '-', players.goals)
    print()



start = input('Would you like to play week 1? Y/N ').upper()
game(Beauts, 'BUF', Whitecaps, 'MIN')
game(Pride, 'BOS', Whale, 'CTW')
standings()
leagueleaders()

start = input('Would you like to play week 2? Y/N ').upper()
game(Riveters, 'RIV', Beauts, 'BUF')
game(Whitecaps, 'MIN', Pride, 'BOS')
standings()
leagueleaders()
    
start = input('Would you like to play week 3? Y/N ').upper()
game(Riveters, 'RIV', Pride, 'BOS')
game(Whale, 'CTW', Whitecaps, 'MIN')
standings()
leagueleaders()
    
start = input('Would you like to play week 4? Y/N ').upper()
game(Riveters, 'RIV', Whitecaps, 'MIN')
game(Beauts, 'BUF', Whale, 'CTW')
standings()
leagueleaders()

start = input('Would you like to play week 5? Y/N ').upper()
game(Riveters, 'RIV', Whale, 'CTW')
game(Beauts, 'BUF', Pride, 'BOS')
standings()
leagueleaders()

start = input('Would you like to play week 6? Y/N ').upper()
game(Pride, 'BOS', Riveters, 'RIV')
game(Whitecaps, 'MIN', Whale, 'CTW')
standings()
leagueleaders()

start = input('Would you like to play week 7? Y/N ').upper()
game(Beauts, 'BUF', Riveters, 'RIV')
game(Pride, 'BOS', Whitecaps, 'MIN')
standings()
leagueleaders()

start = input('Would you like to play week 8? Y/N ').upper()
game(Whitecaps, 'MIN', Riveters, 'RIV')
game(Whale, 'CTW', Beauts, 'BUF')
standings()
leagueleaders()

start = input('Would you like to play week 9? Y/N ').upper()
game(Whale, 'CTW', Riveters, 'RIV')
game(Pride, 'BOS', Beauts, 'BUF' )
standings()
leagueleaders()

start = input('Would you like to play week 10? Y/N ').upper()
game(Whitecaps, 'MIN', Beauts, 'BUF')
game(Whale, 'CTW', Pride, 'BOS' )
standings()
leagueleaders()


start = input('Would you like to play week 11? Y/N ').upper()
game(Beauts, 'BUF', Whitecaps, 'MIN')
game(Pride, 'BOS', Whale, 'CTW')
standings()
leagueleaders()

start = input('Would you like to play week 12? Y/N ').upper()
game(Riveters, 'RIV', Beauts, 'BUF')
game(Whitecaps, 'MIN', Pride, 'BOS')
standings()
leagueleaders()
    
start = input('Would you like to play week 13? Y/N ').upper()
game(Riveters, 'RIV', Pride, 'BOS')
game(Whale, 'CTW', Whitecaps, 'MIN')
standings()
leagueleaders()
    
start = input('Would you like to play week 14? Y/N ').upper()
game(Riveters, 'RIV', Whitecaps, 'MIN')
game(Beauts, 'BUF', Whale, 'CTW')
standings()
leagueleaders()

start = input('Would you like to play week 15? Y/N ').upper()
game(Riveters, 'RIV', Whale, 'CTW')
game(Beauts, 'BUF', Pride, 'BOS')
standings()
leagueleaders()

start = input('Would you like to play week 16? Y/N ').upper()
game(Pride, 'BOS', Riveters, 'RIV')
game(Whitecaps, 'MIN', Whale, 'CTW')
standings()
leagueleaders()

start = input('Would you like to play week 17? Y/N ').upper()
game(Beauts, 'BUF', Riveters, 'RIV')
game(Pride, 'BOS', Whitecaps, 'MIN')
standings()
leagueleaders()

start = input('Would you like to play week 18? Y/N ').upper()
game(Whitecaps, 'MIN', Riveters, 'RIV')
game(Whale, 'CTW', Beauts, 'BUF')
standings()
leagueleaders()

start = input('Would you like to play week 19? Y/N ').upper()
game(Whale, 'CTW', Riveters, 'RIV')
game(Pride, 'BOS', Beauts, 'BUF' )
standings()
leagueleaders()

start = input('Would you like to play week 20? Y/N ').upper()
game(Whitecaps, 'MIN', Beauts, 'BUF')
game(Whale, 'CTW', Pride, 'BOS' )
standings()
leagueleaders()

'''
   
#League leaders
def leaders(players):
    leader = ""
    topGoals = 0
    for each in players:
        if each.goals > topGoals:
            topGoals = each.goals
            leader = each.name
        return leader, topGoals

print (leaders(Riveters))
'''
