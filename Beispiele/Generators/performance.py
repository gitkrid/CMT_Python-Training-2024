import random
import time
# from memory_profiler import profile
import sys


# print(f"Speicher vor Start: {mem_profile.memory_usage()[0]} MB")

vornamen = ["Johannes", "Lara", "Petra", "Stefan", "Sabine"]
nachnamen = ["Müller", "Krause", "Schreiber", "Meyer", "Schäfer"]



def menschen_liste(anzahl):
    result = []
    for i in range(anzahl):
        person = {
            "id": i,
            "vorname": random.choice(vornamen),
            "nachname": random.choice(nachnamen)
        }
        result.append(person)
    return result

def menschen_gen(anzahl):
    for i in range(anzahl):
        person = {
            "id": i,
            "vorname": random.choice(vornamen),
            "nachname": random.choice(nachnamen)
        }
        yield person


t1 = time.time()
menschen = menschen_liste(1000000)
t2 = time.time()
print(f"Zeit: {t2 - t1} s")

# print(f"Speicher am Ende: {mem_profile.memory_usage()[0]} MB")
print(f"Speicherbedarf: {sys.getsizeof(menschen)} Bytes")

