sets={"here","there","about"}
for elemt in sets:
    print(elemt)
sets={'a','b','c','d'}
for i in sets:
    print(i)
sst={"Aditi","Aditi","Nirbhaya"}
#sets does'nt accept the duplicate elements
for elemt in sst:
    print(elemt)
sst.add('raman')
sst.add('rajesh')
print(len(sst))
print(type(sst))
#dict() ,set()
#for eg
d=dict(name="Nitin",Age=17,Sex='male')
print(d)
set={
    'a','b','c','d'
}
print(set)
for element in set:
    print(element)
print('a' in set)
#update elemnt to add a new set
#for eg
s={'a','b','c','d'}
e={'f','g'}
i={'g','h','i'}
s.update(e)
s.update(i)
print(s)
#remove any element from the set is removable by the .remove()
#for eg
s.remove('a')
print(s)
s.remove('d')
s.discard('g')
#discard() is also like an remove() function
#remove() function is used to remove elements if there is not such elements in the set they gave an error
s.pop()
print(s)
sset={
    'This','There','Thus','Here'
}
sset.pop()
print(sset)
string="this si an string"
n='#'.join(string)
print(n)
#sets methods like intersection(),union() etc
s1={
    'Britain',
    'USSR',
    'Usa',
    'Germany',
    'Japan',
    'China'
}
s2={
    'India',
    'Mexico',
    'South Africa'
    'USSR'
}
p=s1.intersection(s2)
print(p)
europe={
    'Germany',
    'France',
    'Denmark',
    'Swizertland'
}
S_Asia={
    'Cambodia',
    'Thailand',
    'Myammar',
    'Vietnam'
}
Other_asia={
    'China',
    'India',
    'Austrailia',
    'Newzeland',
    'Israel'
}
p=europe.union(S_Asia)
q=europe.union(Other_asia)
print(p,q)
#intersection()
print(europe.intersection(S_Asia))
Other_asia.add('Russia')
europe.add('Russia')
print(Other_asia.intersection(europe))
#India china conflict alies situation
India_alies={
    'UAE',
    'USA',
    'Britain',
    'Israel',
    'Greece',
    'France'
}
China_alies={
    'Pakistan',
    'Nepal',
    'Bangladesh',
    'Srilanka',
    'Cambodia'
}
Netural={
    'Russia',
    'South east asia',
    'OIC'
}

ind=India_alies.intersection(Netural)
china=China_alies.intersection(Netural)
print(ind,china)
Names={
    'Arvind','Gajraj','Himanshu'
}
Names2={'Kartikey','Jaideep','Himanshu'}
s=Names.intersection(Names2)
print(s)
x={'Cheery','Microsoft','Azure'}
y={'Apple','Mango','China'}
a=x.intersection(y)
b=x.difference_update(y)
c=x.symmetric_difference_update(y)
print(x)
x.symmetric_difference(y)
print(x)
a={'x','y','z'}
b={'a','b','c','x','y','z'}
p=a.issubset(b)
s=b.issuperset(a)
print(p,s)
