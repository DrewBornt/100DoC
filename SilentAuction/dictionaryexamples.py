# dict = {
#     "Key": "Value",
#     "OtherKey": "OtherValue",
#     3: 3,
# }

# print(dict["Key"])
# print(dict[3])

# dict["newKey"] = "newValue Added to the dictionary"

# print(dict)

# dict["Key"] = "Changed Value"
# dict[3] = 4

# print(dict)

# for keyPair in dict:
#     print(keyPair)
#     print(dict[keyPair])

# emptyDict = {}
# dict = emptyDict

# print(dict)

# Nested list in a dictionary
travelLog = {
    "France": ["paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
} 
# Nested list in a nested dictionary in a dictionary
travelLog = {
    "France": {
        "Cities Visited": ["Paris", "Lille", "Dijon"], 
        "Total Visits": 12},
    "Germany": {
        "Ciities Visited": ["Berlin", "Hamburg", "Stuttgart"],
        "Total Visits": 10},
}

# Nesting Dictionary in a List

otherTravelLog = [
    {
        "country": "France",
        "cities visited": ["Paris", "Lille", "Dijon"],
        "total visits": 5
    },
    {
        "country": "Germany", 
        "cities visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total visits": 6
    },
]

print(otherTravelLog)