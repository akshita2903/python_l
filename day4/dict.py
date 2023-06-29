dict={
    "hello" : "In Normal way",
    'xie xie':"Thank you",
    "list":[1,2,3,4],
    "another_dict":{
        "key1":"value1",
        "key2":"value2"
    },
    5:120
}
# print(dict["hello"])
# print(dict["another_dict"]["key1"])
# print(dict[5])
# print(dict.keys(),type(dict.keys())) print keys of dict
print(dict.values()) #print values

#ite,s
print(dict.items()) #print key value pair of dictionary in tuples form

#update dictionary
dict["hello"]="find"
dict.update({"Good":"Friend"})
print(dict)