from dataclasses import dataclass

@dataclass
class Salario:
    id:object
    anno:object
    team_code:object
    team_id:object
    giocatore_id:object
    salario:object
    def __hash__(self):
        return hash(self.id)