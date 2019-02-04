---
title: Entenda o desempacotamento do Python
date: 2019-02-02 15:40
tags: python, unpacking-tuple, programacao
category: python
slug: entenda-o-desempacotamento-do-python
summary: # TODO
---

Um dos exercícios mais comuns nas aulas básicas de programação é sem dúvida
alguma o de trocar os valores das variáveis `a` e `b`.

```c
// Codigo classico em linguagem c
int main(){
    int a = 5, b = 7;

    int tmp = a;
    a = b;
    b = tmp;
}
```

Mas se a linguagem for Python, existe uma outra maneira:

```Python
a = 5
b = 7
a, b = b, a
```

Ok até agora não tivemos muitas novidades, provavelmente você já viu isso em
algum lugar. Mas neste post eu vou apresentar mais
algumas possibilidades deste **desempacotamento** do Python!

## Desempacotamento com Python

Algo que eu faço muito resolvendo exercícios do 
[URI](https://www.urionlinejudge.com.br) é ler a linha dar um `split` na linha
e converter todos os elementos para um tipo especifico, geralmente `int`.

Claro que podemos fazer isso de várias formas, por exemplo:

```Python
linha = input().split()

a = int(linha[0])
b = int(linha[1])
c = int(linha[2])
d = int(linha[3])
```

Esse exemplo funcionaria, mas seria extremamente lento de se escrever isso se
tivermos várias variáveis diferentes na linha, então hoje eu uso muito, mas
muito mesmo essa solução com list-comprehensions:

```Python
a, b, c, d = [int(x) for x in input().split()]
```

De cinco linhas para uma até que nos livramos de uma boa parte de código
repetitivo!

## Melhorando a legibilidade do código

Agora vamos a um exemplo menos bobinho, e também com menos cara de exercício
de programação, sem unpacking:

```Python
curso = get_curso_by_id(2)

print("Nome:", curso[1])
print("Coordenador:", curso[3])
print("Data de Inicio:", curso[4])
print("Descrição:", curso[2])
```

A função `get_curso_by_id()` retorna uma tupla com: id, nome, descrição,
coordenador, data de inicio. Referenciar estes campos por seu índices é
uma solução feia que permite muitos erros. Então vamos deixar este código mais
legível com desempacotamento:

```Python
id_curso, nome, desc, coordenador, dt_inicio = get_curso_by_id(2)

print("Nome:", nome)
print("Coordenador:", coordenador)
print("Data de Inicio:", dt_inicio)
print("Descrição:", desc)
```

Muito mais legível!

Agora vamos dizer que a data retorna também uma tupla com anos, mês e dia. Para
separar esses valores também nos poderíamos fazer o seguinte:

```Python
id_curso, nome, desc, coordenador, (ano, mes, dia) = get_curso_by_id(2)

print("Nome:", nome)
print("Coordenador:", coordenador)
print("Data de Inicio:", "{}/{}/{}".format(dia, mes, ano))
print("Descrição:", desc)
```

## Ignorando valores

Agora vamos dizer que você precisa apenas do nome do curso e do coordenador,
o Python não possui nenhuma sintaxe específica pra isso, mas você pode
simplesmente atribuir esses campos para uma variável aleatória, como `_`:

```Python
_, nome, _, coordenador, _ = get_curso_by_id(2)
```

## Desempacotando valores de iteráveis de tamanho variável

Tudo isso e muito bonito mas é no caso de iteráveis que eu não sei exatamente o
tamanho? É agora que entram as `*` no Python, mas acalme-se meu jovem
traumatizado pelos ponteiros de C essa estrelinha não tem nenhuma relação com
eles.

```Python
>>> aluno
('João', 'joao@bol.com.br', '(11) 93233-32323', '(11) 93233-3863', '(11) 98603-32323')
>>> nome, email, *telefones
>>> nome
'João'
>>> email
'joao@bol.com.br'
>>> telefones
['(11) 93233-32323', '(11) 93233-3863', '(11) 98603-32323']
```

Em detalhes: `nome` e `email` receberam os dois primeiros elementos, e
`telefones` recebeu todo o resto.

E claro que as 'estrelinhas' não servem só pra desempacotar os últimos
elementos: elas podem estar no meio, no incio e no fim da expressões de
desempacotamento.

A única exigência e que exista apenas um 'valor estrelado' na expressão:

```Python
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> a, *b, c, *d = l
  File "<stdin>", line 1
SyntaxError: two starred expressions in assignment
>>>
```

## Passando um iterável ou dicionário como argumentos de uma função

Essa talvez você já tenha visto em algum lugar:

```Python
>>> def a(*args, **kwargs):
...     print(args)
...     print(kwargs)
...
>>> a(1, 2, 'a', 'b', z=9, x=8)
(1, 2, 'a', 'b')
{'z': 9, 'x': 8}
>>>
```

E aí, o que achou dessa forma de desempacotar dados com o Python?


