from dependency_injector import containers, providers
from typing import Callable
from app.repositories.user_repository import UserRepository, DjangoORMUserRepository
from app.services.user_management_service import UserManagementService, DefaultUserManagementService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    user_repository: Callable[[], UserRepository] = providers.Factory(
        DjangoORMUserRepository
    )

    user_management_service: Callable[[], UserManagementService] = providers.Factory(
        DefaultUserManagementService,
        repository=user_repository
    )


app_service_provider = Container()
