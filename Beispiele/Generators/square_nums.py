def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i**2)
    return result

my_numbers = square_numbers([1, 2, 3, 4, 5])
print(my_numbers)


# as generator
def square_numbers_gen(nums):
    for i in nums:
        yield i**2

my_numbers = square_numbers_gen([1, 2, 3, 4, 5])
print(my_numbers) # generator object, weil generators nicht alles im Speicher vorhalten
# stattdessen
# print(next(my_numbers))
# print(next(my_numbers))
# print(next(my_numbers))
# print(next(my_numbers))
# print(next(my_numbers))
# print(next(my_numbers)) # StopIteration error, weil keine Werte mehr verfügbar sind

# so oft nutzbar:
for num in my_numbers:
    print(num)

    # 1. lesbar, weil Werte nach und nach zurückgegeben werden
    # 2. keine Speicherüberladung

# theoretisch möglich, aber man verliert alle Performance Vorteile
my_numbers = square_numbers_gen([1, 2, 3, 4, 5])
print(list(my_numbers))
