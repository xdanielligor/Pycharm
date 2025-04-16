
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def mostra_no(self):
        print(self.valor)


class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo = No(valor)
        if self.raiz is None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                if valor < atual.valor:
                    atual = atual.esquerda
                    if atual is None:
                        pai.esquerda = novo
                        return
                else:
                    atual = atual.direita
                    if atual is None:
                        pai.direita = novo
                        return

    def mostrar_em_ordem(self, no=None):
        if no is None:
            no = self.raiz
        if no is not None:
            self.mostrar_em_ordem(no.esquerda)
            print(no.valor, end=" ")
            self.mostrar_em_ordem(no.direita)

    # NOVO: imprime a estrutura visualmente
    def imprimir_estrutura(self, no=None, nivel=0):
        if no is None:
            no = self.raiz
        if no.direita:
            self.imprimir_estrutura(no.direita, nivel + 1)
        print("     " * nivel + f"-> {no.valor}")
        if no.esquerda:
            self.imprimir_estrutura(no.esquerda, nivel + 1)



