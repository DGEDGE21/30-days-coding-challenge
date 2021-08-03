from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import Combobox
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import Calendar
from modelo import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
import threading




root=Tk()
root.configure(bg='#E3E3E3')
root.geometry("1330x700")
#franes primarios
global op
global navegacao
global inforoot
global holder
navegacao = Frame(root, width=400, height=30)
op = Frame(root)
inforoot = Label(navegacao, bg='#019d95', width=140)
holder = Label(inforoot, bg='#019d95')

def registar_aluno():
    global navegacao
    global inforoot
    global imageholder
    inforoot.destroy()
    reg = Button(navegacao1, text='Registar', font='D-DIN', width='32', fg='white', bg='#019d95', relief="flat",
                 borderwidth=0, command=registar_aluno)
    seac = Button(navegacao1, text='Pesquisar ', font='D-DIN', width='30', bg='white', relief="flat",
                  borderwidth=0, command=pesquisar_aluno)
    aprov = Button(navegacao1, text='Aproveitamento', font='D-DIN', width='30', bg='white', relief="flat",
                   borderwidth=0,command=aproveitamento_geral)
    lisy = Button(navegacao1, text='Registos', font='D-DIN', width='32', bg='white',
                  relief="flat", borderwidth=0,command=registo)
    reg.grid(row=0, column=0)
    seac.grid(row=0, column=1)
    aprov.grid(row=0, column=2)
    lisy.grid(row=0, column=3)

    inforoot = Label(navegacao, bg='#019d95', width=140)
    inforoot.grid(pady=10)
    novo_pti = Label(inforoot, text="Novo Aluno", font="D-DIN", fg="White", bg="#053f40", width=122)
    novo_pti.grid(sticky=E + W)
    #Label cotento image holder info
    holder=Label(inforoot, bg='#019d95')
    holder.grid(sticky=E + W)
    #Label da imaggem
    way="an.PNG"
    w2 = Image.open(way)
    w2.thumbnail((370, 300))
    imagem2 = ImageTk.PhotoImage(w2)

    imageholder=Label(holder,image=imagem2)
    imageholder.image = imagem2
    imageholder.grid(row=0,column=0)

    #label das informacoes basicas
    novo_pt = Label(holder, bg='#019d95')
    novo_pt.grid(row=0,column=3,sticky=E + W)
    #funcao responsavel por abrir a imagagem e projectar na label
    def nav():
        global imagi
        global imageholder
        imageholder.destroy()
        sd = filedialog.askopenfilename()
        print(sd)
        w = Image.open(sd)
        w.thumbnail((370, 300))
        imagem1 = ImageTk.PhotoImage(w)
        imageholder = Label(holder,image=imagem1)
        imageholder.grid(row=0, column=0)
        imageholder.image = imagem1
        imagi = open(sd, 'rb').read()
    def registross():
        global a
        a = Toplevel(bg="#019d95")
        a.overrideredirect(True)
        lab = Label(a, text="Registando na base dados ONLINE....", bg="#019d95", fg="White", font="D-DIN")
        lab.grid()
        io = ttk.Progressbar(a, orient=HORIZONTAL, mode="determinate", length=500)
        io.grid()
        io.start()
        io['value'] = 100

        def bd_man():
            global a
            data_acess("base dados remota ").registar_aluno(nomei.get(),apelidoi.get(),sexoi.get(),dnascimentoi.get(),
                                                                                nati.get(),cursoi.get(),parantesi.get(),dingressoi.get()
                                                                                ,nrbi.get(),nuiti.get(),imagi,float(nota1i.get())
                                                                                ,float(nota2i.get()),"PNG")
            a.destroy()
            a = Toplevel(bg="#019d95")
            a.overrideredirect(True)
            lab = Label(a, text="Registado com sucesso....", bg="#019d95", fg="White", font="D-DIN")
            lab.grid()

        threading.Thread(target=bd_man).start()
    # nome
    nome = Label(novo_pt, text="Nome:", font="D-DIN", fg="White", bg='#019d95')
    nome.grid(row=0, column=0)
    nomei = Entry(novo_pt,width=30,font='D-DIN')
    nomei.grid(row=0, column=1, padx=5)
    #Apelido
    apelido = Label(novo_pt, text="Apelido:", font="D-DIN", fg="White", bg='#019d95')
    apelido.grid(row=0, column=2)
    apelidoi = Entry(novo_pt, width=30, font='D-DIN')
    apelidoi.grid(row=0, column=3, padx=5,pady=5)
    #SEXO
    sexo = Label(novo_pt, text="sexo:", font="D-DIN", fg="White", bg='#019d95')
    sexo.grid(row=1, column=2, padx=5)
    sexoi = Combobox(novo_pt, values=["Feminino", "Masculino"],
                          font="D-DIN",width=17)
    sexoi.grid(row=1, column=3, padx=5)
    #DATA DE NASCIMENTO
    dnascimento=Label(novo_pt,text="Data de Nascimento:", font="D-DIN", fg="White", bg='#019d95')
    dnascimento.grid(row=1,column=0)
    dnascimentoi=Entry(novo_pt, width=30, font='D-DIN')
    dnascimentoi.grid(row=1, column=1, padx=5,pady=5)
    #Naturalidade
    nat=Label(novo_pt,text="Nacionalidade:", font="D-DIN", fg="White", bg='#019d95')
    nat.grid(row=2,column=0)
    nati = Entry(novo_pt, width=30, font='D-DIN')
    nati.grid(row=2, column=1, padx=5, pady=5)
    #Curso
    curso=Label(novo_pt,text="Curso:", font="D-DIN", fg="White", bg='#019d95')
    curso.grid(row=2,column=2)
    cursoi = Entry(novo_pt, width=30, font='D-DIN')
    cursoi.grid(row=2, column=3, padx=5, pady=5)
    # Parantes
    parantes = Label(novo_pt, text="Progenitores:", font="D-DIN", fg="White", bg='#019d95')
    parantes.grid(row=3, column=0)
    parantesi = Entry(novo_pt, width=30, font='D-DIN')
    parantesi.grid(row=3, column=1, padx=5, pady=5)
    # DATA de INGRESSO
    dingresso = Label(novo_pt, text="Data ingresso:", font="D-DIN", fg="White", bg='#019d95')
    dingresso.grid(row=3, column=2)
    dingressoi = Entry(novo_pt, width=30, font='D-DIN')
    dingressoi.grid(row=3, column=3, padx=5, pady=5)
    #Numero deBI
    nrb=Label(novo_pt, text="Numero de BI:", font="D-DIN", fg="White", bg='#019d95')
    nrb.grid(row=4, column=0)
    nrbi = Entry(novo_pt, width=30, font='D-DIN')
    nrbi.grid(row=4, column=1, padx=5, pady=5)
    # Numero de NUIT
    nuit = Label(novo_pt, text="Numero de NUIT:", font="D-DIN", fg="White", bg='#019d95')
    nuit.grid(row=4, column=2)
    nuiti = Entry(novo_pt, width=30, font='D-DIN')
    nuiti.grid(row=4, column=3, padx=5, pady=5)
    #Nota1
    nota1=Label(novo_pt, text="Teste 1:", font="D-DIN", fg="White", bg='#019d95')
    nota1.grid(row=5, column=0)
    nota1i = Entry(novo_pt, width=30, font='D-DIN')
    nota1i.grid(row=5, column=1, padx=5, pady=5)
    #
    nota2 = Label(novo_pt, text="Teste 2:", font="D-DIN", fg="White", bg='#019d95')
    nota2.grid(row=5, column=2)
    nota2i = Entry(novo_pt, width=30, font='D-DIN')
    nota2i.grid(row=5, column=3, padx=5, pady=5)
    # Adicionar IMG

    imagem = Label(novo_pt, text="Imagem:", font="D-DIN", fg="White", bg='#019d95')
    imagem.grid(row=6, column=0)

    anuncio = Button(novo_pt, text='Adicionar Imagem', font='D-DIN', width='20', bg="#053f40", fg='white',
                     relief="flat", borderwidth=0,command=nav)
    anuncio.grid(row=6, column=1)
    #Registar Estudante
    regis = Button(novo_pt, text='Registar Aluno', font='D-DIN', width='20', bg="#053f40", fg='white',
                     relief="flat", borderwidth=0, command=registross)
    regis.grid(row=7, column=3)
    #Responsive
    navegacao.grid(ipady=310)

def pesquisar_aluno():
    global navegacao
    global inforoot
    global imageholder
    global holder
    inforoot.destroy()
    reg = Button(navegacao1, text='Registar', font='D-DIN', width='32', bg='white', relief="flat",
                 borderwidth=0, command=registar_aluno)
    seac = Button(navegacao1, text='Pesquisar ', font='D-DIN', width='30', fg='white', bg='#019d95', relief="flat",
                  borderwidth=0, command=pesquisar_aluno)
    aprov = Button(navegacao1, text='Aproveitamento', font='D-DIN', width='30', bg='white', relief="flat",
                   borderwidth=0,command=aproveitamento_geral)
    lisy = Button(navegacao1, text='Registos', font='D-DIN', width='32', bg='white',
                  relief="flat", borderwidth=0,command=registo)
    reg.grid(row=0, column=0)
    seac.grid(row=0, column=1)
    aprov.grid(row=0, column=2)
    lisy.grid(row=0, column=3)

    inforoot = Label(navegacao, bg='#019d95', width=140)
    inforoot.grid(pady=10)
    def find_student(args):
        global holder

        a = Toplevel(bg="#019d95")
        a.overrideredirect(True)
        lab = Label(a, text="Conectando a base dados ONLINE....", bg="#019d95", fg="White", font="D-DIN")
        lab.grid()
        io = ttk.Progressbar(a, orient=HORIZONTAL, mode="determinate", length=500)
        io.grid()
        io.start()
        io['value'] = 100
        def bd_man():
            global holder
            global extracao
            extracao = data_acess(
                "base dados remota ").pesquisar(
                int(fg.get()))
            afixar()
        threading.Thread(target=bd_man).start()
        def afixar():
            global holder
            if extracao==[]:
                messagebox.askokcancel(title="Aluno não encontrado", icon="error",
                                       detail="O numero de identificação que introduziu\nnão consta da base de dados")
            else:
                holder.destroy()
                #montando a imagem
                gerar_img = data_acess("base dados remota ").recuperar_img(int(fg.get()))
                open(f"{gerar_img[2]}.{gerar_img[1]}", 'wb').write(gerar_img[0])
                #informacoes sobre o aluno
                holder = Label(inforoot, bg='#019d95')
                holder.grid(sticky=E + W)
                #----------------
                c=Label(holder, width=100, bg='#019D95')
                c.grid(sticky=E + W, padx=10,row=0,column=0)
                c_info=Label(holder, width=100, bg='#019D95')
                c_info.grid(row=0,column=1, sticky=W)
                # informacoes sobre o aluno
                #nome
                nome = Label(c_info, text="Nome:", fg='white', font='D-DIN', bg='#019D95')
                nome.grid(row=0, column=0, pady=17)
                nomei = Label(c_info, text=extracao[1], fg='#019D95', font='D-DIN', bg='white')
                nomei.grid(row=0, column=1)
                #apelido
                apelido = Label(c_info, text="Apelido:", fg='white', font='D-DIN', bg='#019D95')
                apelido.grid(row=0, padx=10, column=2, pady=17)
                apelidoi = Label(c_info, text=extracao[2], fg='#019D95', font='D-DIN', bg='white')
                apelidoi.grid(row=0, column=3, pady=17)
                #sexo
                sexo = Label(c_info, text="Sexo:", fg='white', font='D-DIN', bg='#019D95')
                sexo.grid(row=1, column=0, padx=10)
                sexoi = Label(c_info, text=extracao[3], fg='#019D95', font='D-DIN', bg='white')
                sexoi.grid(row=1, column=1)
                #Dnascimento
                dnasci = Label(c_info, text="D.Nascim:", fg='white', font='D-DIN', bg='#019D95')
                dnasci.grid(row=1, column=2, padx=10)
                dnascii = Label(c_info, text=extracao[4], fg='#019D95', font='D-DIN', bg='white')
                dnascii.grid(row=1, column=3)
                #nacionalidade
                nacio = Label(c_info, text="Nacionalidade:", fg='white', font='D-DIN', bg='#019D95')
                nacio.grid(row=2, column=0, padx=10)
                nacioi = Label(c_info, text=extracao[5], fg='#019D95', font='D-DIN', bg='white')
                nacioi.grid(row=2, column=1, pady=17)
                #curso
                curso = Label(c_info, text="Curso:", fg='white', font='D-DIN', bg='#019D95')
                curso.grid(row=2, column=2, padx=10)
                cursoi = Label(c_info, text=extracao[6], fg='#019D95', font='D-DIN', bg='white')
                cursoi.grid(row=2, column=3)
                #pais
                parent = Label(c_info, text="Parente:", fg='white', font='D-DIN', bg='#019D95')
                parent.grid(row=3, column=0, padx=10)
                parenti = Label(c_info, text=extracao[7], fg='#019D95', font='D-DIN', bg='white')
                parenti.grid(row=3, column=1)
                #dingresso
                ingresso = Label(c_info, text="Ingresso:", fg='white', font='D-DIN', bg='#019D95')
                ingresso.grid(row=3, column=2, padx=10)
                ingressoi = Label(c_info, text=extracao[8], fg='#019D95', font='D-DIN', bg='white')
                ingressoi.grid(row=3, column=3)
                #bi
                bi = Label(c_info, text="BI:", fg='white', font='D-DIN', bg='#019D95')
                bi.grid(row=4, column=0, padx=10)
                bii = Label(c_info, text=extracao[8], fg='#019D95', font='D-DIN', bg='white')
                bii.grid(row=4, column=1, pady=17)
                #Nuit
                sexo = Label(c_info, text="Nuit:", fg='white', font='D-DIN', bg='#019D95')
                sexo.grid(row=4, column=2, padx=10)
                sexoi = Label(c_info, text=extracao[0], fg='#019D95', font='D-DIN', bg='white')
                sexoi.grid(row=4, column=3)
                #nota1
                testp = Label(c_info, text="Teste1:", fg='white', font='D-DIN', bg='#019D95')
                testp.grid(row=5, column=0, padx=10)
                testpi = Label(c_info, text=extracao[10], fg='#019D95', font='D-DIN', bg='white')
                testpi.grid(row=5, column=1)
                #nota2
                tests = Label(c_info, text="Teste2:", fg='white', font='D-DIN', bg='#019D95')
                tests.grid(row=5, column=2, padx=10)
                testsi = Label(c_info, text=extracao[11], fg='#019D95', font='D-DIN', bg='white')
                testsi.grid(row=5, column=3)

                imag = Label(c_info, text="IMAGEM:", bg='#053f40', fg='white', font='D-DIN')
                # imag.grid(row=0, column=7)
                w = Image.open(f"{gerar_img[2]}.{gerar_img[1]}")
                w.thumbnail((370, 300))
                imagem1 = ImageTk.PhotoImage(w)
                retrato = Label(c, image=imagem1)
                retrato.grid(row=0, padx=20, column=0)
                retrato.image = imagem1
                navegacao.grid(ipady=250)
    novo_pti = Label(inforoot, text="Pesquisar de Aluno", font="D-DIN", fg="White", bg="#053f40", width=122)
    novo_pti.grid(sticky=E + W)

    import conct
    a = conct.start_listening("sdsd", "dsdsd")

    pesquisa = Label(inforoot, bg='#019d95')
    pesquisa.grid(sticky=E + W, pady=7)

    info = Label(pesquisa, text="INTRODUZA O CODIGO", bg='#053f40', fg='white', font='D-DIN')
    info.grid(row=0, column=0)
    fg = Entry(pesquisa, width=103, font='D-DIN', relief="flat",
               borderwidth=0)
    fg.grid(row=0, column=1)
    fg.bind('<Return>', find_student)
    navegacao.grid(ipady=400)

def aproveitamento_geral():
    global navegacao
    global inforoot
    global imageholder
    global a
    inforoot.destroy()
    reg = Button(navegacao1, text='Registar', font='D-DIN', width='32', bg='white', relief="flat",
                 borderwidth=0, command=registar_aluno)
    seac = Button(navegacao1, text='Pesquisar ', font='D-DIN', width='30', bg='white', relief="flat",
                  borderwidth=0, command=pesquisar_aluno)
    aprov = Button(navegacao1, text='Aproveitamento', font='D-DIN', width='30', fg='white', bg='#019d95', relief="flat",
                   borderwidth=0, command=aproveitamento_geral)
    lisy = Button(navegacao1, text='Registos', font='D-DIN', width='32', bg='white',
                  relief="flat", borderwidth=0,command=registo)
    reg.grid(row=0, column=0)
    seac.grid(row=0, column=1)
    aprov.grid(row=0, column=2)
    lisy.grid(row=0, column=3)
    inforoot = Label(navegacao, bg='#019d95', width=140)
    inforoot.grid(pady=10)
    navegacao.grid(ipady=430)
    a=Toplevel(bg="#019d95")
    a.overrideredirect(True)
    lab=Label(a,text="Conectando a base dados ONLINE....",bg="#019d95",fg="White",font="D-DIN")
    lab.grid()
    io=ttk.Progressbar(a,orient=HORIZONTAL,mode="determinate",length=500)
    io.grid()
    io.start()
    io['value'] = 100

    def bd_man():
        global ai
        ai=data_acess("pbase dados remota ").aproveita()
        dash_board()

    threading.Thread(target=bd_man).start()
    def dash_board():
        global a
        a.destroy()
        info=Label(inforoot, bg='#019d95')
        info.grid()
        nc = Label(info, text=f'Numero de Alunos Aprovados: {ai[0]}',bg='#019d95', font='D-DINExp-Bold', fg='#053f40')
        nc.grid(row=0, column=0, padx=10)
        nc2 = Label(info, text=f'Facturas de Alunos Reprovados: {ai[1]}',bg='#019d95', font='D-DINExp-Bold', fg='red')
        nc2.grid(row=0, column=1, padx=10)

        dash = Label(inforoot)
        dash.grid()
        f = Figure(figsize=(4, 4), dpi=100)
        a = f.add_subplot(111)
        b = f.add_subplot(111)

        a.bar([1], [ai[0]], label='Positivo', width=0.2, color='#053f40')
        b.bar([2], [ai[1]], label='Negativo', width=0.2, color='red')
        a.get_xaxis().set_visible(False)
        b.get_xaxis().set_visible(False)
        # f.legend()
        canvas = FigureCanvasTkAgg(f, dash)
        # canvas.show()
        # NavigationToolbar2Tk.info()
        canvas.get_tk_widget().grid(row=0, column=0)
        # pie chart
        fi = Figure(figsize=(5, 4), dpi=100)
        circulo = fi.add_subplot(111)
        parcelas = [ai[0], ai[1]]
        actividades = ['Positivo', 'Negativo']
        colr = ['#053f40', 'red', ]
        circulo.pie(parcelas, wedgeprops=dict(width=0.3), startangle=0, colors=colr, autopct='%1.1f%%')
        canvas = FigureCanvasTkAgg(fi, dash)
        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-"),
                  bbox=bbox_props, zorder=0, va="center")
        fi.legend(actividades)

        canvas.get_tk_widget().grid(row=0, column=1)
        navegacao.grid(ipady=222)

def  registo():
    global navegacao
    global inforoot
    global imageholder
    inforoot.destroy()
    reg = Button(navegacao1, text='Registar', font='D-DIN', width='32', bg='white', relief="flat",
                 borderwidth=0, command=registar_aluno)
    seac = Button(navegacao1, text='Pesquisar ', font='D-DIN', width='30', bg='white', relief="flat",
                  borderwidth=0, command=pesquisar_aluno)
    aprov = Button(navegacao1, text='Aproveitamento', font='D-DIN', width='30', bg='white', relief="flat",
                   borderwidth=0, command=aproveitamento_geral)
    lisy = Button(navegacao1, text='Registos', font='D-DIN', width='32', fg='white', bg='#019d95',
                  relief="flat", borderwidth=0, command=registo)
    reg.grid(row=0, column=0)
    seac.grid(row=0, column=1)
    aprov.grid(row=0, column=2)
    lisy.grid(row=0, column=3)
    inforoot = Label(navegacao, bg='#019d95', width=14230)
    inforoot.grid(pady=6,stick=E+W)
    kk=Label(inforoot,text="Lista de Alunos Registados",width=127,font="D-DIN",fg="White", bg='#019d95')
    kk.grid(sticky=E+W)
    navegacao.grid(ipady=430)
    #top level
    a = Toplevel(bg="#019d95")
    a.overrideredirect(True)
    lab = Label(a, text="Conectando a base dados ONLINE....", bg="#019d95", fg="White", font="D-DIN")
    lab.grid()
    io = ttk.Progressbar(a, orient=HORIZONTAL, mode="determinate", length=500)
    io.grid()
    io.start()
    io['value'] = 100
    def bd_manuseamento():
        global ai
        global kl
        ai = data_acess("base dados remota ").lista_alunos()
        kl=data_acess("base dados remota ").lista_alunosid()
        afixar()
    threading.Thread(target=bd_manuseamento).start()
    def afixar():
        tabela = ttk.Treeview(inforoot, height=29)
        tabela['columns'] = ("Nome", "Apelido", "Sexo", "Nascimento", "Nacionalidade", "Curso", "BI","NUIT")
        tabela.column("#0", width=10)
        tabela.column("Nome", width=10, minwidth=60)
        tabela.column("Apelido", width=10, minwidth=60)
        tabela.column("Sexo", width=10, minwidth=60)
        tabela.column("Nascimento", width=10, minwidth=60)
        tabela.column("Nacionalidade", width=10, minwidth=60)
        tabela.column("Curso", width=10, minwidth=60)
        tabela.column("BI", width=10, minwidth=60)
        tabela.column("NUIT", width=10, minwidth=60)
        # heading
        tabela.heading("#0", text="N.Produto")
        tabela.heading("Nome", text="Nome")
        tabela.heading("Apelido", text="Apelido")
        tabela.heading("Sexo", text="Sexo")
        tabela.heading("Nascimento", text="Nascimento")
        tabela.heading("Nacionalidade", text="Nacionalidade")
        tabela.heading("Curso", text="Curso")
        tabela.heading("BI", text="BI")
        tabela.heading("NUIT",text="NUIT")

        #
        tabela.winfo_x()
        a = 0
        while a != len(ai):
            tabela.insert(parent='', index='end', iid=a, text=kl[a],
                          values=ai[a])
            a += 1
        tabela.grid(sticky=E + W)
        navegacao.grid(ipady=120)

# navegcaoop=Frame(root)
navegacao = Frame(root, width=400, height=30)
# ik=Label(op,bg='blue')
pagina_inicial = Button(op, text='Página inicial', font='D-DINExp-Bold', fg='#019d95', width='12', relief="flat",
                        borderwidth=0)
navegacao1 = Label(navegacao, bg='#019d95')
reg = Button(navegacao1, text='Registar', font='D-DIN', width='32' ,fg='white', bg='#019d95', relief="flat",
                  borderwidth=0,command=registar_aluno)
seac = Button(navegacao1, text='Pesquisar ', font='D-DIN', width='30', bg='white', relief="flat",
                 borderwidth=0,command=pesquisar_aluno)
aprov = Button(navegacao1, text='Aproveitamento', font='D-DIN', width='30', bg='white', relief="flat",
                     borderwidth=0,command=aproveitamento_geral)
lisy = Button(navegacao1, text='Registos', font='D-DIN', width='32', bg='white',
                 relief="flat", borderwidth=0,command=registo)

op.grid(row=0, column=0, padx=50, pady=20, ipady=440)
navegacao.grid(row=0, column=1, padx=0, pady=0)
navegacao1.grid(pady=0)
pagina_inicial.grid(pady=20, padx=10)

# navegacao
reg.grid(row=0, column=0)
seac.grid(row=0, column=1)
aprov.grid(row=0, column=2)
lisy.grid(row=0, column=3)

if __name__=="__main__":
    root.mainloop()