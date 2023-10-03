## grafos
Em base fazer um caixeiro viajante


Baseando-se no algoritmo de Kruskal e um problema classico, problema da mochila
que consistemem ter a melhor carga com maior volor, tendo o menor percurso possivel,


# Passo a passo

1 => Primeiro passo vai ser definir o tamanho da carga e o destino,
os rotas vamos tratar como um grafo, cada cidade tem pelo menos um cidade de destino
para faciliatar faremos um especie de banco de dados com excel, para ficar gravado as
arestas, que serão uma classe que vai ter origem,destino,distancia;

2 => criar uma classe carga que vair um id, um destino , um peso, um valor
criar um caminhão (mochila) e definir o peso por ela suportado, e achar a combinação com 
maior valor d carga possivel

3 => depois de definir a carga, pegar os destino e fazer um caminho minimo que ligue todas as cidades 
e volte para a origem da empresa 


