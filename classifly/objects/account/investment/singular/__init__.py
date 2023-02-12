"""
    Investment - Object Representation
"""
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.account.investment.dataclass.investment_vehicles import InvestmentVehicles
from classifly.objects.account.utils import ClassiflyAccountDocumentReference
from classifly.objects.account.portfolio_company.singular import PortfolioCompany
from classifly.objects.account.fund.singular import Fund
from classifly.objects.account.investment.constants import InvestmentFieldNames

class Investment(ClassiflyAccountDocumentReference):
    """
        An Investment. Represents a Fund's investment in A Portfolio Company
    """
    portfolio_company: PortfolioCompany = FirestoreProperty(InvestmentFieldNames.PORTFOLIO_COMPANY, PortfolioCompany) #: The Portfolio Company recieving the Investment.
    amount: float = FirestoreProperty(InvestmentFieldNames.AMOUNT, float) #: The Investment's Dollar amount
    fund: Fund = FirestoreProperty(InvestmentFieldNames.FUND, Fund) #: The Fund the Investment is coming from
    date: DatetimeWithNanoseconds = FirestoreProperty(InvestmentFieldNames.DATE,DatetimeWithNanoseconds) #: When the Investment occurred
    vehicle: InvestmentVehicles = FirestoreProperty(InvestmentFieldNames.VEHICLE, InvestmentVehicles) #: The investment vehicle. Ex: Equity, Warrants, Debt.
    name: str = FirestoreProperty(InvestmentFieldNames.NAME,str) #: The Investment's Name

    def __init__(self, *args, investment_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Investments",document_id=investment_id)
