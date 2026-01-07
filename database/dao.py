from database.DB_connect import DBConnect
from model.salario import Salario
from model.team import Team
from model.giocatore import Giocatore



class DAO:
    @staticmethod
    def get_teams():
        conn = DBConnect.get_connection()
        teams = []
        cursor = conn.cursor()
        query = """ SELECT * FROM team """
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            team = Team(row[0], row[1], row[2],row[-2])
            teams.append(team)

        cursor.close()
        conn.close()
        return teams

    @staticmethod
    def get_giocatori():
        conn = DBConnect.get_connection()
        giocatori = []
        cursor = conn.cursor()
        query = """ SELECT * FROM player """
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            giocatore = Giocatore(row[0])
            giocatori.append(giocatore)

        cursor.close()
        conn.close()
        return giocatori

    @staticmethod
    def get_salari():
        conn = DBConnect.get_connection()
        salari = []
        cursor = conn.cursor()
        query = """ SELECT * FROM salary """
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            salario = Salario(row[0], row[1], row[2],row[3],row[4],row[5])
            salari.append(salario)

        cursor.close()
        conn.close()
        return salari