<h1 align="center">Repositório de exemplo de Web Scraping</h1>

<img src="https://img.shields.io/static/v1?label=RP&message=Dev&color=7159c1&style=for-the-badge&logo=Meteor"/>

No mundo atual, onde dados são a base na tomada de decisões, análises de comportamento e são essenciais na previsão não só do tempo, mas também de preços e energia, ter os dados no melhor formato possível, sem outliers e disponível de forma rápida é sinonimo de economia de tempo (e tempo é dinheiro).
A aquisição de um dado bruto toma uma boa parte do tempo de um analista de dados e essa aquisição pode consumir semanas que poderiam estar sendo utilizadas para desenvolver o produto final com maior qualidade.
Nem sempre esses dados estão disponíveis em um formato amigável, que possa ser lido por um programa de computador simples, sendo assim, além do tempo de adquirir o dado, muitas vezes é necessário realizar um pré processamento no mesmo.

Quem é desenvolvedor provavelmente já se deparou com um site que possui um dado valioso, que seria de extrema importância para atingir um objetivo final, mas que não é disponível um download ou acesso direto. Neste pequeno tutorial, mostro um exemplo de _data scraping_, com o objetivo de coletar dados disponíveis em uma URL que foi pensada para o usuário final do sistema, e não para o desenvolvedor que lidaria melhor com uma Application User Interfaces (APIs), por exemplo.

### Python 

O python possui bibliotecas como **BeautifulSoup** e **Requests** para a coleta de dados em arquivos HTML, porém, alguns sites utilizam **páginas dinâmicas** que utiliza um JavaScript para modificar o código HTML da página. Isso significa que, mesmo que os dados apareçam em uma página acessada de um navegador, é possível que esses mesmos dados não estejam disponíveis no arquivo HTML retornado por um request, caso tente utilizar uma biblioteca python como as citadas acima.

O JavaScript (.js) nada mais é do que um motorzinho que fica rodando no _back end_ do que você vê no seu navegador ;)

### Dados de maré  

Neste exemplo, eu precisava de dados previstos e observados de maré para alimentar um banco de dados e posteriormente visualizar em uma página que seria destinada a um cliente final, que precisava saber os horários da maré alta/baixa.

Fui então, atrás de um dado público e encontrei o site do CIRAM (https://ciram.epagri.sc.gov.br/litoral-online/), mas que só disponibilizava o dado na própria tela.

![alt text](https://github.com/pimentelrenan/web-scraping/blob/master/figuras/mare.jpg)

Este exemplo é o que chamamos de **Página Dinâmica**, então, a alternativa para acessar dados nesse sistema é utilizar as ferramentas de desenvolvedor presentes nos navegadores para analisar o funcionamento da página e identificar de onde vem a informação desejada. (No Google Chrome/ Firefox basta pressionar a tecla **F12** do teclado e analisar o _console_)

Ao fazer a análise foi possível identificar uma chamada para o endereço: https://ciram.epagri.sc.gov.br/graficos/getDataMare6_2963.php. Este endereço retorna um arquivo .json com os valores de maré que aparecem abaixo. Ou seja, essa API alimenta o gráfico que atualiza em tempo real com as informações que eu precisava.

![alt text](https://github.com/pimentelrenan/web-scraping/blob/master/figuras/dadosmare.jpg)

