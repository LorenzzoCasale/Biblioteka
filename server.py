from repository import get_user, create_user, update_user, delete_user

class User:
    def __init__(self, cpf, name, tel):
        self.cpf = cpf
        self.name = name
        self.tel = tel

    @classmethod
    def get(cls, cpf):
        user = get_user(cpf)
        if user:
            return cls(*user)
        return None

    @classmethod
    def create(cls, cpf, name, tel):
        create_user(cpf, name, tel)
        return cls(cpf, name, tel)

    def update(self, name=None, tel=None):
        update_user(self.cpf, name, tel)
        if name is not None:
            self.name = name
        if tel is not None:
            self.tel = tel

    def delete(self):
        delete_user(self.cpf)