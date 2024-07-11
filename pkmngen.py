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

