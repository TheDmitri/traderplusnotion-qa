# Frequently Asked Questions

Owner: Dmitri Medeleiv

- **How do I set something to infinite stock?**
    
    *You need to alter the MaxStock value within each item to be ‘-1’*
    
    *For example, the below has a max stock of 50 cans*
    
    ***"SodaCan_Cola,1,50,-1,500,0.25",***
    
    *The below has an infinite stock*
    
    ***"SodaCan_Cola,1,-1,-1,500,0.25",***
    
- **When I buy a magazine, it is empty, can I set them to be full when purchased?**
    
    *No you cannot, they will always be sold to you empty BUT when you buy the ammo which fits those magazines it will automatically fill those magazines before placing the ammo into other inventory spaces*
    
- **When my player buys an item, the trader takes the money, but the player doesn't get the item, what's wrong?**
    
    *These items are most likely to have an associated volume, or quantity to them, a can of drink, a piece of meat or a cooking pot as a couple of examples.*
    
    *If this is the case then you need to treat the TradeQty value for each of these items slightly differently to other items*
    
    *The value you need to change is the TradeQty value, the 4th value in the below*
    
    ***"SodaCan_Cola,1,50,1,500,0.25",***
    
    *So, only buy/sell FULL Cans (as an example)*
    
    ***"SodaCan_Cola,1,50,-1,500,0.25",***
    
    *Only buy/sell the item if you have at least 50% of that item spread between all within your inventory (2 items at 25% or more will equal 50% and be able to be sold)*
    
    ***"SodaCan_Cola,1,50,0.5,500,0.25",***
    
    *Or all of, or part of, the actual full volume (Drink cans have a maximum volume of '**300**' so you can use anything between 1 and 300 for the TradeQty, for example 150 which again equals at least 50% of a can of drink before it can be sold to the Trader)*
    
    ***"SodaCan_Cola,1,50,150,500,0.25",***
    
- **Why can’t I sell cooked meat?**
    
    *Cooked meat cannot be sold due to how it is seen by the game itself, it is a different state of an item rather than a different item itself.*
    
    *Rotten Meat cannot be sold due to it being in a ‘Ruined’ condition*
    
- **I don’t understand consumable settings, what's it all about?**
    
    *See the question below - ‘**What does the Coefficient mean and how does it work?’***
    
- **How do I add a fire barrel to the safe zone?**
    
    *You can either place the FireBarrel with Admin Tools and ensure they have a very high lifetime, or you can add the FireBarrel to the ‘TraderObjects’ Array in the TraderPlusGeneralConfig.json file*
    
    *If you need a Fire Barrel that cannot be picked up by Players use something similar to the below:-*
    
    *https://steamcommunity.com/sharedfiles/filedetails/?id=2658185718*
    
- **The price I set in the trader file isn't the exact price they are selling for, what’s wrong?**
    
    *TraderPlus is an Economy based Trader by default, the more of each item Players sell to the Trader the cheaper that item becomes to Buy from the Trader and the less money you get from the Trader for selling that same item to the Trader again - see the question below ‘**What does the Coefficient mean and how does it work?**’*
    
    *This entry will set the Sell and Buy prices according to the amount of stock of that item:-*
    
    ***"SodaCan_Cola,0.998,50,-1,500,0.25",***
    
    *This entry will keep the Buy and Sell price static at all times and also provides infinite stock of that item*
    
    ***"SodaCan_Cola,1,-1,-1,500,0.25",***
    
- **My vehicles spawn in with no doors, what did I miss?**
    
    *In the above example the only items the Ada will spawn in with are the 4 wheels, if you want your Vehicles sold with more items attached to them you need to add them to that file correctly, for example:*
    
    ```json
    {
    	"Version": "2.2",
    	"VehiclesParts": [
         {
            "VehicleName": "OffroadHatchback_Blue",
            "Height": 0,
            "VehicleParts": [
    			    "SparkPlug",
    			    "CarBattery",
    			    "CarRadiator",
    			    "HeadlightH7",
    			    "HeadlightH7",
    			    "HatchbackDoors_CoDriver",
    			    "HatchbackDoors_Driver",
    			    "HatchbackHood",
    			    "HatchbackTrunk",
    			    "HatchbackWheel",
    			    "HatchbackWheel",
    			    "HatchbackWheel",
    			    "HatchbackWheel"
            ]
        }
      ]
    }
    ```
    
- **I bought a vehicle and it spawned on my head and killed me, what the hell?**
    
    *First, test with a Vanilla Vehicle (Sarka, Ada, Olg etc) and see if it happens again.*
    
    *The most likely cause for this is the Vehicle not being in the TraderPlusVehiclesConfig.json file correctly, in the below example a Blue Ada will be sold to you as a Receipt but any other Vehicle will spawn on your head as it is not in the file*
    
    ```json
    *{*
    	"Version": "2.2",
    	"VehiclesParts": [
    	    {
    	        "VehicleName": "OffroadHatchback_Blue",
    	
    	        "Height": 0,
    	
    	        "VehicleParts": [
    	            "HatchbackWheel",
    	            "HatchbackWheel",
    	            "HatchbackWheel",
    			        "HatchbackWheel"
    	        ]
    	    }
       ]
    }
    ```
    
- **Is there a group option for banking?**
    
    *Not at the moment but check out the ‘Feature Requests’ in Trello*
    
    *[https://trello.com/invite/b/SOFdxrZ2/3b9b59373f487eff21be39867a2302a8/traderplus-bug-tracking](https://trello.com/invite/b/SOFdxrZ2/3b9b59373f487eff21be39867a2302a8/traderplus-bug-tracking)*
    
- **How do I give money to my users as fresh spawns?**
    
    *This value will only apply to NEWLY CREATED Banking Database files AFTER you have made the change to the ‘DefaultStartCurrency’ value, to apply this change to current Players, and Bank Database files, you will need to use a tool such as Notepad++ to ‘Find and Replace’*
    
- **I loaded the mod and I am on “custom_map”, the default traders are in the sky, are there other configs available?**
    
    *Check the #👏-share-your-trader-files  in Dmitris Discord Server, there are plenty of configs available for different maps*
    
- **I want the trader to have xx number of an item after restart, how do I do that?**
    
    *There is no built in option for this to happen, you will need to create a Powershell script, or similar, to update/replace your Stock files at each restart*
    
    *You need to alter the TraderPlusBankingConfig.json file and the ‘DefaultStartCurrency’ value within that file.*
    
- **I can’t get vending machines to spawn in correctly, what's wrong?**
    
    *This is most likely due to the Vending Machines not inheriting the BuildingBase{} or BuildingSuper{} class and you will need a Compatibility Mod to make them spawn in, **search the TraderPlus PDF for ‘Vending Machine’** and you will find more details*
    
    - I set the location of all my traders, but they are not where they should be, what happened?
    - **Why are my traders are naked?**
    
    *You need to ensure your Traders have ‘clothing’ attached to them in the TraderPlusGeneralConfig.json file*
    
    *The below will spawn in a naked Trader*
    
    ```json
    "Traders": [
         {
            "Id": 0,
            "Name": "SurvivorF_Irena",
            "GivenName": "Marie",
            "Role": "Food Trader",
            "Position": [
    	        3692.14599609375,
              402.09783935546877,
              6000.333984375
            ],
            "Orientation": [
    			    120.0,
    	        0.0,
    	        0.0
        ],
        "Clothes": []
       }
    ]
    
    //The below will ensure the Trader is clothed
    
    "Traders": [
         {
           "Id": 0,
           "Name": "SurvivorF_Irena",
           "GivenName": "Marie",
           "Role": "Food Trader",
           "Position": [
             3692.14599609375,
             402.09783935546877,
             6000.333984375
        ],
        "Orientation": [
    	    120.0,
    	    0.0,
    	    0.0
        ],
    "Clothes": [
            "BoxCerealCrunchin",
    		    "SurgicalGloves_White",
    		    "Bandana_Polkapattern",
    		    "MiniDress_PinkChecker",
    		    "DressShoes_White"
          ]
        }
    ]
    ```
    
- **I have a dayz wrench in hand, why can’t I pack my vehicle?**
    
    *This is likely due to 1 or more reasons*
    
    1. *You have the **‘IsReceiptTraderOnly’** set to 1 in the TraderPlusGeneralConfig.json file and you are NOT in a Safezone*
    2. *You do not have a CarLock attached to the Vehicle*
    3. *If you use MuchCarKey or Expansion Keys there could be another reason*
    - What actions are logged in the log files?
    
    *This is likely to not work as expected - "sodacan_Cola,1,-1,-1,500,0.25",*
    
    *This will work as expected - "SodaCan_Cola,1,-1,-1,500,0.25",*
    
- **I have items that are in the pricing file that do not have a picture or real name?**
    
    *This is likely due to the item Classname in the TraderPlusPriceConfig.json file not being correct. Ensure the Classname is EXACTLY as it is displayed when you go into Admin Tools in game.*
    
    *e.g. Item Classname seen in Admin Tools - SodaCan_Cola*
    
- **When I buy a modded car, it spawns underground, what do I need to change?**
    
    *Try to increase the ‘Height’ for the problem cars within the TraderPlusVehiclesConfig.json file, go up in steps of 1 or more until you find the correct height value.*
    
    *Some modded Vehicles continue to have problems.*
    
- **How can I allow players to use a CarLockPick in a Safezone?**
    
    *You cannot do this at present unless you mod this in yourself*
    
- **How can I automatically remove the stock of an item as stock is full and players cannot sell any more?**
    
    *Ensure the EnableAutoDestockAtRestart value in the TraderPlusPriceConfig.json file is set to 1 AND each item that you want to DESTOCK when full MUST have the 7th element set to the percentage*
    
    *E.g.*
    
    *"SodaCan_Cola,1,50,-1,500,0.25",    Will NOT auto destock*
    
    *"SodaCan_Cola,1,50,-1,500,0.25,0.8",  – WILL auto destock at restart when stock is full*
    
- **Can TP automatically move Traders to different locations randomly?**
    
    *No but you can do this via an external script at restart - e.g. Powershell*
    
- **I have set TP up but I cannot see any items in the Traders to buy, what have I done wrong?**
    
    *You are not viewing ‘All Stock’/only viewing items actually in stock*
    
    *Ensure the **EnableShowAllCheckBox** setting in the **TraderPlusGeneralConfig.json** file is set to 1, then select the ‘Show All’ checkbox at the top of the page when interacting with a Trader in game.*
    
- **I can sell items over and over again, I get the money but the item doesn't get removed from my inventory**
    
    *Any items that have a ‘Volume associated with them (Waterbottle, Meat Steak etc) must have either -1 (full), 0.5 (percentage full) or the actual value in volume 300 (as an example, check the code or trial and error)*
    
- **I made a change to the TP files and now I cannot see any traders/items etc, what have I done wrong?**
    
    *Ensure you run your files through a json, or xml, validator each and every time you make changes to ensure the formatting is correct ([www.jsonlint.com](http://www.jsonlint.com/) or [https://codebeautify.org/jsonvalidator](https://codebeautify.org/jsonvalidator) are good sites)*
    
- **I have increased the 'Starter Money' for players but some players are still on the original amount, what's broken?**
    
    *Starter Money only applies to players that access a Trader for the first time after you have set the amount, it is NOT retrospective*
    
- **Can I stop Zombies/Animals from spawning in, or coming into, the Safezone?**
    
    *By default Zombies and Animals will be cleaned from the zone when they target a player*
    
- **Does TP work with Expansion?**
    
    *Yes it does*
    
- **How can I add light to the Trader Area/s?**
    
    *Use a Firebarrel or another mod such as ForeverBurningFires*
    
- **How to deactivate ATM or TraderPlus Bank system ?**
    
    You simply have to not place any ATM NPC.
    
- **Do I HAVE to use the Garage and Bank or can I disable them?**
    
    *You do not HAVE to use the Garage or Bank.*
    
    *If you would rather not use them then simply do not set them up in the TraderPlusGeneralConfig.json file*
    
- **Why can I not sell Car Receipts to the Trader?**
    
    *Try to 'Place' the Car (usually twice) UNTIL you can see the hologram of the car (DO NOT ACTUALLY PLACE THE CAR).*
    
    *Once you can see the Vehicle Hologram simple place the Receipt into your inventory again and it will be sellable at the Trader*
    
- **What does the Coefficient mean and how does it work?**
    
    *This is how much the Buy Price will be MULTIPLIED by after each sale of the item to the Trader*
    
    *e.g.*
    
    ***Classname, Coefficient, MaxStock, BuyPrice, Sell Price***
    
    ***HK 416A7,       0.5,             10,              10000,         0.8***
    
    *Initial Buy Price is 10000 'rubles' with 1 item in stock.*
    
    *With two HK416A7's in stock the current Buy Price is multiplied by the coefficient of 0.5 (10000x0.5 = 5000) meaning a player can buy one from the Trader for 5000 rubles now.*
    
    *With a third HK416A7 sold to the Trader that 5000 is multiplied by the Coefficient again (5000x0.5 = 2500) so with 3 HK416A7 in stock a player will be able to buy one from the Trader for 2500 'rubles'*
    
- **How does the license work?**
    
    Licenses allow you as an admin to restrict some trader or category to players that owns a license.
    
    In the GeneralConfig, you can setup a keyword for the Licence that will allow the mod to detect Licence product and category.
    
    Then in the Licences array, you can create as many Licences as you like. keep in mind the License name must contain the keyword setup previously in order to work.
    
    Then you can either manually add the Licence of your choosing in the player bank database file. (check in the TraderPlusBankDatabase folder and look for your player steamID64)
    
    Or add your Licence in a trader category with a BuyPrice so Players can buy it.
    
    Now if you want to restrict a trader so only players that own the chosen license can open the menu, you need to add the Licence in the dedicated trader id in the variable LicenceRequired in TraderPlusIDsConfig.
    
    If you want to restrict only a category, you must name the category like your license.