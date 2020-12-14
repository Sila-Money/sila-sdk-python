from enum import Enum


class RegistrationFields(str, Enum):
    EMAIL = 'email',
    PHONE = 'phone',
    IDENTITY = 'identity',
    ADDRESS = 'address',
    ENTITY = 'entity',
    DEVICE = 'device'
