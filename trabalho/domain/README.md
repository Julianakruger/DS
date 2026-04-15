# Refatoração com Arquitetura Limpa

Este projeto tem como objetivo refatorar um código com responsabilidades misturadassss,
aplicando conceitos de Arquitetura Limpa.

## Estrutura

- Controller: responsável pela entrada e saída de dados
- Use Case: responsável por orquestrar o fluxo da aplicação
- Domain: onde ficam as regras de negócio
- Repository: responsável por fornecer configurações

## Regras de negócio

- Cálculo baseado em peso:
  - até 1kg: 5
  - até 5kg: 10
  - acima de 5kg: 20
- Distância: 0.5 por km
- Cliente VIP recebe 20% de desconto
- Valor mínimo do frete: 15

## Objetivo

Organizar o código separando responsabilidades e centralizando regras de negócio no domínio.