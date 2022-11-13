import json


def find_item_list(item_id):

    _id = '_id'  # id for the item
    file_path = ''  # json file path
    item_list = []

    # opening json file
    f = open(file_path)
    res = json.load(f)
    # iterating through json data
    for item in res:
        # exception in case the key "_id" does not exist
        try:
            # looking for the given item id
            if(item[_id] == item_id):
                break
        except KeyError:
            pass

    for key in item.keys():
        # appending the list with the other items of the same product
        if (key != _id):
            item_list.append(item[key])

    return item_list

id_s=""
print(find_item_list(id_s))
