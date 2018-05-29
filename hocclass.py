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
    
    
NYR = team_stats("Rangers", 0,0,0,0,0)
NYI = team_stats("Islanders", 0,0,0,0,0)
NJD = team_stats("Devils", 0,0,0,0,0)
PHI = team_stats("Flyers", 0,0,0,0,0)
PIT = team_stats("Pittsburgh", 0,0,0,0,0)
CAR = team_stats("Hurricanes", 0,0,0,0,0)

all_teams = (NYR, NYI, NJD, PHI, PIT, CAR)

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

player1 = player_stats("Rangers", "Megan", "C", 24,7,8,7,0,0,0)
player2 = player_stats("Rangers", "Brianna", "W", 29,6,8,2,0,0,0)
player3 = player_stats("Rangers", "Amanda", "W", 34,5,4,4,0,0,0)
player4 = player_stats("Rangers", "Kacey", "D", 27,8,2,6,0,0,0)
player5 = player_stats("Rangers", "Lee", "D",22,5,9,8,0,0,0)
player6 = player_stats("Rangers", "Alex", "G", 27,0,0,0,20,0,0)

player11 = player_stats("Islanders", "Kate", "C", 24,7,2,3,0,0,0)
player12 = player_stats("Islanders", "Jean", "W", 29,6,6,5,0,0,0)
player13 = player_stats("Islanders", "Samatha", "W", 34,5,4,3,0,0,0)
player14 = player_stats("Islanders", "Elena", "D", 27,6,6,5,0,0,0)
player15 = player_stats("Islanders", "Kelli", "D",22,2,4,7,0,0,0)
player16 = player_stats("Islanders", "April", "G", 27,0,0,0,16,0,0)

player21 = player_stats("Devils", "Natalie", "C", 24,3,6,4,0,0,0)
player22 = player_stats("Devils", "Emily", "W", 29,5,5,2,0,0,0)
player23 = player_stats("Devils", "Haley", "W", 34,5,4,4,0,0,0)
player24 = player_stats("Devils", "Jocelyne", "D", 27,7,4,7,0,0,0)
player25 = player_stats("Devils", "Laura", "D",22,7,6,9,0,0,0)
player26 = player_stats("Devils", "Shannon", "G", 27,0,0,0,16,0,0)


player31 = player_stats("Flyers", "Dora", "C", 25,2,6,7,0,0,0)
player32 = player_stats("Flyers", "Jane", "W", 23,6,8,4,0,0,0)
player33 = player_stats("Flyers", "Judy", "W", 27,5,2,6,0,0,0)
player34 = player_stats("Flyers", "Karla", "D", 27,8,2,6,0,0,0)
player35 = player_stats("Flyers", "Sheri", "D",25,1,6,6,0,0,0)
player36 = player_stats("Flyers", "Tammy", "G", 25,0,0,0,16,0,0)

player41 = player_stats("Penguins", "Shannon", "C", 24,4,4,4,0,0,0)
player42 = player_stats("Penguins", "Elsa", "W", 29,8,6,6,0,0,0)
player43 = player_stats("Penguins", "Eva", "W", 27,4,7,4,0,0,0)
player44 = player_stats("Penguins", "Lindsey", "D", 27,6,5,7,0,0,0)
player45 = player_stats("Penguins", "Kristina", "D",22,3,7,7,0,0,0)
player46 = player_stats("Penguins", "Jana", "G", 27,0,0,0,15,0,0)

player51 = player_stats("Hurricanes", "Cathy", "C", 24,9,3,5,0,0,0)
player52 = player_stats("Hurricanes", "Hattie", "W", 29,4,5,2,0,0,0)
player53 = player_stats("Hurricanes", "Blanche", "W", 34,5,6,3,0,0,0)
player54 = player_stats("Hurricanes", "Casey", "D", 27,4,5,9,0,0,0)
player55 = player_stats("Hurricanes", "Karen", "D",22,4,5,8,0,0,0)
player56 = player_stats("Hurricanes", "Diane", "G", 27,0,0,0,19,0,0)


team_01 = [player1, player2, player3, player4, player5, player6]
team_02 = [player11, player12, player13, player14, player15, player16]
team_03 = [player21, player22, player23, player24, player25, player26]
team_04 = [player31, player32, player33, player34, player35, player36]
team_05 = [player41, player42, player43, player44, player45, player46]
team_06 = [player51, player52, player53, player54, player55, player56]

games = 0
while games < 100:
  #Choosing teams
  loop = True
  while loop:
    teams = ["NYR", "NYI", "NJD","PHI", "PIT", "CAR"]
    for once in teams: 
      print (once)
    print
    userteam = input("Please choose team from above: ").upper()
    print()
    print()
    
    if userteam == "NYR" or "MON" or "DET" or "BOS" or "TOR" or "CHI":
      break
    else:
      print ("Follow the instructions")
      

  loop = True
  while loop:
    teamscomp = ["NYR", "NYI", "NJD","PHI", "PIT", "CAR"]
    teamscomp.remove(userteam)
    for once in teamscomp: 
      print (once)
    print
    teamcomp = input("Please choose another team from above: ").upper()
    print()
    print()
    
    if teamcomp == "NYR" or "MON" or "DET" or "BOS" or "TOR" or "CHI":
      break
    else:
      print ("Follow the instructions")

  the_team = userteam
  if the_team == "NYR":
    teama = team_01
  elif the_team == "NYI":
    teama = team_02
  elif the_team == "NJD":
    teama = team_03
  elif the_team == "PHI":
    teama = team_04
  elif the_team == "PIT":
    teama = team_05
  elif the_team == "CAR":
    teama = team_06
        
  the_team = teamcomp
  if the_team == "NYR":
    teamb = team_01
  elif the_team == "NYI":
    teamb = team_02
  elif the_team == "NJD":
    teamb = team_03
  elif the_team == "PHI":
    teamb = team_04
  elif the_team == "PIT":
    teamb = team_05
  elif the_team == "CAR":
    teamb = team_06      

  # whos playing
  #teama = team_01
  #teamb = team_05



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


  again = input("Would you like to play another game? Y/N ").upper()
  if again == "Y":
    games += 1
  else:
    break  

    
