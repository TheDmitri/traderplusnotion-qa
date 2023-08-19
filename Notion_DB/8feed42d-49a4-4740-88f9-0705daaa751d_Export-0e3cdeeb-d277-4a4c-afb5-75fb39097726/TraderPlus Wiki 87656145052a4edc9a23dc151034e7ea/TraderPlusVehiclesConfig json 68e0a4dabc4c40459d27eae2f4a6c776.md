# TraderPlusVehiclesConfig.json

Owner: Dmitri Medeleiv

## Summary:

---

This file is dedicated to car and its attachments

## File explanations:

- Toggle for example file.
    
    ```json
    				{ "VehicleName": "CivilianSedan",
                "Height": 0,
                "VehicleParts": [
                    "SparkPlug",
                    "CarBattery",
                    "CarRadiator",
                    "HeadlightH7",
                    "HeadlightH7",
                    "CivSedanDoors_Driver",
                    "CivSedanDoors_CoDriver",
                    "CivSedanDoors_BackLeft",
                    "CivSedanDoors_BackRight",
                    "CivSedanHood",
                    "CivSedanTrunk",
                    "CivSedanWheel",
                    "CivSedanWheel",
                    "CivSedanWheel",
                    "CivSedanWheel"
                ]
            },
            {
                "VehicleName": "Dmns_MRAP",
                "Height": 2,
                "VehicleParts": [
                    "SparkPlug",
                    "CarBattery",
                    "CarRadiator",
                    "HeadlightH7",
                    "HeadlightH7",
                    "MRAPDriverDoor",
                    "MRAPCoDriverDoor",
                    "MRAPCargo1Door",
                    "MRAPCargo2Door",
                    "MRAP_wheel",
                    "MRAP_wheel",
                    "MRAP_wheel",
                    "MRAP_wheel"
                ]
            }
    }
    ```
    

---

To add a new vehicle, copy and paste the json snippet into your config file. You can place it either at the top or bottom of the current config then change VehicleName to the classname of the vehicle and put the attachments needed for that car below in the array.

```json
				{ "VehicleName": "Example_Car",
            "Height": 0,
            "VehicleParts": [
                "SparkPlug",
                "CarBattery",
                "CarRadiator",
                "HeadlightH7",
                "HeadlightH7",
                "Example_Car_Door_Driver",
                "Example_Car_Door_CoDriver",
                "Example_Car_Door_BackLeft",
                "Example_Car_Door_BackRight",
                "Example_Car_Hood",
                "Example_Car_Trunk",
                "Example_Car_Wheel",
                "Example_Car_Wheel",
								"Example_Car_Wheel",
								"Example_Car_Wheel"
            ]
        }
```

<aside>
⚠️ Don’t forget to check your JSON with a [validator!](https://www.notion.so/XML-JSON-Validators-d9b2bc2fc1594b04bd02483634bb5b8e?pvs=21)

</aside>

**“Height”:** 

Integer variable that represents the default set by the hologram during the deployment.  Height is increased by the defined value to fix the deployment above ground.

Normally, cars should be deployed correctly above ground. For vanilla cars and most of them it’s working well.

<aside>
💡 However, since deploying a car like a Pokemon seems a bit weird, some mod creators didn’t think of that.  Some things are missing in the vehicle geometry making the hologram of the car appear in the ground.

So the only way I found to make them deploy above ground is to increase the height. So if you see that your modded car is being deployed in the ground, increase the height until it’s not.

<aside>
⚠️ Keep in mind that the actual Hologram will still appear in the ground, only the final result is fixed that way.

</aside>

</aside>

Now let’s take a look on how to set up a safe area for your traders to work with the [TraderPlusSafeZoneConfig.json](TraderPlusSafeZoneConfig%20json%20e6d485d37c66485287111890f9c35b64.md)