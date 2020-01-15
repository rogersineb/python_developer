segundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dias = segundos // (3600*24)
horas = (segundos - ((3600*24) * dias)) // 3600 
minutos = (segundos - (3600*24*dias + horas*3600)) // 60
segundos = segundos % 60
print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")