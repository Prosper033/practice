from abc import abstractmethod, ABCMeta
from typing import List
from app.dto.user_dto import *
from app.models import User


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_user(self, model: CreateUserDto):
        """create User Object"""
        raise NotImplementedError

    @abstractmethod
    def list_users(self) -> List[ListUserDto]:
        """List User Objects"""
        raise NotImplementedError

    @abstractmethod
    def edit_user(self, model: EditUserDto, user_id=None, email=None):
        """Edit User Object"""
        raise NotImplementedError

    @abstractmethod
    def user_details(self, user_id=None, email=None) -> UserDetailsDto:
        """User Details Object"""
        raise NotImplementedError

    @abstractmethod
    def change_password(self, model: ChangePasswordDto, user_id=None, email=None):
        """Change Object Password"""
        raise NotImplementedError


class DjangoORMUserRepository(UserRepository):
    def create_user(self, model: CreateUserDto):
        user = User()
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.email = model.email
        user.password = model.password
        user.phone_number = model.phone_number
        user.save()

    def list_users(self) -> List[ListUserDto]:
        users = User.objects.all()
        result: List[ListUserDto] = []

        for user in users:
            item = ListUserDto()
            item.name = user.first_name + " " + user.last_name
            item.email = user.email
            item.phone_number = user.phone_number
            result.append(item)
        return result

    def edit_user(self, model: EditUserDto, user_id=None, email=None):
        if user_id is not None:
            user = User.objects.get(id=user_id)
        elif email is not None:
            user = User.objects.get(id=email)
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.email = model.email
        user.phone_number = model.phone_number
        user.save()

    def user_details(self, user_id=None, email=None) -> UserDetailsDto:
        if user_id is not None:
            user = User.objects.get(id=user_id)
        elif email is not None:
            user = User.objects.get(id=email)
        item = UserDetailsDto()
        item.id = user.id
        item.first_name = user.first_name
        item.last_name = user.last_name
        item.email = user.email
        item.phone_number = user.phone_number
        item.last_login = user.last_login
        item.active = user.active
        return item

    def change_password(self, model: ChangePasswordDto, user_id=None, email=None):
        if user_id is not None:
            user = User.objects.get(id=user_id)
        elif email is not None:
            user = User.objects.get(id=email)
        user.password = model.new_password
        user.save()

