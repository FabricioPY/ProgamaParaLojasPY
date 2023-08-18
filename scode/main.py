import tkinter as tk
from tkinter import ttk
from telas_secundarias import Telas_Secudarias


root = tk.Tk()
listas_abas = {}
listas = {}


class Application(Telas_Secudarias):

    def __init__(self):
        self.root = root
        self.tela()
        self.frame_da_tela()
        self.label()
        self.botoes()
        self.entrey()

        root.mainloop()

    def tela(self):
        self.root.title('Jc Valclef Atendimento')
        self.root.configure(background='#F5D17C')
        self.root.attributes('-fullscreen', True)

    def frame_da_tela(self):
        self.frame_alto = tk.Frame(
            self.root, bd=4, bg='#ffffff', highlightthickness=3,)
        self.frame_alto.place(relx=0.01, rely=0.01,
                              relheight=0.17, relwidth=0.98)

        self.frame_1 = tk.Frame(
            self.root, bd=4, bg='#ffffff', highlightthickness=3,)
        self.frame_1.place(relx=0.01, rely=0.20, relheight=0.77, relwidth=0.65)

        self.frame_2 = tk.Frame(
            self.root, bd=4, bg='#ffffff', highlightthickness=3,)
        self.frame_2.place(relx=0.67, rely=0.20, relheight=0.77, relwidth=0.32)

        self.frame_add_produto = tk.Frame(self.frame_2)
        self.frame_add_produto.place(relx=0.01, rely=0.30,
                                     relheight=0.5, relwidth=0.99)

    def abas_d(self):
        self.abas = ttk.Notebook(self.frame_1)
        listas_abas = {}

        listas_abas[f"Aba {len(listas) + 1}"] = tk.Frame(self.abas)
        for aba in listas_abas:
            print(len(listas_abas))
            self.abas.add(listas_abas[f"Aba {len(listas) + 1}"],
                          text=f'Nota{len(listas)}')

        self.abas.place(relx=0.00, rely=0.00, relheight=0.99, relwidth=1)

        self.balconista = tk.Label(self.abas, text='Balcao')
        self.balconista.place(rely=0.05, relheight=0.05, relwidth=1)

        self.lista()

        self.valor_total = tk.Label(self.abas, text='Valor Total:')
        self.valor_total.place(relx=0, rely=0.87,
                               relheight=0.10, relwidth=0.87)

        self.valor_total_n = tk.Label(self.abas, text='0.00')
        self.valor_total_n.place(relx=0.85, rely=0.87,
                                 relheight=0.10, relwidth=0.13)

        self.somar_valor()

        listas[f"Aba {len(listas) + 1}"] = 1

    def botoes(self):
        self.botao_nova_nota = tk.Button(
            self.frame_2, text='Nova\n Nota', command=self.abas_d)
        self.botao_nova_nota.place(relx=0.02, rely=0.02,
                                   relheight=0.11, relwidth=0.23)

        self.botao_bucar_cliente = tk.Button(
            self.frame_alto, text='Buscar', command=self.funciona)
        self.botao_bucar_cliente.place(relx=0.02, rely=0.02,
                                       relheight=0.30, relwidth=0.05)

        self.botao_bucar_produto = tk.Button(
            self.frame_add_produto, text='Buscar', command=self.janela_buscar)
        self.botao_bucar_produto.place(relx=0.25, rely=0.025,
                                       relheight=0.15, relwidth=0.20)

        self.botao_Add = tk.Button(
            self.frame_add_produto, text='Add', command=self.add_novo_item)
        self.botao_Add.place(relx=0.15, rely=0.40,
                             relheight=0.20, relwidth=0.40)

        self.botao_Remove = tk.Button(
            self.frame_add_produto, text='Remove', command=self.remover_item)
        self.botao_Remove.place(relx=0.20, rely=0.7,
                                relheight=0.20, relwidth=0.30)

        self.botao_fechar_nota_P = tk.Button(
            self.frame_2, text='Fechar\n Nota\nP')
        self.botao_fechar_nota_P.place(relx=0.77, rely=0.88,
                                       relheight=0.11, relwidth=0.23)

        self.botao_fechar_nota = tk.Button(self.frame_2, text='Fechar\n Nota',
                                           command=self.fechar_lista)
        self.botao_fechar_nota.place(relx=0.54, rely=0.88,
                                     relheight=0.11, relwidth=0.23)

    def label(self):
        self.cliente = tk.Label(self.frame_alto, text='Cliente:')
        self.cliente.place(relx=0.01, rely=0.80,
                           relheight=0.20, relwidth=1)

        self.qtd = tk.Label(self.frame_add_produto, text='Qtd')
        self.qtd.place(relx=0.75, rely=0.07,
                       relheight=0.15, relwidth=0.15)

    def entrey(self):
        self.produto_add = tk.Entry(self.frame_add_produto)
        self.produto_add.place(relx=0.10, rely=0.20,
                               relheight=0.15, relwidth=0.50)

        self.quantidade = tk.Entry(self.frame_add_produto)
        self.quantidade.place(relx=0.75, rely=0.20,
                              relheight=0.15, relwidth=0.15)

    def lista(self):
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


Application()


'''  def abas_d(self):
        self.abas = ttk.Notebook(self.frame_1)
        if len(listas_abas) == 0:
            self.aba = tk.Frame(self.abas)
            listas_abas[f"Aba {len(listas) + 1}"] = tk.Frame(self.abas)
            self.abas.add(self.aba, text=f'Nota{len(listas)}')

        else:
            print('else fuciona')
            for nome, resutado in listas_abas.items():
                print('for ligado')
                listas_abas[f"Aba {len(listas) + 1}"] = tk.Frame(self.abas)
                if nome == f"Aba {len(listas) + 1}":

                    print(nome)
                    print(resutado)

                    self.abas.add(listas_abas[f"Aba {len(listas) + 1}"],
                                  text=f'Nota{len(listas)}')'''
