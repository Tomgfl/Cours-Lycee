# laff cest la liste a afficher
# [Article,Article,...]


while laff:
	mini = laff[0].prix
	art = laff[0]
	id_art = 0
	for i in range(len(laff)):
		if laff[i].prix < mini:
			art = laff[i]
			id_art = i
	print(art.prix,art.nom)
	laff.pop(id_art)
