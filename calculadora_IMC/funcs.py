import tkinter as tk

# CORREÇÃO 1: removido "from new_front import ..." — esse import criava um ciclo
# (new_front importava funcs e funcs importava new_front), o que quebrava o programa.
# Agora os widgets são recebidos como parâmetro em vez de importados.

def calculate_imc(entry_weith, entry_height):
    weith = entry_weith.get()
    height = entry_height.get()
    try:
        w = float(weith)
        h = float(height)
    except ValueError:
        return False
    else:
        if w <= 0 or h <= 0:
            return False
        else:
            # CORREÇÃO 2: faltava text= (config sem a palavra-chave não funciona)
            imc = w/(h**2)
            return imc

def classify_imc(imc):
    # CORREÇÃO 4: faltava text= em todos os config abaixo
    if imc < 18.5: return "Magreza / Baixo peso"
    elif imc <= 24.9: return "Peso normal (ideal)"
    elif imc <= 29.9: return "Sobrepeso (Grau I)"
    elif imc <= 34.9: return "Obesidade Grau I"
    elif imc <= 39.9: return "Obesidade Grau II (Severa)"
    else: return "Obesidade Grau III (Mórbida / Grave)"

def result_imc(entry_weith, entry_height, lbl_exit_imc, lbl_exit_class):
    lbl_exit_imc.config(text="")
    lbl_exit_class.config(text="")
    # CORREÇÃO 5: chamada correta das funções, passando os widgets recebidos
    
    imc = calculate_imc(entry_weith, entry_height)
    if imc:
        clasification = classify_imc(imc)
        lbl_exit_imc.config(text=f"{imc:.2f}")
        lbl_exit_class.config(text=f"{clasification}")
    else:
        lbl_exit_imc.config(text="Erro, Dado invalido")