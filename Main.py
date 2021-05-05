from Mouse import Mouse
from Periferico import Periferico
from Teclado import Teclado

formato = '----=------=-----=----'
separacao = '################################'
print(formato)
mouse = Mouse()
mouse.cadastrar()
print(formato)
mouse.marca = 'Redragon'
mouse.cor = 'Vermelho'
mouse.preco = 104.00
mouse.tipoConexao = 'USB'
mouse.getInformacoes()
print(separacao)
print(formato)
mouse = Teclado()
mouse.cadastrar()
print(formato)
mouse.marca = 'Redragon'
mouse.cor = 'Azul'
mouse.preco = 156.00
mouse.layout = 'ABNT'
mouse.getInformacoes()
print(formato)