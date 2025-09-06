import random

subject = [
    "Nawaz Sharif",
    "Imran Khan",
    "Bilawal Bhutto",
    "Shahbaz Sharif",
    "Maryam Nawaz",
    "Asif Zardari",
    "Shireen Mazari",
    "Fawad Chaudhry",
    "Pervez Musharraf",
    "Shaukat Aziz",
    "Yousaf Raza Gillani"
]

# Funny actions
actions = [
    "steals all the biryani",
    "dances in a rainstorm",
    "buys 1000 pet goats",
    "accidentally joins a circus",
    "starts selling samosas",
    "paints the parliament pink",
    "sleeps for 3 days straight",
    "becomes a TikTok star",
    "rides a donkey to work",
    "opens a chai shop",
    "declares everyday as holiday"
]

# Funny places
places = [
    "in the moon bazaar",
    "at the underwater cafe",
    "inside a giant samosa",
    "on top of the Eiffel Tower",
    "at the world's largest chai stall",
    "in the middle of a traffic jam",
    "inside a giant shoe",
    "on Mars",
    "in a haunted biryani shop",
    "at the donkey race",
    "inside a balloon factory"
]

while(True):
  news = random.choice(subject) + " " + random.choice(actions) + " " + random.choice(places) 
  print(news)
  ans=input(" do you want another news y/n : ")
  if(ans=="n"):
     break