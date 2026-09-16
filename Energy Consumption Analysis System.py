#!/usr/bin/env python
# coding: utf-8

# ## GROUP A PROJECT
# 
# # Energy Consumption Analysis System
# 

# In[53]:


## Customer Information for Electricity Consumption in Nigeria
## Loading data as a dictionary in a list
energy_data = [
{
"customer_id": "C001",
"customer_name": "Greenview Estate",
"customer_type": "Residential",
"location": "Lagos",
"month": "January",
"consumption_kwh": 280,
"tariff_per_kwh": 120,
"peak_consumption_kwh": 160,
"renewable_share": 10,
"outage_hours": 14,
"payment_status": "Paid"
},
{
"customer_id": "C002",
"customer_name": "Sunrise Bakery",
"customer_type": "SME",
"location": "Lagos",
"month": "January",
"consumption_kwh": 850,
"tariff_per_kwh": 120,
"peak_consumption_kwh": 520,
"renewable_share": 5,
"outage_hours": 10,
"payment_status": "Paid"
},
{
"customer_id": "C003",
"customer_name": "CityCare Hospital",
"customer_type": "Hospital",
"location": "Abuja",
"month": "January",
"consumption_kwh": 1450,
"tariff_per_kwh": 120,
"peak_consumption_kwh": 780,
"renewable_share": 15,
"outage_hours": 8,
"payment_status": "Paid"
},
{
"customer_id": "C004",
"customer_name": "Bright Future School",
"customer_type": "School",
"location": "Abuja",
"month": "February",
"consumption_kwh": 620,
"tariff_per_kwh": 120,
"peak_consumption_kwh": 310,
"renewable_share": 20,
"outage_hours": 12,
"payment_status": "Paid"
},
{
"customer_id": "C005",
"customer_name": "AgroFresh Farms",
"customer_type": "Agricultural",
"location": "Ibadan",
"month": "February",
"consumption_kwh": 980,
"tariff_per_kwh": 115,
"peak_consumption_kwh": 490,
"renewable_share": 35,
"outage_hours": 18,
"payment_status": "Pending"
},
{
"customer_id": "C006",
"customer_name": "Metro Apartments",
"customer_type": "Residential",
"location": "Ibadan",
"month": "February",
"consumption_kwh": 340,
"tariff_per_kwh": 115,
"peak_consumption_kwh": 190,
"renewable_share": 8,
"outage_hours": 20,
"payment_status": "Paid"
},
{
"customer_id": "C007",
"customer_name": "Prime Plastics",
"customer_type": "Industrial",
"location": "Lagos",
"month": "March",
"consumption_kwh": 3200,
"tariff_per_kwh": 125,
"peak_consumption_kwh": 1900,
"renewable_share": 5,
"outage_hours": 7,
"payment_status": "Paid"
},
{
"customer_id": "C008",
"customer_name": "Lakeside Hotel",
"customer_type": "SME",
"location": "Lagos",
"month": "March",
"consumption_kwh": 1750,
"tariff_per_kwh": 125,
"peak_consumption_kwh": 920,
"renewable_share": 12,
"outage_hours": 9,
"payment_status": "Paid"
},
{
"customer_id": "C009",
"customer_name": "Hope Clinic",
"customer_type": "Hospital",
"location": "Ibadan",
"month": "March",
"consumption_kwh": 1100,
"tariff_per_kwh": 115,
"peak_consumption_kwh": 600,
"renewable_share": 18,
"outage_hours": 16,
"payment_status": "Pending"
},
{
"customer_id": "C010",
"customer_name": "Unity Secondary School",
"customer_type": "School",
"location": "Lagos",
"month": "April",
"consumption_kwh": 540,
"tariff_per_kwh": 125,
"peak_consumption_kwh": 270,
"renewable_share": 25,
"outage_hours": 11,
"payment_status": "Paid"
},
{
"customer_id": "C011",
"customer_name": "FreshFields Agro",
"customer_type": "Agricultural",
"location": "Abuja",
"month": "April",
"consumption_kwh": 1250,
"tariff_per_kwh": 120,
"peak_consumption_kwh": 650,
"renewable_share": 40,
"outage_hours": 13,
"payment_status": "Paid"
},
{
"customer_id": "C012",
"customer_name": "Oakwood Residence",
"customer_type": "Residential",
"location": "Abuja",
"month": "April",
"consumption_kwh": 410,
"tariff_per_kwh": 120,
"peak_consumption_kwh": 230,
"renewable_share": 10,
"outage_hours": 15,
"payment_status": "Paid"
},
{
"customer_id": "C013",
"customer_name": "Naija Foods Ltd",
"customer_type": "Industrial",
"location": "Ibadan",
"month": "May",
"consumption_kwh": 2800,
"tariff_per_kwh": 115,
"peak_consumption_kwh": 1500,
"renewable_share": 10,
"outage_hours": 21,
"payment_status": "Pending"
},
{
"customer_id": "C014",
"customer_name": "TechHub Workspace",
"customer_type": "SME",
"location": "Abuja",
"month": "May",
"consumption_kwh": 760,
"tariff_per_kwh": 120,
"peak_consumption_kwh": 410,
"renewable_share": 15,
"outage_hours": 6,
"payment_status": "Paid"
},
{
"customer_id": "C015",
"customer_name": "Hope Residence",
"customer_type": "Residential",
"location": "Lagos",
"month": "May",
"consumption_kwh": 190,
"tariff_per_kwh": 125,
"peak_consumption_kwh": 105,
"renewable_share": 5,
"outage_hours": 24,
"payment_status": "Paid"
},
{
"customer_id": "C016",
"customer_name": "Industrial Works Ltd",
"customer_type": "Industrial",
"location": "Abuja",
"month": "June",
"consumption_kwh": 3600,
"tariff_per_kwh": 120,
"peak_consumption_kwh": 2200,
"renewable_share": 8,
"outage_hours": 5,
"payment_status": "Paid"
},
{
"customer_id": "C017",
"customer_name": "GreenMart Store",
"customer_type": "SME",
"location": "Ibadan",
"month": "June",
"consumption_kwh": 690,
"tariff_per_kwh": 115,
"peak_consumption_kwh": 350,
"renewable_share": 18,
"outage_hours": 17,
"payment_status": "Pending"
},
{
"customer_id": "C018",
"customer_name": "Community Hospital",
"customer_type": "Hospital",
"location": "Lagos",
"month": "June",
"consumption_kwh": 1600,
"tariff_per_kwh": 125,
"peak_consumption_kwh": 850,
"renewable_share": 20,
"outage_hours": 10,
"payment_status": "Paid"
},
{
"customer_id": "C019",
"customer_name": "Victory School",
"customer_type": "School",
"location": "Ibadan",
"month": "June",
"consumption_kwh": 480,
"tariff_per_kwh": 115,
"peak_consumption_kwh": 240,
"renewable_share": 22,
"outage_hours": 19,
"payment_status": "Paid"
},
{
"customer_id": "C020",
"customer_name": "FarmLink Cooperative",
"customer_type": "Agricultural",
"location": "Lagos",
"month": "June",
"consumption_kwh": 1350,
"tariff_per_kwh": 125,
"peak_consumption_kwh": 720,
"renewable_share": 45,
"outage_hours": 14,
"payment_status": "Paid"
}
]


## DATA EXPLORATION
# checks for number of data stored in energy data
customer_records = (len(energy_data))
print(f"There are {customer_records} Customer Records ")
print()

## prints dataset in a neat format
print("=========================================")
print("     CLEANER CUSTOMER INFORMATION        ")
print("=========================================")

for customer in energy_data:
    # loopa through customer in energy_data
    print(f"""
    Customer ID:{customer["customer_id"]}
    Customer Name: {customer["customer_name"]}
    Customer Type: {customer["customer_type"]}
    Location: {customer["location"]}
    Month: {customer["month"]}
    Consumption: {customer["consumption_kwh"]}Kwh
    Tariff:  ₦{customer["tariff_per_kwh"]}
    Peak Consumption: {customer["peak_consumption_kwh"]}Kwh
    Renewable Share: {customer["renewable_share"]}Kwh
    Outage Hours: {customer["outage_hours"]}Hr
    Payment Status: {customer["payment_status"]}
    """)
print("=========================================")



# In[54]:


## Checking for all customers

print("=========================================")
print("          CUSTOMER NAMES                 ")
print("=========================================")
for customer in energy_data:
    print(customer["customer_name"])
print("=========================================")

## Checking for Customers and their respective consumption
print()
print("=========================================")
print("          CUSTOMER CONSUMPTION           ")
print("=========================================")
for customer in energy_data:
    print(customer["customer_name"], "→" , customer["consumption_kwh"], "Kwh")
print("=========================================")


# In[55]:


## Calculate Electricity Cost.
print("=======================================")
print("ELECTRICITY USAGE COST")
print("=======================================")

def electricity_cost(energy_data):
    """ A function that calculates the cost of electricity by customers"""
    for customer in energy_data:
        ## loop through customer in energy_data
        consumption =  customer["consumption_kwh"]

        # assigning a value from the list to a variable
        tariff = customer["tariff_per_kwh"]

        electricity_cost =  consumption * tariff
        # multiply the consumption cost and the tariff in kwh
        print(f"{customer["customer_name"]}: ₦{electricity_cost}")


electricity_cost(energy_data)



# In[56]:


# Location Analysis

location_consumption = {
    # initialising consumption to Zero by location
    "Lagos": 0,
    "Abuja": 0,
    "Ibadan": 0
}


#Total consumption of each states

for customer in energy_data:
    location = customer["location"]
    consumption = customer["consumption_kwh"]

    location_consumption[location] += consumption
    # aggregates the consumption by Location

print("==============================================")
print("LOCATION CONSUMPTION ANALYSIS                 ")
print("==============================================")
for location in location_consumption:
    total = location_consumption[location]
    print(F"{location}: {total}kwh")
print("==============================================")

#The highest consuming location y comparing the values 
# initialising  highest value to Zero for comparison 
highest_location = ""
highest_value = 0

for location in location_consumption:
    if location_consumption[location] > highest_value:

        highest_value = location_consumption[location]
        highest_location = location









# In[57]:


# Customer Type and Monthly  Analysis

customer_type_consumption = {
     # initialising consumption to Zero by Customer type 
    "Residential": 0,
    "SME": 0,
    "Industrial":0,
    "Hospital":0,
    "School": 0,
    "Agricultural": 0
}

for customer in energy_data:

    customer_type = customer["customer_type"]
    consumption = customer ["consumption_kwh"]

    customer_type_consumption[customer_type] += consumption
print("======================================")
print("CUSTOMER TYPE "                    )
print("======================================")

for customer in customer_type_consumption:
    type_consumption = customer_type_consumption[customer]
    print(f"{customer}: {type_consumption}kwh")

# initialising  highest value to Zero for comparison
highest_customer = ""
highest_values = 0

for customer in customer_type_consumption:
    if customer_type_consumption[customer_type] > highest_values:

        highest_values = customer_type_consumption[customer_type]
        highest_customer = customer


# Energy Consumption Monthly Analysis
print()
monthly_consumption = {
    # initialising consumption to Zero by Month
    "January": 0,
    "February":0,
    "March":0,
    "April":0,
    "May":0,
    "June":0
}

for customer in energy_data:

    month = customer["month"]
    consumption = customer["consumption_kwh"]

    monthly_consumption [month] += consumption

print("========================================")
print("MONTHLY CONSUMPTION"                     )
print("========================================")
for month in monthly_consumption:
    customer_consumption = monthly_consumption[month]
    print(F"{month}: {customer_consumption}kwh")


# In[58]:


# Breaking the Program into Functions

def view_all_records():
    """ This function shows all the customer records """

    print("=========================================")
    print("     CLEANER CUSTOMER INFORMATION        ")
    print("=========================================")

    for customer in energy_data:
        print(f"""
        Customer ID:{customer["customer_id"]}
        Customer Name: {customer["customer_name"]}
        Customer Type: {customer["customer_type"]}
        Location: {customer["location"]}
        Month: {customer["month"]}
        Consumption: {customer["consumption_kwh"]}Kwh
        Tariff:  ₦{customer["tariff_per_kwh"]}
        Peak Consumption: {customer["peak_consumption_kwh"]}Kwh
        Renewable Share: {customer["renewable_share"]}Kwh
        Outage Hours: {customer["outage_hours"]}Hr
        Payment Status: {customer["payment_status"]}
        """)
    print("=========================================")

def validate_data(energy_data):
    """ This function checks for the integrity of the data and ensure user inputs the right values for each variable"""
    seen_id = []
    # seen_id list gets the customer ids that are found after looping through the dataset
    errors_found = 0
    # intializing errors found to zero to count the number of errors found if any

    for customer in energy_data:
        # looping through the dataset
        customer_id = customer["customer_id"]
        customer_name = customer["customer_name"]
        customer_type =  customer["customer_type"]
        location =  customer["location"]
        month = customer["month"]
        consumption = customer["consumption_kwh"]
        tariff = customer["tariff_per_kwh"]
        peak_Consumption = customer["peak_consumption_kwh"]
        renewable_share = customer["renewable_share"]
        outage_hours = customer["outage_hours"]
        payment_status = customer["payment_status"]

        try:
            # Using try and except to catch error before code crashes
            if customer_id == "":
                # checks if customer id is empty
                raise ValueError("Customer_id cannot be empty")
                # raise an exception if customer id is empty
            elif customer_id in seen_id:
                # checks if there is a duplicate id
                raise ValueError("Duplicate Value Detected")
                # raise an exception if customer id is more than one
            else:
                seen_id.append(customer_id)
                # .append adds ids seen while looping through the dataset
        except ValueError as error:
            print(f"Error for{customer_name}: {error}")
            error_found +=1
            # this counts the error, everytime the code catches an error

        try:
            if customer_name == "":
                # checks if customer name is empty
                raise ValueError("Customer_name cannot be empty")
                 # raise an exception if customer name is empty
        except ValueError as error:
            print(f"Error for{customer_name}: {error}")
            error_found +=1

        try:
            if customer_type != "Residential" and customer_type != "SME" and customer_type != "Industrial" and customer_type != "Hospital" and customer_type != "School" and customer_type != "Agricultural":
                # checks if input can be found in the datatype stated
                raise ValueError("Customer Type Does not Exist, please enter the right one")
                 # raise an exception if customer type cannot be found in the above mentioned
        except ValueError as error:
            print(f"Error for{customer_name}: {error}")
            error_found +=1

        try:
            if consumption <= 0:
                # checks if consumption is less that or equal to zero
                raise ValueError("Consumption cannot be Zero or Negative")
                # raise an exception if condition is true
        except ValueError as error:
            print(f"Error for{customer_name}: {error}")
            error_found +=1

        try:
            if not (0 < renewable_share <= 100):
                # checks if renewable share is not between 0 and 100
                raise ValueError("Renewable Share must be from 0 through 100")
                # raises a value error if false
        except ValueError as error:
            print(f"Error for{customer_name}: {error}")
            error_found +=1

        try:
            if outage_hours < 0:
                # checks if outage hours is less than zero
                raise ValueError("Outage Hours cannot be Zero or Negative")
                # raise a Value error if true
        except ValueError as error:
            print(f"Error for{customer_name}: {error}")
            error_found +=1

        try:
            if payment_status != "Paid" and payment_status != "Pending":
                # checks if payment status between the stated condition

                raise ValueError ("Payment Status can only be paid or pending")

        except ValueError as error:
            print(f"Error for{customer_name}: {error}")
            error_found +=1
             # update counter
    return errors_found





def calculate_total_consumption():
    """ The function calculates the total energy consumption of all the 20 customers."""
    total_consumption = 0
    # Intitialistng total consumption to zero

    for customer in energy_data:
        # loops through energy data
        total_consumption += customer["consumption_kwh"]
        # aggregate consumption for every customer


    return total_consumption



def calculate_average_consumption (total_consumption, customer_records):
    """ The function calculates the average electriity consumption per customer."""

    average_consumption = total_consumption / customer_records
    # divides total consumption by customer_records

    return average_consumption


def calculate_total_electricity_cost(energy_data):
    """The function calculates the total electricity cost"""

    total_electricity_cost = 0
    # initialising total electricity cost to zero

    for customer in energy_data:
        electricity_cost =  customer["consumption_kwh"] * customer["tariff_per_kwh"]
        # multiplies the consumption by tariff for each customer
        total_electricity_cost += electricity_cost
        # sums up the electricity cost to get the total costs for all customers

    return total_electricity_cost


def calculate_Average_electricity_cost(energy_data):
    """The function calculates the Average electricity cost"""

    total_cost = calculate_total_electricity_cost(energy_data)
    # returns the total electricity cost

    average_electricity_cost = total_cost/ len(energy_data)
    # divides the total cost by the number of customers


    return average_electricity_cost


# Customer Classification and attention analysis

def classify_customers(energy_data):
    """The function classifies customers based on their energy consumption"""

    for customer in energy_data:
        consumption = customer ["consumption_kwh"]
        renewable_share = customer["renewable_share"]
        status = "Normal"
        if consumption < 500:
            category = "Low"
            # checks if conditions returns true and return the category
        elif consumption < 1000:
            category = "Medium"
        else:
            category = "High"

            if consumption >= 1000 and renewable_share < 15:
                status = "High Atention"   
                # checks if both condition returns true and return status

        # prints output
        print(f"Customer:{customer['customer_name']}")
        print(f"Consumption: {consumption} kwh")
        print(f"Classification: {category}")
        print(f"Status: {status}")
        print()




def find_highest_consumer(energy_data):
    """ The function finds the customer with the highest energy consumption."""

    highest_consumption = energy_data[0]
    # initialising highest consumption to the first customer in the list


    for customer in energy_data:
        # loops through the energy data
        if customer["consumption_kwh"] > highest_consumption["consumption_kwh"]:
            # compare each customer against the first customer
            highest_consumption = customer
            # if true, highest consumption becomes the benchmark

    return highest_consumption["customer_id"],highest_consumption["customer_name"], highest_consumption["consumption_kwh"]




def find_lowest_consumer(energy_data):
    """ The function finds the customer with the lowest energy consumption."""

    lowest_consumption = energy_data[0]
    #  initialising Lowest consumption to the first customer in the list

    for customer in energy_data:
        # loops through the energy data
        if customer["consumption_kwh"] < lowest_consumption["consumption_kwh"]:
             # compare each customer against the first customer
            lowest_consumption = customer 
            #  if true, lowest consumption becomes the benchmark

    return lowest_consumption["customer_id"], lowest_consumption["customer_name"], lowest_consumption["consumption_kwh"]


def analyze_locations(energy_data):
    """ The function analyze the total energy consumption for each location."""

    location_consumption = {
        # initialising consumption to Zero by state
    "Lagos": 0,
    "Abuja": 0,
    "Ibadan": 0
    }

    for customer in energy_data:
        # loops through energy data
        location = customer["location"]
        consumption = customer["consumption_kwh"]

        location_consumption[location] += consumption
        # adds consumption by states

    return location_consumption


def analyze_customer_types(energy_data):
    """ The function analyze the total energy consumption for each customer type."""

    customer_type_consumption = {
       # initialising consumption to Zero by customer type
    "Residential": 0,
    "SME": 0,
    "Industrial":0,
    "Hospital":0,
    "School": 0,
    "Agricultural": 0
    }

    for customer in energy_data:
        # loops through the energy data
        customer_type = customer["customer_type"]
        consumption = customer ["consumption_kwh"]

        customer_type_consumption[customer_type] += consumption
        # adds consumption by customer type

    return customer_type_consumption


def analyze_monthly_consumption(energy_data):
    """The function analyze the energy consumption for a month)"""
    monthly_consumption = {
        # initialising consumption to Zero by Month
    "January": 0,
    "February":0,
    "March":0,
    "April":0,
    "May":0,
    "June":0
    }

    for customer in energy_data:
        # loops through the energy data
        month = customer["month"]
        consumption = customer["consumption_kwh"]

        monthly_consumption [month] += consumption
        # adds consumption by month

    return monthly_consumption


def high_attention_customers(energy_data):
    """The function identifies customers that require high attention."""

    high_attention_count = 0
    # initialising counter to Zero

    status = []
    # Get status in a List

    for customer in energy_data:
        # loops through energy data
        renewable_share = customer["renewable_share"]
        consumption = customer["consumption_kwh"]

        if consumption >= 1000 and renewable_share < 15:
            # checks input against both conditions 
            status.append(
               { "name": customer["customer_name"],
                "consumption": customer["consumption_kwh"],
                 "renewable_share": customer["renewable_share"]
               } )
            # returns status if true
            high_attention_count += 1
            # update counter

    return  status, high_attention_count 





# Energy Consumption analysis System Menu


def display_menu(): 
    """ This displays various options that the company may want to see"""

    print("   =================================================")
    print("   ENERGY CONSUMPTION ANALYSIS MENU SYSTEM          ")
    print("   =================================================")

    print("    1. View All Records")
    print("    2. View Total Consumption")
    print("    3. View Average Consumption")
    print("    4. Find Highest Consumer")
    print("    5. Find Lowest Consumer")
    print("    6. Calculate Electricity Cost")
    print("    7. Classify Customers")
    print("    8. Location Analysis")
    print("    9. Customer -Type Analysis")
    print("   10. Monthly Analysis")
    print("   11. High- Attention Customers")
    print("   12. Generate Summary")
    print("   13. Exit")





# In[59]:


print(f"""
    Welcome, Energy Analyst. This system helps analyze electricity consumption, cost and usage patterns.
    Kindly Go through the Menu
    """)

while True:
    # This loops run while the logical statements remains true
    display_menu()
    # displays the menu so user can select variuos options
    choice = input("Enter your choice: ")
    # takes user input

    if choice == "1":
        # if codition is true, run the follow up code
        print("View Records")

        # calling view_all_records() function
        view_all_records()



    elif choice == "2":
        # if codition is true, run the follow up code
        print("View Total Consumption")

          # calling calculate_total_consumption() function
        total_consumption = calculate_total_consumption()

        print(f"Total Consumption: {total_consumption} kWh")

    elif choice == "3":
        # if codition is true, run the follow up code
        print("View Average Consumption")

         # calling calculate_average_consumption function
        average_consumption = calculate_average_consumption (total_consumption, customer_records)

        print(f"Average Consumption: {average_consumption} kWh")

    elif choice == "4":
        # if codition is true, run the follow up code
        print("Find Highest Consumer")

        # calling find_highest_consumer function 
        highest_name = find_highest_consumer(energy_data)[0]
        highest_consumption = find_highest_consumer(energy_data)[2]

        print(f"Highest Consumer: {highest_name}")
        print(f"Consumption: {highest_consumption} kWh")

    elif choice == "5":
        # if codition is true, run the follow up code
        print("Find Lowest Consumer")

        # calling find_lowest_consumer function
        lowest_name = find_lowest_consumer(energy_data)[0]
        lowest_consumption = find_lowest_consumer(energy_data)[2]

        print(f"Lowest Consumer: {lowest_name}")
        print(f"Consumption: {lowest_consumption} kWh")

    elif choice == "6":
        # if codition is true, run the follow up code
        print("Calculate Electricity Cost")

        # calling calculate_total_electricity_cost function
        total_electricity = calculate_total_electricity_cost(energy_data)

        print(f"Total Electricity Cost: ₦{total_electricity}")

    elif choice == "7":
        # if codition is true, run the follow up code
        print("Classify Customers")

        # calling classify_customers function
        classify_customers(energy_data)


    elif choice == "8":
        # if codition is true, run the follow up code
        print("Location Analysis")

         # calling analyze_location function
        location_consumptions = analyze_locations(energy_data)

        for location in location_consumptions:
            # loops through location consuption
            total = location_consumptions[location]

            # returns print statement
            print(f"{location}: {total}kwh")

    elif choice == "9":
         # if codition is true, run the follow up code

        print("Customer_Type Analysis")

        # calling analyze_customer_types function
        customer_type_consumption = analyze_customer_types(energy_data)

        for customer in customer_type_consumption:
            # loops through customer type consumption
            type_consumption = customer_type_consumption[customer]

            # returns print statement
            print(f"{customer}: {type_consumption}kwh")

    elif choice == "10":
         # if codition is true, run the follow up code

        print("Monthly Analysis")

        # calling analyze_monthly_consumption function
        monthly_analysis = analyze_monthly_consumption(energy_data)

        for month in monthly_analysis:
            # loops through monthly analysis
            customer_consumption = monthly_analysis[month]

            # returns print statement
            print(f"{month}: {customer_consumption}kw")

    elif choice == "11":
         # if codition is true, run the follow up code
        print("High_Attention Customers")

        # calling high_attention_customers function
        status, high_attention_count = high_attention_customers(energy_data)

        for customer in status:
            # loops through status and returns print statement
            print(f""" 
            Name: {customer["name"]}
            Consumption: {customer["consumption"]}
            Renewable Share: {customer["renewable_share"]}
            """)    

    elif choice == "12":
         # if codition is true, run the follow up code
        print("Generate Summary")

        # calling  generate_summary function
        generate_summary(energy_data)

    elif choice == "13":
        # if codition is true, run the follow up code
        print("Thank you for using the System.")
        break
        # breaks exit the while loop

    else:
        print("Invalid Option.")



# In[60]:


# Generate Summary

def generate_summary(energy_data):
    """The function generates summary of the energy consumption analysis."""

    # calling all def functions created above
    total_consumption = calculate_total_consumption()
    average_consumption = calculate_average_consumption(total_consumption,customer_records)
    total_electricity = calculate_total_electricity_cost(energy_data)
    average_electricity = calculate_Average_electricity_cost(energy_data)
    highest_id, highest_name, highest_consumer = find_highest_consumer(energy_data)
    lowest_id, lowest_name, lowest_consumer = find_lowest_consumer(energy_data)
    high_attention_count = high_attention_customers(energy_data)
    location_consumption= analyze_locations(energy_data)
    customer_type_consumption= analyze_customer_types(energy_data)
    monthly_analysis = analyze_monthly_consumption(energy_data)

    # Energy consumption summary
    print("=================================================")
    print("ENERGY CONSUMPTION SUMMARY                      " )
    print("=================================================")


    print(f"Total Customers:{len(energy_data)}")
    print(F"Total Consumption: {total_consumption} kwh")
    print(F"Average Consumption: {average_consumption} kwh")

    print()
    print(F"Total Electricity Cost: ₦{total_electricity}")
    print(F"Average Electricity Cost: ₦{average_electricity}")

    print()
    print(f"Consumer: {highest_id}")
    print(F"Consumer Type: {highest_name}")
    print(f"Electricity Consumption: {highest_consumer} kwh")

    print()
    print(f"Consumer: {lowest_id}")
    print(F"Consumer Type: {lowest_name}")
    print(f"Electricity Consumption: {lowest_consumer} kwh")
    print()


    print(f"Highest Consuming Location: {highest_location}")
    print(f"Consumption Value: {highest_value} kwh")
    print()


    print(f"Customer Needing Attention:  {high_attention_count[1]} ")
    print("=================================================")

# calling summary function
generate_summary(energy_data)




# In[61]:


# Location sub-menu

def analyze_locations(energy_data):

    """The function uses a nested while loop to allow repeated investigation of location and customer_type combinations.
    The while loop was used in th location analysis section to alloow the analyst to repeatedly investigate
    different customer-type combinations within a selected location. The outer loop mnages  location selection,
    while the inner loop manages customer-types selection. This allows combinations suc as Lagos + SME or ABUja +Hospital
    to be investigated without returning to the main menu after each selection."""


    while True:          
        # Outer loop to manage location selection

        print()
        print("SELECT LOCATION")
        print("1 Lagos")
        print("2. Abuja")
        print("3. Ibadan")
        print("4. Return to Main Menu")

        location_choice = input("Enter your location choice:")

        if location_choice == "1":
            location = "Lagos"

        elif location_choice == "2":
            location = "Abuja"

        elif location_choice == "3":
            location = "Ibadan"

        elif location_choice == "4":
            break
        else:
            print("Invalid Location Choice.")  


        if location_choice == "1" or location_choice == "2" or location_choice == "3":

            while True:            
                # Inner loop to manage customer type selection

                print()
                print(f"Select Customer Type in {location}")
                print("1. Residential")
                print("2. SME")
                print("3. Industrial")
                print("4. Hospital")
                print("5. School")
                print("6. Agricultural")
                print("7. Return to Location Menu")

                type_choice = input("Enter your customer type choice: ")

                if type_choice == "1":
                    customer_type = "Residential"

                elif type_choice == "2":
                    customer_type = "SME"

                elif type_choice == "3":
                    customer_type = "Industrial"

                elif type_choice == "4":
                    customer_type = "Hospital"

                elif type_choice == "5":
                    customer_type = "School"

                elif type_choice == "6":
                    customer_type = "Agricultural"

                elif type_choice == "7":
                    break

                else:
                    print("Invalid customer type choice.")


                if type_choice == "1" or type_choice == "2" or type_choice == "3" or type_choice =="4" or type_choice == "5"or type_choice == "6":
                    total_consumption = 0

                    for customer in energy_data:
                        if customer["location"] == location and customer["customer_type"] == customer_type:
                            total_consumption += customer["consumption_kwh"] 

                    print()
                    print(F"{location} + {customer_type}")
                    print(F"Total Consumption: {total_consumption}kwh")

# calling analyze location function
analyze_locations(energy_data)


# In[62]:


# Validating Dataset
data = validate_data(energy_data)
# calling validate data function

print(f"Error Found: {data}")


# ## CHALLENGE

# In[63]:


## Energy Efficiency Score
def calculate_efficiency_score(energy_data):
    """ Calculate efficiency score based on parameters selected in the ranges of 0 throug 100"""

    print("==============================================================")
    print("                  EFFICIENCY SCORE                            ")
    print("==============================================================")

    for customer in energy_data:
        # loops through the data set
        score = 0
        # initializing score to Zero

        conservation_points = 0
        # initialising conversion points to Zero

        # getting values from the list
        customer_id = customer["customer_id"]
        customer_name = customer["customer_name"]
        customer_type =  customer["customer_type"]
        location = customer["location"]
        month = customer["month"]
        consumption = customer["consumption_kwh"]
        tariff = customer["tariff_per_kwh"]
        peak_consumption = customer["peak_consumption_kwh"]
        renewable_share = customer["renewable_share"]
        outage_hours = customer["outage_hours"]
        payment_status =  customer["payment_status"]

        # Energy conversion performance

        if consumption < 500:
            conservation_points = 40
            # if consumption values returns true, user gains 40 points
        elif consumption < 1000:
            conservation_points = 25
            # if consumption values returns true, user gains 25 points
        else:
            # else, user gains 10 points
            conservation_points = 10


        score += conservation_points
        # updating customer score 

        # Renewable energy opportunities

        renewable_point = 0
        # initialising renewable points to Zero

        if renewable_share >= 15:
            renewable_point = 40
            # if renewable share values returns true, user gains 40 points
        else:
            # else, user gains 1 points
            renewable_point = 10

         # updating customer score
        score += renewable_point


        # Outage analysis

        # initialising outage points to Zero
        outage_points = 0

        if outage_hours < 2:
            outage_points = 20
             # if outage hours returns true, user gains 20 points
        elif outage_hours < 5:
            outage_points = 10
           # if outage hours returns true, user gains 10 point
        else:
            # else, user gain zero points
            outage_points = 0

        # update user score
        score += outage_points

        # returns print statement
        print(f"""
        Customer: {customer_name}
        Customer Type: {customer_type}
        Consumption Grade: {conservation_points}
        Clean Energy : {renewable_point}
        Power Outage: {outage_points}
        Efficiency_Score: {score}%
        """)

        # if aggregated score is true, return print statement
        if score < 50:
            print("Critical Focus: High opportunities for infastructure")
        elif score < 80:
            print("Moderate: Target Outage or expand renewable options")
        else:
            print("Excellent: High Efficiency Operational Profile")

        print()
        print("==============================================================")     
# calling efficiency score function        
calculate_efficiency_score(energy_data)           













# In[64]:


## Top Ten customer by consumption using Bubble sort
def calculate_top_10_customers(energy_data):
    """ This calculates the top ten 10 customers by consumption using the bubble sort """

    print("=============================================================")
    print("                   TOP 10 CUSTOMERS                          ")
    print("=============================================================")
    top_customers = []
    # stores output as a list

    for customer in energy_data:
        top_customers.append(customer)
        # loops through customers and adds to the top customer list


    n = len(top_customers)
    # counts nuumber of customers in the top customer list

    for i in range(n):
        for j in range(0, n-i-1):
            # This loops through the list until the customers is properly arranged
            if top_customers[j]["consumption_kwh"] < top_customers[j + 1]["consumption_kwh"]:
                 # changes the position of top customers using the logical statement
                temporary_storage = top_customers[j]
                top_customers[j] = top_customers[j + 1]
                top_customers[j + 1] = temporary_storage
    rank = 1
    # initialising counter to 1

    for k in range(10):
        # loops through the first 10 customers
        if k < len(top_customers):
            customer = top_customers[k]
            electricity_cost = customer["consumption_kwh"] * customer["tariff_per_kwh"]
            status = high_attention_customers(energy_data)[0]

            # returns print statement
            print(f"""
            {rank}. 
            Customer ID: {customer["customer_id"]}
            Customer Type: {customer["customer_type"]}
            Location: {customer["location"]}
            Consumption: {customer["consumption_kwh"]}kwh
            Electricity Cost:  ₦{electricity_cost}
            Renewable Share: {customer["renewable_share"]}
            """)
            print("=============================================================")
            # update counter
            rank += 1

# calling top 10 customer function
calculate_top_10_customers(energy_data)



# In[65]:


## Evaluating Consumption against Outages

def analyse_consumption_outage(energy_data):
    """ Investigates if higher outage correspond with lower consumption"""

    print("==============================================================")
    print("OUTAGE GROUP BY PERCENTAGE AVERAGE INCOME                     ")
    print("==============================================================")

    # initialising counters and aggregates to Zero
    low_outage_total = 0
    low_outage_count = 0

    high_outage_total = 0
    high_outage_count  = 0

    for customer in energy_data:
        # loops through energy data
        outage = customer["outage_hours"]
        consumption = customer["consumption_kwh"]

        if outage < 10:
            # if codition returns true, excecute the next code
            low_outage_total += consumption
            low_outage_count += 1
        else:
            # else, execute this
            high_outage_total += consumption
            high_outage_count += 1

    if  low_outage_count > 0:
        # if codition returns true, excecute the next code
        low_output_average = low_outage_total / low_outage_count 
    else:
         # else, execute this
        low_output_average = 0

    if high_outage_count > 0:
        # if codition returns true, excecute the next code
        high_output_average = high_outage_total / high_outage_count
        # returns high output average
    else:
        # else, zero
        high_output_average = 0

    return high_output_average,  low_output_average

# calling consumption outage function
high_outage, low_outage = analyse_consumption_outage(energy_data)           

# return print statement
print(f"High Outage Group: {high_outage:.2f}kwh")
print(f"Low Outage Group: {low_outage:.2f}kwh")
print()

if high_outage < low_outage:
    # if high outage is less than low outage, return following print statement
    print("Conclusion: Higher output exposure corresponds with lower recorded consumption")
else:
    # else, return this
    print("Conclusion: Higher output exposure does not correspond with lower recorded consumption")






# In[67]:


## Energy Affordability

# Assumed Average income of a Nigerian 
assumed_income = 150000

def analyse_energy_affordability(energy_data):
    """ This function calculates the elcectricity cost as a percentage of the average income"""

    print("==============================================================")
    print(" ELECTRICITY AFFORDABILITY BY AVERAGE INCOME                  ")
    print("==============================================================")

    for customer in energy_data:
        customer_type = customer["customer_type"]
        consumption = customer["consumption_kwh"]
        tariff = customer["tariff_per_kwh"]

        electricity_cost = consumption * tariff

        cost_percentage = (electricity_cost / assumed_income) * 100

        # classiying affordability based on standard metric
        if cost_percentage <= 60:
            category = "Affordable Burden"
        elif cost_percentage <=100:
            category = "Moderate Burden"
        else:
            category = "High Burden"

        # return print statement
        print(f" Customer Type: {customer_type}")
        print(f" Electricity Cost: ₦ {electricity_cost}")
        print(f" Percentage of Income: {cost_percentage:.2f}%")
        print(f" Affordability: {category }")
        print("==============================================================")
analyse_energy_affordability(energy_data)       


# In[ ]:




