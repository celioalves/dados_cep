import requests

class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP INVÁLIDO")

    def __str__(self):
        return self.format_cep()

    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f' {self.cep[:5]}-{self.cep[5:]}'

    def acessa_via_cep(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json'
        r = requests.get(url)
        dados = r.json()
        return ( dados ['logradouro'],
                 dados ['complemento'],
                 dados ['bairro'],
                 dados ['localidade'],
                 dados ['uf']
        )

cep = input('Informe o CEP (Sem hífen " - "): ')
objeto_cep = BuscaEndereco(cep)
logradouro, complemento, bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(f'Logradouro: {logradouro} \n' 
      f'Complemento: {complemento} \n'
      f'Bairro: {bairro}\n'
      f'Cidade: {cidade}\n'
      f'Estado: {uf}')

