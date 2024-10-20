# Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Aurora',
    'last_name': 'Luna',
    'age': 6,
    'country': 'Indonesia',
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Jl. Jalan',
        'zipcode': '123456'
    }
}
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

# Check if the person dictionary has skills key, if so check if the person has ‘Python’ skill and print out the result.

# If a person skills has only JavaScript and React, print(‘He is a front end developer’), if the person skills has Node, Python, MongoDB, print(‘He is a backend developer’), if the person skills has React, Node and MongoDB, Print(‘He is a fullstack developer’), else print(‘unknown title’) - for more accurate results more conditions can be nested!

# If the person lives in Indonesia, print the information in the following format:

# Aurora Luna lives in Indonesia.

if "skills" in person.keys():
   print("Middle skill in skill list :",person['skills'][int((len(person['skills']))/2)])
   print("Is python in skill list? Yes") if "Python" in person['skills'] else print("Is python in skill list? No")

   if "React" in person['skills']:
      if "Node" in person['skills'] or "MongoDB" in person['skills']:
         print("He is a fullstack developer")
      if "Javascript" in person['skills'] and "Node" not in person['skills']:
         print("He is a front end developer")
   elif "Node" in person['skills'] and "Javascript" not in person['skills']:
      print("He is a back end developer")
   else:
      print("Unknown title")

if person["country"] == "Indonesia":
   print(f"{person['first_name']} {person['last_name']} lives in {person['country']}")
