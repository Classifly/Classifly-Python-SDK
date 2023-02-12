from classifly.objects.utils.document_reference.decorators import convert_to_classifly_object
from classifly.objects.account.report.data.singular import ReportData

def convert_to_report_data(func):
    return convert_to_classifly_object(classifly_object_type=ReportData)(func)