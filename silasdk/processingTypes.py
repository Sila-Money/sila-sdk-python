from enum import Enum


class ProcessingTypes(str, Enum):
    STANDARD_ACH = 'STANDARD_ACH',
    SAME_DAY_ACH = 'SAME_DAY_ACH',
    CARD = "CARD",
    INSTANT_SETTLEMENT = "INSTANT_SETTLEMENT",
