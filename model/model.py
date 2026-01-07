import networkx as nx

from database import dao

class Model:
    def __init__(self):
        self.G=None
        self.salari=dao.DAO.get_salari()
        self.teams_grezzi=dao.DAO.get_teams()


    def crea_grafo(self,anno):

        self.teams_grezzi=dao.DAO.get_teams()
        teams=[]
        for t in self.teams_grezzi:
            if float(t.anno)==float(anno):
                teams.append(t)
        self.G=nx.Graph()
        for team in teams:
            self.G.add_node(team)
        for i in range(len(teams)):
            for j in range(i+1,len(teams)):
                team=teams[i]
                team1=teams[j]
                salario=self.calcola_salario(team.id)
                salario1=self.calcola_salario(team1.id)
                self.G.add_edge(team,team1,weight=salario+salario1)
        #creo mappa team_code -> nodo
        self.nodi_per_codice = {n.team_code: n for n in self.G.nodes}


    def calcola_salario(self,id_squadra):
        salario_trovato=0
        for salario in self.salari:
            if salario.team_id==id_squadra:
                salario_trovato+=salario.salario
        return salario_trovato

    def trova_anni(self):
        anni=[]
        for team in self.teams_grezzi:
            if float(team.anno)>=1980:
                if float(team.anno) not in anni:
                    anni.append(team.anno)
        return anni

    def squadre_anno(self,anno):
        risultati = []
        for team in self.teams_grezzi:
            if float(team.anno)==float(anno):
                    tupla=(team.team_code,team.nome)
                    risultati.append(tupla)
        return risultati

    def analisi_dettagli(self,team_code):
        squadra = self.nodi_per_codice[team_code]
        archi=self.G.edges(squadra,data='weight')

        risultati=[]
        for u,v,peso in archi:
            risultati.append((v,peso))
        risultati_ordinati=sorted(risultati,key=lambda tup: tup[1],reverse=True)

        #devo sistempare come viene mostrata la roba
        return risultati_ordinati



    def crea_percorso(self,team_code):
        nodo_corrente = self.nodi_per_codice[team_code]
        peso_ultimo_arco=None
        peso_percorso={"peso":0}
        peso_best={"peso":0}

        K=100
        percorso_best=[]
        percorso_corrente=[]
        visitati=set()


        self.ricorsione(K,nodo_corrente,peso_ultimo_arco,peso_percorso,peso_best,percorso_best,percorso_corrente,visitati)
        return percorso_best

    def ricorsione(self, K, nodo_corrente, peso_ultimo_arco, peso_percorso, peso_best, percorso_best, percorso_corrente,visitati):


        visitati.add(nodo_corrente)
        if peso_percorso["peso"]>peso_best["peso"]:
            peso_best["peso"]=peso_percorso["peso"]
            percorso_best.clear()
            percorso_best.extend(percorso_corrente)

        #percorso_corrente.appen(nodo_corrente)

        edges = sorted(self.G.edges(nodo_corrente, data=True),key=lambda x: x[2].get("weight", 1),reverse=True)[:K]

        #edges restituisce lista di tuple tipo ('A', 'B', {'weight': x})

        for archi in edges:
            peso_arco=archi[2]["weight"]
            prossimo=archi[1]
            if peso_ultimo_arco is None or peso_arco<peso_ultimo_arco:
                if prossimo not in visitati:


                    percorso_corrente.append((archi[0], prossimo, peso_arco))
                    peso_percorso["peso"] += peso_arco

                    #print("Da:", nodo_corrente, "a:", prossimo, "peso:", peso_arco, "ultimo:", peso_ultimo_arco,"visitati:", visitati)
                    self.ricorsione(K, prossimo, peso_arco, peso_percorso, peso_best, percorso_best,percorso_corrente,visitati)
                    percorso_corrente.remove((archi[0], prossimo, peso_arco))
                    peso_percorso["peso"] -= peso_arco

        visitati.remove(nodo_corrente)






