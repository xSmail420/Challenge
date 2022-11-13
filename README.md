# My Solution

My solution for this challenge using python is to open the json file and load it,
searching for items based on a key and quick access time is an important requirement,
unique keys are available for the data we want to store, and that leaves us to 
iterate through the items to compaire the data with the one we're 
searching for .Once we get it (product id) all we have left to do is to append in a list 
the other items in the json file that describe the same product and then return the list

# How to get it to work

1.Fill the _id with the key used as product id 
  in the json file
2.Fill the file_path with the json file path 
  (Preferably downloaded in the same folder/repository)
3.enter the id of the product in id_s in the main 

```
{
    def find_item_list(item_id):
        _id = '_id'
        file_path = '' 
}
```

```
{
    id_s=""
    print(find_item_list(id_s))
}
```

# ClickN Challenge

ClickN Challenge for matching algorithm

## Challenge Description

We have a json file that contain products from different sources
The items have the same field structure as follows:

```
{
    "_id", // id for the item: type ObjectId
    "store", // contains store name: type string
    "category", // contains category of said item : type string
    "brand", // contains item brand: type string
    "name", // contains product name: type string
    "description", // contains description of the product: type string
    "image", // contains a link to the image of the product: type string
    "measurement", // contains the measurement of the product: type string
    "price", // contains the price of the product: type double
}
```

We want a function that would take the id of a product and return a list of the other items in the json file that describe the same product

```
find_item_list(string item_id):
return(list)
```

## Rewards
1. Cash prize of $100
2. Chance to join our startup team

## Submission Requirements
1. Implementation of the solution. (Preferably in Python but not mandatory)
2. Documentation on dependencies and how to build your solution (e.g. Makefile, shell scripts, requirements.txt files)
3. Include a separate descriptive file as a writeup of how you approached solving the challenge. (Preferably as PDF)
4. Submissions are done via branches based on main branch. Use relevant github account names to easily identify the person.

## Criteria for challenge submission
1. Challenge will have a deadline of 1 week. (Final submissions date: November 14rd 2022)
2. Challenge should make use of parsed_data.json file provided. First make sure to extract the parsed_data.7z to get the json file
3. Challenge should meet challenge guidelines and requirements stated above.
