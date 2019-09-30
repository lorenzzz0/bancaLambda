import boto3
import datetime
import uuid
from boto3 import resource
from boto3.dynamodb.conditions import Key


class ModelCuenta():
    dynamoDB = None
    clientDynamoDB = None
    
    def __init__(self):
        self.dynamoDB = boto3.resource('dynamodb')
        self.clientDynamoDB = boto3.client('dynamodb')

    def validarExisteUsuario(self, idUsuario):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('users')
        response = table.query(
            KeyConditionExpression= Key('id_user').eq(idUsuario)
        )
        if (response['Count'] > 0 ):
            return 'true'
        else:
            return 'false';
    
    def obtenerCuentasUsuario(self, idUsuario):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('accounts')
        cuentas = self.clientDynamoDB.scan(
            TableName="accounts",
            FilterExpression='user_id = :s',
            ExpressionAttributeValues={
                 ":s": {"S": idUsuario }
            }
        )
        return cuentas
        
    def ingresaCantidad(self, idUser, idCuenta, candidad ):
        tablaTransactions = self.dynamoDB.Table('transactions')
        v = {"account_id": idCuenta,"amount": candidad,"date":  datetime.datetime.now().isoformat(),"transactions_id": str(uuid.uuid4()), "user_id":idUser, "type":'Deposito'}
        result = tablaTransactions.put_item( Item = v )
        return result
    
    def retiraCantidad(self, idUser, idCuenta, candidad ):
        tablaTransactions = self.dynamoDB.Table('transactions')
        v = {"account_id": idCuenta,"amount": candidad,"date":  datetime.datetime.now().isoformat(),"transactions_id": str(uuid.uuid4()), "user_id":idUser, "type":'Retiro'}
        result = tablaTransactions.put_item( Item = v )
        return result    
        
        
    def actualizaSaldos(self, idUser, idCuenta, cantidad ):
        dynamodb = boto3.resource('dynamodb')
        cuentas = self.clientDynamoDB.scan(
            TableName="accounts",
            FilterExpression='account_id = :e and user_id = :s',
            ExpressionAttributeValues={
                 ":e": {"S": idCuenta },
                 ":s": {"S": idUser }
            }
        )
        balance_actual = cuentas['Items'][0]['balance']['N']
        credito_actual = cuentas['Items'][0]['credit_used']['N']
        
        balance = int(balance_actual) + int(cantidad)
        credito = int(credito_actual) - int(cantidad)
        
        accounts = self.dynamoDB.Table("accounts")
        accounts.update_item(
            Key={
                'account_id': idCuenta
            },
            UpdateExpression="set balance = :b, credit_used = :c",
            ExpressionAttributeValues={
                    ':b': balance,
                    ':c': credito
            },
            ReturnValues="UPDATED_NEW"
        )
        return cuentas
    
    def actualizaSaldosRetiro(self, idUser, idCuenta, cantidad ):
        dynamodb = boto3.resource('dynamodb')
        cuentas = self.clientDynamoDB.scan(
            TableName="accounts",
            FilterExpression='account_id = :e and user_id = :s',
            ExpressionAttributeValues={
                 ":e": {"S": idCuenta },
                 ":s": {"S": idUser }
            }
        )
        balance_actual = cuentas['Items'][0]['balance']['N']
        credito_actual = cuentas['Items'][0]['credit_used']['N']
        
        balance = int(balance_actual) - int(cantidad)
        credito = int(credito_actual) + int(cantidad)
        
        accounts = self.dynamoDB.Table("accounts")
        accounts.update_item(
            Key={
                'account_id': idCuenta
            },
            UpdateExpression="set balance = :b, credit_used = :c",
            ExpressionAttributeValues={
                    ':b': balance,
                    ':c': credito
            },
            ReturnValues="UPDATED_NEW"
        )
        return cuentas
    
    def obtenerMovimientos(self, idUser, idCuenta ):
        dynamodb = boto3.resource('dynamodb')
        movimientos = self.clientDynamoDB.scan(
            TableName="transactions",
            FilterExpression='account_id = :e and user_id = :s',
            ExpressionAttributeValues={
                 ":e": {"S": idCuenta },
                 ":s": {"S": idUser }
            },
            Limit= 20
        )
        return movimientos