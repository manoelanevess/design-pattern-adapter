# Com o padrão Adapter
# Interface padrão que o sistema espera
class Pagamento:
    def pagar(self, valor, dado):
        pass

# Sistemas de pagamento existentes (não podem ser alterados)
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

# Adapters — traduzem pagar() para o método correto
class AdapterCartao(Pagamento):
    def __init__(self):
        self.pagamento = PagamentoCartao()

    def pagar(self, valor, dado):
        self.pagamento.pagar_cartao(valor, dado)

class AdapterPix(Pagamento):
    def __init__(self):
        self.pagamento = PagamentoPix()

    def pagar(self, valor, dado):
        self.pagamento.realizar_pix(valor, dado)

class AdapterBoleto(Pagamento):
    def __init__(self):
        self.pagamento = PagamentoBoleto()

    def pagar(self, valor, dado):
        self.pagamento.gerar_boleto(valor, dado)

# Vantagem: o caixa sempre chama pagar()
# sem precisar saber os detalhes de cada sistema
adapters = {
    "cartao": AdapterCartao(),
    "pix": AdapterPix(),
    "boleto": AdapterBoleto()
}

print("=== SISTEMA DE PAGAMENTO COM ADAPTER ===\n")

tipo = input("Escolha o pagamento (cartao/pix/boleto): ")

if tipo not in adapters:
    print("Tipo de pagamento inválido!")
else:
    dado = input("Informe o número do cartão / chave Pix / CPF: ")
    valor = float(input("Valor: R$ "))
    adapters[tipo].pagar(valor, dado)