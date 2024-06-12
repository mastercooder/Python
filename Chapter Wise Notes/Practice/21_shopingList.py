class Shoping:
    laptop = 75000
    mobile = 25000
    usb = 1000
    cloths = 10000
    
    def shopintList(self):
        print("")
        print("-------------------------------------------------------------------")
        print("")
        print("                   SHOPING LIST                                    ")
        print("                   _____________                                   ")
        print("")
        print(f"Asus Tuf Gaming Laptop (8GB / 1TB)               -          {self.laptop}")
        print(f"Realme X7 Max Mobile  (8GB / 128 GB)             -          {self.mobile}")
        print(f"USB Rubber Duckey                                -          {self.usb}")
        print(f"Cloths                                           -          {self.cloths}")
       # print(f"Tax                                              -          {self.tax}")
        print("                                                            ________")
        print(f"Total                                             -          {s.totalCost}")
        print("")
        print("-------------------------------------------------------------------")
        print("")
        
    @property    
    def totalCost(self):
        return self.laptop + self.mobile + self.usb + self.cloths
        
s = Shoping()
s.shopintList()
