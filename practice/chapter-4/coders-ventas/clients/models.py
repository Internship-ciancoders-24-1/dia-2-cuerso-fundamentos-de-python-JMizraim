import uuid

class Client:
    def __init__(self, name, company, email, position, _uuid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uuid = _uuid or uuid.uuid4()
    
    def to_dict(self):
        # representa a la instancia a su equivalente en diccionario
        return vars(self)
    
    @staticmethod
    def schema():
        return ["name", "company", "email", "position", "uuid"]