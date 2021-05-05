# Construir código necessário em Python para implementar o seguinte projeto:

# Uma classe abstrata chamada de Periférico que contém os atributos/propriedades marca, cor e preço. Esta classe também possui um método getInformacoes() que retorna todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().

# O projeto também deve possuir as classes Teclado e Mouse que herdam da classe Periférico.

# A classe Teclado possui o atributo/propriedade fracamente privado layout. Esta classe reimplementa o método getInformacoes() herdado de Periférico.

# A classe Mouse possui o atributo/propriedade fortemente privado tipoConexao. Esta classe reimplementa o método getInformacoes() herdado de Periférico.

# Você pode enviar os arquivos do projeto ou criar um repositório no Github e enviar só o link do repositório.
from Periferico import Periferico

class Mouse(Periferico):
    def init(self, marca, cor, preco, tipoConexao):
        self._marca = marca
        self._cor = cor
        if preco > 0:
            self._preco = preco
        else:
            self._preco = 0        
        self.__tipoConexao = tipoConexao

    @property
    def marca(self):
        return self._marca

    @property
    def cor(self):
        return self._cor
    
    @property
    def preco(self):
        return self._preco

    @property
    def tipoConexao(self):
        return self.__tipoConexao

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @preco.setter
    def preco(self, preco):
        if preco > 0:
            self._preco = preco
        else:
            self._preco = 0

    @tipoConexao.setter
    def tipoConexao(self, tipoConexao):
        self.__tipoConexao = tipoConexao
    
    def cadastrar(self):
        return print('Mouse Cadastrado')

    def getInformacoes(self):
        print(f'''
Marca: {self._marca}
Cor: {self._cor}
Preço: {self._preco}
Conexão: {self.__tipoConexao}
        ''')
    
