from turtle import *
from casioplot import *
from random import *

hideturtle()

def wait(nb):
  for i in range(nb):
    pass

def pendu(faute):
  penup()
  if faute==1:
    goto(-175,-50)
    setheading(0)
    pendown()
    forward(70)
  elif faute==2:
    goto(-140,-50)
    pendown()
    setheading(90)
    forward(70)
  elif faute==3:
    goto(-140,20)
    pendown()
    setheading(0)
    forward(35)
  elif faute==4:
    goto(-105,20)
    pendown()
    setheading(270)
    forward(15)
  elif faute==5:
    goto(-105,5)
    pendown()
    setheading(180)
    circle(5)
  elif faute==6:
    goto(-105,-5)
    pendown()
    setheading(270)
    forward(13)        
  elif faute==7:
    goto(-105,-15)
    pendown()
    setheading(55)
    forward(13)  
  elif faute==8:
    goto(-105,-15)
    pendown()
    setheading(125)
    forward(13)
  elif faute==9:
    goto(-105,-18)
    pendown()
    setheading(325)
    forward(13)
  elif faute==10:
    goto(-105,-18)
    pendown()
    setheading(215)
    forward(13)
    return False,"L"
  return True,None

def traits(mot):
  if len(mot)>9:
    for i in range(len(mot)//9+1):
      penup()
      goto(-75,30-(20*i))
      setheading(0)
      if len(mot)-9*(i+1)>0:
        for l in range(9):  
          pendown()
          forward(20)
          penup()
          forward(10)
      else:
        for l in range(len(mot)-9*i):
          pendown()
          forward(20)
          penup()
          forward(10)
  else:
    penup()
    goto(-75,30)
    for l in range(len(mot)):
      pendown()
      forward(20)
      penup()
      forward(10)

    
def jeu():
  run_mot=True
  while run_mot:
    guess=[]
    mot_dict={}
    mot=input("Quelle mot? ")
    if len(mot)<63:
      run_mot=False
    else:
      print("mot trop long") 
  traits(mot)
  for i in mot:
    guess.append("")
    mot_dict[i.upper()]=False
  return mot,mot_dict,guess

keydict={41:"A",42:"B",43:"C",44:"D",45:"E",46:"F",51:"G",52:"H",53:"I",54:"J",55:"K",56:"L",61:"M",62:"N",63:"O",71:"P",72:"Q",73:"R",74:"S",75:"T",81:"U",82:"V",83:"W",84:"X",85:"Y",91:"Z",92:" "}

mot,mot_dict,guess = jeu()
run=True
faute=0
li=[]
guess_str=""
while run:
  key=getkey()
  if key in keydict.keys():
    li=[]
    for k,v in keydict.items():
      if k==key:
        lettre=v
    if lettre in mot.upper():
      for i in range(len(mot)):
        if lettre==mot[i].upper():
          li.append((i))
      for l in range(len(li)):
        if mot_dict[lettre]==False:
          guess[li[l]]=lettre
          if li[l]<9:
            penup()
            goto(-75+(30*li[l]),45)
            if lettre!=" ":
              write(lettre)
            else:
              write("-")
          else:
            penup()
            goto(-75+(30*(li[l]-9*(li[l]//9))),45-(20*(li[l]//9)))
            if lettre!=" ":
              write(lettre)
            else:
              write("-")
      mot_dict[lettre]=True
    else:
      faute+=1
  for i in guess:
    guess_str+=str(i)
  run,V=pendu(faute)
  if guess_str==mot.upper():
    run=False
    V="W"
  else:
    guess_str=""
  wait(9990)
  

if V=="W":
  penup()
  goto(-190,50)
  write("Bravo !")
else:
  penup()
  goto(-190,50)
  write("Perdu, le mot etait "+mot)