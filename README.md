# Introdução à Matemática e Física Para Videojogos I - Relatório Projeto Individual

## Controlos Esfera
* Como primeira parte do projeto, a alteração dos controlos do viewer da esfera, de modo a que fosse possivel controlar a esfera a partir das teclas. Para tal, foi reutilizado parte de código já imposta no programa que fazia a esfera rodar por si só, alterando para que consoante a tecla pressionada fosse possivel rodar a esfera e até mesmo movimenta-la pela tela.

        ax = (axis * math.radians(angle) * delta_time)

        q = Quaternion.AngleAxis(axis, math.radians(angle) * delta_time)
        obj1.rotation = q * obj1.rotation

## Viewer e Loader de Ficheiros .Obj
* Para a criação do ficheiro [obj_loader.py], foram utilizadas algumas bibliotecas diferentes, estas como [pyWavefront] e [OpenGL], duas bibliotecas que ajudam na leitura de objetos 3D (.obj, .mtl, .gz).
* Na construção do código, foi utilizado sites como [github.com] e [Stackoverflow.com]. como também o esclarecimento de duvidas e ajuda entre colegas.
* Após a criação do loader, foram feitos vários testes com ficheiros .obj e .mtl, tal como também apenas .obj, para analisar se o programa interpretava bem os ficheiros ou se causava algum erro. Ficando o ficheiro [Buggy.obj] como ultimo ficheiro para ser entregue.

## Conclusão
* Sendo a primeira parte do projeto mais fácil, a criação do loader de ficheiros .obj foi o que causou mais problemas. Não sendo programação o meu forte a pesquisa intensiva que tive de fazer para encontrar alguma ajuda na criação do projeto foi bastante e ajuda dos colegas foi necessária para uma melhor compreensão do trabalho em geral.
* Após a criação do loader e de perceber melhor como este funcionava, acabei por me divertir na leitura dos ficheiros e na alteração de código acrescentado mais código para uma melhor experiência. No Loader acabei por adicionar a mais a biblioteca do pygame de musica, para quando este abrir dar uma musica de fundo enquanto o objeto é mostrado.