#calculadora de isr
top1 = 416220.00
top2 = 624329.00
top3 = 867123.00
salario = float(input("ingrese su sueldo mensual:"))
salario_anual = salario * 12
isr = 0

if salario_anual <= top1:
    print("Excenta")
elif salario_anual <= top2:
    excedente = salario_anual - top1
    isr = excedente * 0.15
elif salario_anual <= top3:
    excedente = salario_anual - top2
    isr = 31216.00 + (excedente * 0.20)
else:
    excedente = salario_anual - top3
    isr = 79776.00 + excedente * 0.25

print(isr / 1250)
