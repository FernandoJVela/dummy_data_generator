import random
import os

first_names = ["John", "Emma", "Michael", "Sophia", "James", "Olivia", "Robert", "Ava", "William", "Isabella",
               "Carlos", "Maria", "Juan", "Ana", "Luis", "Sofia", "Diego", "Valentina", "Pedro", "Camila",
               "Hiroshi", "Yuki", "Aoi", "Haruto", "Sakura", "Takashi", "Yui", "Naoki", "Hina"]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
              "Gonzalez", "Lopez", "Hernandez", "Perez", "Sanchez", "Torres", "Ramirez", "Rivera", "Cruz", "Diaz",
              "Suzuki", "Tanaka", "Watanabe", "Ito", "Yamamoto", "Nakamura", "Kato", "Sato", "Kobayashi", "Takahashi"]

def generate_full_names(num_names):
    full_names = []
    for _ in range(num_names):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        full_names.append(f"{first_name} {last_name}")
    return full_names

def save_to_txt(names_list):
    with open("random_names.txt", "w") as file:
        for name in names_list:
            file.write(name + "\n")

def check_names_availability():
    names_file_path = "random_names.txt"
    if ~os.path.exists(names_file_path):
        random_names = generate_full_names(100)
        save_to_txt(random_names)

def get_random_name():
    with open("random_names.txt", 'r') as file:
        lines = file.readlines()
        return random.choice(lines).rstrip()    