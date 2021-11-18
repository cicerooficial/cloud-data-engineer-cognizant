from datetime import date, time, datetime, timedelta

# data_atual = date.today() #Traz a data atual
# print(data_atual)
# print(data_atual.strftime('%d/%m/%y')) # y trás apenas 2 digitos do ano
# print(data_atual.strftime('%d/%m/%Y')) # Y Trás os 4 digitos do ano
# print(data_atual.strftime('%d-%m-%Y'))
# print(data_atual.strftime('%d %m %Y'))
#
# print(data_atual.strftime('%A %B %Y')) # A-traz o nome do dia, B-traz o nome do mês
# data_atual_str = data_atual.strftime('%A %B %Y')
# print(data_atual_str)
# print(type(data_atual))
# print(type(data_atual_str))

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%A %B %Y'))
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)
    print(type(data_atual))
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    print(type(horario))
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.hour)
    print(data_atual.minute)
    print(data_atual.date())
    print(data_atual.weekday())
    print(data_atual.month)
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15) #Retirar dias de uma data
    print(nova_data)


if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()