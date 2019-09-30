import json
from controller.cuenta import Cuenta

def lambda_handler(event, context):
    # TODO implement
    cuenta = Cuenta()
    if( event['opid'] == '001' ):
        respuesta = cuenta.validarExisteUsuario(event['usr'])
        cuentas = cuenta.obtenerCuentasUsuario( event['usr'] )
    
        return {
            'statusCode': 200,
            'usuario': respuesta,
            'cuentas':cuentas
            
        }
    elif( event['opid'] == '002' ):
        respuesta = cuenta.ingresaCantidad( event )
        if( respuesta ):
            cuentas = cuenta.actualizaSaldos( event )
        return {
            'statusCode': 200,
            'cuentas':cuentas
        }
    elif( event['opid'] == '003' ):
        respuesta = cuenta.obtenerMovimientos( event )
        return {
            'statusCode': 200,
            'cuentas':respuesta
        }
    elif( event['opid'] == '004' ):
        respuesta = cuenta.retiraCantidad( event )
        if( respuesta ):
            cuentas = cuenta.actualizaSaldosRetiro( event )
        return {
            'statusCode': 200,
            'cuentas':respuesta
        }
