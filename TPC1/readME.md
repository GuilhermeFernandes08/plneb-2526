No ex1.py, a lógica baseia-se na inversão da ordem dos caracteres através de slicing com passo negativo ([::-1]), que gera uma cópia da string ao contrário. O programa depois percorre essa sequência num ciclo for para reconstruir o texto numa nova variável antes de o exibir.

No ex2.py, o programa utiliza uma iteração simples para analisar cada letra da frase, aplicando uma estrutura condicional com o operador or. Esta lógica permite identificar tanto o 'A' maiúsculo como o 'a' minúsculo, somando-os a um contador acumulador.

No ex3.py, a lógica recorre ao operador de pertença in para validar se cada caractere da string existe dentro de uma sequência pré-definida de vogais. Esta funcionalidade evita a escrita de múltiplos "OU", tornando a verificação de múltiplos caracteres muito mais eficiente.

No ex4.py, a lógica aproveita o método de manipulação de strings .lower(), que percorre internamente toda a cadeia de caracteres e substitui qualquer letra maiúscula pela sua versão minúscula correspondente na tabela ASCII.

No ex5.py, o processo é o inverso do anterior, utilizando o método nativo .upper(). A lógica foca-se em garantir a uniformidade do texto em caixa alta, transformando todos os caracteres da string de forma automática.

No ex6.py, a lógica de verificação de capicua assenta no uso da função range() com passo negativo para aceder aos índices da string do fim para o início. Ao reconstruir a string desta forma, o programa pode usar um operador de comparação (==) para validar se a leitura é idêntica nos dois sentidos.

No ex7.py, a lógica avalia se uma string está contida noutra através de uma verificação booleana elemento a elemento. Utiliza o operador not in para interromper o ciclo imediatamente (com return False) caso detete um único caractere na primeira string que não exista na segunda.

No ex8.py, a lógica utiliza o conceito de janela deslizante através de slicing dinâmico ([i:i+len(s1)]). O programa calcula o comprimento da substring e "corta" pedaços da string principal com esse tamanho exato, comparando-os em cada posição para contar as ocorrências.

No ex9.py, a lógica de deteção de anagramas baseia-se na ordenação de listas (.sort()). Ao converter as strings em listas e ordená-las alfabeticamente, o programa neutraliza a ordem original das letras, permitindo que uma comparação direta confirme se ambas as palavras usam exatamente os mesmos caracteres.