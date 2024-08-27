my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

values_to_add = [50, 60, 70]

my_list.extend(values_to_add)

my_list.pop()

my_list.sort()

index = my_list.index(30)
print(f"The index of '{30}' is {index}.")

print(my_list)