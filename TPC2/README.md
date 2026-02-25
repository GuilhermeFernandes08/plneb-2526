# Descrição do TPC2

Os objetivos pedagógicos desta ficha são os seguintes:
- Compreender a sintaxe básica das expressões regulares;
- Aplicar operadores e quantificadores em padrões de pesquisa;
- Utilizar funções do módulo re para pesquisa, substituição e divisão de strings;
- Desenvolver funções para validação e extração de informação textual;
- Aplicar expressões regulares a exemplos práticos e dados do quotidiano.


As expressões regulares permitem definir padrões formais para identificar sequências de caracteres. Ao longo da ficha são utilizados os seguintes elementos:


^ – indica o início da string

$ – indica o fim da string

? – corresponde a zero ou uma ocorrência

+ – corresponde a uma ou mais ocorrências

* – corresponde a zero ou mais ocorrências

[abc] – corresponde a um dos caracteres a, b ou c

[a-z] – corresponde a uma letra minúscula

[A-Za-z] – corresponde a qualquer letra

\d – corresponde a um dígito numérico

re.match() – verifica correspondência no início da string

re.search() – procura um padrão em qualquer posição

re.findall() – devolve todas as correspondências

re.sub() – substitui padrões

re.split() – divide strings com base num padrão

Exercício 1 – Manipulação da palavra “hello”

Este exercício tem como objetivo introduzir as funções básicas de pesquisa, extração, substituição e divisão de strings.

1.1 – Verificação no início da string

Nesta alínea pretende-se verificar se a palavra "hello" ocorre no início da linha.
É utilizado o operador ^ em conjunto com a função re.match, que apenas valida correspondências no início da string.

1.2 – Pesquisa global na string

O objetivo consiste em verificar se a palavra "hello" ocorre em qualquer posição da linha.
Para tal, recorre-se à função re.search, que permite localizar padrões independentemente da sua posição.

1.3 – Pesquisa múltipla sem distinção de maiúsculas

Nesta alínea são identificadas todas as ocorrências da palavra "hello", ignorando diferenças entre maiúsculas e minúsculas.
Utiliza-se a função re.findall combinada com a flag re.IGNORECASE, sendo o resultado devolvido sob a forma de lista.

1.4 – Substituição de padrões

O objetivo é substituir todas as ocorrências da palavra "hello" pela expressão *YEP*.
Este exercício demonstra a aplicação da função re.sub para substituições globais.

1.5 – Divisão de strings

Nesta alínea a string é dividida sempre que ocorre uma vírgula.
A função re.split permite obter uma lista de substrings, facilitando o tratamento posterior dos dados.

Exercício 2 – Palavra Mágica

Este exercício consiste na implementação da função palavra_magica, cuja finalidade é verificar se uma frase termina com a expressão "por favor" seguida de um sinal de pontuação.
A validação é realizada através do operador $ e da definição de classes de caracteres adequadas.

Exercício 3 – Narcisismo

Neste exercício é definida a função narcissismo, que contabiliza o número de ocorrências da palavra "eu" numa frase.
São aplicadas expressões regulares para identificar o padrão pretendido e contabilizar os resultados.

Exercício 4 – Troca de Curso

O objetivo deste exercício é criar a função troca_de_curso, responsável por substituir todas as ocorrências da sigla "LEI" pelo nome de um curso fornecido como argumento.
Este exercício reforça o conceito de substituição dinâmica de padrões.

Exercício 5 – Soma de Números numa String

A função soma_string recebe uma string contendo números separados por vírgulas e devolve a soma total desses valores.
A solução envolve a extração dos números com expressões regulares e a sua posterior conversão para valores inteiros.

Exercício 6 – Pronomes Pessoais

Neste exercício é implementada a função pronomes, que identifica todos os pronomes pessoais presentes numa frase.
É utilizada uma expressão regular com alternativas (|) e pesquisa sem distinção entre maiúsculas e minúsculas.

Exercício 7 – Validação de Variáveis

A função variavel_valida verifica se uma string corresponde a um nome válido de variável.
As regras aplicadas são:
- a string deve iniciar por uma letra;
- apenas são permitidos caracteres alfanuméricos e underscore.

Exercício 8 – Identificação de Inteiros

Neste exercício a função inteiros devolve todos os números inteiros presentes numa string, incluindo valores positivos e negativos.
São utilizados sinais opcionais e quantificadores para garantir a correta identificação dos números.

Exercício 9 – Normalização de Espaços

O objetivo é substituir todos os espaços por underscores, assegurando que múltiplos espaços consecutivos resultam num único underscore.
Este exercício aplica quantificadores para normalização textual.

Exercício 10 – Códigos Postais

Neste exercício é criada a função codigos_postais, que recebe uma lista de códigos postais válidos e os divide nos seus componentes numéricos.
O exercício demonstra a aplicação de expressões regulares a dados estruturados do mundo real.
