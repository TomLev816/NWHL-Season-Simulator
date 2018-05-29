#NWHL 2018-2019

import random

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
CTW = team_stats("Whale", 0,0,0,0,0)
BUF = team_stats("Beauts", 0,0,0,0,0)
BOS = team_stats("Pride", 0,0,0,0,0)
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

player1 = player_stats("Riveters", "Madison Packer", "C", 24,9,9,7,0,0,0)
player2 = player_stats("Riveters", "Miye D'Oench", "W", 29,7,8,7,0,0,0)
player3 = player_stats("Riveters", "Rebecca Russo", "W", 34,6,4,7,0,0,0)
player4 = player_stats("Riveters", "Kelsey koelzer", "D", 27,5,7,9,0,0,0)
player5 = player_stats("Riveters", "Courtney Burke", "D",22,3,7,8,0,0,0)
player6 = player_stats("Riveters", "Katie Fitzgerald", "G", 27,0,0,0,22,0,0)

player11 = player_stats("Whale", "Emily Fluke", "C", 24,4,6,4,0,0,0)
player12 = player_stats("Whale", "Meghan Huertas", "W", 29,3,5,4,0,0,0)
player13 = player_stats("Whale", "Kelly Babstock", "W", 34,1,6,2,0,0,0)
player14 = player_stats("Whale", "Amanda Boulier", "D", 27,4,6,4,0,0,0)
player15 = player_stats("Whale", "Emma Greco", "D",22,1,4,5,0,0,0)
player16 = player_stats("Whale", "Sydney Rossman", "G", 27,0,0,0,19,0,0)

player21 = player_stats("Beauts", "Hayley Scamurra", "C", 24,7,7,5,0,0,0)
player22 = player_stats("Beauts", "Maddie Elia", "W", 29,1,7,5,0,0,0)
player23 = player_stats("Beauts", "Kristin Lewicki", "W", 34,5,5,6,0,0,0)
player24 = player_stats("Beauts", "Lisa Chesson", "D", 27,2,4,7,0,0,0)
player25 = player_stats("Beauts", "Sarah Casorso", "D",22,1,6,6,0,0,0)
player26 = player_stats("Beauts", "Amanda Leveille", "G", 27,0,0,0,22,0,0)


player31 = player_stats("Pride", "Jillian Dempsey", "C", 25,7,7,4,0,0,0)
player32 = player_stats("Pride", "Sydney Daniels", "W", 23,3,6,4,0,0,0)
player33 = player_stats("Pride", "Emily Field", "W", 27,2,6,3,0,0,0)
player34 = player_stats("Pride", "Alyssa Gagliardi", "D", 27,3,5,7,0,0,0)
player35 = player_stats("Pride", "Kaleigh Fratkin", "D",25,1,5,6,0,0,0)
player36 = player_stats("Pride", "Brittany Ott", "G", 25,0,0,0,21,0,0)

player41 = player_stats("Whitecaps", "Bray Ketchum", "C", 24,1,6,7,0,0,0)
player42 = player_stats("Whitecaps", "Taylor Accursi", "W", 29,6,6,2,0,0,0)
player43 = player_stats("Whitecaps", "Jess Jones", "W", 27,4,6,2,0,0,0)
player44 = player_stats("Whitecaps", "Jenny Ryan", "D", 27,4,7,7,0,0,0)
player45 = player_stats("Whitecaps", "Ashley Johnston", "D",22,2,2,9,0,0,0)
player46 = player_stats("Whitecaps", "Brianna Laing", "G", 27,0,0,0,14,0,0)


team_01 = [player1, player2, player3, player4, player5, player6]
team_02 = [player11, player12, player13, player14, player15, player16]
team_03 = [player21, player22, player23, player24, player25, player26]
team_04 = [player31, player32, player33, player34, player35, player36]
team_05 = [player41, player42, player43, player44, player45, player46]


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
    
    if userteam == "RIV" or "MON" or "DET" or "BOS" or "TOR" or "CHI":
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
    
    if teamcomp == "RIV" or "MON" or "DET" or "BOS" or "TOR" or "CHI":
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

  # scores team def
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
  

  
  
  print ("Team A")
  print (team_off_teama)
  print (team_dfnce_teama)
  print (team_a_goalie)
  print ()
  print ("Team B")
  print (team_off_teamb)
  print (team_dfnce_teamb)
  print (team_b_goalie)
  print ()




  #Shot on Goal
  def shot_on_goal(sog,goalie):
    son = 0
    while son < 1:
      shooter = (random.choice(sog))
      if shooter.shot > 1:
        if shooter.shot > random.randint(0,(goalie * 2)):
          shooter.goals += 1 
          print (shooter.team,"-", shooter.name)
          return 1
        else:
          return 0
        son += 1

  shots_teama = 0
  shots_teamb = 0
  goals_teamb = 0
  goals_teama = 0
  per = 0



  while per < 3:
      per += 1
      print ("Start of period", per )
      print ("Goals by:")
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

      print ()
      print ("Stats thru", per)
      print (userteam, " Shots: ", shots_teama)
      print (teamcomp, "Shots: ", shots_teamb)
      print ()
      print (userteam, " Goals: ", goals_teama)
      print (teamcomp, " Goals: ", goals_teamb)
      print ()
      print ()
    
  #convert from strings to list
  teamcomp_eval = eval(teamcomp)
  userteam_eval = eval(userteam)
  
  if goals_teama > goals_teamb:
    userteam_eval.wins += 1
    userteam_eval.gf += goals_teama
    userteam_eval.ga += goals_teamb
    teamcomp_eval.loses += 1
    teamcomp_eval.gf += goals_teamb
    teamcomp_eval.ga += goals_teama
  elif goals_teamb > goals_teama:
    userteam_eval.loses += 1
    userteam_eval.gf += goals_teama
    userteam_eval.ga += goals_teamb
    teamcomp_eval.wins += 1
    teamcomp_eval.gf += goals_teamb
    teamcomp_eval.ga += goals_teama
  else:
    userteam_eval.ties += 1
    userteam_eval.gf += goals_teama
    userteam_eval.ga += goals_teamb
    teamcomp_eval.ties += 1
    teamcomp_eval.gf += goals_teamb
    teamcomp_eval.ga += goals_teama
  
  print ("Team Name - GP - Wins - Loses - Ties - Points - GF - GA")

  for i in all_teams:
    i = team_stats(i.teamname, i.wins,i.loses,i.ties,i.gf,i.ga)  
    print (i.teamname, " - ", i.gp," - ", i.wins," - ",i.loses," - ",i.ties," - ",i.points," - ",i.gf," - ",i.ga)
    
  print()

  #userteam_eval = team_stats(userteam_eval.teamname, userteam_eval.wins,userteam_eval.loses,userteam_eval.ties,userteam_eval.gf,userteam_eval.ga)
  #teamcomp_eval = team_stats(teamcomp_eval.teamname, teamcomp_eval.wins,teamcomp_eval.loses,teamcomp_eval.ties,teamcomp_eval.gf,teamcomp_eval.ga)


  #print (userteam, " Points: ", userteam_eval.points)
  #print (teamcomp, " Points: ", teamcomp_eval.points)
  #print()
  #print (userteam, " Total Stats: ")
  
  for players in teama:
    if players.pos == "G":
      print (players.name, '-', players.pos, '-', 'saves')
    else:
        print (players.name, '-', players.pos, '-', players.goals)
  print ()
  print (teamcomp, " Total Stats: ")
  for players in teamb:
    if players.pos == "G":
      print (players.name, '-', players.pos, '-', 'saves')
    else:
      print (players.name, '-', players.pos, '-', players.goals)
  print()
  print()


  again = input("Would you like to stop playing? Y/N ").upper()
  if again == "Y":
    break
  else:
    games += 1  

    
