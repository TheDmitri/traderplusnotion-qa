# TraderPlusGeneralConfig.json

Owner: Dmitri Medeleiv

## Summary:

---

The general config allows to set npc positions and enable/disable features included in the mod

## File explanation:

---

So once you’ve opened the file, you’ll see something that contains:

- Toggle to open the example config.
    
    ```json
    {
    "Version": "2.3",
    "ConvertTraderConfigToTraderPlus": 0,
    "ConvertTraderConfigToTraderPlusWithStockBasedOnCE": 0,
    "UseGarageToTradeCar": 1,
    "DisableHeightFailSafeForReceiptDeployment": 0,
    "HideInsuranceBtn": 0,
    "HideGarageBtn": 0,
    "HideLicenceBtn": 0,
    "EnableShowAllPrices": 1,
    "EnableShowAllCheckBox": 1,
    "IsReceiptTraderOnly": 1,
    "IsReceiptSaveLock": 0,
    "IsReceiptSaveAttachment": 0,
    "IsReceiptSaveCargo": 0,
    "LockPickChance": 0.05000000074505806,
    "LicenceKeyWord": "ID",
    "Licences": [
    "Military ID Card",
    "Hunter ID Card",
    "Building Permit ID"
    ],
    "AcceptedStates": {
    "AcceptWorn": 1,
    "AcceptDamaged": 1,
    "AcceptBadlyDamaged": 1
    },
    "StoreOnlyToPristineState": 0,
    "Currencies": [
    { "ClassName": "TraderPlus_Bitcoin", "Value": 15000},
    { "ClassName": "TraderPlus_Money_Dollar100", "Value": 100 },
    { "ClassName": "TraderPlus_Money_Dollar50", "Value": 50 },
    { "ClassName": "TraderPlus_Money_Dollar20", "Value": 20 },
    { "ClassName": "TraderPlus_Money_Dollar10", "Value": 10 },
    { "ClassName": "TraderPlus_Money_Dollar5", "Value": 5 },
    { "ClassName": "TraderPlus_Money_Dollar1", "Value": 1 }
    ],
    "Traders": [
    {"_comment": "Hazelands ATM",
    "Id": -2,
    "Name": "TraderPlus_BANK_ATM",
    "GivenName": "ChaChing",
    "Role": "ATM",
    "Position": [4390.802734375, 9.600011825561523, 3197.518310546875],
    "Orientation": [115, 0, 0],
    "Clothes": []
    },
    {"_comment": "Hazelands Medical",
    "Id": 0,
    "Name": "SurvivorF_Judy",
    "GivenName": "Jaycee Parks",
    "Role": "Medical Supplier",
    "Position": [4389.14, 9.67108, 3241.47],
    "Orientation": [180, 0, 0],
    "Clothes": [
    "DisinfectantSpray",
    "ThinFramesGlasses",
    "MedicalScrubsHat_Blue",
    "LabCoat",
    "MedicalScrubsShirt_White",
    "MedicalScrubsPants_Blue",
    "Sneakers_White"
    ]
    },
    {"_comment": "Hazelands Grocery",
    "Id": 1,
    "Name": "SurvivorF_Linda",
    "GivenName": "Paige Lane",
    "Role": "Food Trader",
    "Position": [4428.44, 9.60386, 3182.76],
    "Orientation": [30, 0, 0],
    "Clothes": [
    "KitchenKnife",
    "SurgicalGloves_White",
    "Sweater_Green",
    "MedicalScrubsHat_White",
    "Jeans_Black",
    "JoggingShoes_Black"
    ]
    },
    {"_comment": "Hazelands Gardener",
    "Id": 12,
    "Name": "SurvivorF_Eva",
    "GivenName": "Julie Lawson",
    "Role": "Hazelands Gardener",
    "Position": [4387.95, 9.71076, 3165.8],
    "Orientation": [335, 0, 0],
    "Clothes": [
    "Tomato",
    "Bandana_Polkapattern",
    "Sweater_Green",
    "WorkingGloves_Beige",
    "Jeans_BlueDark",
    "HikingBootsLow_Grey"
    ]
    },
    {"_comment": "Hazelands Weaponry",
    "Id": 2,
    "Name": "SurvivorM_Seth",
    "GivenName": "Matthias Porter",
    "Role": "Weapon Trader",
    "Position": [4369.91, 9.60831, 3161.12],
    "Orientation": [5, 0, 0],
    "Clothes": [
    "M4A1",
    "M4_RISHndgrd",
    "Universallight",
    "M4_OEBttstck",
    "Mag_CMAG_20Rnd",
    "M68Optic",
    "MilitaryBeret_UN",
    "TacticalGloves_Black",
    "M65Jacket_Olive",
    "PlateCarrierVest",
    "Jeans_Black",
    "CombatBoots_Black"
    ]
    },
    {"_comment": "Hazelands Ammo & Accessories",
    "Id": 3,
    "Name": "SurvivorF_Gabi",
    "GivenName": "Lucy Jalalyan",
    "Role": "Weapon Accessories",
    "Position": [4374.628418, 9.58783, 3175.716309],
    "Orientation": [85, 0, 0],
    "Clothes": [
    "Mag_STANAG_30Rnd",
    "BaseballCap_Camo",
    "BDUJacket",
    "UKAssVest_Black",
    "CargoPants_Beige",
    "WorkingBoots_Yellow",
    "HuntingBag"
    ]
    },
    {"_comment": "Hazelands Clothes",
    "Id": 4,
    "Name": "SurvivorF_Frida",
    "GivenName": "Nina Bozhko",
    "Role": "Clothes Trader",
    "Position": [4386.325195, 9.5, 3189.863525],
    "Orientation": [270, 0, 0],
    "Clothes": [
    "ThinFramesGlasses",
    "ZmijovkaCap_Red",
    "QuiltedJacket_Yellow",
    "Jeans_Black",
    "Sneakers_Red"
    ]
    },
    {"_comment": "Hazelands Tool & Auto",
    "Id": 5,
    "Name": "SurvivorM_Jose",
    "GivenName": "Jorge Posada",
    "Role": "Tool Trader",
    "Position": [4364.94140625, 9.684199333190918, 3179.944091796875],
    "Orientation": [20, 0, 0],
    "Clothes": [
    "Wrench",
    "WorkingGloves_Brown",
    "BeanieHat_Brown",
    "JumpsuitJacket_Gray",
    "JumpsuitPants_Grey",
    "Sneakers_Black"
    ]
    }
    ],
    "TraderObjects": []
    }
    ```
    

### **"ConvertTraderConfigToTraderPlus":**

Boolean variable that allows you to convert Dr.Jones TraderConfig.txt and TraderVehiclesParts.txt to TraderPlusPriceConfig.json, TraderPlusIDsConfig.json and TraderPlusVehiclesParts. 

### **"** **ConvertTraderConfigToTraderPlusWithStockBasedOnCE ":**

Boolean variable that you to decide if the price config from Dr.Jones TraderConfig.txt  must be converted with stock defined from each item’s nominal value in your server types.xml or if the price config must have all product with infinite stock. 

<aside>
💭 Check the part [How to convert trader to TraderPlus config](Dr%20Jones%20Trader%20Conversion%20b35b8c7ac2dc4e42a5f98e3252eb6787.md) if you need to do so.

</aside>

### **"DisableHeightFailSafeForReceiptDeployment":**

Boolean variable that disables the failsafe to avoid cars to be deployed on roof and stuff. Useful for custom maps. Set to 1 to disable, 0 to enable.

### **"UseGarageToTradeCar":**

Boolean variable that allows you to get your cars directly in your garage if enabled. If not, the cars are given as a receipt to unpack later.

### **“EnableShowAllCheckBox”:**

- Boolean variable that allows you to hide the SHOW ALL check box if you don’t want your players to be able to see goods not available in stock.
    - 1 to enable (Show) , 0 to disable (Hide).

### "IsReceiptTraderOnly": ****

Boolean variable that allows you to define if you want the receipt system for the car to work in the entire map or only inside a trading area/safe zone.

### **"LockPickChance":**

Define the chance value of successful lock picking a car if using the car lock system in TraderPlus.

### **"LicenceKeyWord"**:

String variable that controls the licence system. 

> Because all of you have your own language, you also have your own word to say “Licence”. You need to define the word “Licence’ in your own language. This keyword is required in every license you define. If you don’t, licenses cannot be recognized by the mod.
> 
> 
> Other Words for Licence: 
> 
> License, Permit, ID, Certificate, Voucher, Credential. 
> 

### **"Licences”:**

Add licenses you want to use on your server. Keep in mind that as mentioned above, it must contain the keyword.

**Example:**

```json
"LicenceKeyWord": "License",
"Licences": [
    "Military License",
    "Hunter License",
    "Fishermans License",
    "Drivers License",
    "Pilots License"
  ],
```

As you can see, all the licenses contain the keyword “ID”.

At this point you probably want to know how to link it to traders and how to allow players to buy the licenses. So don’t forget to check **[TraderPlusIDsConfig.json**](TraderPlusIDsConfig%20json%20f208ea4128d149b6a1b7b4fca27f871b.md) for linking it to traders id.

To allow players to buy licenses, check **[TraderPlusPriceConfig.json](TraderPlusPriceConfig%20json%20bafb5261d89349f1ac68f82e53eb3b46.md)**

### **"StoreOnlyToPristineState":**

Boolean variable that allows you to sell items no matter the state and store it only as pristine. Set it to 1 to enable, set it to 0 to disable.

*ex. Sell damaged item to trader and buy back as pristine.*

```json
"AcceptedStates": {
"AcceptWorn":  1, //boolean var that allows you to decide if you want to accept an item in such condition to be traded. 0: disable ; 1: enable
"AcceptDamaged": 0, //same as above
"AcceptBadlyDamaged": 0 //same as above
}
```

### **"Currencies":**

Array of string integers that allows you to control what currency you want to use for the mod. 

> Value must be integer, 1.0 or above. *Cannot be float, ex. 0.99 or lower.*
> 

**Example: I want to add Lat_25 as a currency:**

25 is between 20 and 50 so I’ll add a line between those two options. 

```json
{"ClassName": "Classname_Currency", "Value": 0 }
```

```json
{"ClassName":    "TraderPlus_Money_Dollar50,TraderPlus_Money_Euro50,TraderPlus_Money_Ruble50 ",
		"Value": 50
},
{"ClassName": "Lat_25",
		"Value": 25
},
{"ClassName": "TraderPlus_Money_Dollar20,TraderPlus_Money_Euro20",
		"Value": 20
},
```

Here you can find more currency types. 

[Currencies](TraderPlusBankingConfig%20json%206d6e28a44e8940bba0d413665f8fdfbc/Bank%20System%20020b28eb9605467ea43bd1a228aef2b4/Currencies%20a349ab84d47d4cf6a58366a6f1f5aa95.md)

Now that you understand how to add a currency value that wasn’t already set, let’s check how to add a currency that already is set. I like having multiple currencies so I can either pay with Dollars ,Euros or Rubles. I want to add Lat_50 to the already existing currency. I just have to add to the string Lat_50 as so:

```json
"TraderPlus_Money_Dollar50,TraderPlus_Money_Euro50,TraderPlus_Money_Ruble50,**Lat_50"**,
```

Keep in mind that the **first currency set in each string is the primary currency.** This is the currency the trader will return to you as change when purchasing items.

## **"Traders":**

## ATM Trader

This variable is the traders array. That’s where you’re gonna set up where and what spawn as a trader in the map. You can either set an Object NPC (a sign for example) or a real character model like SurvivorM_Peter. Below is a working example of an ATM.

```json
		{ "_comment": "Example ATM",
			"Id": -2,
      "Name": "TraderPlus_BANK_ATM",
      "GivenName": "ATM",
      "Role": "ATM",
      "Position": [11623.0, 57.90999984741211, 14676.0],
      "Orientation": [-37.0, 0.0, 0.0],
      "Clothes": []
    }
```

## Normal Trader

Below is a working example of one trader who sells Medical Supplies under the Id 0.

```json
{     "_comment": "Medical",
      "Id": 0,
      "Name": "SurvivorM_Peter",
      "GivenName": "Peter Parker",
      "Role": "Medical Supplier",
      "Position": [4389.14, 9.67108, 3241.47],
      "Orientation": [180, 0, 0],
      "Clothes": [
        "DisinfectantSpray",
        "ThinFramesGlasses",
        "MedicalScrubsHat_Blue",
        "LabCoat",
        "MedicalScrubsShirt_White",
        "MedicalScrubsPants_Blue",
        "Sneakers_White"
      ]
    },
```

### **"Id":**

That id will represent what the npc is selling. Check out TraderPlusIDsConfig.json to get the id value.

> *“Hey Dmitri, can I have different trader with same Id ?”: Yes you can, it will mean they will all share the same stock.*
> 

How to know the id value, you need to open the [TraderPlusIdsConfig.json.](TraderPlusIDsConfig%20json%20f208ea4128d149b6a1b7b4fca27f871b.md)

Once you know what the trader should be selling, you need to define it’s classname:

### **"Name":**

```json
"Name": "SurvivorM_Peter",
```

String variable that corresponds to the classname of the entity you want to use as trader, can be a static object or survivor.  You can find a list of all survivor names and their faces here. [Character Models / Names](https://dayzland.ru/vip-persona.html)

(I*f you’ve got a special static object you want to use, make sure that static object extends BuildingBase*)

<aside>
💡 “*All right Dmitri, but how do I make my static object extend from BuildingBase ? I’m a noob in scripting :/.”*

[How to make static object works with TraderPlus ?](TraderPlusGeneralConfig%20json%20eef7f811207c48aca418cffd41121735/How%20to%20make%20static%20object%20works%20with%20TraderPlus%20d913e762a02844e0a3d6a555cd4e7509.md)

</aside>

### **"GivenName":**

```json
"GivenName": "Peter Parker",
```

String variable that corresponds to the name shown in the trader UI.**"Role":** string var that correspond to the role shown in the trader UIYou can put Weapon Trader, Car Trader, whatever you want.

### **"Position":**

```json
"Position": [4389.14, 9.67108, 3241.47],
```

Vector variable that corresponds to the position in the map of the trader. (Can be obtained with [DayZ Editor](https://steamcommunity.com/sharedfiles/filedetails/?id=2250764298&searchtext=DayZ+Editor) or Community offline mod)

### **"Orientation":**

```json
"Orientation": [180, 0, 0],
```

Vector variable that corresponds to the orientation degree that trader should be facing in the game.  (Can be obtained with any modding tool such as DayZ Editor or Community offline mod).

- Expand for a quick reference compass rose.
    
    ![https://sandbox.dodona.be/en/activities/211107823/description/fKZMiBZiyGGv1863/media/compassrose.png](https://sandbox.dodona.be/en/activities/211107823/description/fKZMiBZiyGGv1863/media/compassrose.png)
    

### **"Clothes":**

String array that allows you to add Attachments to the trader if using a classname for base game survivor models. ex. ‘SurvivorM_Peter’

**Example:**

```json
"Clothes": [
        "DisinfectantSpray",
        "ThinFramesGlasses",
        "MedicalScrubsHat_Blue",
        "LabCoat",
        "MedicalScrubsShirt_White",
        "MedicalScrubsPants_Blue",
        "Sneakers_White"
      ]
```

<aside>
❗ *Never **add a comma at the last element in the array,** in addition don’t forget to use a [json validator](Useful%20Tools%20&%20Resources%20bdc17538c1bc4645a7695ea5ae284095.md) if something doesn’t work.*

</aside>

### **"TraderObjects":**

array <string, vector, vector> var that allows you to add a custom object to spawn with the trader.

### **ObjectName":**

String variable of the classname of the object you want to spawn

### **"Position":**

Vector variable that corresponds to the position in the map of the object.(Can be obtained with any modding tool such as DayZ Editor or Community offline mod)

### **"Orientation":**

Vector variable that corresponds to the orientation in the map of the object.

> **How can I see products not available in stock ?**
> 

In [TraderPlusGeneralConfig.json](TraderPlusGeneralConfig%20json%20eef7f811207c48aca418cffd41121735.md), there is a variable called:

### **“EnableShowAllCheckBox”,**

Boolean variable to allow the player to toggle the checkbox in order to see items not in stock, but listed in the [TraderPlusPriceConfig.json](TraderPlusPriceConfig%20json%20bafb5261d89349f1ac68f82e53eb3b46.md)

Now we’re done explaining the TraderPlusGeneralConfig.json, let’s move on to: [TraderPlusPriceConfig.json](TraderPlusPriceConfig%20json%20bafb5261d89349f1ac68f82e53eb3b46.md)

[TraderPlus Licensing System](TraderPlusGeneralConfig%20json%20eef7f811207c48aca418cffd41121735/TraderPlus%20Licensing%20System%2068c5afe7933245afbc65c9f40b5b777d.md)