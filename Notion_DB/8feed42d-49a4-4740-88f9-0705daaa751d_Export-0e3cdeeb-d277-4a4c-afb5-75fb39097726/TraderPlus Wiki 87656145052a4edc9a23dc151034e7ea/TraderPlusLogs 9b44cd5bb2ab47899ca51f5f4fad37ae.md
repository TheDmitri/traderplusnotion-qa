# TraderPlusLogs

Owner: Dmitri Medeleiv

## Summary:

---

In order to get information about how the mod is doing, you’ll have some logs to help you see if config is loading correctly and also a trace of each player's transaction.

These logs can be found in *TraderPlus\TraderPlusLogs\*

The most important entry in a TraderPlus log is an error entry.
**[ERROR]**

In most cases a problem can be solved by looking in your logs for the above entry.=-0987456321852

### Troubleshooting:

*Here is an example of troubleshooting using the log files.*

**Situation:** 

You’ve found your trader is not functioning correctly after some recent changes to you config files.  

**Your first step** should be to open your logs and read through the first dozen or so lines in the newest log file.

[You can see above that there is an error regarding the file read after [TraderPlusVehiclesConfig](https://www.notion.so/68e0a4dabc4c40459d27eae2f4a6c776?pvs=21).json but before [TraderPlusIDsConfig](https://www.notion.so/f208ea4128d149b6a1b7b4fca27f871b?pvs=21).json.](https://lh6.googleusercontent.com/j_Mf1q4GuK5-VMuaDKlaMHwNsFSUqXTZ40ieayjs6XTpMQ453yseqG0pPYlnPCMTXOJEvdVIoj7qIEZAVBd8ljBwEvSD9zgI6FCumbcGpxl7uEGXTV8R5ULlwEvpZl-Ch3nBi3eNbr2OXCdu7Q)

You can see above that there is an error regarding the file read after [TraderPlusVehiclesConfig](https://www.notion.so/68e0a4dabc4c40459d27eae2f4a6c776?pvs=21).json but before [TraderPlusIDsConfig](https://www.notion.so/f208ea4128d149b6a1b7b4fca27f871b?pvs=21).json.

---

> *“All right Dmitri, I’m no scripter. I don’t know this stuff. What should I be looking for?”*
> 

<aside>
💭 A*s you can see in the screenshot above, there is a config file that is showing an error. You need to open this file and find the error in the json. We can deduce it’s the PriceConfig because it’s the only config not showing in the logs. It’s recommended that you verify each TraderPlus json file with a validator before implementation on your server. Below is a link to a list of many useful resources for server owners.*

</aside>

### *[Useful Tools & Resources](Useful%20Tools%20&%20Resources%20bdc17538c1bc4645a7695ea5ae284095.md)*