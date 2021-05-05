# Construir código necessário em Python para implementar o seguinte projeto:

# Uma classe abstrata chamada de Periférico que contém os atributos/propriedades marca, cor e preço. Esta classe também possui um método getInformacoes() que retorna todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().

# O projeto também deve possuir as classes Teclado e Mouse que herdam da classe Periférico.

# A classe Teclado possui o atributo/propriedade fracamente privado layout. Esta classe reimplementa o método getInformacoes() herdado de Periférico.

# A classe Mouse possui o atributo/propriedade fortemente privado tipoConexao. Esta classe reimplementa o método getInformacoes() herdado de Periférico.

# Você pode enviar os arquivos do projeto ou criar um repositório no Github e enviar só o link do repositório.
from abc import ABCMeta, abstractmethod

class Periferico (metaclass=ABCMeta):
    @property
    def marca(self):
        pass
        
    @property
    def cor(self):
        pass

    @property
    def preco(self):
        pass

    @marca.setter
    @cor.setter
    @preco.setter
    
    @abstractmethod    
    def cadastrar(self):
        pass
    
    def getInformacoes(self, marca, cor, preco):  
        pass
        
        