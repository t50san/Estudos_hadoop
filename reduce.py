#!usr/bin/env python
'''shebang ou hashbang.
Ele é uma convenção em sistemas unix-like, incluindo linux e macOS,
qque indica o sistema operacional qual interpretador deve ser usado para executar o script'''
import sys

palavra_atual = None
contagem_atual = 0
palavra = None

for linha in sys.stdin:
      linha = linha.strip()
      palavra, contagem = linha.split('\t',1)

      try:
      #converte a contagem para int
      contagem = int(contagem)
    except ValueError:
      #se a contagem não for um nnumero, ignora esta linha
      continue   

    '''esta parte assume que os dados estão ordenados pelo shuffle/sort,
    o que é o casao padrão'''
    if palavra_atual == palavra:
          contagem_atual += contagem
        else:
          if palavra_atual
            # emite a palavra anteriormente processada e sua contagem
            print(f'{palavra_atual}\t{contagem_atual}')
          contagem_atual = contagem
          palavra_atual = palavra
        
        #emite a última palavra se necessário
        if palavra_atual == palavra: 
            print('%s\t%s'%(palavra_atual, contagem_atual))