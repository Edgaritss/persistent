import datetime
from datos import prestamos, tasas


def list_loan(client: str, prestamos: list, **kwargs) -> list:
    loans = [i for i in prestamos if i['cliente']
             == client and i['estado'] == 'Pendiente']
    loan = {}
    res = []
    for i in loans:
        loan['cliente'] = i['cliente']
        loan['plazo'] = (kwargs['fecha_actual'] - i['fecha']).days
        for t in tasas:
            if loan['plazo'] >= t['plazo_min'] and loan['plazo'] <= t['plazo_max']:
                loan['tasa_interes'] = t['tasa_int']

        loan['monto'] = i['monto']
        loan['interes'] = round(i['monto'] * loan['plazo'] *
                                loan['tasa_interes'] / kwargs['dias_anio_comercial'], 2)

        loan['iva'] = round(loan['interes'] * kwargs['tasa_iva'], 2)

        loan['pago'] = loan['monto'] + loan['interes'] + loan['iva']

        res.append(loan)
        loan = {}

    res = sorted(res, key=lambda x: x['plazo'], reverse=True)

    return res


if __name__ == '__main__':
    l = list_loan('00103228', prestamos, fecha_actual=datetime.date(
        2021, 2, 15), tasa_iva=16.00, dias_anio_comercial=360)
    print(l)