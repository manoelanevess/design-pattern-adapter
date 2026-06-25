# Sem o padrão Adapter
class PagamentoCartao:
    def pagar_cartao(self, valor, numero_cartao):
        print(f"Processando pagamento com cartão...")
        print(f"Cartão: **** **** **** {numero_cartao[-4:]}")
        print(f"Valor: R$ {valor:.2f}")
        print(f"Status: Pagamento aprovado!")
        print()

class PagamentoPix:
    def realizar_pix(self, valor, chave_pix):
        print(f"Processando pagamento via Pix...")
        print(f"Chave Pix: {chave_pix}")
        print(f"Valor: R$ {valor:.2f}")
        print(f"Status: Pix enviado com sucesso!")
        print()

class PagamentoBoleto:
    def gerar_boleto(self, valor, cpf):
        print(f"Gerando boleto...")
        print(f"CPF: {cpf}")
        print(f"Valor: R$ {valor:.2f}")
        print(f"Vencimento: 3 dias úteis")
        print(f"Status: Boleto gerado com sucesso!")
        print()

# Problema: o caixa precisa saber exatamente qual
# método chamar para cada tipo de pagamento
print("=== SISTEMA DE PAGAMENTO SEM ADAPTER ===\n")

tipo = input("Escolha o pagamento (cartao/pix/boleto): ")

if tipo == "cartao":
    numero = input("Número do cartão: ")
    valor = float(input("Valor: R$ "))
    pagamento = PagamentoCartao()
    pagamento.pagar_cartao(valor, numero)
elif tipo == "pix":
    chave = input("Chave Pix: ")
    valor = float(input("Valor: R$ "))
    pagamento = PagamentoPix()
    pagamento.realizar_pix(valor, chave)
elif tipo == "boleto":
    cpf = input("CPF: ")
    valor = float(input("Valor: R$ "))
    pagamento = PagamentoBoleto()
    pagamento.gerar_boleto(valor, cpf)
else:
    print("Tipo de pagamento inválido!")