from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.portfolio_company.singular import PortfolioCompany

def convert_to_portfolio_company(func):
    return convert_to_classifly_object(classifly_object_type=PortfolioCompany)(func)
