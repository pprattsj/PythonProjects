#import sys
#sys.path.append('C:\\users\\owners\\documents')
#import house


#import os
#import sys 
import math
import random as rand
#import json as j
#from collections import defaultdict as defdic

class House:

  def __init__(self,roomcount=25,floorcount=2):
    roomrow = int(math.sqrt(roomcount))
    roomcol = int(roomcount/roomrow)
    self.roomcount= [roomrow,roomcol,floorcount]
    self.keys = ['Entry', 'Hallway','Living Room','Library', 'Dinning Room', 'Kitchen', 'Pantry', 'Bedroom','Bathroom','Ballroom','Game Rooom', 'Trophy Room', 'Nursery', 'Gun Room', 'Pool', 'Patio','Exit']
    self.rooms=[]
    for k in range(0,floorcount):
     #for j in range(1,roomcol):
      for i in range(0,roomrow):
       self.rooms.append(rand.choices(self.keys,weights=(1,5,1,5,1,1,1,6,8,2,3,3,3,2,1,1,1),k=roomcol))

  def draw(self):
    pass

  def display(self):
    for k in range(0,self.roomcount[2]): 
     print('Floor',k)
     for j in range(0,self.roomcount[0]):
      print(j,j+((self.roomcount[1])*k), self.rooms[j+((self.roomcount[1])*k)] )
    print('\n OR\n\n')

    for k,r in enumerate(self.rooms):
     if (k%self.roomcount[1] ==0):
      print('  next floor')
     print(k,r)

#print("Testing with GothHouse")
#gothhouse= House(roomcount=8,floorcount=1)
#gothhouse.display()
#print(gothhouse.roomcount)
#del gothhouse
#print("GothHouse passed and deleted")
#    print(gothhouse.keys)
#    for r in range(1,gothhouse.roomcount[1])
#     print(gothhouse.rooms[r])
