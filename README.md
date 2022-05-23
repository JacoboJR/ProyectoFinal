# Proyecto Final
## Main.py
En el codigo se muestra la biblioteca Dispatch y esta nos va ayudar a abrir cualquier aplicación que se le solicite y estas están alojadas en la libreria win32com
Además de que hay otro tipo que se llama DispatchEx y la diferencia entre cada una es que el Dispatch solo te permite abrir la aplicacion una vez.
Minetras que el dispatchEx te permite abrir una aolicacion sin importar que esta ya este abierte, es decir te permite crear varias instancias de la misma aplicación.

En la primera función del codigo que se muestra la memoria RAM total que tenemos disponible para nuestro equipo. 
En la segunda función se obtiene la memoria ram que se ha utilizado y con eso hacemos una regla de tres con el total de nuestra memoria RAM 
En el main tenemos le decimos al programa cuanta memoria RAM en porcentaje queremos que se ocupe y la aplicación que va a ser abierta en este caso Word y se repetira el ciclo hasta que se cumpla el llenado asignado.

## Script.ps1
Con un codigo de powershell pudimos identificar cuando una usb entra a nuestra computadora por medio del sonido. Una vez que haya entrado valida su nombre y su espacio en memoria y si es correcto procede a ejecutar el ram.exe
