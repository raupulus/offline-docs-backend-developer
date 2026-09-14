---
title: Sub-procesos
source_url: https://docs.python.org/es/3
source_path: library/asyncio-subprocess.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1720
---

# Sub-procesos

**Código fuente:** Lib/asyncio/subprocess.py,
Lib/asyncio/base_subprocess.py

======================================================================

Esta sección describe APIs de alto nivel de *async/await* de asyncio
para crear y gestionar sub-procesos.

Aquí podemos encontrar un ejemplo de cómo asyncio puede ejecutar un
comando de *shell* y obtener su resultado:

   import asyncio

   async def run(cmd):
       proc = await asyncio.create_subprocess_shell(
           cmd,
           stdout=asyncio.subprocess.PIPE,
           stderr=asyncio.subprocess.PIPE)

       stdout, stderr = await proc.communicate()

       print(f'[{cmd!r} exited with {proc.returncode}]')
       if stdout:
           print(f'[stdout]\n{stdout.decode()}')
       if stderr:
           print(f'[stderr]\n{stderr.decode()}')

   asyncio.run(run('ls /zzz'))

mostrará en pantalla:

   ['ls /zzz' exited with 1]
   [stderr]
   ls: /zzz: No such file or directory

Ya que todos las funciones de sub-procesos de asyncio son asíncronas y
asyncio proporciona herramientas para trabajar con tales funciones, es
fácil ejecutar y monitorear múltiples subprocesos en paralelo.  De
hecho es trivial modificar los ejemplos de arriba para ejecutar varios
comandos simultáneamente:

   async def main():
       await asyncio.gather(
           run('ls /zzz'),
           run('sleep 1; echo "hello"'))

   asyncio.run(main())

Véase también la subsección Examples.

## Creando sub-procesos

async asyncio.create_subprocess_exec(program, *args, stdin=None, stdout=None, stderr=None, limit=None, **kwds)

   Crea un sub-proceso.

   The *limit* argument sets the buffer limit for "StreamReader"
   wrappers for "stdout" and "stderr" (if "subprocess.PIPE" is passed
   to *stdout* and *stderr* arguments).

   Retorna una instancia de "Process".

   Véase la documentación de "loop.subprocess_exec()" para los otros
   parámetros.

   If the process object is garbage collected while the process is
   still running, the child process will be killed.

   Distinto en la versión 3.10: Se eliminó el parámetro *loop*.

async asyncio.create_subprocess_shell(cmd, stdin=None, stdout=None, stderr=None, limit=None, **kwds)

   Ejecuta el comando de shell *cmd*.

   The *limit* argument sets the buffer limit for "StreamReader"
   wrappers for "stdout" and "stderr" (if "subprocess.PIPE" is passed
   to *stdout* and *stderr* arguments).

   Retorna una instancia de "Process".

   Véase la documentación de "loop.subprocess_shell()" para los otros
   parámetros.

   If the process object is garbage collected while the process is
   still running, the child process will be killed.

   Importante:

     Es la responsabilidad de la aplicación asegurarse que todos los
     espacios en blanco y caracteres especiales estén citados
     apropiadamente para evitar vulnerabilidades de inyección de
     instrucciones. La función "shlex.quote()" puede ser usada para
     escapar caracteres en blanco y caracteres especiales de *shell*
     en cadenas de caracteres a ser usadas para construir comandos de
     *shell*.

   Distinto en la versión 3.10: Se eliminó el parámetro *loop*.

Nota:

  Los subprocesos están disponibles para Windows si se utiliza un
  "ProactorEventLoop". Consulte Soporte de subprocesos en Windows para
  obtener más detalles.

Ver también:

  asyncio también tiene las siguientes APIs de *bajo nivel* para
  trabajar con sub-procesos: "loop.subprocess_exec()",
  "loop.subprocess_shell()", "loop.connect_read_pipe()",
  "loop.connect_write_pipe()", así como también los Sub-procesos de
  Transportes y los Sub-procesos de Protocolos.

## Constantes

asyncio.subprocess.PIPE

   Se le puede pasar a los parámetros *stding*, *stdout* o *stderr*.

   If *PIPE* is passed to *stdin* argument, the "Process.stdin"
   attribute will point to a "StreamWriter" instance.

   If *PIPE* is passed to *stdout* or *stderr* arguments, the
   "Process.stdout" and "Process.stderr" attributes will point to
   "StreamReader" instances.

asyncio.subprocess.STDOUT

   Un valor especial que puede ser usado como el argumento de *stderr*
   e indica que los errores estándar deben ser redireccionados en la
   salida estándar.

asyncio.subprocess.DEVNULL

   Un valor especial que puede ser usado como el argumento de *stdin*,
   *stdout*, *stderr* para procesar funciones de creación.  Indica que
   el archivo especial "os.devnull" será usado para la correspondiente
   transmisión del sub-proceso.

## Interactuando con Subprocesos

Las dos funciones "create_subprocess_exec()" y
"create_subprocess_shell()" retornan instancias de la clase *Process*.
*Process* es un envoltorio de alto nivel que permite comunicarse con
los subprocesos y estar atento a sus términos.

class asyncio.subprocess.Process

   An object that wraps OS processes created by the
   "create_subprocess_exec()" and "create_subprocess_shell()"
   functions.

   Esta clase está diseñada para tener un API similar a la clase
   "subprocess.Popen", pero hay algunas diferencias notables:

   * a diferencia de Popen, las instancias de Process no tiene un
     equivalente del método "poll()";

   * los métodos "communicate()" y "wait()" no tienen un parámetro
     *timeout*: use la función "wait_for()";

   * el método "Process.wait()" es asíncrono, mientras que el método
     "subprocess.Popen.wait()" es implementado como un bucle de espera
     activa;

   * el parámetro *universal_newlines* no es compatible.

   Esta clase no es segura para subprocesos (not thread safe).

   Véase también la sección Subprocesos e Hilos.

   async wait()

      Espera a que el proceso hijo termine.

      Define y retorna el atributo "returncode".

      Nota:

        Este método puede bloquearse cuando usa "stdout=PIPE" o
        "stderr=PIPE" y el proceso hijo genera tanta salida que se
        bloquea esperando a que la tubería de búfer del SO acepte más
        datos. Use el método "communicate()" cuando use tuberías para
        evitar esta condición.

   async communicate(input=None)

      Interactuar con el proceso:

      1. envía datos a *stdin* (si *input* no es "None");

      2. cierra *stdin*;

      3. lee datos desde *stdout* y *stderr*, hasta que el llegue al
         EOF;

      4. espera a que el proceso termine.

      El argumento opcional *input* son los datos (objetos "bytes")
      que serán enviados a los procesos hijos.

      Retorna una tupla "(stdout_data, stderr_data)".

      Si se lanza la excepción "BrokenPipeError" o
      "ConnectionResetError" cuando se escribe *input* en *stdin*, la
      excepción es ignorada. Esta condición ocurre cuando el proceso
      finaliza antes de que todos los datos sean escritos en *stdin*.

      Si se desea enviar datos al *stdin* del proceso, el proceso
      necesita ser creado con "stdin=PIPE". De manera similar, para
      obtener cualquier cosa excepto "None" en la tupla del resultado,
      el proceso tiene que ser creado con los argumentos "stdout=PIPE"
      y/o "stderr=PIPE".

      Tenga en cuenta que los datos leídos son almacenados en memoria,
      por lo que no utilice este método si el tamaño de los datos es
      más grande o ilimitado.

      Distinto en la versión 3.12: *stdin* gets closed when
      "input=None" too.

   send_signal(signal)

      Envíe la señal *signal* al proceso hijo.

      Nota:

        On Windows, "SIGTERM" is an alias for "terminate()".
        "CTRL_C_EVENT" and "CTRL_BREAK_EVENT" can be sent to processes
        started with a *creationflags* parameter which includes
        "CREATE_NEW_PROCESS_GROUP".

   terminate()

      Para al proceso hijo.

      On POSIX systems this method sends "SIGTERM" to the child
      process.

      On Windows the Win32 API function "TerminateProcess()" is called
      to stop the child process.

   kill()

      Mata el proceso hijo.

      On POSIX systems this method sends "SIGKILL" to the child
      process.

      En Windows este método es un alias para "terminate()".

   stdin

      Standard input stream ("StreamWriter") or "None" if the process
      was created with "stdin=None".

   stdout

      Standard output stream ("StreamReader") or "None" if the process
      was created with "stdout=None".

   stderr

      Standard error stream ("StreamReader") or "None" if the process
      was created with "stderr=None".

   Advertencia:

     Utilice el método "communicate()" en vez de
     "process.stdin.write()", "await process.stdout.read()" o "await
     process.stderr.read". Esto evita bloqueos debido a que los flujos
     pausan la lectura o escritura y bloqueando al proceso hijo.

   pid

      Número de identificación del Proceso (PID por sus siglas en
      inglés).

      Note that for processes created by the
      "create_subprocess_shell()" function, this attribute is the PID
      of the spawned shell.

   returncode

      Código de retorno del proceso cuando finaliza.

      Un valor "None" indica que el proceso todavía no ha finalizado.

      For processes created with "create_subprocess_exec()", a
      negative value "-N" indicates that the child was terminated by
      signal "N" (POSIX only).

      For processes created with "create_subprocess_shell()", the
      return code reflects the exit status of the shell itself (e.g.
      "/bin/sh"), which may map signals to codes such as "128+N". See
      the documentation of the shell (for example, the Bash manual's
      Exit Status) for details.

### Subprocesos y Hilos

Por defecto el bucle de eventos de asyncio estándar permite correr
subprocesos desde hilos diferentes.

En Windows, sólo "ProactorEventLoop" proporciona subprocesos (por
defecto), "SelectorEventLoop" no es compatible con subprocesos.

Tenga en cuenta que implementaciones alternativas del bucle de eventos
pueden tener limitaciones propias; por favor consulte su
documentación.

Ver también: La sección Concurrencia y multihilos en asyncio.

### Ejemplos

Un ejemplo usando la clase "Process" para controlar un subproceso y la
clase "StreamReader" para leer de su salida estándar.

El subproceso es creado por la función "create_subprocess_exec()":

   import asyncio
   import sys

   async def get_date():
       code = 'import datetime as dt; print(dt.datetime.now())'

       # Create the subprocess; redirect the standard output
       # into a pipe.
       proc = await asyncio.create_subprocess_exec(
           sys.executable, '-c', code,
           stdout=asyncio.subprocess.PIPE)

       # Read one line of output.
       data = await proc.stdout.readline()
       line = data.decode('ascii').rstrip()

       # Wait for the subprocess exit.
       await proc.wait()
       return line

   date = asyncio.run(get_date())
   print(f"Current date: {date}")

Véase también los ejemplos de prueba escritos usando APIs de bajo
nivel.
