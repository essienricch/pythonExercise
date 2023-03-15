
from json_module import json_format

if __name__ == '__main__':
    list_one = ['football', 'movies', 'dance']
    my_list = {"name": "rich", "gender": "male", "class": "C13", "hobbies": ['football', 'movies', 'dance']}
    json_format.my_json_dump(my_list)

    json_format.my_json_load(my_list)

