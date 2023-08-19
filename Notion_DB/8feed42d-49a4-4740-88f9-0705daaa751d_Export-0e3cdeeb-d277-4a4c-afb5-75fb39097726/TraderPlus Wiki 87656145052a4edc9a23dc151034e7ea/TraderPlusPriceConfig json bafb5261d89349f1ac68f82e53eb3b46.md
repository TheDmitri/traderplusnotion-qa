# TraderPlusPriceConfig.json

Owner: Dmitri Medeleiv

## Summary:

This file allows server owners to control the items, stock, and manage the dynamic prices of the items in your servers economy.

---

### **"EnableAutoCalculation”:**

Boolean variable that automatically calculates the coefficient based on the stock. 

### **"EnableAutoDestockAtRestart"**:

Boolean variable that enables the de-stock feature once the stock is reached per product. *(De-stock will not happen until server restart)*

### **"EnableDefaultTraderStock"**:

Integer variable that allows each trader to re-stock during a server restart.

> **How can I make the trader restock all the products after each restart ?**
> 

You have 3 options:

- "EnableDefaultTraderStock": 0 //*no restock during a server restart.*
- "EnableDefaultTraderStock": 1 //*stock added based on the max stock value.*
- "EnableDefaultTraderStock": 2 //*stock added based on a random value between 0 and max stock value.*

## **How does the de-stock feature works ?**

---

You want to know more about the **de-stock variable**? Here is an example:

> In one of your traders, you noticed that the stock of LAR/FAL Mag is full like below:
> 
> 
> [https://lh4.googleusercontent.com/jCDFCY-j2aCk9fqkYv5Qxf-zEIrLLWABouRQF16DeTYm_7meMVOSHr5pQ4qQWK24fE0sswS8iFyU-FSPb4O5sxxkI1J0Oc3-rfuXdDi7MX0DAmlZvHsxKCbFOgZxkA_6EBHpds-8rHeyFSOBiA](https://lh4.googleusercontent.com/jCDFCY-j2aCk9fqkYv5Qxf-zEIrLLWABouRQF16DeTYm_7meMVOSHr5pQ4qQWK24fE0sswS8iFyU-FSPb4O5sxxkI1J0Oc3-rfuXdDi7MX0DAmlZvHsxKCbFOgZxkA_6EBHpds-8rHeyFSOBiA)
> 
> It means the player can’t sell any more FAL mag unless someone buys some to free some space in the stock. This is why the de-stock feature is so important for a well-balanced and free-flowing server economy. 
> 

**"EnableAutoDestockAtRestart"** 

Boolean variable that allows traders to update stock at server restart. 

> You’ll have the possibility to individually control the de-stock percentages for all items in your economy.
> 
> 
> Let’s say you want the Fal Mag stock to be reduce by 75% when the stock is full. You’ll need to add another variable at the end of the item string. 
> 
> 0.75 = 75%, variable from 0.0 → 100.0
> 
> | Classname | coefficient | maxstock | trade quantity | buy price | sell price | destock coeffcient |
> | --- | --- | --- | --- | --- | --- | --- |
> | Mag_FAL_20Rnd | 0.78 | 32 | 0 | 100 | 50 | 0.75 |
> 
> Keep in mind that if you do not use the de-stock feature, you don’t have to define a coefficient for it. This variable can be left blank.
> 

<aside>
❓ **What is the meaning of all the values for each product ?**

</aside>

Each product contains six elements that are **REQUIRED**:

| Classname | coefficient | maxstock | trade quantity | buy price | sell price |
| --- | --- | --- | --- | --- | --- |

**Classname:** classname of the product 

<aside>
⚠️ *The class name is CaseSensitive.*

- “M4A1”  → OK  /  “m4A1” → WRONG
</aside>

**Coefficient:** The variable that controls the price based on the amount of back stock the trader has.

**Max Stock:** Maximum allowed back stock a trader is allowed to have.

**Trade Quantity:** Maximum value of the item that can be traded in one transaction.

**Buy Price:** Maximum price you’ll pay at the trader. 

**Sell Price:** Maximum sell price you’ll receive when selling to the trader. 

<aside>
♾️ **How can I make a product unlimited in stock ?**

Keep in mind that you’ll be able to do one of three things with an item. 

1. Product that have dynamic price based on max stock value
2. Product that have a static price and a max stock value
3. Product that have a static price and unlimited stock (like Dr.Jones trader)
</aside>

So let’s start by trying to make a dynamic price based on max stock value

## **Make a product that have a dynamic price based on max stock value**

---

For this section, server admins have two possibilities:

1. Let the mod calculate the maxstock value based on the nominal value in your types.xml, in addition to the coefficient based on the lowest price desired when the stock is reached.
2. Configure it manually by playing with the PriceCalculator.xls. 

<aside>
💡 Let’s use an example: I want to add a Weapon form Morty’s Weapon: the HK 416A7

</aside>

| Classname | coefficient | maxstock | trade quantity | buy price | sell price |
| --- | --- | --- | --- | --- | --- |
| HK_416A7 | 0.4 | -1 | 1 | 10000 | 0.8 |

So let’s try to understand what I set.

- ~~I want the HK to have a **maxstock** based on the nominal value so I put -2. (don’t try to understand that, just put -2)~~
    
    <aside>
    ❗ This feature is currently disabled.
    
    </aside>
    
- I want the lowest price for the HK to be 40% of the buy price. (buy price is always the highest price when the stock is low), so I put 0.4 (= 40%) in the **coefficient**.
- I set to 1 the **trade quantity** because it’s a gun and that’s actually the max quantity I can set. (You can’t put a tradeqty bigger than the max qty of the item or superior to the max count for ammunition => 20 for 7.62x39mm)You can also set tradeqty to -1 if you want it to be max qty of the item or to a coefficient such as 0.75; that means you can trade if the product has at least 75% of quantity.
- I set the **buyprice** to 10000 as the highest price.
- I set the **sellprice** to 0.8. That means it will be equal to 80% of the buy price. You can also put a number such as 8000 or 7500 or whatever. The two are possible.

<aside>
💡 To disable the ability to buy, you can set buy price it to -1.
To disable the ability to sell, you can set sell price it to -1.
Keep in mind that a *buy or sell* price below 8 cannot be dynamic.

</aside>

Once done, I can either config a new product or make the auto calculation happen.

To force an autocalculation, follow these steps.

**Step 1:** There is a variable called **"EnableAutoCalculation":** in the [TraderPlusPriceConfig.json](TraderPlusPriceConfig%20json%20bafb5261d89349f1ac68f82e53eb3b46.md). You would need to set it to 1.

**Step 2:** Start your server and wait for it to boot completely. Once the price config has been modified you can stop your server.

**Step 3:** Disable the **"EnableAutoCalculation" with 0.**

**Step 4:** Check out the line you added and normally you should see that it has changed 😉

Now, if you want to set your product with a custom stock and a custom coefficient then you can open and run the TraderPlusCoefficientCalc.xlsx located below.

[TraderPlusCoefficientCalc.xlsx](TraderPlusPriceConfig%20json%20bafb5261d89349f1ac68f82e53eb3b46/TraderPlusCoefficientCalc.xlsx)

[Coefficient Calculator](TraderPlusPriceConfig%20json%20bafb5261d89349f1ac68f82e53eb3b46/Coefficient%20Calculator%2062960e874bfc4c81913cfb6cccb1f633.csv)

Once open, you’ll be able to set it up to your product values and put your own max stock and your own coefficient ( between 0.0 and 0.99999999), I suggest to start with 0.993 and increase with a step of 0.001 to get an interesting result.

Once done, you’ll have three more variables called

You can define a potential stock and get the buy price and sell price when the stock is equal to said potential.

Once you're satisfied, put the chosen value into your [TraderPlusPriceConfig.json](TraderPlusPriceConfig%20json%20bafb5261d89349f1ac68f82e53eb3b46.md), start your server and enjoy !

## **Make a product that have a static price with a max stock value**

---

Let’s reuse our previous example with the the HK 416A7, but with new variables in our table.

| Classname | coefficient | maxstock | trade quantity | buy price | sell price |
| --- | --- | --- | --- | --- | --- |
| HK_416A7 | 1 | 10 | 1 | 10000 | 0.8 |

As you can see, the coefficient is set to 1, that way the price will always be buy price (10000) and sell price (0.8*10000 = 8000). 

<aside>
💭 ~~You can define the stock based on your nominal value, you can either do a. and then put a coefficient equal to 1 or go directly to your types and look for nominal value.~~

❗**This feature is currently disabled!**❗

</aside>

**How can I make a product with unlimited stock ?**

Let’s once again use our previous example, but with variables that would reflect unlimited stock.

| Classname | coefficient | maxstock | trade quantity | buy price | sell price |
| --- | --- | --- | --- | --- | --- |
| HK_416A7 | 1 | -1 | 1 | 10000 | 0.8 |

It’s simple to have unlimited stock: **maxstock = -1**

<aside>
➡️ For more about [Trade Quantity](TraderPlusPriceConfig%20json%20bafb5261d89349f1ac68f82e53eb3b46/Trade%20Quantity%20dd3fdd4f6191440c9c0df4d6ed31685e.md), click this link.

</aside>

## **How to allow player to buy a license**

---

If you’re using the license system, you’re probably wondering how to allow players to buy licenses. 

Few Notes: 

- Licenses are not physical items and will not appear in your inventory.
    - They are added to your bank account file and stored on the server database. Only server admins can access that file.
- Licenses cannot be sold once purchased.

**Example:**

```json
{ "CategoryName": "License",
      "Products": [
        "Building Permit ID,0.92,-1,1,1000,-1,1",
        "Drivers ID Card,0.92,-1,1,5000,-1,1",
        "Fishermans ID Card,0.92,-1,1,3000,-1,1",
        "Hunter ID Card,0.92,-1,1,6000,-1,1",
        "KR_BankingCard,0.92,-1,1,100,-1,1",
        "Military ID Card,0.92,-1,1,12000,-1,1",
        "Pilots ID Card,0.92,-1,1,10000,-1,1"
      ]
    },
```

| Classname | coefficient | maxstock | trade quantity | buy price | sell price |
| --- | --- | --- | --- | --- | --- |
| Building Permit ID | 0.92 | -1 | 1 | 1000 | -1 |

> *“Hey Dmitri, I get that, but I would like to restrain the ability to give a license to only specific players, how do I do that ?”*
> 

<aside>
💡 For that, dear user, you’ll have to directly add the license to the player bank account file located in the **TraderPlusBankDatabase** folder.

</aside>

- You open the file of the player based on his steamID64. Once you find it, you open it and add it like this:
Expand:
    
    [https://lh4.googleusercontent.com/VsOQrEiuP9yQPMs0BxNTEMNstEe_td4Z6AtXh--AMqwu4KTz0cE6WvkCeUWJvCwdmkSZse-KM6bmFbnZW0iduOq8fg6SOUi3PUCe3abODit40wfLOKJnjxFEv7CI3vrVC8VW3Ms](https://lh4.googleusercontent.com/VsOQrEiuP9yQPMs0BxNTEMNstEe_td4Z6AtXh--AMqwu4KTz0cE6WvkCeUWJvCwdmkSZse-KM6bmFbnZW0iduOq8fg6SOUi3PUCe3abODit40wfLOKJnjxFEv7CI3vrVC8VW3Ms)
    

That should be all for the TraderPlusPriceConfig.json, let’s move on to the [TraderPlusIDsConfig.json.](TraderPlusIDsConfig%20json%20f208ea4128d149b6a1b7b4fca27f871b.md)

[TraderPlusStock_ID_X.json](TraderPlusPriceConfig%20json%20bafb5261d89349f1ac68f82e53eb3b46/TraderPlusStock_ID_X%20json%20d18f41837fde44a5a56e6c63460c5e9e.md)

[Trade Quantity](TraderPlusPriceConfig%20json%20bafb5261d89349f1ac68f82e53eb3b46/Trade%20Quantity%20dd3fdd4f6191440c9c0df4d6ed31685e.md)