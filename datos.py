import datetime

prestamos = [
    {
        'cliente': '00103228',
        'id': 1,
        'fecha': datetime.date(2021, 1, 10),
        'monto': 37500.00,
        'estado': 'Pendiente'
    },
    {
        'cliente': '00103228',
        'id': 2,
        'fecha': datetime.date(2021, 1, 19),
        'monto': 725.18,
        'estado': 'Pendiente'
    },
    {
        'cliente': '00103228',
        'id': 3,
        'fecha': datetime.date(2021, 1, 31),
        'monto': 1578.22,
        'estado': 'Pendiente'
    },
    {
        'cliente': '00103228',
        'id': 4,
        'fecha': datetime.date(2021, 2, 4),
        'monto': 380,
        'estado': 'Pendiente'
    },
    {
        'cliente': '70099925',
        'id': 1,
        'fecha': datetime.date(2021, 1, 7),
        'monto': 2175.25,
        'estado': 'Pagado'
    },
    {
        'cliente': '70099925',
        'id': 2,
        'fecha': datetime.date(2021, 1, 13),
        'monto': 499.99,
        'estado': 'Pagado'
    },
]

tasas = [
    {
        'plazo_min': 1,
        'plazo_max': 1,
        'tasa_int': .07
    },
    {
        'plazo_min': 2,
        'plazo_max': 7,
        'tasa_int': .065
    },
    {
        'plazo_min': 8,
        'plazo_max': 15,
        'tasa_int': .06
    },
    {
        'plazo_min': 16,
        'plazo_max': 30,
        'tasa_int': .0550
    },
    {
        'plazo_min': 31,
        'plazo_max': 360,
        'tasa_int': .050
    },
]

print(prestamos[cliente[0]])