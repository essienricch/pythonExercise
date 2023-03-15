import json


def my_json_dump(my_list):
    my_json_list = 'my_list.json'
    with open(my_json_list, 'w') as file_object:
        json.dump(my_list, file_object)
        print('i will remember you')


def my_json_load(my_list):
    new_list = 'my_list.json'
    with open(new_list) as file:
        file_obj = json.load(file)
        print(file_obj)
