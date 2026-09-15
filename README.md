# cadastro-cliente-validacao-email-telefone
# Cadastro de Cliente — TechBairro (Gabarito)

Gabarito da atividade de cadastro de clientes da TechBairro, desenvolvido em Python com Tkinter. O programa oferece uma interface gráfica simples para cadastrar clientes, validando os campos preenchidos, incluindo telefone e e-mail.

## Sobre o projeto

O sistema apresenta um formulário com os campos Nome, Telefone, E-mail e Endereço. Ao clicar em "Salvar", os dados são validados e, se estiverem corretos, o cliente é adicionado a uma lista em memória. É possível consultar todos os clientes cadastrados em uma janela separada.

## Requisitos

- Python 3
- Tkinter (já incluído na instalação padrão do Python na maioria dos sistemas)

## Como executar

```bash
python cadastro_cliente.py
```

## Funcionalidades

- Cadastro de clientes com os campos Nome, Telefone, E-mail e Endereço
- Validação de campos obrigatórios (não permite salvar com campos em branco)
- Validação de telefone: aceita somente números
- Validação de e-mail: exige o formato `nome@dominio.com`
- Botão "Cancelar" para limpar o formulário
- Botão "Consultar Clientes" para visualizar todos os cadastros em uma janela separada, com barra de rolagem
- Contador de clientes cadastrados

## Estrutura do código

- Criação da janela principal e do cabeçalho
- Montagem dinâmica do formulário a partir de uma lista de campos
- Função `email_parece_valido()` para validar o formato do e-mail
- Função `salvar()` com as validações e a atualização do status e do contador
- Função `cancelar()` para limpar o formulário
- Função `abrir_consulta()` para exibir os clientes cadastrados em uma nova janela (`Toplevel`)

## Observações

Este projeto tem finalidade educacional e foi disponibilizado como gabarito de uma atividade de sala de aula.
abarito de atividade: sistema de cadastro de clientes em Python/Tkinter (TechBairro) com validacao de e-mail e telefone.
