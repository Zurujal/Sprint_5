from faker import Faker
from random import randint


def generate_name():
    fake = Faker()
    return fake.name()


def generate_email():
    return f'kuznetsovsergei11{randint(000, 999)}@ya.ru'


def generate_password():
    return "".join(chr(randint(33, 125)) for _ in range(12))
