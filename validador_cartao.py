import re

def luhn_check(card_number):
    """Implementação do Algoritmo de Luhn para validar o número do cartão."""
    digits = [int(d) for d in card_number]
    checksum = 0
    reverse_digits = digits[::-1]
    
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        checksum += digit
    
    return checksum % 10 == 0

class CreditCardValidator:
    def __init__(self):
        self.card_patterns = {
            'Visa': r'^4[0-9]{12}(?:[0-9]{3})?$',
            'MasterCard': r'^(5[1-5][0-9]{14}|2[2-7][0-9]{14})$',
            'American Express': r'^3[47][0-9]{13}$',
            'Diners Club': r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$',
            'Discover': r'^6(?:011|5[0-9]{2})[0-9]{12}$',
            'JCB': r'^(?:2131|1800|35\d{3})\d{11}$',
            'UnionPay': r'^62[0-9]{14,17}$',
            'Maestro': r'^(?:5[0678]\d\d|6304|6390|67\d\d)\d{8,15}$',
            'Elo': r'^(4011(78|79)\d{10}|(50(4175|4183|4192)|636368|636297|504175)\d{10})$',
            'Hipercard': r'^(606282\d{10}(\d{3})?|3841\d{15})$'
        }

    def validate(self, card_number):
        card_number = re.sub(r'\D', '', card_number)  # Remove espaços e traços
        
        detected_brand = None
        for card_type, pattern in self.card_patterns.items():
            if re.match(pattern, card_number):
                detected_brand = card_type
                break
        
        if detected_brand:
            if luhn_check(card_number):
                return f"Cartão válido da bandeira {detected_brand}."
            else:
                return f"Número inválido, mas parece um cartão {detected_brand}."
        return "Número de cartão inválido ou bandeira desconhecida."

if __name__ == "__main__":
    validator = CreditCardValidator()
    card_number = input("Digite o número do cartão de crédito: ")
    result = validator.validate(card_number)
    print(result)
