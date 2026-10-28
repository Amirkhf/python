ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# remplace la valeur de l'indice 1 par world
ft_list[1] = 'World!'

# ça nous permet de repartir de zéro et de mettre de nouvelles valeurs
ft_tuple = ("Hello", "France!")

# on ne peut pas accéder à un élément via son indice quand c'est un set
# donc on supprime l'élément pas sa valeur
ft_set.remove('tutu!')
# et on ajoute l'élément que l'on veut à la fin
ft_set.add('Paris!')
# on va chercher la clé puis on modifie sa valeur
ft_dict['Hello'] = '42Paris!'
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)