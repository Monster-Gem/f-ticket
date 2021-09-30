from domain.maintenance.extended_enum import ExtendedEnum

class OrderStatus(ExtendedEnum):
    RESERVED = 'RESERVED'
    FINISHED = 'FINISHED'