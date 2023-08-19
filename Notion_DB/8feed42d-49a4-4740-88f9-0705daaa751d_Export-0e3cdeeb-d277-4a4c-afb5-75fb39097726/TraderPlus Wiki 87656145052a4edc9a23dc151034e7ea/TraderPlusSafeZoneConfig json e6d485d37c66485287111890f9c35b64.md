# TraderPlusSafeZoneConfig.json

Owner: Dmitri Medeleiv

## Summary:

This mod creates a safe zone that disables most of the actions that can happen in a trader, such as:

- Injection on target
- Disinfect on target
- Force consume on target
- Pack tent
- GiveBlood to target
- Collect blood from target
- Deploy Object
- Restrain yourself or target
- Force feed someone
- Lock doors
- Unpin grenades
- Lock pick car from MuchCarKey
- Cut Tree

In addition, zombies will be cleaned when they see a player. Animals that come to the player will also be deleted in each 20s. (the check is in the client, so don’t worry, it won’t affect server performances)

You're also able to set items that will be cleaned over time and set admins that can bypass disable action while in safe zone!

Finally, as server owner, you’ve got the possibility to place fire barrel or fireplace in the safe zone. These objects can be ignited even without their normally required ingredients. 

## Example Config

- Expand for an example of a full TraderPlusSafeZoneConfig.json
    
    ```json
    {
      "Version": "2.5",
      "IsHideOutActive": 1,
      "EnableAfkDisconnect": 0,
      "KickAfterDelay": 30,
      "MsgEnterZone": "Welcome! Don't worry, you're in our safe zone now.",
      "MsgExitZone": "Good luck, have fun and don't die! You've left our safe zone.",
      "MsgOnLeavingZone": "Heads up, safe zone expires in:",
      "MustRemoveArmband": "Please remove armbands to see your secret stash!",
      "SafeAreaLocation": [
        {
          "SafeZoneStatut": "General Trader",
          "X": 4394.00,
          "Y": 3198.12,
          "Radius": 80,
          "Countdown": 15
        },
        {
          "SafeZoneStatut": "Military Trader",
          "X": 8561.72,
          "Y": 8707.67,
          "Radius": 40,
          "Countdown": 10
        }
      ],
      "CleanUpTimer": 600,
    	"WhitelistEntities": [
    		"Doggo_Follow1",
    		"Doggo_Follow2"
    ],
      "ObjectsToDelete": ["Paper"],
      "SZSteamUIDs": [
    			"76561198047475641"],
      "BlackListedItemInStash": [
    			"TraderPlus_Bitcoin",
    			"Collectable_GPU",
    			"Collectable_IPhone"
    	]
    }
    ```
    

---

## Variables:

**"Version":**

Notated version of the config that is updated by Dmitri when necessary.

**"IsHideOutActive"**: 

Boolean variable that enables (1) or disables (0) the hideout stash while in the safe zone.

**"EnableAfkDisconnect":** 

Set to 1 to enable the afk kicker system, set to 0 otherwise. 

**"KickAfterDelay":** 

Set to whatever value in **minutes** that will be used to check if the player is afk or not. Players will be notified if position has not moved since last AFK check.

**"MsgEnterZone":**

String variable that will be displayed as a notification when a player enters the safe zone area.

**"MsgExitZone":** 

String variable that will be displayed as a notification when a player leaves the the safe zone and the countdown has finished.

**“MsgOnLeavingZone”:** 

String variable that will be displayed as a notification when a player is leaving the area during countdown.

**“MustRemoveArmband”:** 

String variable that will be displayed as a notification when a player has an armband equipped, refusing them access to their safe zone stash..

**"CleanUpTimer":** 

Time in seconds where items defined in “ObjectsToDelete”: get deleted within the safe zone.

**"WhitelistEntities":**

Array of entities to NOT delete from within the Safezones (e.g. DayZDog)

**"ObjectsToDelete":** 

Array <string> that allow you to add items that will be cleaned over time in the safe zone

**"SafeAreaLocation":**

Safe zones in TraderPlus are circle areas that originate from a central coordinate. Those coordinates are designated in the “SafeAreaLocation”: section of the config. You can use [iZurvive](https://www.izurvive.com) to find coordinates and see what settings you should use .

```json
"SafeAreaLocation": [
    {
      "SafeZoneStatut": "Hazeland Trader",
      "X": 4394.00,
      "Y": 3198.12,
      "Radius": 80,
      "Countdown": 15
    }
```

![The safe zone area of the above settings.](TraderPlusSafeZoneConfig%20json%20e6d485d37c66485287111890f9c35b64/Untitled.png)

The safe zone area of the above settings.

### “SafeZoneStatut”:

Name of safe zone. ⚠️ Each zones name much be unique. ⚠️

### “X”:

### “Y”:

Coordinates for center of the safe zone.

### **“Radius”:**

Integer value of the distance from the center of the safe zone to the perimeter.

### **“Countdown”:**

Integer value that will count down in a timer after leaving the safe zone.

### **"SZSteamUIDs":**

array<string> that allows you to add steamID64 of admins that aren’t concerned about all the blocking actions in the safe zone such as unpinning a grenade, placing an object, etc…

```json
"SZSteamUIDs": [
"76561198047475641"
]
```

### **"BlackListedItemInStash":**

String array that allows you to add items that can not be added in the personal stash. This would normally be used to keep players from stashing high value items with low nominal counts in a safe location that cannot be raided.

```json
"BlackListedItemInStash": [
"Apple",
"Plum",
"Plier"
]
```