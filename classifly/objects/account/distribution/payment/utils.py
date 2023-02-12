from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.distribution.payment.singular import DistributionPayment

def convert_to_distribution_payment(func):
    return convert_to_classifly_object(classifly_object_type=DistributionPayment)(func)
