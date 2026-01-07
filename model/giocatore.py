from dataclasses import dataclass

@dataclass
class Giocatore:
    id:object
    def __hash__(self):
        return hash(self.id)