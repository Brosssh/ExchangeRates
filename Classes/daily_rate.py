from typing import List
from typing import Any
from dataclasses import dataclass

@dataclass
class Rate:
    country: str
    currency: str
    isoCode: str
    uicCode: str
    avgRate: str
    exchangeConvention: str
    exchangeConventionCode: str
    referenceDate: str

    @staticmethod
    def from_dict(obj: Any) -> 'Rate':
        _country = str(obj.get("country"))
        _currency = str(obj.get("currency"))
        _isoCode = str(obj.get("isoCode"))
        _uicCode = str(obj.get("uicCode"))
        _avgRate = str(obj.get("avgRate"))
        _exchangeConvention = str(obj.get("exchangeConvention"))
        _exchangeConventionCode = str(obj.get("exchangeConventionCode"))
        _referenceDate = str(obj.get("referenceDate"))
        return Rate(_country, _currency, _isoCode, _uicCode, _avgRate, _exchangeConvention, _exchangeConventionCode, _referenceDate)

@dataclass
class ResultsInfo:
    totalRecords: int
    timezoneReference: str

    @staticmethod
    def from_dict(obj: Any) -> 'ResultsInfo':
        _totalRecords = int(obj.get("totalRecords"))
        _timezoneReference = str(obj.get("timezoneReference"))
        return ResultsInfo(_totalRecords, _timezoneReference)

@dataclass
class DailyRates:
    resultsInfo: ResultsInfo
    rates: List[Rate]

    @staticmethod
    def from_dict(obj: Any) -> 'DailyRates':
        _resultsInfo = ResultsInfo.from_dict(obj.get("resultsInfo"))
        _rates = [Rate.from_dict(y) for y in obj.get("rates")]
        return DailyRates(_resultsInfo, _rates)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
