dni= "55555555F"
dni2= "53768462M"
palabra='TRWAGMYFPDXBNJZSQVHLCKE'
#print('La letra del DNI es: ', palabra[DNI%23])


def valid_dni(dni):
    dni_number = dni[:-1]
    dni_letter = dni[-1]
    palabra='TRWAGMYFPDXBNJZSQVHLCKE'
    is_valid = True
    if dni_number.__len__() >8 or dni_number.__len__() <7:
        is_valid = False
    if dni_letter != palabra[int(dni_number)%23]:
        is_valid = False
    return is_valid

print(valid_dni(dni))
print(valid_dni(dni2))