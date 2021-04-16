from abc import abstractmethod, ABCMeta
from app.repositories.user_repository import *
from app.dto.user_dto import *
from typing import List

class UserManagementService(metaclass=ABCMeta):
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

    def authenticate(self, model: AuthenticateDto):
        """Authenticate User Object"""
        raise NotImplementedError


class DefaultUserManagementService(UserManagementService):
    repository: UserRepository

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, model: CreateUserDto):
        user = self.repository.user_details(email=model.email)
        if user is not UserDetailsDto:
            self.repository.create_user(model)
            return True
        else:
            return False

    def list_users(self) -> List[ListUserDto]:
        return self.repository.list_users()

    def edit_user(self, model: EditUserDto, user_id=None, email=None):
        return self.repository.edit_user(model, user_id, email)

    def user_details(self, user_id=None, email=None) -> UserDetailsDto:
        user = self.repository.user_details(user_id, email)
        if isinstance(user, (UserDetailsDto,)):
            user.__delattr__('password')
            return user

    def change_password(self, model: ChangePasswordDto, user_id=None, email=None):
        return self.repository.change_password(model, user_id, email)

    def authenticate(self, model: AuthenticateDto):
        user = self.repository.user_details(email=model.email)
        if isinstance(user, (UserDetailsDto,)):
            if user.password == model.password:
                user.__delattr__('password')
                return user







