import requests
from config import cnpj, xbz_token


class Integrator:

    def __init__(self, cnpj=cnpj, xbz_token=xbz_token):
        self.xbz_token = xbz_token
        self.cnpj = cnpj
        self.xbz_url = f'https://api.minhaxbz.com.br:5001/api/clientes/GetListaDeProdutos?cnpj={self.cnpj}&token={self.xbz_token}'

    def get_data_from_xbz(self):
        response = requests.get(self.xbz_url)
        return response.json()
    
    def generate_csv(self, data):
        columns = [
            'ID',
            'Código',
            'Descrição',
            'Unidade',
            'NCM',
            'Origem',
            'Preço',
            'Valor IPI fixo',
            'Observações',
            'Situação',
            'Estoque',
            'Preço de custo',
            'Cód no fornecedor',
            'Fornecedor',
            'Localização',
            'Estoque máximo',
            'Estoque mínimo',
            'Peso líquido (Kg)',
            'Peso bruto (Kg)',
            'GTIN/EAN',
            'GTIN/EAN da embalagem',
            'Largura do produto',
            'Altura do produto',
            'Profundidade do produto',
            'Data Validade',
            'Descrição do Produto no Fornecedor',
            'Descrição Complementar',
            'Itens p/ caixa',
            'Produto Variação',
            'Tipo Produção',
            'Classe de enquadramento do IPI',
            'Código da lista de serviços',
            'Tipo do item',
            'Grupo de Tags/Tags',
            'Tributos',
            'Código Pai',
            'Código Integração',
            'Grupo de produtos',
            'Marca',
            'CEST',
            'Volumes',
            'Descrição Curta',
            'Cross-Docking',
            'URL Imagens Externas',
            'Link Externo',
            'Meses Garantia no Fornecedor',
            'Clonar dados do pai',
            'Condição do produto',
            'Frete Grátis',
            'Número FCI',
            'Vídeo',
            'Departamento',
            'Unidade de medida',
            'Preço de compra',
            'Valor base ICMS ST para retenção',
            'Valor ICMS ST para retenção',
            'Valor ICMS próprio do substituto',
            'Categoria do produto',
            'Informações Adicionais'
        ]
        with open('xbz_data.csv', 'w') as f:
            first_line = ';'.join(columns) + '\n'
            f.write(first_line)
            for product in data:
                line = [' ',
                        (product['CodigoComposto'].replace('$', '')),
                        product['Nome'],
                        'UN',
                        (product['Ncm'].replace('O', '0') if product['Ncm'] else '999999'),
                        ' ',
                        product['PrecoVendaFormatado'],
                        '0',
                        '',
                        product['StatusConfiabilidade'],
                        product['QuantidadeDisponivel'],
                        '0',
                        product['CodigoXbz'],
                        '',
                        '',
                        '1000',
                        '0',
                        product['Peso'], '',
                        '','',
                        product['Largura'],
                        product['Altura'],
                        product['Profundidade'],
                        '',
                        product['Nome'],
                        product['Nome'],
                        '1',
                        product['CorWebPrincipal'],
                        '','','','',
                        '',
                        '','','','','','','','','',
                        product['ImageLink'],
                        product['SiteLink'],
                        '','','','','','',
                        '','','','','','','','']
                line = [str(x) for x in line]
                # breakpoint()
                line = ";".join(line) + '\n'
                f.write(line)
        print('CSV gerado com sucesso!')

if __name__ == '__main__':
    integrator = Integrator()
    data = integrator.get_data_from_xbz()
    integrator.generate_csv(data)