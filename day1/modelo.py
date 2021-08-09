import psycopg2
import urllib.parse as up



class data_acess:
    def __init__(self, endereco):
        up.uses_netloc.append("postgres")
        self.url = up.urlparse(endereco)
        self.con = psycopg2.connect(database=self.url.path[1:],
                                    user=self.url.username,
                                    password=self.url.password,
                                    host=self.url.hostname,
                                    port=self.url.port
                                    )
    def registar_aluno(self,nome,apelido,sexo,datanas,nascion,curso,pais,daingresso,bi,nui,img,nota1,nota2,extimg):
        con = self.con
        self.img=img
        cur = con.cursor()
        cur.execute('select * from student')
        rows=cur.fetchall()
        idw = 1
        for r in rows:
            idw+=r[0]
        cur.execute(f"Insert into student values({idw},'{nome}','{apelido}','{sexo}','{datanas}','{nascion}','{curso}','{pais}','{daingresso}','{bi}','{nui}',{psycopg2.Binary(self.img)},{nota1},{nota2},'{extimg}')")
        con.commit()
        cur.close()
        con.close()
        print("sucess0")
        pass
    def recuperar_img(self,nrest):
        con = self.con
        cur = con.cursor()
        cur.execute('select * from student')
        rows = cur.fetchall()
        info = []
        for r in rows:
            if nrest == r[0]:
                img=r[11]
                ext=r[14]
                nome=r[2]
                info=[img,ext,nome]
        cur.close()
        con.close()
        return info
    def pesquisar(self,nrestudante):
            con = self.con
            cur = con.cursor()
            cur.execute('select * from student')
            rows = cur.fetchall()
            info=[]
            for r in rows:
                if nrestudante==r[0]:
                   info=[r[10],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[12],r[13]]
            cur.close()
            con.close()
            return info
    def aproveita(self):
        con = self.con
        cur = con.cursor()
        cur.execute('select * from student')
        rows = cur.fetchall()
        info = []
        posi=0
        neg=0
        media=0
        for r in rows:
            media=(r[12]+r[13])/2
            if media>=10:
                posi+=1
            else:
                neg+=1
        info=[posi,neg]
        cur.close()
        con.close()
        return info
    def lista_alunos(self):
        con = self.con
        cur = con.cursor()
        cur.execute('select * from student')
        rows = cur.fetchall()
        a=0
        for r in rows:
            a+=1
        print(a)
        info = list(range(a))
        posi = 0
        for r in rows:
            info[posi]=(r[1],r[2],r[3],r[4],r[5],r[6],r[9],r[10])
            posi+=1
        cur.close()
        con.close()
        return info
    def lista_alunosid(self):
        con = self.con
        cur = con.cursor()
        cur.execute('select * from student')
        rows = cur.fetchall()
        a = 0
        for r in rows:
            a += 1
        info = list(range(a))
        posi = 0
        for r in rows:
            info[posi]=r[0]
            posi += 1
        cur.close()
        con.close()
        return info

