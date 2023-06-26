class AutomatoFinitoDeterministico:
    def __init__(self, estados, estado_inicial, estados_finais, transicoes):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

    def processar_palavra(self, palavra):
        estado_atual = self.estado_inicial

        for simbolo in palavra:
            if (estado_atual, simbolo) in self.transicoes:
                estado_atual = self.transicoes[(estado_atual, simbolo)]
            else:
                return False

        return estado_atual in self.estados_finais

estados = input("Digite os estados separados por vírgula: (Ex: q0,q1,q2)").split(',')

estado_inicial = input("Digite o estado inicial: ")

estados_finais = input("Digite o(s) estado(s) final(is) separado(s) por vírgula: ").split(',')

transicoes = {}
while True:
    transicao = input("Digite a transição (Ex:q1,a,q2) ou 'sair' para encerrar: ")

    if transicao == 'sair':
        break

    estado_atual, simbolo, estado_destino = transicao.split(',')
    transicoes[(estado_atual.strip(), simbolo.strip())] = estado_destino.strip()

automato = AutomatoFinitoDeterministico(estados, estado_inicial, estados_finais, transicoes)

while True:
    palavra = input("Digite uma palavra para verificar se a mesma é aceita pelo autômato (ou 'sair' para encerrar): ")

    if palavra == 'sair':
        break

    if automato.processar_palavra(palavra):
        print("A palavra é aceita pelo autômato.")
    else:
        print("A palavra é rejeitada pelo autômato.")
