# TraderPlusBankingConfig.json

Owner: Dmitri Medeleiv

## Summary:

---

TraderPlus banking database is stored in your *Server*\profiles\TraderPlus\TraderPlusBankDatabase\folder. This is where you can view stored information for players on your server. 

```json
{
  "Version": "2.3",
  "BankingLogs": 1,
  "IsCreditCarNeededForTransaction": 1,
  "TransactionFees": 0.023,
  "DefaultStartCurrency": 500,
  "DefaultMaxCurrency": 100000,
  "CurrenciesAccepted": [],
  "TheAmountHasBeenTransferedToTheAccount": "The Amount has been successfully send to the account of destination !"
}
```

## Location:

---

As with other bank systems, you’re able to get access to each player’s bank account file. These files are saved inside TraderPlus\TraderPlusBankDatabase\.

Each file starts by Account_ followed by the SteamID64 of the player.

```json
{
    "Version": "2.3",
    "SteamID64": "76561198002429591",
    "Name": "Biffdit",
    "MoneyAmount": 0,
    "MaxAmount": 100000,
    "Licences": [
        "Military ID Card",
        "Hunter ID Card",
        "Building Permit ID"
    ],
    "Insurances": {}
}
```

### “Version”:

Notated version of the config that is updated by Dmitri when necessary.

### “SteamID64”:

SteamID of the player.

### “Name”:

In-game name of the player

### **“MoneyAmount”**:

Amount of money stored.

### **“MaxAmount”:**

Maximum amount of money that this player can store.

<aside>
📢 Max currency must be an int variable. DayZ is built on 32-bit architecture, meaning the max amount you can enter is 2147483647.

</aside>

### **“Licences”**:

String array that contains all the licenses owned by the player.

You can add licenses directly into a players database if you don’t want to set it up to be purchased at a trader. 

### **“Insurances”**:

Listed insurances held by the player. 

*You can read more about insurances here [TraderPlusInsuranceConfig.json](TraderPlusInsuranceConfig%20json%202a8e56b87f5943ecae07333669df3394.md)* 

[Bank System](TraderPlusBankingConfig%20json%206d6e28a44e8940bba0d413665f8fdfbc/Bank%20System%20020b28eb9605467ea43bd1a228aef2b4.md)