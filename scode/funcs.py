import pandas as pd
import datetime


df = pd.read_csv(
    'Produtos_sem.csv')


class Funcs():

    # Botoes da Janela Pricipal

    def add_novo_item(self):
        codigo = self.produto_add.get()
        quantidade = self.quantidade.get()

        if not quantidade:  # Verifica se o Entry está vazio
            quantidade = 1

        self.add(codigo=codigo, quantidade=quantidade)

        self.somar_valor()

    def remover_item(self):
        # Obter o item selecionado
        selection = self.lista_decompra.focus()

        # Obter o item selecionado
        self.lista_decompra.delete(selection)

        self.somar_valor()

    def pemu_dar_item(self, nome):
        # Obter todos os itens da Treeview
        itens = self.lista_decompra.get_children()

        for item in itens:
            if self.lista_decompra.item(item, "text") == nome:
                # Selecionar o item encontrado
                self.lista_decompra.selection_set(item)
                break  # Parar o loop ao encontrar o item

    def fechar_lista(self):
        # Obter a data e hora atual
        data_hora_atual = datetime.datetime.now()
        print(data_hora_atual)

        # Separar a data e o horário
        # data_atual = data_hora_atual.date()
        # horario_atual = data_hora_atual.time()

        codigos = []
        quatidades = []

        nota = ['balcao', {'codigos': codigos,
                'quantidade': quatidades}]

        for item in self.lista_de_compra.get_children():
            codigo = self.lista_de_compra.item(item)['values'][0]
            quatidade = self.lista_de_compra.item(item)['values'][2]
            codigos.append(codigo)
            quatidades.append(quatidade)

            print(codigos)
            print(quatidades)
            print(nota)

        nota = pd.DataFrame(nota)

        nota.to_csv(f'nota:{data_hora_atual}.csv')

    def double_click_alterar(self, event):
        item = self.lista_de_compra.focus()
        produto = self.lista_de_compra.item(item)['values'][1]
        print(produto)
        self.janela_de_alterar()

    # Botoes da Janela de Busca

    def buscar_nome(self, event):
        nomes = self.entrey_bucar.get()

        # função para buscar itens pelo nome
        nomes = nomes.split()
        filtered_df = df['Nome'].notnull()
        for nome in nomes:
            filtered_1 = df['Nome'].str.contains(nome, case=False)
            filtered_df = (filtered_df & filtered_1)

        # Limpar a lista de resultados
        filtered_df = df[filtered_df]
        self.lista_de_busca.delete(*self.lista_de_busca.get_children())

        for index, row in filtered_df.iterrows():
            self.lista_de_busca.insert('',
                                       index,
                                       text=index,
                                       values=(row['Codigo'], row['Nome'],
                                               row['Valor'], 10))

    def double_click_buscar(self, event):
        # Obter o item selecionado
        item = self.lista_de_busca.focus()
        codigo = self.lista_de_busca.item(item)['values'][0]

        codigo = str(codigo)

        self.add(codigo=codigo, quantidade=1)

        self.somar_valor()

        self.root_buscar.destroy()

    # Botoes da Janela de Alterar

    def alterar_quantidade(self):
        # Recebeu
        quatidade = self.ja_alterar_quatidade.get()
        codigo = self.ja_codigo_poduto.cget('text')

        # Tratameto do Recebido
        codigo = str(codigo)[4:]

        # Verifica se o Entry está vazio

        # Procesamento
        for item in self.lista_de_compra.get_children():
            verificar = str(self.lista_de_compra.item(item)['values'][0])

            if verificar == codigo:
                valor = self.lista_de_compra.item(item)['values'][3]
                valor = float(quatidade) * float(valor)

            # Passar informacao
                self.root_alterar.destroy()
                self.lista_de_compra.set(item, 'Qtd', quatidade)
                self.lista_de_compra.set(item, 'Vlr_Total',
                                         "{:.2f}".format(valor))

        self.somar_valor()

    def alterar_deletar(self):
        codigo = self.ja_codigo_poduto.cget('text')
        codigo = str(codigo)[4:]

        for item in self.lista_de_compra.get_children():
            verificar = str(self.lista_de_compra.item(item)['values'][0])
            if verificar == codigo:
                self.root_alterar.destroy()
                self.lista_de_compra.delete(item)

        self.somar_valor()

    # Fucionamento do add  #

    def add(self, codigo, quantidade):
        aba_selecionada = self.abas.tab(self.abas.select(), "text")
        print(aba_selecionada)

        produto = df.loc[(df['Codigo'] == codigo) | (df['Id'] == codigo)]

        if len(produto) == 1:
            for i, row in produto.iterrows():
                valor_total = round(int(quantidade) * row['Valor'], 2)
                self.lista_de_compra.insert('', i, text='', values=(
                    row['Id'], row['Nome'], quantidade,
                    "{:.2f}".format(row['Valor']),
                    "{:.2f}".format(valor_total)))

    def somar_valor(self):
        soma = 0

        for item in self.lista_de_compra.get_children():
            valor = self.lista_de_compra.item(item)['values'][4]
            soma += float(valor)
        self.valor_total_n.config(text="R$:{:.2f}".format(soma))

    def funciona(self):
        print('funciona')


'''    def criar_nova_aba():
        # Cria uma nova aba no notebook
        self.nova_aba = ttk.Frame(notebook)
        self.notebook.add(nova_aba, text=f"Aba {len(listas) + 1}")

        # Cria uma nova lista para a nova aba
        self.lista_de_compra = ttk.Treeview(
            self.abas, height=4,
            columns=('Codigo', 'Nome', 'Qtd', 'Vlr_Unit', 'Vlr_Total'))
        self.lista_de_compra.heading('#0', text='')
        self.lista_de_compra.heading('#1', text='Codigo')
        self.lista_de_compra.heading('#2', text='Nome')
        self.lista_de_compra.heading('#3', text='Qtd')
        self.lista_de_compra.heading('#4', text='Vlr_Unit')
        self.lista_de_compra.heading('#5', text='Vlr_Total')

        self.lista_de_compra.column('#0', width=1)
        self.lista_de_compra.column('#1', width=100)
        self.lista_de_compra.column('#2', width=450)
        self.lista_de_compra.column('#3', width=40)
        self.lista_de_compra.column('#4', width=100)
        self.lista_de_compra.column('#5', width=100)

        self.lista_de_compra.place(relx=0.00, rely=0.11,
                                   relheight=0.75, relwidth=0.98)

        self.scroo_list = ttk.Scrollbar(self.abas, orient='vertical')
        self.lista_de_compra.configure(yscroll=self.scroo_list.set)
        self.scroo_list.place(relx=0.98, rely=0.11,
                              relheight=0.75, relwidth=0.02)

        self.lista_de_compra.bind('<Double-1>', self.janela_de_alterar)
'''
