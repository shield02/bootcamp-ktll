# Type hinting
"""
Type hints or annotations are special syntax that allows declearing of
type of a variable. By declearing types of your variables, editors and
other tools can give you better support like suggestions on methods
based on the type of a variable you are working with.
"""
def full_name(firstname: str, lastname: str) -> str:
    full_name = firstname.title() + " " + lastname.title()
    return full_name

def fullname(firstname: str = "john") -> str:
    full_name = firstname + " " + "doe"
    return full_name

def get_name_and_age(name: str, age: int) -> str:
    name_with_age = name + " is this years old:" + str(age)
    return name_with_age

print(get_name_and_age("John", 45))

print(full_name("john", "doe"))

# Generic type
"""
They are called generic types because the are made up of some inner structure usually
from primitive data types.
This generic types always have what is called parameters.
Example: list -> [str, int, str, float, bool]

When working with these generic types Python support for it is not the same throughout
all Python versions.

In Python verions 3.6 to 3.9 you will need to be using the `typing` python standard
module to have the type hinting or anotation features.
"""
# LIST
# A list of string values
names = ['john', 'doe', 'rob', 'itoro']

# syntax for 3.10
def capitalize_names(names: list[str]) -> None:
    for name in names:
        print(name.title())

def title_names(names_tuple: tuple[int, int, str],
                names_set: set[str]) -> None: # this is for 3.10
    return names_tuple, names_set

def title_names(names_tuple: int | str,
                names_set: set[str]) -> None: # this is for 3.10
    return names_tuple, names_set

def process_items(items: dict[str, float]): # str is the dt key, float is the dt for value
    for k, v in items.items():
        print(k)
        print(v)

def greetings(name: str | None = None):
    if name:
        print(f"Hello {name}")
    else:
        print("Hello stranger!!!")

def greetings(name: Optional[str] = None):
    if name:
        print(f"Hello {name}")
    else:
        print("Hello stranger!!!")


# syntax for 3.8+
from typing import List, Tuple, Set, Dict, Union, Optional

def cap_names(names: List[str]) -> None:
    for name in names:
        print(name.title())


def title_names(names_tuple: Tuple[int, int, str],
                names_set: Set[str]) -> None:
    return names_tuple, names_set

def process_items(items: Dict[str, float]): # str is the dt key, float is the dt for value
    for k, v in items.items():
        print(k)
        print(v)

def title_names(names_tuple: Union[int, str],
                names_set: set[str]) -> None: # this is for 3.10
    return names_tuple, names_set

def greetings(name: Optional[str] = None):
    if name:
        print(f"Hello {name}")
    else:
        print("Hello stranger!!!")

def greetings(name: Union[str, None] = None):
    if name:
        print(f"Hello {name}")
    else:
        print("Hello stranger!!!")

# Classes as types
class Person:
    def __init__(self, name: str) -> None:
        self.name = name

def get_person_name(person: Person):
    return person.name
