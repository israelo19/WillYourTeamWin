# Python Script
# 02-03-2021
# Israel Ogwu
# This is a code that will predict the chance that your Football(Soccer)team will win their league.




# List of Soccer/Football Teams in the Premier Leauge(currently)
t = ["Liverpool", "Manchester City", "Manchester United", "Leicester City", "West Ham", "Everton", "Tottenham",
     "Chelsea", "Aston Villa", "Arsenal", "Leeds United",
     "Crystal Palace", "Wolves", "Brighton", "Newcastle", "Burnely", "Fulham", "West Brom", "Sheffield United"]
#To add a "," after each Team. This is the "join" funchtion
s=", "
s=s.join(t)
# Set player to false
player = False
league_wins = False
league_rank = False
a=False
p=False

# Allows me to use "randint"
from random import randint

# List of allowed club names
print ("Choose a club from this list of Preimer Leauge teams: ")
print (s)    # join function in action! Lines 16-17
# Lets make player=True
while player == False:
    player = input ("What is the name of your club?")
    # Player will come back at the end
    if player in t:
        print (player, "is a nice choice.")
    else:
        player = False
        print ("Hmm? Check your spelling. Make sure your team name is spelled like in the list above.")

#Just in case I want to lop this
#        player = False

while p == False:
    p = int(input("What is your team's starting percentage? EX: If team's rank is 1st then starting percentage is 95% If teams rank is 2nd the starting percenttage is 90. As the rank goes down the starting percentage goes down by 5%. Disclaimer: Do not add number with percent sign! Ex: 60"))  # Wrapped int around input so that the
    if p >= 0:
        print ("Oooooooh OK!")

    p = True

while league_wins == False:
    league_wins = int(input ("How many times has this team won the Premier League? (Just the number please. Ex: 5)")) #Wrapped int around input so that the
# outcome will be a int and not a variable
    if league_wins >= 3:
      print("Oh that's NICEEEE")
    elif league_wins <= 2:
      print("Oooh, ok")
    league_wins = True

#league_wins will comeback later

while league_rank == False:
    league_rank = int(input("What place is your team in right now? (Just the number please. Ex: 5)"))#Wrapped int around input so that the
    if league_rank >= 0:
        print("Oooooooh OK!")

    league_rank = True



while a == False:
    a = int(input("How many teams are above your team? Ex: This is out of 20 teams! If you are in 10th place, then 10 teams are above your team. Ex: 10"))  # Wrapped int around input so that the
    if a >= 0:
        print ("Oooooooh OK!")

    a = True

#r=(p+league_rank+league_wins)-a
#print(r)
#print("chance of winning!")
print(player + " Has a ")
print(randint(70,89))
print("percent chance to win the league!")
#o=(league_wins*league_rank)
#print(o)



# outcome will be a int and not a variable
#NEED TO ADD "IF NOT A NUMBER PRINT..." "MAKE IT A LOOP!
#Might come in handy later!
#print(league_rank * league_wins)\
#Equation:p=(s+(H%*w^2)-t

#h=(abs(league_rank-20)+1)


# ------------------------------------------------------------------------------------------------------------------------------
# Function to print a list
# def listToString(t):
# str1= ','
# return (str1.join(t))
# t=["Liverpool,", "Manchester City,", "Manchester United,", "Leicester City,", "West Ham,", "Everton,", "Tottenham,",
#   "Chelsea,", "Aston Villa,", "Arsenal,", "Arsenal,", "Leeds United,",
#   "Crystal Palace,", "Wolves,", "Brighton,", "Newcastle,", "Burnely,", "Fulham,", "West Brom,", "Sheffield United."]
# print(listToString(t))
