dicts={
    'Name':'Rajveer',
    'Sex':'Male',
    'Age':18,
    'Country':'Indian'
}
print(dicts.popitem())
print(dicts)
print(dicts.pop('Sex'))
print(dicts)
dicts.clear()
print(dicts)
#clear method is used to clear the dictonary items
dics={
    'Name':'Rajesh',
    'Age':25,
    'Sex':'Male',
    'Nationality':'Indian'
}
news=dics.copy()
print(news)
#the copy method creates a shallow copy of the dictonary
dicts={}.fromkeys([1,2,3,4,5,6],3)
print(dicts)
n=dics.get('Name','Rajesh')
print(n)
dics.popitem()
print(dics)
dics.popitem()
print(dics)
