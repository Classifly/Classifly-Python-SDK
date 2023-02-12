"""
    Portfolio Company - Object Representation
"""
from google.cloud.firestore import FirestoreProperty, DocumentReference

from classifly.objects.account.utils import ClassiflyUserEnabledPipelineAccountDocumentReference
from classifly.objects.account.portfolio_company.constants import PortfolioCompanyFieldNames

class PortfolioCompany(ClassiflyUserEnabledPipelineAccountDocumentReference):
    """
        A Portfolio Company or Company within Classifly
    """
    about: str = FirestoreProperty(PortfolioCompanyFieldNames.ABOUT,str) #: A description about the Portfolio Company

    def __init__(self, *args, portfolio_company_id: str=None) -> None:
        initalized = False
        if len(args) == 1:
            if isinstance(args[0],DocumentReference):
                super().__init__(*args)
                initalized = True
        if initalized is False:
            super().__init__(account_name="Portfolio_Companies",document_id=portfolio_company_id)


if __name__ == "__main__":
    for user in PortfolioCompany(portfolio_company_id="RZEXM48WEZC7vvfcnHD1").get_users():
        print(user.email)
