from enum import Enum
from typing import List


class MandatoryColumns(Enum):
    Date = "Date"
    From = "From"
    To = "To"
    Rate = "Rate"

    @staticmethod
    def get_names() -> List[str]:
        return [e.value for e in MandatoryColumns]

