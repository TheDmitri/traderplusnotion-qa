# TraderPlusInsuranceConfig.json

Owner: Dmitri Medeleiv

## Summary:

---

Insurance allow you to get reimbursed when an insured car is destroyed during gameplay. 

Here are some specifications regarding the license system:

- The insurance can only be obtained when buying a car.
- Insurance is removed and attached to receipt when packing an insured car.
- Insurance is removed when the car is stored in the garage.

```json
{ "Version": "2.5",
  "AuthorizedIDInsurance": [4],
  "Insurances": [
    { "VehicleName": "OffroadHatchback",
      "InsurancePriceCoefficient": 1.25,
      "CollateralMoneyCoefficient": 0.75
    },
    { "VehicleName": "Hatchback_02",
      "InsurancePriceCoefficient": 1.25,
      "CollateralMoneyCoefficient": 0.75
    },
    { "VehicleName": "CivilianSedan",
      "InsurancePriceCoefficient": 1.25,
      "CollateralMoneyCoefficient": 0.75
    }
  ]
}
```

## File explanations:

---

Inside the TraderPlusInsuranceConfig.json, you should find the following variables:

### “Version”:

Notated version of the config that is updated by Dmitri when necessary. Please do not adjust.

### **“AuthorizedIDInsurance”**:

Integer array that defines which TraderID has the right to give the insurance reimbursement if the car is destroyed.

### “**Insurances**”:

Integer array where you will be able to set up insurance cost for each car classname.  

"VehicleName": "CivilianSedan",                // classname of the vehicle to be insured.
 "InsurancePriceCoefficient": 1.25,            // coefficient calculation for the price of insurance. 
 "CollateralMoneyCoefficient": 0.75          // coefficient calculation of reimbursement to player if vehicle is destroyed.