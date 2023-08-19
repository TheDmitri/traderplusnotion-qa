# TraderPlusGarageConfig.json

Owner: Dmitri Medeleiv

# Summary:

---

The garage system is pretty like what you may have seen already in the modding community. It allows users to store vehicles into an external database to “protect” the vehicle from the server environment such as raiding, server database wipe, DayZ bugs and mainly to improve server performances. And then, when the user wants it, to get back the car in a parking location near the garage npc. This garage system **is for now compatible with TraderPlus CarLock, Trader keys and MuchCarKey.**

Now that we know how the garage system works, let’s talk about how to set it up.In your TraderPlusConfig folder, you should find a new config folder called:-**TraderPlusGarageConfig.json**

## Files explanations:

### **"UseGarageOnlyToTrade": (default is 0)**

This Boolean specifies if the Garage can be used to Store Vehicles or only to be used to Sell Vehicles
1 = Vehicles only stay in the Garage for as long as is specified within the ‘SavedVehicleInGarageForTradeInHour' setting
0 = The setting in ‘SavedVehicleInGarageForTradeInHour’ is ignored and Vehicles will stay in the Garage until sold or retrieved

### **"SavedVehicleInGarageForTradeInHour": (default is 1)**

This value specifies, in hours, how long the Vehicles will stay in the Garage if the setting ‘UseGarageOnlyToTrade’ is set to 1

### **"VehicleMustHaveLock":**

That Boolean allow you to define if you want to be able to store vehicle without the need of locking the vehicle by any mods compatible with this system (TP, Trader, MCK)

### **"SaveVehicleCargo":**

That Boolean allows you to define if you want to be able to store items that are in the vehicle cargo. ***Keep in mind that vehicle cargo is saved in the json database***. 

<aside>
📖 Please refer to the [Garage - FAQ](TraderPlusGarageConfig%20json%2069e491d7eeb644049c1adc3e30b1030d/Garage%20-%20FAQ%20f30358393f934cfa9aac58d8aca6b47b.md) for more details on this.

</aside>

### **"SaveVehicleHealth":**

That Boolean allows you to define if you want to be able to save the vehicle health’s state.

### **"SaveVehicleFuel":**

That Boolean allows you to define if you want to be able to save the vehicle fuel’s level.

### **"MaxVehicleStored": (default is 5)**

Maximum number of Vehicles each player can store in the Garage

### **"ParkInCost":**

That integer variable allows you to define the amount of money needed to store the vehicle. Keep in mind, the money used is the same as the money set up for the bank ATM.

### **"ParkOutCost":**

That integer variable allows you to define the amount of money needed to get the vehicle. Keep in mind, the money used is the same as the money set up for the bank ATM.

### **“PayWithBankAccount”:**

That Boolean allows you to define if you want to be able to use a bank account to pay for garage fees instead of real money.

### **"WhitelistedObjects":**

That string array allows you to define objects that can be bypassed if detected in the parking spot.

### **"NPCs":**

That class array allows you to define each Garage NPC location and parking spot.**"ClassName":** Set the object that will be used as an NPC. It can be a static object of a survivor.

### **"Position":**

Vector position of the npc

### **"Orientation":**

Vector orientation of the npc

### **"ParkingPosition":**

Vector position of the parking spot of the npc

### **"ParkingOrientation":**

Vector orientation of the parking spot of the npc

### **"Clothes":**

String array of class name that a survivor can have to be dressed

# Further Reading on TraderPlus Garage

[Garage Database](TraderPlusGarageConfig%20json%2069e491d7eeb644049c1adc3e30b1030d/Garage%20Database%20dc265b51fc7c44549eb9a01446148c05.md)

[Garage - FAQ](TraderPlusGarageConfig%20json%2069e491d7eeb644049c1adc3e30b1030d/Garage%20-%20FAQ%20f30358393f934cfa9aac58d8aca6b47b.md)

[TraderPlus CarLock](TraderPlusGarageConfig%20json%2069e491d7eeb644049c1adc3e30b1030d/TraderPlus%20CarLock%2034493322d95f4a858ec362035d5de1dc.md)

### TraderPlus Receipts

[https://www.youtube.com/watch?v=0L8bYWo3T0U](https://www.youtube.com/watch?v=0L8bYWo3T0U)

## Summary:

---

Receipts are piece of paper containing all your vehicle’s information. 

This includes:

- The vehicle’s health
- The vehicle’s attachment
- The vehicle’s cargo

The receipt can be used to:

- Provide as proof of ownership to a trader when selling the vehicle.
- Storing your vehicle to protect it from damage or being stolen.

### How can I pack a vehicle into a receipt ?

In order to pack a vehicle you must have a TraderPlusWrench in your hand and satisfy the following condition:

---

- The vehicle must have a CarLock attached ( if CarLock is not disabled)
    
    OR the vehicle must have a key assigned and be unlock (MCK, Trader, ExpansionKey)
    
- You should be in the safe zone (if IsReceiptTraderOnly is set to 1)
- The cargo of the vehicle must be empty (if SaveVehicleCargo is set to 0)

## How can I deploy a car once it’s a receipt ?

---

**Keep in mind you can only deploy a receipt in a safe zone if IsReceiptTraderOnly is set to 1.**

The vehicle can be either deployed by placing the hologram on the position and orientation of your choosing

**OR**

You can throw the receipt (*yes, you’re right, fucking Dmitri is telling you to throw it like a PokeBall*) and it will deploy the car when it reach the ground. Make sure the area where you are placing it is clear.

(There are script securities to make sure that we can’t deploy a car on a player or on a roof)