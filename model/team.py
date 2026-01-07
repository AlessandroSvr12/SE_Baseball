from dataclasses import dataclass

@dataclass
class Team:
    id:object
    anno:object
    team_code:object
    nome:object
    def __hash__(self):
        return hash(self.id)