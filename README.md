## Don't speak portuguese?
[Click here to view this page in English](https://github.com/faillerplays/desafiojgp/blob/main/README-en.md)
# Análise de Inflação dos EUA (Desafio JGP Macro)

Este repositório contém a solução para o desafio de processo seletivo para cientista de dados Macro da JGP. O objetivo do desafio é analisar dados de inflação dos Estados Unidos (CPI) obtidos do Bureau of Labor Statistics (BLS).

## Estrutura do Repositório

*  **question1.py:** Script para obter os dados de inflação da API do BLS, processá-los e salvá-los em um arquivo CSV.

*  **question2&3.py:** Script para gerar um gráfico interativo mostrando a evolução do CPI "Todos os itens menos alimentos e energia" (ajustado sazonalmente) e sua variação percentual anual. E resposta para pergunta 3.

*  **question4.py:** Script para gerar o (cpiallvscpigasoline.html) - analisar a relação entre o CPI "Todos os itens" e o CPI da "Gasolina".

*  **question5.py** Script para criar uma API FastAPI que permite consultas aos dados do CPI.

*  **cpi_data.csv:** Arquivo CSV contendo os dados de inflação obtidos da API do BLS.

*  **cpiallvscpigasoline.html:** Arquivo HTML contendo os gráficos da variação percentual do CPI geral e da gasolina.

*  **cpilfeyoy.html:** Arquivo HTML contendo o gráfico de mudança percentual ano a ano CPI Todos os itens menos alimentos e energia 

*  **requirements.txt:** Lista das dependências Python necessárias para executar o projeto.\n

## Como Executar o Projeto

1. **Clone o repositório:**
  
```bash
  git clone [https://github.com/faillerplays/desafiojgp.git](https://github.com/faillerplays/desafiojgp.git)
```


2. **Instale as dependências:**
  
```bash
  pip install -r requirements.txt
```


3. **Execute os scripts:**
  
```bash
  python question1.py
  python question2&3.py
  python question4.py
  python question5.py
```
4. **Iniciar o servidor da question5.py**
  
```bash
   uvicorn questao5:app --reload
```

## Interactive Visualization

Voce pode ver os gráficos interativos aqui:

[Questão 2. Ver mudança ano a ano da CPI todos itens menos comida e energia em percentual](https://faillerplays.github.io/desafiojgp/cpilfeyoy.html)

[Questão 4. Ver CPI todos itens vs Gasolina](https://faillerplays.github.io/desafiojgp/cpiallvscpigasoline.html)



## Autor

*  [Miguel Dargains] - [miguel.dargains@gmail.com]

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.
