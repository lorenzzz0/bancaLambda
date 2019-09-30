from model.modelcuenta import ModelCuenta

class Cuenta:
    
    def validarExisteUsuario(self, idUsuario):
        model = ModelCuenta() 
        result = model.validarExisteUsuario(idUsuario)
        if (result == 'true'):
            return 'existe'
        else:
            return 'no existe'
    def obtenerCuentasUsuario( self, idUsuario ):
        model = ModelCuenta() 
        result = model.obtenerCuentasUsuario(idUsuario)
        return result
    
    def ingresaCantidad( self, data ):
        model = ModelCuenta()
        
        idUser      = data['usr'] 
        idCuenta    = data['idCuenta']
        candidad    = data['cantidad']
        
        result = model.ingresaCantidad( idUser, idCuenta, candidad )
        return result;
        
    def retiraCantidad( self, data ):
        model = ModelCuenta()
        
        idUser      = data['usr'] 
        idCuenta    = data['idCuenta']
        candidad    = data['cantidad']
        
        result = model.retiraCantidad( idUser, idCuenta, candidad )
        return result;
    
    def actualizaSaldos( self, data ):
        idUser      = data['usr'] 
        idCuenta    = data['idCuenta']
        cantidad    = data['cantidad']
        model = ModelCuenta()
        respuesta = model.actualizaSaldos( idUser, idCuenta, cantidad )
        return respuesta
    
    def actualizaSaldosRetiro( self, data ):
        idUser      = data['usr'] 
        idCuenta    = data['idCuenta']
        cantidad    = data['cantidad']
        model = ModelCuenta()
        respuesta = model.actualizaSaldosRetiro( idUser, idCuenta, cantidad )
        return respuesta
    
    def obtenerMovimientos( self, data ):
        idUser      = data['usr'] 
        idCuenta    = data['idCuenta']
        
        model = ModelCuenta()
        movimientos = model.obtenerMovimientos( idUser, idCuenta )
        return movimientos