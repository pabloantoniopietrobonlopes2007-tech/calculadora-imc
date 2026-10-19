import tkinter as tk
# CORREÇÃO 6: era "from .funcs import ..." (import relativo) — só funciona dentro
# de um pacote (com __init__.py). Como os arquivos rodam direto, usamos import normal.
from funcs import result_imc

calculadora = tk.Tk()
calculadora.title("Calculadora de IMC")
calculadora.geometry("500x600")

lbl_weith = tk.Label(calculadora, text="Peso(Kg)", width=10)
lbl_weith.pack(pady=10)

entry_weith = tk.Entry(calculadora, width=20)
entry_weith.pack(pady=20)

lbl_height = tk.Label(calculadora, text="Altura(m)", width=10)
lbl_height.pack(pady=10)

entry_height = tk.Entry(calculadora, width=20)
entry_height.pack(pady=20)

lbl_exit_imc = tk.Label(calculadora, text="", width=20)
lbl_exit_imc.pack(pady=20)

lbl_exit_class = tk.Label(calculadora, text="", width=20)
lbl_exit_class.pack(pady=20)

# CORREÇÃO 7: result_imc agora recebe os widgets como parâmetros,
# então usamos lambda para passá-los quando o botão for clicado
btn_send = tk.Button(
    calculadora,
    text="calculate",
    command=lambda: result_imc(entry_weith, entry_height, lbl_exit_imc, lbl_exit_class),
)
btn_send.pack(pady=20)

tk.mainloop()