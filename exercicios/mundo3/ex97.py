def escreva (msg):
    tam = len(msg)+4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)

txt = str(input('Mesagem: '))
escreva(txt)
