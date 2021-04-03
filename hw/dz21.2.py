dict_ = {}

for i in range(1, 101):
    dict_[i] = i**2

dict_new = {}

for key, value in dict_.items():
    key, value = value, key
    dict_new[key] = value
dict_ = dict_new
print(dict_)
print(len(dict_))
