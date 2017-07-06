import getplayers
import datetime
import asyncio
import strawpoll
import time

async def main():
  api = strawpoll.API()

  noms = getplayers.get_potg_noms()

  today = datetime.date.today()
  time = datetime.datetime.now().time()
  
  #west coast games can end fairly late. if it's after 2 am and this breaks no one is gonna
  #be awake to vote anyway. 
  if time.hour < 2:
    today = today + datetime.timedelta(-1)
  
  title = "Who is your Astros player of the game? (" + str(today.month)+ '/' + str(today.day)+ ')'
  
  print(title)
  for nom in noms:
    print(nom)
  poll = strawpoll.Poll(title, noms)
  poll = await api.submit_poll(poll)
  #time.sleep(2)
  print(poll.url)
  
  print("success!")

asyncio.get_event_loop().run_until_complete(main())
