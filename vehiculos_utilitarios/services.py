from .models import Vehiculo, Chofer, registro_contabilidad


def crear_vehiculo(patente, marca, modelo, year):
    Vehiculo.objects.create(patente=patente, marca=marca, modelo=modelo, year=year)

    
def crear_chofer(rut, nombre, apellido): 
    Chofer.objects.create(rut=rut, nombre=nombre, apellido=apellido)       
    
    
def crear_registro_contable(fecha_compra, valor, Vehiculo_id):
    registro_contabilidad.objects.create(fecha_compra=fecha_compra, valor=valor, Vehiculo_id=Vehiculo_id)
    
    
    
def deshabilitar_chofer(rut):
    Chofer.objects.filter(rut=rut).update(activo=False)
    
    
    
def deshabilitar_vehiculo(patente):
    Vehiculo.objects.filter(patente=patente).update(activo=False)
    
    
def habilitar_chofer(rut):  
    Chofer.objects.filter(rut=rut).update(activo=True)
    
def habilitar_vehiculo(patente):
    Vehiculo.objects.filter(patente=patente).update(activo=True)
    
    
def obtener_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    print(f'Patente:{vehiculo.patente} Marca:{vehiculo.marca} Modelo:{vehiculo.modelo} año:{vehiculo.year}')

def obtener_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    print(f'Rut:{chofer.rut} Nombre:{chofer.nombre} Apellido:{chofer.apellido}')
    
    
def asignar_chofer_a_vehiculo(chofer, vehiculo):
    Chofer.objects.filter(rut=chofer).update(vehiculo_id=vehiculo)
    
    
def imprimir_datos_vehiculos():
    vehiculo = Vehiculo.objects.all()
    for vehiculo in vehiculo:
        print(f'Patente:{vehiculo.patente} Marca:{vehiculo.marca} modelos:{vehiculo.modelo} año:{vehiculo.year}')