# Calculadora de IMC

Aplicação em Python que calcula o Índice de Massa Corporal e classifica o resultado
nas faixas da OMS. Tem duas versões: uma de terminal e outra com interface gráfica
em Tkinter.

## Funcionalidades

- Cálculo do IMC a partir de peso (kg) e altura (m)
- Classificação em 6 faixas, de baixo peso a obesidade grau III
- Validação de entrada: rejeita texto, valores negativos e zero
- Duas interfaces: terminal e janela

## Como rodar

Requisito: Python 3.10+. Tkinter já vem na instalação padrão do Python.

```bash
git clone https://github.com/pabloantoniopietrobonlopes2007-tech/calculadora-imc.git
cd calculadora-imc/calculadora_IMC
```

Interface gráfica:

```bash
python new_front.py
```

Versão de terminal:

```bash
python imc.py
```

## Estrutura

```
calculadora_IMC/
├── imc.py         # versão de terminal
├── funcs.py       # cálculo, classificação e validação
└── new_front.py   # interface Tkinter
```

## Decisões

- A lógica de cálculo e classificação fica isolada em `funcs.py`, sem nada de
  interface, para poder ser usada pelas duas versões.
- A interface recebe os widgets como parâmetro em vez de importar o módulo de
  lógica, o que evita dependência circular entre os dois arquivos.
- A validação fica em loop até receber um número válido, em vez de encerrar o
  programa no primeiro erro de digitação.

## O que eu aprendi

- Separar lógica de apresentação
- Tratar `ValueError` na conversão de entrada
- Montar uma janela com `pack()` e passar estado por parâmetro

## Próximos passos

- [ ] Salvar o histórico de cálculos em SQLite
- [ ] Testes unitários para o cálculo e a classificação
- [ ] Exportar o resultado em PDF
