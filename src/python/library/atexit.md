---
title: '"atexit" --- Exit handlers'
source_url: https://docs.python.org/es/3
source_path: library/atexit.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1790
---

# "atexit" --- Exit handlers

======================================================================

The "atexit" module defines functions to register and unregister
cleanup functions.  Functions thus registered are automatically
executed upon normal interpreter termination.  "atexit" runs these
functions in the *reverse* order in which they were registered; if you
register "A", "B", and "C", at interpreter termination time they will
be run in the order "C", "B", "A".

**Nota:** Las funciones registradas a través de este módulo no son
llamadas cuando el programa es eliminado por una señal no manejada por
Python, cuando se detecta un error fatal interno en Python o cuando se
llama a la función "os._exit()".

**Nota:** El efecto de registrar o cancelar el registro de funciones
dentro de una función de limpieza no esta definido.

Distinto en la versión 3.7: Cuando se usan con sub-intérpretes API C,
las funciones registradas son locales para el intérprete en el que se
registraron.

atexit.register(func, *args, **kwargs)

   Registra *func* como una función que se ejecutará cuando el
   intérprete se termine. Cualquier argumento opcional que deba
   pasarse a *func* debe pasarse como un argumento para la función
   "register()". Es posible registrar la misma función y argumentos
   más de una vez.

   En la finalización normal del programa (por ejemplo, si se llama a
   la función "sys.exit()" o finaliza la ejecución del módulo
   principal), todas las funciones registradas son llamadas en el
   orden último en entrar, primero en salir. Se supone que los módulos
   de menor nivel normalmente se importarán antes que los módulos de
   mayor nivel,  y por lo tanto, se limpiarán al final.

   Si se lanza una excepción durante la ejecución de los manejadores
   de salida, se muestra un rastreo (a menos que se haya lanzado
   "SystemExit") y se guarda la información de la excepción. Después
   de que todos los manejadores de salida hayan tenido la oportunidad
   de ejecutarse, la última excepción lanzada se vuelve a lanzar.

   Esta función retorna *func*, lo que hace posible usarlo como
   decorador.

   Advertencia:

     Iniciar nuevos hilos o llamar a "os.fork()" desde una función
     registrada puede llevar a una condición de carrera entre el hilo
     principal de Python liberando estados de hilos mientras las
     rutinas internas de "threading" o el nuevo proceso intentan usar
     ese estado. Esto puede provocar fallos en lugar de un cierre
     limpio.

   Distinto en la versión 3.12: Los intentos de iniciar un nuevo hilo
   o "bifurcar" un nuevo proceso en una función registrada conducen
   ahora a un "RuntimeError".

atexit.unregister(func)

   Remove *func* from the list of functions to be run at interpreter
   shutdown. "unregister()" silently does nothing if *func* was not
   previously registered.  If *func* has been registered more than
   once, every occurrence of that function in the "atexit" call stack
   will be removed.  Equality comparisons ("==") are used internally
   during unregistration, so function references do not need to have
   matching identities.

Ver también:

  Módulo "readline"
     Useful example of "atexit" to read and write "readline" history
     files.

## "atexit" Example

El siguiente ejemplo muestra cómo un módulo puede inicializar un
contador desde un archivo cuando se importa, y guardar el valor del
contador actualizado automáticamente cuando finaliza el programa, sin
necesidad de que la aplicación realice una llamada explícita en este
módulo cuando el intérprete se detiene.

   try:
       with open('counterfile') as infile:
           _count = int(infile.read())
   except FileNotFoundError:
       _count = 0

   def incrcounter(n):
       global _count
       _count = _count + n

   def savecounter():
       with open('counterfile', 'w') as outfile:
           outfile.write('%d' % _count)

   import atexit

   atexit.register(savecounter)

Los argumentos posicionales y de palabras clave también se pueden
pasar a la función "register()" para volver a pasar a la función
registrada cuando se llama:

   def goodbye(name, adjective):
       print('Goodbye %s, it was %s to meet you.' % (name, adjective))

   import atexit

   atexit.register(goodbye, 'Donny', 'nice')
   # or:
   atexit.register(goodbye, adjective='nice', name='Donny')

Usar como un *decorator*:

   import atexit

   @atexit.register
   def goodbye():
       print('You are now leaving the Python sector.')

Esto solo funciona con funciones que se puedan llamar sin argumentos.
