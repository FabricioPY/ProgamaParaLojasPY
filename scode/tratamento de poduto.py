import pandas as pd

# Abre csv e retira o cabesario
self.planilha = pd.read_csv(
    c.caminho('downloads') + 'Produtos.csv', sep=';', header=1)

# Retira colunas desnessesarias
planilha_colunas = self.planilha.drop(
    columns=['Empresa', 'Grupo', 'Subgrupo', 'Custo', 'Lucro', 'Unid', 'Peso Bruto',
             'Peso Liq', 'Ncm', 'Cest', 'Cfop', 'Cst Icms', 'Cst Pis', 'Cst Cofins',
             'Complemento', 'Estoque', 'Total Vendido', 'Total Aliq', 'Trib Aprox',
             'Comissao', 'Motivador', 'Ultima Alteracao', 'Impressora', 'Servico',
             'Data Cadastro', 'Imagem', 'Unnamed: 30', 'Unnamed: 31'])

# Cria csv proto para uploads e evia para pasta certa
planilha_colunas.to_csv('Produtos.csv', index=False)
os.system('mv Produtos.csv ' + c.caminho('pasta produtos'))
sleep(10)


# Deleta relatorio antigo
os.system('rm ' + c.caminho('downloads') + 'Produtos.csv')
