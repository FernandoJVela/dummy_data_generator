import random

def generate_random_roles():    
    roles_list = ['admin', 'default', 'client', 'sales']
    num_roles = random.randint(0, len(roles_list))
    selected_roles = random.sample(roles_list, num_roles)
    return selected_roles