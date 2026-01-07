import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""

        anno=self._view.dd_anno.value
        self._model.crea_grafo(anno)

        for nodo in self._model.G.nodes():
            #ricordati che python fa giochi strani mettendo nodo come value
                self._view.dd_squadra.options.append( ft.dropdown.Option( key=nodo.team_code, text=f"{nodo.team_code} ({nodo.nome})" ) )
        self._view.page.update()

    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""

        risultati=self._model.analisi_dettagli(self._view.dd_squadra.value)
        self._view.txt_risultato.clean()
        for i in risultati:
            self._view.txt_risultato.controls.append(ft.Text(i))
        self._view.page.update()


    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""


        percorso_best=self._model.crea_percorso(self._view.dd_squadra.value)
        print(len(percorso_best))
        for i in percorso_best:
            print(i)

    """ Altri possibili metodi per gestire di dd_anno """""
    def handle_anno(self):
        anni=self._model.trova_anni()
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(str(anno)))
        self._view.page.update()

    def handle_change_anno(self,e):
        anno=self._view.dd_anno.value
        risultati=self._model.squadre_anno(anno)
        self._view.txt_out_squadre.clean()
        self._view.txt_out_squadre.controls.append(ft.Text(f"numero squadre {len(risultati)}"))
        for sigla,squadra in risultati:
            self._view.txt_out_squadre.controls.append(ft.Text(f"{sigla}({squadra})"))
        self._view.page.update()



