import random

def generate_random_email():
    domains = ["example.com", "mail.com", "test.com"]
    name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=random.randint(5, 10)))
    domain = random.choice(domains)
    return f"{name.lower()}@{domain}"