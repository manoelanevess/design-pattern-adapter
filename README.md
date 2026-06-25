# Padrão de Projeto: Adapter

## O que é?

O Adapter é um padrão de projeto estrutural que permite que objetos com interfaces incompatíveis trabalhem juntos. Funciona como um adaptador de tomada: você tem um plugue que não encaixa na tomada, então usa um adaptador para fazer a conexão funcionar.

## Problema

Imagine um sistema de pagamento que aceita cartão, Pix e boleto. Cada sistema tem seu próprio método com nome diferente (`pagar_cartao()`, `realizar_pix()`, `gerar_boleto()`). Sem o Adapter, o código precisa de um `if/elif` gigante que verifica o tipo de pagamento e chama o método certo — o que torna o sistema difícil de manter e expandir.

## Solução com o Adapter

O Adapter cria uma interface comum (`pagar()`) e cada adapter faz a tradução para o método correto de cada sistema. Assim, o código sempre chama o mesmo método, sem precisar conhecer os detalhes de cada implementação. Para adicionar um novo meio de pagamento, basta criar um novo adapter.

## Estrutura

- `sem_padrao.py` — sistema de pagamento sem o padrão: usa if/elif para chamar métodos diferentes em cada caso
- `com_padrao.py` — sistema de pagamento com o padrão Adapter: sempre chama `pagar()`, independente do tipo

## Como executar

```bash
python sem_padrao.py
python com_padrao.py
```

## Pontos Fortes

- Permite integrar sistemas com interfaces incompatíveis sem alterar o código existente
- Segue o princípio aberto/fechado: aberto para extensão e fechado para modificação
- Facilita a adição de novos sistemas no futuro — basta criar um novo adapter
- Reduz o risco de bugs ao evitar modificação de código já funcionando

## Pontos Fracos

- Aumenta a complexidade do código com a criação de classes extras
- Pode ser excessivo para sistemas simples
- Com muitos adapters, o código pode ficar difícil de rastrear

## Conclusão

O padrão Adapter é muito útil quando precisamos integrar sistemas que não foram projetados para trabalhar juntos. No exemplo deste projeto, ele elimina a necessidade de verificar manualmente o tipo de pagamento a cada operação, tornando o código mais limpo, organizado e fácil de expandir. É amplamente usado no mundo real, especialmente em integrações com APIs externas e bibliotecas de terceiros.
