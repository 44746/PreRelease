# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

import random
from datetime import *
ACE_HIGH = False
NO_OF_RECENT_SCORES = 10

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.date = ""
Deck = [None]
RecentScores = [None]
Choice = ''

def GetRank(RankNo):
  Rank = ''
  if RankNo == 1:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print("5. Options")
  print('6. Save high scores')
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input()
  print()
  Choice = Choice.lower()[0]
  return Choice

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard):
  if ACE_HIGH and NextCard.Rank == 1:
    NextCard.Rank = 14
  if ACE_HIGH and LastCard.Rank == 1:
    LastCard.Rank = 14
  if not ACE_HIGH and NextCard.Rank == 14:
    NextCard.Rank = 1
  if not ACE_HIGH and LastCard.Rank == 14:
    LastCard.Rank = 1
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def GetPlayerName():
  print()
  PlayerName = ""
  while PlayerName == "":
      PlayerName = input('Please enter your name: ')
      print()
      return PlayerName
  
        


def GetChoiceFromUser():
  Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
  Choice = Choice.lower()[0]
  return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].date = None

def DisplayRecentScores(RecentScores):
  print()
  print('Recent Scores: ')
  print()
  print("{0:<12}{1:<10}{2:<5}".format("Date","Name","Score"))
  print()
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    if RecentScores[Count].date != None:
      Date = RecentScores[Count].date.strftime("%d/%m/%Y")
    else:
      Date = "N/A"
    print("{0:<12}{1:<10}{2:<5}".format(Date,RecentScores[Count].Name,RecentScores[Count].Score))
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score):
  
  FoundSpace = False
  Count = 1
  name_on_table = input("Do you want to put your name on the table?(y/n): ")
  if name_on_table == "y":
    PlayerName = GetPlayerName()
    current_date= datetime.now()
    
    current_date_string = datetime.strftime(current_date, "%d/%m/%Y")
    while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
      if RecentScores[Count].Name == '':
        FoundSpace = True
      else:
        Count = Count + 1
    if not FoundSpace:
      for Count in range(1, NO_OF_RECENT_SCORES):
        RecentScores[Count].Name = RecentScores[Count + 1].Name
        RecentScores[Count].Score = RecentScores[Count + 1].Score
        RecentScores[Count].date = RecentScores[Count + 1].date
      Count = NO_OF_RECENT_SCORES
    RecentScores[Count].Name = PlayerName
    RecentScores[Count].Score = Score
    RecentScores[Count].date = date.today()

def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y' and Choice !='Y' and Choice !="yes" and Choice !="Yes") and (Choice != 'n' and Choice !="N" and Choice !="No" and Choice !="no"):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard)
    if (Higher and Choice == 'y'or Choice=='Y' or Choice =="yes" or Choice=="Yes") or (not Higher and Choice == 'n' or Choice =="N" or Choice =="No" or Choice =="no"):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

def DisplayOptions():
  print()
  print('OPTION MENU')
  print()
  print('1. Set Ace to be HIGH or LOW')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetOptionChoice():
  boolean = False
  while not  boolean:
      option = input("")
      if option == "1" or option == "q":
        boolean = True
  else:
    print("Please enter a valid option")
    print()
  
  return option.lower()[0]

def SetOptions(OptionChoice):
  if OptionChoice == '1':
      SetAceHighOrLow()

def SetAceHighOrLow():
  global ACE_HIGH
  boolean = False
  while not boolean:
      Ace = input("Do you want the Ace to be (h)igh or (l)ow: ")
      Ace = Ace.lower()[0]
      if Ace== "h" or Ace == "l":
         boolean = True
      if Ace == "h":
        ACE_HIGH = True
      else:
        ACE_HIGH = False

def BubbleSortScores(RecentScores):
  no_more_swaps = True
  listLen = len(RecentScores)
  while noMoreSwaps == True:
      listLen = listLen - 1
      no_more_swaps = False
      for place in range(1,listLen-1):
          if RecentScores[place].Score < RecentScores[place+1].Score:
              temp = RecentScores[place+1]
              RecentScores[place+1] = RecentScores[place]
              RecentScores[place] = temp
              no_more_swaps = True

def LoadScores():
  try:
    with open("scores.txt",mode="r",encoding="utf-8") as file:
      scores = file.read().splitlines()
    for score in range(len(scores)):
        temp = scores[score].split(",")
        scores[score] = temp
        
        ScoreDate = scores[score][0] 
        day = ScoreDate[0:2]
        month = ScoreDate[3:5]
        year = ScoreDate[6:]
        ScoreDate = date(int(year),int(month),int(day))
        scores[score][0] = ScoreDate
    RecentScores = [None]
    for score in scores:
      NewScore = TRecentScore()
      NewScore.date = score[0]
      NewScore.Name = score[1]
      NewScore.Score = int(score[2])
      RecentScores.append(NewScore)
  except FileNotFoundError:
    RecentScores = None
  return RecentScores



def SaveScores(RecentScores):
  
  with open("scores.txt",mode="w",encoding="utf-8") as File:
    for score in RecentScores:
      if score != None:
        if score.Name != "":
          File.write(score.date.strftime("%d/%m/%Y")+",")
          File.write(score.Name+",")
          File.write(str(score.Score)+"\n")

if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  RecentScores = LoadScores()
  if len(RecentScores) == 0 or len(RecentScores) < NO_OF_RECENT_SCORES:
    AdditionalScores = NO_OF_RECENT_SCORES - len(RecentScores) + 1
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())


  Choice = ""
  while Choice != "q":
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      BubbleSortScores(RecentScores)
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      DisplayOptions()
      OptionChoice = GetOptionChoice()
      if OptionChoice != "q":
        SetOptions(OptionChoice)
    elif Choice == '6':
      SaveScores(RecentScores)
  
  
