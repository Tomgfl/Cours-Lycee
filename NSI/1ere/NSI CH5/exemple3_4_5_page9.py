#exemple 3

print(sorted(['bb', 'aaa'])) # ordre lexicographique par défaut [’aaa ’, ’bb ’]
print(sorted(['aaa', 'bb'], key=len)) # longueur [’bb’, ’aaa ’]



#exemple 4
def f(x):
    return x*2

g = lambda x: x*2

print(f(3))
print(g(3))



#exemple 5

ma_table =[{'Nom':'Baron','Prenom':'Paul','NSI':'18','Physique ':'16','Maths':'15'},
{'Nom':'Taillant','Prenom':'Greg','NSI':'1','Physique':'3','Maths':'5'},
{'Nom':'Gourdy','Prenom':'Zoé','NSI':'14','Physique ':'13','Maths':'16'}]

table_triee=sorted(ma_table, key=lambda lyceen: lyceen["NSI"])

print (table_triee)

