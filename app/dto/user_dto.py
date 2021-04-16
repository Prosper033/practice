import datetime
class CreateUserDto:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    password: str
    confirm_password: str


class ListUserDto:
    name: str
    email: str
    phone_number: str


class EditUserDto:
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str


class UserDetailsDto:
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    active: bool
    last_login: datetime
    password: str


class AuthenticateDto:
    email: str
    password: str


class ChangePasswordDto:
    id: int
    email: str
    old_password: str
    new_password: str
