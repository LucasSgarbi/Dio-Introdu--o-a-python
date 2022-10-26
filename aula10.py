from datetime import date, time, datetime , timedelta


def trabalhando_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y - %H:%M:%S'))
    print(data_atual.strftime('%c'))
    tupla_dias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sesta', 'Sabado', 'Domingo')
    print(tupla_dias[data_atual.weekday()])

    data_string = '04/11/2001'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print('Data comvertida = {}'.format(data_convertida.strftime('%c')))
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)
def trabalhando_data():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%A %B %Y'))


def trabalhando_time():
    horario = time(hour=11, minute=22, second=59)
    print(horario.strftime('%H:%M:%S'))


if __name__ == '__main__':
    # trabalhando_data()
    # trabalhando_time()
    trabalhando_datetime()
