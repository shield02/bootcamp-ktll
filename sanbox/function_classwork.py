def print_full_name(full_name):
    print(full_name)


my_full_name = 'Uduak Edikan Eti-mfon'
print_full_name(my_full_name)


def print_full_name_with_return(full_name):
    return full_name


print_full_name_with_return(my_full_name)


result = print_full_name


def print_fll_name(first_name, last_name):
    print(first_name + ' ' + last_name)


my_first_name = 'Uduak'
my_last_name = 'Eti-mfon'
my_full_name = my_first_name + ' ' + my_last_name
print_fll_name(my_first_name,  my_last_name)


def print_fll_name_with_return(first_name, last_name):
    return first_name,  last_name


print(print_fll_name_with_return(my_first_name, my_last_name))
output = print_fll_name_with_return(my_first_name, my_last_name)
print(output)

first_nom = input('Enter your first name: ')
last_nom = input('Enter your last name: ')

