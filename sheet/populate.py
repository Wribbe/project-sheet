import sqlite3
import random
from sheet import db

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
ALPHABET = sorted(VOWELS+CONSONANTS)

db.init()

def _name():
    letters = []
    for _ in range(random.randint(3,8)):
        if len(letters) > 2 and all([c in CONSONANTS for c in letters[:-2]]):
            pool = VOWELS
        elif letters and letters[-1] in VOWELS:
            pool = CONSONANTS
        else:
            pool = random.choice([VOWELS, CONSONANTS])
        letters.append(random.choice(pool))
    return ''.join(letters).title()


def users(num_users=10):
    for _ in range(num_users):
        max_tries = 40
        try_current = 0
        while True:
            try_current += 1
            if try_current >= max_tries:
                print("WARNING: Could not generate non-colliding user.")
                break
            name = _name()
            try:
                db.user_create(name)
            except sqlite3.IntegrityError:
                continue
            break
        print(f"Populated database with {name}.")
