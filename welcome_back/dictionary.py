value = dict(name="Mr sam", age=30)
print(value)
print(value['name'])

dictionary = {
    "Name": "Felix",
    "age": 30,  
    "Skill": {
        "Soft": [
            "Hardworking",
            "Diligent",
            "Brilliant"
        ],
        "Tech": [
            "Full Stack Engineer",
            "Backend Engineer",
            "Programming"
        ]
    }
}
print(dictionary)
print(dictionary["Name"])
print(dictionary["Skill"]["Tech"][1])
