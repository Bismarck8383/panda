import  jpype
import  asposecells
jpype.startJVM()
from asposecells.api import Workbook

exel_antiguo = input("Nombre del archivo a convertir: ")
exe_covertido= input("Nombre que le dara al nuevo archivo: ")
#libreria para modificar la extencion de un archivo a otro
workbook = Workbook(f"{exel_antiguo}.xls")
workbook.save(f"{exe_covertido}.xlsx")
jpype.shutdownJVM()