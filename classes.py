class Animal:
    nome= ""
    idade = 0
    peso = 0

    def __init__(self, nome, idade, peso):
        self.nome = nome 
        self.idade = idade
        self.peso = peso
    
    def exibirInformacoes(self):
        print('----------Petshop----------')
        print(f'Nome do pet: {self.nome}')
        print(f'Idade do pet: {self.idade}')
        print(f'Peso do pet: {self.peso}kg')

    def exibirNome(self):
        return self.nome
    
    def exibirIdade(self):
        return self.idade
    
    def exibirPeso(self):
        return self.peso
    

class Cachorro(Animal):
    def __init__(self,nome,idade,peso,raca,nivelEnergia,soltaPelos):
        super().__init__(nome,idade,peso)
        self.__raca = raca
        self.__nivelEnergia = nivelEnergia
        self.__soltaPelos = soltaPelos

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f'Raça do cachorro: {self.__raca}')
        print(f'Intensidade do cachorro é: {self.__nivelEnergia}')
        print(f'A raça do cachorro é {self.__raca}')
        if self.__soltaPelos:
            print(f'O cachorro solta pelos')
        else:
            print(f'O cachorro não solta pelos')

class Gato(Animal):
    def __init__(self, nome, idade, peso, cor_pelo,agressivo):
        super().__init__(nome, idade, peso)
        self.__cor_pelo = cor_pelo
        self.__agressivo = agressivo

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f'Cor do pelo: {self.__cor_pelo}')
        if self.__agressivo:
            print(f'Bichano agressivo')
        else:
            print(f'Bichano manso')