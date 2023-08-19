# TraderPlusIDsConfig.json

Owner: Dmitri Medeleiv

### Summary:

Let’s take a look at the TraderPlusIDsConfig. That file is fairly easy to understand. But let’s go step by step to explain everything may need to know.

---

### Purpose:

It is used for setting up each “Id” so TraderPlus can know which items each traders are trading, licenses required by the trader and the currencies accepted by the trader.

---

## File explanations:

---

### **“Id”**:

Integer variable used to define which id it should be. Once you choose a value, you need to add this id value to each trader npc that will contain the categories setup in this id. You can use any whole integer from 0-99.

### **"Categories":**

That’s a string array where you’re going to define each category that can be traded by a trader ID**.**

Here’s an example.

I want to add the new category I’ve previously created in my [TraderPlusPriceConfig.json](TraderPlusPriceConfig%20json%20bafb5261d89349f1ac68f82e53eb3b46.md) called “Morty’s Weapons”. I’ll be adding this to my weapons trader. 

```csharp
{
	“Id”: 3,
	"Categories": [
		"Melee",
		"Sidearms",
		"Rifles",
		"Shotguns",
		"Submachine Guns",
		"Assault Rifles",
		"Sniper Rifles",
		"Grenades",
		“Morty’s Weapons”
	],
	"LicencesRequired": []
}
```

As you can see above, I’ve placed my new category at the bottom of the list of categories my trader Id 3 will show in the trader menu. 

### **"LicencesRequired":**

Text array that allows you to define a required license to use the trader.

Example below is to restrict purchase to players who previously purchased the Weapons Trader Licence.

```json
"LicencesRequired": [
“Weapons Trader Licence”
]
```

Keep in mind you need to define the licenses in **[TraderPlusGeneralConfig.json](TraderPlusGeneralConfig%20json%20eef7f811207c48aca418cffd41121735.md)** Before adding them in `“LicencesRequired”`:.

### **"CurrenciesAccepted":**

Array that allows you to restrict the currencies accepted by the trader. 

By default, the array is empty. It means the trader will accept all currencies defined in the [TraderPlusGeneralConfig.json](TraderPlusGeneralConfig%20json%20eef7f811207c48aca418cffd41121735.md) file.

Below is an example to restrict the trader to only accept USD.

```json
"CurrenciesAccepted": [
			"TraderPlus_Money_Dollar100",
			"TraderPlus_Money_Dollar50",
			"TraderPlus_Money_Dollar20",
			"TraderPlus_Money_Dollar10",
			"TraderPlus_Money_Dollar5",
			"TraderPlus_Money_Dollar1"
]
```

I recommend adding them from the highest to the lower value, but it’s not a requirement.

In this case, only the bills defined will work with this trader.

<aside>
💡  If you have prices that are under the minimal value set in the currencies accepted, i.e. .50, you won’t get the money when trading those. Make sure to round your price according to the money you want to use for that trader.

</aside>