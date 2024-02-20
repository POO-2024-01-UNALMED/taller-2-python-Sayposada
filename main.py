#Creamos las clases 

#auto
#asiento
class Asiento:
  def __init__(self, color, precio, registro):
    self.color = color
    self.precio = precio
    self.registro = registro

  #método
  def cambiarColor(self, color):
    if(color == "rojo" or color== "verde" or color == "amarillo" or color == "negro" or color == "blanco"):
      self.color = color

#motor 

class Auto:
  cantidadCreados = 0
  def __init__ (self, modelo, precio, asientos, marca, motor, registro):
    self.modelo = modelo
    self.precio = precio
    self.asientos = asientos
    self.marca = marca
    self.motor = motor
    self.registro = registro
    
  def cantidadAsientos (self):
    numAsientos = 0
    for asiento in self.asientos:
      if (type(asiento) == Asiento):
        numAsientos += 1
    return numAsientos

  def verificarIntegridad(self):
    if (self.motor.registro == self.registro):
      for asiento in self.asientos:
        if (type(asiento) == Asiento):
          if self.registro!=asiento.registro:
            return "Las piezas no son originales"
        return "Auto original"
    else:
      return "Las piezas no son originales"

class Motor:
  def __init__(self, numeroCilindros, tipo, registro):
    self.numeroCilindros = numeroCilindros
    self.tipo= tipo
    self.registro= registro

    # metodos

  def cambiarRegistro(self, registro):
    self.registro = registro

  def asignarTipo(self, tipo):
    if (tipo == "electrico" or tipo == "gasolina"):
      self.tipo = tipo