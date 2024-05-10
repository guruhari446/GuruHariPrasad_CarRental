import unittest
from dao.Implement import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.Implement=Implement()
    def test1(self):
        print("enter invalid credentials customerid=103 and password=123 ")
        result=self.Implement.GetCustomerById(103)
        self.assertEqual("True",str(result))  # add assertion here
    def test2(self):
        print("enter the customerinformation to update")
        result=self.Implement.UpdateCustomer(101, 'krishna', 'menon', 'krishna@123', '9812084523', 'kurnool', 'krishna12', 'menon123',240624)
        self.assertEqual("True",str(result))

    def test3(self):
        print("enter to add new vehicle")
        result=self.Implement.AddVehicle(3,'Indika','Maruti',2018,'white',12082,'yes',450)
        self.assertEqual("True",str(result))

    def test4(self):
        print("enter to update Vehicle")
        result=self.Implement.UpdateVehicle(3,'Indika','Maruti',2018,'Red',12082,'yes',450)
        self.assertEqual("True",str(result))

    def test5(self):
        print("list of available vehicle")
        result=self.Implement.GetAvailableVehicle(1)
        self.assertEqual("True",str(result))

    def test6(self):
        print("list of all vehicle")
        result=self.Implement.GetVehicleById(1)
        self.assertEqual("True",str(result))

if __name__ == '__main__':
    unittest.main()
