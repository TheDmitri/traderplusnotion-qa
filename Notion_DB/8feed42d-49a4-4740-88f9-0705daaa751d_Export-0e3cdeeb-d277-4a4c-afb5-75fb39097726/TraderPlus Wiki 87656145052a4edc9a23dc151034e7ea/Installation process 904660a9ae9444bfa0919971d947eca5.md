# Installation process

Owner: Dmitri Medeleiv

---

## Summary

---

This part is dedicated to the installation of TraderPlus. 

<aside>
⚠️ TraderPlus configuration files are set up for Chernarus by default. You’ll need to manually adjust [TraderPlusGeneralConfig.json](TraderPlusGeneralConfig%20json%20eef7f811207c48aca418cffd41121735.md) settings to customize them for other maps.

</aside>

Before continuing, be sure you are subscribed to the mod in the steam workshop and have opened the mod folder to get access to these folders.

![Untitled](Installation%20process%20904660a9ae9444bfa0919971d947eca5/Untitled.png)

The default folders typically will be found in the following location: 

> !Workshop/@TraderPlus/ServerProfile/TraderPlus
> 
- Here is a helpful video by Scalespeeder Gaming if you are having trouble finding the folders.
    
    [https://bit.ly/3Jw5gab](https://bit.ly/3Jw5gab)
    

The contents of this folder will need to be copied to either of these locations using the steps outlined in the following section.

> DayZ Server/profiles/
DayZ Server/mpmissions/empty.chernarus/
> 

## Manual Installation **Instructions:**

---

**Step 1**: We copy the mod folder ‘*@TraderPlus’* to your DayZ Server Root folder.

**Step 2**: We go inside *DayZServer/@TraderPlus/Keys/* and we copy C4BaseRaidbyDmitiri.bikey & paste it into your *DayZServer/keys/* folder in your DayZ Server Root.

**Step 3:** We copy the TraderPlus_ce folder, which is inside the *DayZServer/@TraderPlus/Centralconomy/* folder, to our main mission folder. *( /mpmissions/empty.chernarus/ )*

**Step 4:** We add the following to our *cfgeconomycore.xml* file in our main server root folder.

```xml
 <!-- Trader Plus -->
	<ce folder="TraderPlus_ce">
		<file name="TraderPlus_types.xml" type="types" />
	</ce>
```

**Step 5**: We go inside *@TraderPlus\ServerProfile* and we copy the TraderPlus folder to paste it in your profile folder located normally in your DayZ Server Root. *(DayZ Server/profiles/)*

**Step 6:** Make sure that you have inside your TraderPlus folder the following folder:

![TPProfile.PNG](Installation%20process%20904660a9ae9444bfa0919971d947eca5/TPProfile.png)

**Step 7**: We have finished the basics step to make the mod work for first time boot up.

**Step 8:** Your next steps should be to verify the mod works properly in game. 

**Step 9:** In case you’re wondering where the default trade zone is:

![Default Trading.png](Installation%20process%20904660a9ae9444bfa0919971d947eca5/Default_Trading.png)

Click the following link to read about the [TraderPlusGeneralConfig.json](TraderPlusGeneralConfig%20json%20eef7f811207c48aca418cffd41121735.md)