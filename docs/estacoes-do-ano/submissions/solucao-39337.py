hemisferio_norte = 0
hemisferio_sul = 1

def esatcaoAno(hemisferio ,dia, mes):

    if hemisferio == hemisferio_sul:
        # Caso mes seja entre Dezembro e Mar�o
        if mes == 12 or mes <= 3:
            # Casos especiais
            if mes == 3 and dia <= 20:
                return "VERAO"
            if mes == 3 and dia >= 21:
                return "OUTONO"
            if mes == 12 and dia >= 21:
                return "VERAO"
            if mes == 12 and dia < 21:
                return "PRIMAVERA"

            # Caso principal
            return "VERAO"


        # Caso mes seja entre mar�o e junho
        if mes >= 3 and mes <= 6:
            # casos especiais
            if mes == 6 and dia > 20:
                return "INVERNO"
            # Caso geral
            return "OUTONO"

        # Caso mes seja entre mar�o e junho (INVERNO)
        if mes >= 6 and mes <= 9:
            # Casos Especiais
            if mes == 9 and dia > 20:
                return "PRIMAVERA"
            # Caso Geral
            return "INVERNO"


        else:
            "PRIMAVERA"

    if hemisferio == hemisferio_norte:

        # Caso mes seja entre Junho e Setembro (VERAO)
        if mes >= 6 and mes <= 9:
            # Casos especiais
            if mes == 6 and dia < 21:
                return "PRIMAVERA"
            if mes == 9 and dia > 20:
                return "OUTONO"
            # Caso Gearl
            return "VERAO"


        # Caso mes seja entre Setembro e Dezembro (OUTONO)
        if mes >= 9 and mes <= 12:
            # Casos especiais
            if mes == 12 and dia > 20:
                return "INVERNO"
            # Caso Geral
            return "OUTONO"

        # Caso mes seja entre Dezembro e Mar�o (INVERNO)
        if mes == 12 or mes <= 3:
            # Casos especiais
            if mes == 3 and dia > 20:
                return "PRIMAVERA"
            # Caso geral
            return "INVERNO"
        
        else:
            return "PRIMAVERA"




hemisferio = int(input())
diaTeste = int(input())
mesTeste = int(input())


print(esatcaoAno(hemisferio, diaTeste, mesTeste))