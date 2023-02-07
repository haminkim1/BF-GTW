import os
import hashlib


url = "https://eaassets-a.akamaihd.net/battlelog/battlebinary/gamedata/Casablanca/12/71/MG34-f447ad5e.png"

filename = url.split("/")[-1]

# def remove_elements_before_index(lst, index):
#     return lst[index:]




my_list = [1, 2, 3, 4, 5, 6, 7]
# new_list = remove_elements_before_index(my_list, 4)
new_list = my_list[0:]
print(new_list)
# Output: [5, 6, 7]