# Repositório de exemplo de Web Scraping

No mundo atual, onde dados são a base na tomada de decisões, análises de comportamento e são essenciais na previsão não só do tempo, mas também de preços e energia, ter os dados no melhor formato possível, sem outliers e disponível de forma rápida é sinonimo de economia de tempo (e tempo é dinheiro).
A aquisição de um dado bruto toma uma boa parte do tempo de um analista de dados e essa aquisição pode consumir semanas que poderiam estar sendo utilizadas para desenvolver o produto final com maior qualidade.
Nem sempre esses dados estão disponíveis em um formato amigável, que possa ser lido por um programa de computador simples, sendo assim, além do tempo de adquirir o dado, muitas vezes é necessário realizar um pré processamento no mesmo.

Quem é desenvolvedor provavelmente já se deparou com um site que possui um dado valioso, que seria de extrema importância para atingir um objetivo final, mas que não é disponível um download ou acesso direto. Neste pequeno tutorial, mostro um exemplo de _data scraping_, com o objetivo de coletar dados disponíveis em uma URL que foi pensada para o usuário final do sistema, e não para o desenvolvedor que lidaria melhor com uma Application User Interfaces (APIs), por exemplo.

### Dados de maré  

Neste exemplo, eu precisava de dados previstos e observados de maré para alimentar um banco de dados e posteriormente visualizar em uma página que seria destinada a um cliente final, que precisava saber os horários da maré alta/baixa.

Fui então, atrás de um dado público e encontrei o site do CIRAM (https://ciram.epagri.sc.gov.br/litoral-online/), mas que só disponibilizava o dado na própria tela.

![alt text](https://github.com/pimentelrenan/web-scraping/blob/master/figuras/ciram.PNG)



```sh
$ teste de script
```