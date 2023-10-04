from lesson29.session_handler import session
from lesson29.models.users import Users
from sqlalchemy.sql.expression import Insert
from sqlalchemy import insert

from sqlalchemy import select


class UsersRepository:
    def __init__(self):
        self.__session = session

    def get_user_by_name(self, first_name):
        return self.__session.query(Users).filter_by(first_name=first_name)

    def get_user_by_id_2(self, user_id):
        return self.__session.get(Users, {'id': user_id})

    def add_one_row(self,user):
        self.__session.add(user)
        self.__session.commit()


    #select(User).where(User.id == 5)

    def get_all(self):
        bunch_of_users = []
        for user in self.__session.query(Users).all():
            bunch_of_users.append(user)
        return bunch_of_users


users_repository = UsersRepository()
#first_user = users_repository.get_user_by_id('BBBBBBBB')
#print(first_user)
user_to_add = Users(id='dddddddd', first_name='DDDD', last_name='DDDD', age=15, email='dddd@ddd.ddd')
users_repository.add_one_row(user_to_add)
all_users_2 = users_repository.get_all()
print(all_users_2)
