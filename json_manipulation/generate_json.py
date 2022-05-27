import json
import random
import time
t = 0

def gen_person():
    name = ''
    tel = '088'
    global t

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 5:
        name += random.choice(letters)

    while len(tel) <=8:
        tel += random.choice(nums)
    t += 1
    person = {'name': name, 'tel': tel, 'time': t}
    return person

def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except:
        data = []
    data.append(person_dict)
    with open('persons.json', 'w') as file:
        json.dump(data, file, indent=3)


l = []
for i in range(5):
    write_json(gen_person())



