#Update Values in Dictionaries and Lists


x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name' : 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Rodney', 'last_name' : 'Bautista'},
    {'first_name' : 'Selena', 'last_name' : 'Chheang'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

"""
#1 Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
def change_x(var):
    var[1][0] = 15

change_x(x)
print(x)

#2 Change the last_name of the first student from 'Jordan' to 'Bryant'
def change_last(last):
    last[0]['last_name']= 'Bryant'

change_last(students)
print(students)

#3 In the Sports_directory, change 'Messi to Andres'
def change_first(sports_directory):
    sports_directory['soccer'][0] = 'Andres'

change_first(sports_directory)
print(sports_directory)

#4 Change the value 20 in z to 30
def change_val(z):
    z[0]['y'] = 30

change_val(z)
print(z)


#Get Values From a List of Dictionaries
def all_values(some_list):
    for dictionary in some_list:
        new_string = ""
        for key, value in dictionary.items():
            new_string += key +' - ' + value + ', '
        print(new_string[:-2])

all_values(students)


def iterateDictionary2(key_name):
    for dictionary in key_name:
        first_name = ""
        for key,val in dictionary.items():
            first_name += val
            break
        print(first_name)

iterateDictionary2(students)

"""

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def dojo_list(some_dict):
    for key, value in some_dict.items():
        my_string = ""
        my_string += '7 ' + key + str(value)
        if key == 'locations':
            print(my_string[:-1])
        if key == "instructors":
            inst_list = ""
            inst_list = '8 ' + key + str(value)
            print(inst_list[:-1])
dojo_list(dojo)

