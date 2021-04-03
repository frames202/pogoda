import random
dict_ = {}
list_ = []
dict_new = {}

while len(dict_) < 10:
    dict_[random.randint(1, 100)] = random.randint(1, 20)
print(dict_)

for key, value in dict_.items():
    key, value = value, key
    list_ = []
    if key in dict_new.keys():
        v = dict_new[key]
        list_.append(value)
        if isinstance(v, list):
            list_.extend(str(v))
        else:
            list_.append(v)
        dict_new[key] = list_
    else:
        dict_new[key] = value

dict_ = dict_new
print(dict_)
