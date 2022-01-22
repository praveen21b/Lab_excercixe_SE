from NewPackage1 import test1
#import test1

(test1.printing())

data = {'name': 'Praveen',
        'age': 31,
        'Places_lived': ['Dharwad', 'Gadag', 'Bengaluru', 'Pune', 'Siegen']}


def get_name():
    return data['name']


def get_age():
    return data['age']


def get_place():
    return data['Places_lived']