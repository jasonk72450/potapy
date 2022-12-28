import os
import random
import sys


def get_random_text(filename):
    file_location = os.path.join('data', filename)
    with open(file_location, "r") as file:
        lines = file.readlines()
        return random.choice(lines).strip()


def print_and_write_file(_id, content):
    print(f"\npota {_id}:\n")
    print(content)

    filename = f"pota_{_id}.txt"
    with open(filename, "w") as file:
        file.write(content)


def generate_all():
    other_call = get_random_text("call_signs.txt").upper()
    rst = get_random_text("rst.txt").upper()
    park = get_random_text("pota_parks.txt").upper()
    pota_state = get_random_text("pota_states.txt").upper()
    text_cq = pota_cq(other_call, park)
    print_and_write_file("pota_cq", text_cq)
    text1 = pota_1(other_call, rst, pota_state)
    print_and_write_file(1, text1)

 
def pota_cq(other_call, park):
    return f"""
CQ POTA {other_call} {park} K
    """.strip()


def pota_1(other_call, rst, pota_state):
    return f"""
{my_call} {rst} {pota_state} TU
    """.strip()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        my_name = sys.argv[1]
        my_call = sys.argv[2]
    else:
        my_call = ("KE5JLN").upper()
        generate_all()
