import requests


class Integrator:

    def __init__(self, cnpj=None, xbz_token=None):
        self.xbz_token = xbz_token
        self.cnpj = cnpj
        self.xbz_url = f'https://api.minhaxbz.com.br:5001/api/clientes/GetListaDeProdutos?cnpj={self.cnpj}&token={self.xbz_token}'

    def get_data_from_xbz(self):
        response = requests.get(self.xbz_url)
        return response.json()
    
    def generate_csv(self, data):
        with open('xbz_data.csv', 'w') as f:
            f.write('CodigoComposto;CodigoAmigavel;Nome;SiteLink;ImageLink;CorWebPrincipal;PrecoVendaFormatado;QuantidadeDisponivel;StatusConfiabilidade;Ncm\n')
            for product in data:
                f.write(f"{product['CodigoComposto']};{product['CodigoAmigavel']};{product['Nome']};{product['SiteLink']};{product['ImageLink']};{product['CorWebPrincipal']};{product['PrecoVendaFormatado']};{product['QuantidadeDisponivel']};{product['StatusConfiabilidade']};{product['Ncm']}\n")
        print('CSV gerado com sucesso!')

if __name__ == '__main__':
    integrator = Integrator()
    data = integrator.get_data_from_xbz()
    integrator.generate_csv(data)