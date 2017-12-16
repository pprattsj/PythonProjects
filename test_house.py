import unittest
import house

class HouseTestCase(unittest.TestCase):
   """ Tests for 'House.py'. """

   def test_house_size(self):
     myhouse= house.House(roomcount=48,floorcount=2)
     self.assertEqual(len(myhouse.rooms),12)
     self.assertEqual(len(myhouse.rooms[0]),8)
     del myhouse
     myhouse = house.House()  
     self.assertEqual(len(myhouse.rooms),10)
     self.assertEqual(len(myhouse.rooms[0]),5)
     del myhouse

if __name__ == '__main__':
    unittest.main()
