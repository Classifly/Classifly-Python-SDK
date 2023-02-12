"""
    Co-Investment - Object Representation
"""
from google.cloud.firestore import DocumentReference, FirestoreProperty

from classifly.objects.account.utils import ClassiflyAccountDocumentReference
from classifly.objects.account.coinvestment.constants import CoInvestmentFieldNames
from classifly.objects.account.coinvestor.singular import CoInvestor
from classifly.objects.account.portfolio_company.singular import PortfolioCompany

class CoInvestment(ClassiflyAccountDocumentReference):
    """
        A Co-Investment. Used to connect Co-Investors to Portfolio Companies
    """
    co_investor: CoInvestor = FirestoreProperty(CoInvestmentFieldNames.CO_INVESTOR,CoInvestor) #: The Co-Investor investing in the Portfolio Company
    portfolio_company: PortfolioCompany = FirestoreProperty(CoInvestmentFieldNames.PORTFOLIO_COMPANY,PortfolioCompany) #: The Portfolio Company the Co-Investor invested in

    def __init__(self, *args, coinvestment_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Co-Investment",document_id=coinvestment_id)