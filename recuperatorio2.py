from grafo import Grafo
from heap_min import Heap
from lista import Lista

# 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:
mi_grafo = Grafo(dirigido=False)

# a) cada vértice debe almacenar el nombre de un personaje, las aristaas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
#a. insertar los vertices del grafo
# d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO,
#  Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.
mi_grafo.insert_vertice('Luke Skywalker')
mi_grafo.insert_vertice('Darth Vader')
mi_grafo.insert_vertice('Yoda')
mi_grafo.insert_vertice('Boba Fett')
mi_grafo.insert_vertice('C-3PO')
mi_grafo.insert_vertice('Leia')
mi_grafo.insert_vertice('Rey')
mi_grafo.insert_vertice('Kylo Ren')
mi_grafo.insert_vertice('Chewbacca')
mi_grafo.insert_vertice('Han Solo')
mi_grafo.insert_vertice('R2-D2')
mi_grafo.insert_vertice('BB-8')

#b. insertar las aristas del grafo
mi_grafo.insert_arista('Luke Skywalker', 'Darth Vader', 7)
mi_grafo.insert_arista('Darth Vader', 'Yoda', 7)
mi_grafo.insert_arista('Yoda', 'Boba Fett', 8)
mi_grafo.insert_arista('Boba Fett', 'C-3PO', 9)
mi_grafo.insert_arista('C-3PO', 'Leia', 10)
mi_grafo.insert_arista('Leia', 'Rey', 11)
mi_grafo.insert_arista('Rey', 'Kylo Ren', 12)
mi_grafo.insert_arista('Kylo Ren', 'Chewbacca', 13)
mi_grafo.insert_arista('Chewbacca', 'Han Solo', 14)
mi_grafo.insert_arista('Han Solo', 'R2-D2', 16)
mi_grafo.insert_arista('R2-D2', 'BB-8', 18)
mi_grafo.insert_arista('BB-8', 'Luke Skywalker', 3)
mi_grafo.insert_arista('BB-8', 'Darth Vader', 3)
mi_grafo.insert_arista('Luke Skywalker', 'Boba Fett', 4)
mi_grafo.insert_arista('Darth Vader', 'C-3PO', 2)
mi_grafo.insert_arista('Luke Skywalker', 'Yoda', 7)
mi_grafo.insert_arista('Luke Skywalker', 'Han Solo', 7)

# c) Determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son.
max_episodes = 0
characters_with_max_episodes = []

for personaje1 in mi_grafo.vertices:
    for personaje2 in mi_grafo.vertices:
        if personaje1 != personaje2:
            episodes = mi_grafo.get_peso_arista(personaje1, personaje2)
            if episodes > max_episodes:
                max_episodes = episodes
                characters_with_max_episodes = [(personaje1, personaje2)]
            elif episodes == max_episodes:
                characters_with_max_episodes.append((personaje1, personaje2))

print("C. Máximo número de episodios compartidos:", max_episodes)
print("   Personajes con el máximo número de episodios compartidos:", characters_with_max_episodes)
print("-----------------------------------------------------------------------------------")

# e) Hallar el camino más corto desde Yoda a Rey.
camino_corto = mi_grafo.dijkstra('Yoda', 'Rey')

if camino_corto:
    print("E. Camino más corto desde Yoda a Rey:", camino_corto)
print("-----------------------------------------------------------------------------------")
