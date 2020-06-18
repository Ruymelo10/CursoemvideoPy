x = str(input('Digite seu sexo: ')).strip()
while x not in 'MFmf':
    x = str(input('Digite novamente. Apenas M ou F: ')).strip()
