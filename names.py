# Part 1 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


# for i in students:
#     print i

def printNames():
    for group in users:
        print group

print printNames()

#         print users
#     return key

# print names() 

# function printName(){
# 		 	for (var group in users){
# 		 		console.log(group);
# 		 		for (var i = 0 ; i < users[group].length; i++){
# 		 			var fullname = users[group][i].first_name + " " + users[group][i].last_name
# 		 			console.log(fullname);
# 		 		}
# 		 	}

# 		 }

# 		 printName();