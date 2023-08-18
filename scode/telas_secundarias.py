import tkinter as tk
from tkinter import ttk
from funcs import Funcs


class Telas_Secudarias(Funcs):
    # Janela  de Busca
    def janela_buscar(self):
        self.tela_buscar()
        self.jb_frame_buscar()
        self.jb_entrey()
        self.jb_lista()

    def tela_buscar(self):
        self.root_buscar = tk.Toplevel()
        self.root_buscar.title('Buscar')
        self.root_buscar.configure(background='#F5D17C')
        self.root_buscar.geometry("1200x588")

    def jb_frame_buscar(self):
        self.frame_buscar = tk.Frame(self.root_buscar,
                                     bd=4, bg='#ffffff', highlightthickness=3,)
        self.frame_buscar.place(relx=0.01, rely=0.01,
                                relheight=0.10, relwidth=0.95)

        self.fb_lista = tk.Frame(self.root_buscar,
                                 bd=4, bg='#ffffff', highlightthickness=3,)
        self.fb_lista.place(relx=0.01, rely=0.15,
                            relheight=0.80, relwidth=0.95)

    def jb_entrey(self):
        self.entrey_bucar = tk.Entry(self.frame_buscar)
        self.entrey_bucar.place(relx=0.01, rely=0.01,
                                relheight=0.90, relwidth=0.90)

# faz o binding da função buscar() com o evento de digitar na caixa de entrada
        self.entrey_bucar.bind("<KeyRelease>", self.buscar_nome)

    def jb_lista(self):
        self.lista_de_busca = ttk.Treeview(
            self.fb_lista, columns=('Codigo', 'Nome', 'Valor', 'Qtd'))
        self.lista_de_busca.heading('#0', text='')
        self.lista_de_busca.heading('#1', text='Codigo')
        self.lista_de_busca.heading('#2', text='Nome')
        self.lista_de_busca.heading('#3', text='Valor')
        self.lista_de_busca.heading('#4', text='Qtd')

        self.lista_de_busca.column('#0', width=1)
        self.lista_de_busca.column('#1', width=90)
        self.lista_de_busca.column('#2', width=490)
        self.lista_de_busca.column('#3', width=110)
        self.lista_de_busca.column('#4', width=110)

        self.lista_de_busca.place(relx=0.01, rely=0.01,
                                  relheight=0.90, relwidth=0.98)

        self.scroo_list = ttk.Scrollbar(self.fb_lista, orient='vertical')
        self.lista_de_busca.configure(yscroll=self.scroo_list.set)
        self.scroo_list.place(relx=0.98, rely=0.01,
                              relheight=0.90, relwidth=0.02)

        self.lista_de_busca.bind('<Double-1>', self.double_click_buscar)

    # Janela  de Alterar ou Deletar

    def janela_de_alterar(self, event):
        item = self.lista_de_compra.focus()
        nome = self.lista_de_compra.item(item)['values'][1]
        valor = self.lista_de_compra.item(item)['values'][3]
        codigo = self.lista_de_compra.item(item)['values'][0]
        quantidade = self.lista_de_compra.item(item)['values'][2]
        self.tela_alterar()
        self.ja_frame()
        self.ja_botoes()
        self.ja_entrey()
        self.ja_label(nome=nome,
                      codigo=codigo,
                      quantidade=quantidade,
                      valor_total=valor)

    def tela_alterar(self):
        self.root_alterar = tk.Toplevel()
        self.root_alterar.title('Alterar')
        self.root_alterar.configure(background='#F5D17C')
        self.root_alterar.geometry("500x250")

    def ja_frame(self):
        self.frame_nome_do_produto = tk.Frame(self.root_alterar,
                                              bd=4, bg='#ffffff',
                                              highlightthickness=3,)
        self.frame_nome_do_produto.place(relx=0.01, rely=0.01,
                                         relheight=0.57, relwidth=0.97)

        self.frame_alterar = tk.Frame(self.root_alterar,
                                      bd=4, bg='#ffffff',
                                      highlightthickness=3,)
        self.frame_alterar.place(relx=0.01, rely=0.60,
                                 relheight=0.37, relwidth=0.97)

    def ja_botoes(self):
        self.ja_botao_de_aterar_valor = tk.Button(
            self.frame_alterar, text='Alterar',
            command=self.alterar_quantidade)
        self.ja_botao_de_aterar_valor.place(relx=0.30, rely=0.10,
                                            relheight=0.80, relwidth=0.30)

        self.ja_botao_deletar = tk.Button(
            self.frame_alterar, text='Deletar',
            command=self.alterar_deletar)
        self.ja_botao_deletar.place(relx=0.65, rely=0.10,
                                    relheight=0.80, relwidth=0.30)

    def ja_entrey(self):
        self.ja_alterar_quatidade = tk.Entry(self.frame_alterar)
        self.ja_alterar_quatidade.place(relx=0.05, rely=0.10,
                                        relheight=0.80, relwidth=0.20)

    def ja_label(self, nome, codigo, quantidade, valor_total):
        self.ja_nome_poduto = tk.Label(
            self.frame_nome_do_produto, text=nome)
        self.ja_nome_poduto.place(relx=0.05, rely=0.01,
                                  relheight=0.45, relwidth=0.90)

        self.ja_valor_poduto = tk.Label(
            self.frame_nome_do_produto, text=f'Valor total:\nR${valor_total}')
        self.ja_valor_poduto.place(relx=0.32, rely=0.35,
                                   relheight=0.30, relwidth=0.40)

        self.ja_valor_uni_poduto = tk.Label(
            self.frame_nome_do_produto,
            text=f'Valor Unidade:\nR${valor_total}')
        self.ja_valor_uni_poduto.place(relx=0.40, rely=0.75,
                                       relheight=0.25, relwidth=0.25)

        self.ja_codigo_poduto = tk.Label(
            self.frame_nome_do_produto, text=f'Cod:{codigo}')
        self.ja_codigo_poduto.place(relx=0.02, rely=0.80,
                                    relheight=0.15, relwidth=0.25)

        self.ja_quantidade_poduto = tk.Label(
            self.frame_nome_do_produto, text=f'Qtd:{quantidade}')
        self.ja_quantidade_poduto.place(relx=0.80, rely=0.75,
                                        relheight=0.25, relwidth=0.20)
