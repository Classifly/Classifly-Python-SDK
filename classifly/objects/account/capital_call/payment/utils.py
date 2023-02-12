from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.capital_call.payment.singular import CapitalCallPayment

def convert_to_capital_call_payment(func):
    return convert_to_classifly_object(classifly_object_type=CapitalCallPayment)(func)
