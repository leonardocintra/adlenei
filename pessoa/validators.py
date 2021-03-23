from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números.', 'length')

def validate_cnpj(value):
    if not value.isdigit():
        raise ValidationError('CNPJ deve conter apenas números.', 'digits')

    if len(value) != 14:
        raise ValidationError('CNPJ deve ter 14 números.', 'length')