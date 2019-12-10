from random import *
import os
import time

#********************************************************************************************************

def color(s):
  print();print()
  r=choice(s)
  print(r)
  s=[]
  g=[]
  d=1
  e=0
  f=0
  a=randint(4,6)
  os.system('cls');print()
  print("                                              Welcome to color guessing game "); print()
  print("                                u have {} attempts .....u must give right answer at least {} attempts".format(a,a-2));print()
  print();print("    HINT : the word contains  ",r[len(r)-3]);print()
  while a>0:
     z=input("    guess {} alphabet : ".format(d))
     x=z.lower()
     d+=1
     a-=1  
     if x in r:
          print("    yes.....guessed alphabet is in the word");print()
          s.append(x)
          e+=1
     else:
          print("    no....guessed alphabet is not in the word");print()
          g.append(x)
          f+=1
  
  print();print()
  print("    all attempts over ");print()
  time.sleep(2)
  print("    calculating result ........")  
  time.sleep(2)
  print()  
  if e>f:  
       print("    u win ...u gave {} right answer{}  and {} wrong answer{}...right answer is  {}".format(e,s,f,g,r))
  elif e==f:
       print("    tie...u gave {} right answer{}  and {} wrong answer{}...right answer is  {}".format(e,s,f,g,r))
  else:
       print("    u loose...u gave {} right answer{}  but {} wrong answer{}...right answer is  {}".format(e,s,f,g,r))     
  print()
  time.sleep(3)
  z12=input("   game over .....press enter to continue")
  
#***************************************************************************************************************************

def animal(s):
  print();print()
  r=choice(s)
  print(r)
  s=[]
  g=[]
  d=1
  e=0
  f=0
  a=randint(4,7); 
  os.system('cls')
  print("                                              Welcome to animal guessing game "); print()
  print("                                u have {} attempts .....u must give right answer at least {} attempts".format(a,a-2));print()
  print();print("    HINT : the word contains  ",r[len(r)-3]);print() 
  while a>0:
     z=input("    guess {} alphabet : ".format(d))
     x=z.lower()
     d+=1
     a-=1  
     if x in r:
          print("    yes.....guessed alphabet is in the word");print()
          s.append(x)
          e+=1
     else:
          print("    no....guessed alphabet is not in the word");print()
          g.append(x)
          f+=1
  
  print();print()
  print("   all attempts over ");print()
  time.sleep(2)
  print("   calculating result ........")  
  time.sleep(3)
  print()  
  if e>f:    
       print("    u win .....u gave {} right answer{}  and {} wrong answer{}.......right answer is  {}".format(e,s,f,g,r))
  elif e==f:
       print("    tie....u gave {} right answer{}  and {} wrong answer{}......right answer is  {}".format(e,s,f,g,r))
  else:
       print("    u loose....u gave {} right answer{}  but {} wrong answer{}......right answer is  {}".format(e,s,f,g,r))     
  print()
  time.sleep(3)
  z12=input("   game over .....press enter to continue")
  
#****************************************************************************************************************

def car(s):
  print();print()
  r=choice(s)
  print(r)
  s=[]
  g=[]
  d=1
  e=0
  f=0
  a=randint(4,6)
  os.system('cls');print()
  print("                                              Welcome to car guessing game "); print()
  print("                                u have {} attempts .....u must give right answer at least {} attempts".format(a,a-2));print()
  print();print("    HINT : the word contains  ",r[len(r)-3]);print()
  while a>0:
     z=input("    guess {} alphabet : ".format(d))
     x=z.lower()
     d+=1
     a-=1  
     if x in r:
          print("    yes.....guessed alphabet is in the word");print()
          s.append(x)
          e+=1
     else:
          print("    no....guessed alphabet is not in the word");print()
          g.append(x)
          f+=1
  
  print();print()
  print("    all attempts over ");print()
  time.sleep(2)
  print("    calculating result ........")  
  time.sleep(2)
  print()  
  if e>f:  
       print("    u win ...u gave {} right answer{}  and {} wrong answer{}...right answer is  {}".format(e,s,f,g,r))
  elif e==f:
       print("    tie...u gave {} right answer{}  and {} wrong answer{}...right answer is  {}".format(e,s,f,g,r))
  else:
       print("    u loose...u gave {} right answer{}  but {} wrong answer{}...right answer is  {}".format(e,s,f,g,r)) 

  print()
  time.sleep(3)
  z12=input("   game over .....press enter to continue")
  
#**********************************************************************************************************************

def bird(s):
  print();print()
  r=choice(s)
  print(r)
  s=[]
  g=[]
  d=1
  e=0
  f=0
  a=randint(4,6)
  os.system('cls');print()
  print("                                              Welcome to bird's name guessing game "); print()
  print("                                u have {} attempts .....u must give right answer at least {} attempts".format(a,a-2));print()
  print();print("    HINT : the word contains  ",r[len(r)-3]);print()
  while a>0:
     z=input("    guess {} alphabet : ".format(d))
     x=z.lower()
     d+=1
     a-=1  
     if x in r:
          print("    yes.....guessed alphabet is in the word");print()
          s.append(x)
          e+=1
     else:
          print("    no....guessed alphabet is not in the word");print()
          g.append(x)
          f+=1
  
  print();print()
  print("    all attempts over ");print()
  time.sleep(2)
  print("    calculating result ........")  
  time.sleep(2)
  print()  
  if e>f:  
       print("    u win ...u gave {} right answer{}  and {} wrong answer{}...right answer is  {}".format(e,s,f,g,r))
  elif e==f:
       print("    tie...u gave {} right answer{}  and {} wrong answer{}...right answer is  {}".format(e,s,f,g,r))
  else:
       print("    u loose...u gave {} right answer{}  but {} wrong answer{}...right answer is  {}".format(e,s,f,g,r)) 
 
  print()
  time.sleep(3)
  z12=input("   game over .....press enter to continue")
#********************************************************************************************************************

def monument(s):
  print();print()
  r=choice(s)
  print(r)
  s=[]
  g=[]
  d=1
  e=0
  f=0
  a=randint(4,6)
  os.system('cls');print()
  print("                                              Welcome to monument's name guessing game "); print()
  print("                                u have {} attempts .....u must give right answer at least {} attempts".format(a,a-2));print()
  print();print("    HINT : the word contains  ",r[len(r)-3]);print()
  while a>0:
     z=input("    guess {} alphabet : ".format(d))
     x=z.lower()
     d+=1
     a-=1  
     if x in r:
          print("    yes.....guessed alphabet is in the word");print()
          s.append(x)
          e+=1
     else:
          print("    no....guessed alphabet is not in the word");print()
          g.append(x)
          f+=1
  
  print();print()
  print("    all attempts over ");print()
  time.sleep(2)
  print("    calculating result ........")  
  time.sleep(2)
  print()  
  if e>f:  
       print("    u win ...u gave {} right answer{}  and {} wrong answer{}...right answer is  {}".format(e,s,f,g,r))
  elif e==f:
       print("    tie...u gave {} right answer{}  and {} wrong answer{}...right answer is  {}".format(e,s,f,g,r))
  else:
       print("    u loose...u gave {} right answer{}  but {} wrong answer{}...right answer is  {}".format(e,s,f,g,r)) 

  print()
  time.sleep(3)
  z12=input("   game over .....press enter to continue")
  
#****************************************************************************************************************

while(True):
 os.system('cls')
 print()
 print("                               ******************* hangman game **********************");print()
 print("           Hangman is basically a word guessing game, In this game u have to guess a random word generated by computer")
 print();print();print()


 print("   press 1. for color guessing game")
 print("   press 2. for animal guessing game")
 print("   press 3. for car guessing game")
 print("   press 4. for bird guessing game")
 print("   press 5. for monuments guessing name")
 print("   press 6. exit")
 print();print()
 c=0
 try:
  c=int(input("   enter ur choice : ")) 
 except ValueError:
  print() 
  print("   plz enter the choices given above  ")

 if c==1:
   l=['white','pink','orange','green','black','silver','golden','saffron','purple','blue' ,'yellow']
   color(l)

 elif c==2:
   l=['tiger','lion','dog','cat','elephant','rhinoceros','girafe','cow','buffalo','pig']
   animal(l)

 elif c==3:
   l=['mercedes','lamborghini','audi','bmw','land lover','range rover','alto','swift desire','waganar','bolero','scorpio']
   car(l)

 elif c==4:
   l=['parrot','peacock','pegion','humming bird','sparrow','crow','cuckoo','kiwi','ostrich']
   bird(l)  

 elif c==5:
   l=['red fort','taj mahal','qutub minar','hawa mahal','char minar','golden temple']
   monument(l)  

 elif c==6:
    print("   thanks for playing......closing the game")
    time.sleep(2)
    exit(0)
 else:
    print()
    print("   invalid choice .....please enter valid choice ")
    time.sleep(2)
  