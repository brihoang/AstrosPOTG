import mlbgame
import datetime

def get_potg_noms():
  players = []
  #get current game 

  #get current date
  today = datetime.date.today()
  time = datetime.datetime.now().time()
  
  if time.hour < 3:
    today = today + datetime.timedelta(-1)

  #get the mlb game
    
  day = mlbgame.day(today.year, today.month, today.day, home="Astros", away="Astros")
  game = day[0]
  
  #determine if the astros are the away team or the home team 
  
  homeaway = 'home'
  
  if game.home_team != 'Astros':
    homeaway = 'away'

  #get stats
  stats = mlbgame.player_stats(game.game_id)
  
  #get the nominees for position players
  for player in stats[homeaway+"_batting"]:
    name = player.name_display_first_last
    if player.h > 0 or player.bb > 0 or player.r > 0 or player.rbi > 0:
      players.append(name)
  
  #get the nominees among pitchers
  for player in stats[homeaway+"_pitching"]:
    name = player.name_display_first_last
    if player.out > 15 or player.er < 2 or player.win or player.save:
      players.append(name)
  #relievers get nominated if gave up 2 runs or less
  return players 
