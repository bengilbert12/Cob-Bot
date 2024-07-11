import random
from tinydb import TinyDB, Query

db = TinyDB('db.json')

poke_table = db.table("pokemon")
trainer_table = db.table("trainers")
pokes = poke_table.all()



def gen_pok():
    poke = random.choice(pokes)
    mon = str(poke['name'])
    return mon


def check_pok(user):
    User = Query()
    if trainer_table.search(User.name == user):
        return User['pokemon']
    else:
        return False

def verify_level(username):
    User = Query()
    does_exist = trainer_table.search(User.name == username)
    print(does_exist)
    if not does_exist:
        return 0
    elif does_exist:
        atemp = does_exist[0]['can_level']
        if atemp == 'False' or not atemp:
            return 1
        elif atemp == 'True':
            new_level = does_exist[0]['level'] + 1
            trainer_table.upsert({'can_level': 'False', 'level': new_level}, User['name'] == username)
            return 2
        else: print('error 1')
    else: print('error 2')