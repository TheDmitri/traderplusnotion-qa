# Dr. Jones Trader Conversion

Owner: Dmitri Medeleiv

## Summary:

---

That part is dedicated to users who already use Dr.Jones trader mod and would like to convert their config to TraderPlus config.

<aside>
⚠️ **Make sure to follow [Installation process](Installation%20process%20904660a9ae9444bfa0919971d947eca5.md) before doing this part !**

</aside>

## Conversion Notes

**What can be converted:**

- *TraderConfig.txt*
- *TraderVehiclesParts.txt*
- TraderObjects.txt (partially)

**What can not be converted:**

- TraderVariables.txt

That most important file from Dr. Jones Trader is TraderConfig.txt, which will be converted so you won’t have to rebuild your price config. 

**Generated Files**

The conversion will regenerate four files located in */DayZServer\profile\TraderPlus\TraderPlusConfig:* 

1. TraderPlusGeneralConfig.json
2. TraderPlusPriceConfig.json,
3. TraderPlusIDsConfig.json
4. TraderPlusVehiclesConfig.json.

The TraderPlusGeneralConfig will receive all trader Ids, name and positions from TraderConfig.txt.

<aside>
📖 It is strongly recommend to review each trader after conversion. Verify which npc/object each is supposed to be, their location, and orientation. Sometimes conversions come over with errors.

</aside>

The TraderPlusPriceConfig will take your *TraderConfig.txt*, add a classname, trade quantity, buy price and sell price to each item. Then add it to the TraderPlusPriceConfig.json within a specified category. 

In addition to that, new variables will be added for each products:

- coefficient:
    - between 0.0 and 1.0
- **maxstock:**
    - it will be either -1 as infinite stock if that’s what you want **or** integer value for a defined stock.

<aside>
📖 F*or ammunition, it will be multiplied by the average number of ammo that spawn in map so it can be higher that current nominal value)*

</aside>

## Example of conversion.

**TraderConfig.txt**

| Classname | TradeQty | Buy Price | Sell Price |
| --- | --- | --- | --- |
| CombinationLock | * | 700 | 300 |

**TraderPlusPriceConfig.json**

| Classname | Coefficient | Max Stock | Trade Qty | Buy Price | Sell Price |
| --- | --- | --- | --- | --- | --- |
| CombinationLock | .97309 | 60 | 0 | 700 | 300 |

### With that, you’re ready for

[Conversion to TraderPlus](Dr%20Jones%20Trader%20Conversion%20b35b8c7ac2dc4e42a5f98e3252eb6787/Conversion%20to%20TraderPlus%2057dc1832c5a846c8abeab212db27d56f.md)