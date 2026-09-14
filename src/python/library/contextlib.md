---
title: '"contextlib" --- Utilidades para declaraciones de contexto "with"'
source_url: https://docs.python.org/es/3
source_path: library/contextlib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2120
---

# "contextlib" --- Utilidades para declaraciones de contexto "with"

**Código fuente:** Lib/contextlib.py

======================================================================

Este módulo proporciona utilidades para tareas comunes que involucran
la declaración "with". Para obtener más información, consulte también
Tipos gestores de contexto y Gestores de Contexto en la Declaración
with.

## Utilidades

Funciones y clases proporcionadas:

class contextlib.AbstractContextManager

   An *abstract base class* for classes that implement "__enter__()"
   and "__exit__()". A default implementation for "__enter__()" is
   provided which returns "self" while "__exit__()" is an abstract
   method which by default returns "None". See also the definition of
   Tipos gestores de contexto.

   Added in version 3.6.

class contextlib.AbstractAsyncContextManager

   An *abstract base class* for classes that implement "__aenter__()"
   and "__aexit__()". A default implementation for "__aenter__()" is
   provided which returns "self" while "__aexit__()" is an abstract
   method which by default returns "None". See also the definition of
   Gestores de contexto asíncronos.

   Added in version 3.7.

@contextlib.contextmanager

   This function is a *decorator* that can be used to define a factory
   function for "with" statement context managers, without needing to
   create a class or separate "__enter__()" and "__exit__()" methods.

   While many objects natively support use in with statements,
   sometimes a resource needs to be managed that isn't a context
   manager in its own right, and doesn't implement a "close()" method
   for use with "contextlib.closing".

   Un ejemplo abstracto sería el siguiente para garantizar la gestión
   correcta de los recursos:

      from contextlib import contextmanager

      @contextmanager
      def managed_resource(*args, **kwds):
          # Code to acquire resource, e.g.:
          resource = acquire_resource(*args, **kwds)
          try:
              yield resource
          finally:
              # Code to release resource, e.g.:
              release_resource(resource)

   La función se puede usar así:

      >>> with managed_resource(timeout=3600) as resource:
      ...     # Resource is released at the end of this block,
      ...     # even if code in the block raises an exception

   La función que se está decorando debe retornar un iterador
   *generador* cuando se llama. Este iterador debe producir
   exactamente un valor, que estará vinculado a los objetivos en la
   "with" declaración de la cláusula "as", si existe.

   En el punto donde el generador cede, se ejecuta el bloque anidado
   en la palabra clave "with". El generador se reanuda luego de salir
   del bloque. Si se produce una excepción no controlada en el bloque,
   se vuelve a plantear dentro del generador en el punto donde se
   produjo el rendimiento. Por lo tanto, puede usar una declaración
   "try"..."except"..."finally" para atrapar el error (si lo hay), o
   asegurarse de que se realice una limpieza. Si una excepción queda
   atrapada simplemente para registrarla o realizar alguna acción (en
   lugar de suprimirla por completo), el generador debe volver a
   generar esa excepción. De lo contrario, el administrador de
   contexto del generador indicará a la palabra clave "with" que se ha
   manejado la excepción, y la ejecución se reanudará con la
   declaración inmediatamente siguiente a la palabra clave "with".

   "@contextmanager" uses "ContextDecorator" so the context managers
   it creates can be used as decorators as well as in "with"
   statements. When used as a decorator, a new generator instance is
   implicitly created on each function call (this allows the otherwise
   "one-shot" context managers created by "@contextmanager" to meet
   the requirement that context managers support multiple invocations
   in order to be used as decorators).

   Distinto en la versión 3.2: Uso de "ContextDecorator".

@contextlib.asynccontextmanager

   Similar to "@~contextlib.contextmanager", but creates an
   asynchronous context manager.

   This function is a *decorator* that can be used to define a factory
   function for "async with" statement asynchronous context managers,
   without needing to create a class or separate "__aenter__()" and
   "__aexit__()" methods. It must be applied to an *asynchronous
   generator* function.

   Un ejemplo simple:

      from contextlib import asynccontextmanager

      @asynccontextmanager
      async def get_connection():
          conn = await acquire_db_connection()
          try:
              yield conn
          finally:
              await release_db_connection(conn)

      async def get_all_users():
          async with get_connection() as conn:
              return conn.query('SELECT ...')

   Added in version 3.7.

   Context managers defined with "@asynccontextmanager" can be used
   either as decorators or with "async with" statements:

      import time
      from contextlib import asynccontextmanager

      @asynccontextmanager
      async def timeit():
          now = time.monotonic()
          try:
              yield
          finally:
              print(f'it took {time.monotonic() - now}s to run')

      @timeit()
      async def main():
          # ... async code ...

   When used as a decorator, a new generator instance is implicitly
   created on each function call. This allows the otherwise "one-shot"
   context managers created by "@asynccontextmanager" to meet the
   requirement that context managers support multiple invocations in
   order to be used as decorators.

   Distinto en la versión 3.10: Async context managers created with
   "@asynccontextmanager" can be used as decorators.

contextlib.closing(thing)

   retorna un gestor de contexto que cierra *thing* al completar el
   bloque. Esto es básicamente equivalente a:

      from contextlib import contextmanager

      @contextmanager
      def closing(thing):
          try:
              yield thing
          finally:
              thing.close()

   Y te permite escribir código como este:

      from contextlib import closing
      from urllib.request import urlopen

      with closing(urlopen('https://www.python.org')) as page:
          for line in page:
              print(line)

   sin necesidad de cerrar explícitamente la "page". Incluso si se
   produce un error, se llamará a "page.close()" cuando salga el
   bloque "with".

   Nota:

     Most types managing resources support the *context manager*
     protocol, which closes *thing* on leaving the "with" statement.
     As such, "closing()" is most useful for third party types that
     don't support context managers. This example is purely for
     illustration purposes, as "urlopen()" would normally be used in a
     context manager.

contextlib.aclosing(thing)

   Retorna un administrador de contexto asíncrono que llama al método
   "aclose()" de *thing* una vez completado el bloque. Esto es
   básicamente equivalente a:

      from contextlib import asynccontextmanager

      @asynccontextmanager
      async def aclosing(thing):
          try:
              yield thing
          finally:
              await thing.aclose()

   Significativamente, "aclosing()" admite la limpieza determinista de
   generadores asincrónicos cuando salen temprano por "break" o una
   excepción. Por ejemplo:

      from contextlib import aclosing

      async with aclosing(my_generator()) as values:
          async for value in values:
              if value == 42:
                  break

   Este patrón garantiza que el código de salida asíncrono del
   generador se ejecute en el mismo contexto que sus iteraciones (de
   modo que las excepciones y las variables de contexto funcionen como
   se esperaba, y el código de salida no se ejecute después de la vida
   útil de alguna tarea de la que depende).

   Added in version 3.10.

contextlib.nullcontext(enter_result=None)

   Return a context manager that returns *enter_result* from
   "__enter__()", but otherwise does nothing. It is intended to be
   used as a stand-in for an optional context manager, for example:

      def myfunction(arg, ignore_exceptions=False):
          if ignore_exceptions:
              # Use suppress to ignore all exceptions.
              cm = contextlib.suppress(Exception)
          else:
              # Do not ignore any exceptions, cm has no effect.
              cm = contextlib.nullcontext()
          with cm:
              # Do something

   Un ejemplo usando *enter_result*:

      def process_file(file_or_path):
          if isinstance(file_or_path, str):
              # If string, open file
              cm = open(file_or_path)
          else:
              # Caller is responsible for closing file
              cm = nullcontext(file_or_path)

          with cm as file:
              # Perform processing on the file

   También se puede utilizar como sustituto de asynchronous context
   managers:

      async def send_http(session=None):
          if not session:
              # If no http session, create it with aiohttp
              cm = aiohttp.ClientSession()
          else:
              # Caller is responsible for closing the session
              cm = nullcontext(session)

          async with cm as session:
              # Send http requests with session

   Added in version 3.7.

   Distinto en la versión 3.10: Se agregó compatibilidad con
   *asynchronous context manager*.

contextlib.suppress(*exceptions)

   Retorna un administrador de contexto que suprime cualquiera de las
   excepciones especificadas si ocurren en el cuerpo de una
   instrucción "with" y luego reanuda la ejecución con la primera
   instrucción que sigue al final de la instrucción "with".

   Al igual que con cualquier otro mecanismo que suprima completamente
   las excepciones, este administrador de contexto debe usarse solo
   para cubrir errores muy específicos en los que se sabe que
   continuar silenciosamente con la ejecución del programa es lo
   correcto.

   Por ejemplo:

      from contextlib import suppress

      with suppress(FileNotFoundError):
          os.remove('somefile.tmp')

      with suppress(FileNotFoundError):
          os.remove('someotherfile.tmp')

   Este código es equivalente a:

      try:
          os.remove('somefile.tmp')
      except FileNotFoundError:
          pass

      try:
          os.remove('someotherfile.tmp')
      except FileNotFoundError:
          pass

   Este gestor de contexto es reentrant.

   If the code within the "with" block raises a "BaseExceptionGroup",
   suppressed exceptions are removed from the group.  Any exceptions
   of the group which are not suppressed are re-raised in a new group
   which is created using the original group's "derive()" method.

   Added in version 3.4.

   Distinto en la versión 3.12: "suppress" now supports suppressing
   exceptions raised as part of a "BaseExceptionGroup".

contextlib.redirect_stdout(new_target)

   Administrador de contexto para redirigir temporalmente "sys.stdout"
   a otro archivo u objeto similar a un archivo.

   Esta herramienta agrega flexibilidad a las funciones o clases
   existentes cuya salida está programada para stdout.

   For example, the output of "help()" normally is sent to
   *sys.stdout*. You can capture that output in a string by
   redirecting the output to an "io.StringIO" object. The replacement
   stream is returned from the "__enter__()" method and so is
   available as the target of the "with" statement:

      with redirect_stdout(io.StringIO()) as f:
          help(pow)
      s = f.getvalue()

   Para enviar la salida de "help()" a un archivo en el disco,
   redirija la salida a un archivo normal:

      with open('help.txt', 'w') as f:
          with redirect_stdout(f):
              help(pow)

   Para enviar la salida de "help()" a *sys.stderr*:

      with redirect_stdout(sys.stderr):
          help(pow)

   Tenga en cuenta que el efecto secundario global en "sys.stdout"
   significa que este administrador de contexto no es adecuado para su
   uso en el código de la biblioteca y en la mayoría de las
   aplicaciones con subprocesos. Tampoco tiene efecto en la salida de
   subprocesos. Sin embargo, sigue siendo un enfoque útil para muchos
   scripts de utilidad.

   Este gestor de contexto es reentrant.

   Added in version 3.4.

contextlib.redirect_stderr(new_target)

   Similar a "redirect_stdout()" pero redirigiendo "sys.stderr" a otro
   archivo u objeto similar a un archivo.

   Este gestor de contexto es reentrant.

   Added in version 3.5.

contextlib.chdir(path)

   Administrador de contexto no seguro en paralelo para cambiar el
   directorio de trabajo actual. Como esto cambia un estado global, el
   directorio de trabajo, no es adecuado para su uso en la mayoría de
   los contextos asincrónicos o de subprocesos. Tampoco es adecuado
   para la mayoría de las ejecuciones de código no lineal, como los
   generadores, donde la ejecución del programa se abandona
   temporalmente; a menos que se desee explícitamente, no debe ceder
   el paso cuando este administrador de contexto está activo.

   Este es un contenedor simple alrededor de "chdir()", cambia el
   directorio de trabajo actual al ingresar y restaura el anterior al
   salir.

   Este gestor de contexto es reentrant.

   Added in version 3.11.

class contextlib.ContextDecorator

   Una clase base que permite que un administrador de contexto también
   se use como decorador.

   Context managers inheriting from "ContextDecorator" have to
   implement "__enter__()" and "__exit__()" as normal. "__exit__"
   retains its optional exception handling even when used as a
   decorator.

   "ContextDecorator" is used by "@contextmanager", so you get this
   functionality automatically.

   Ejemplo de "ContextDecorator":

      from contextlib import ContextDecorator

      class mycontext(ContextDecorator):
          def __enter__(self):
              print('Starting')
              return self

          def __exit__(self, *exc):
              print('Finishing')
              return False

   La clase se puede usar así:

      >>> @mycontext()
      ... def function():
      ...     print('The bit in the middle')
      ...
      >>> function()
      Starting
      The bit in the middle
      Finishing

      >>> with mycontext():
      ...     print('The bit in the middle')
      ...
      Starting
      The bit in the middle
      Finishing

   Este cambio es solo azúcar sintáctico para cualquier construcción
   de la siguiente forma:

      def f():
          with cm():
              # Do stuff

   "ContextDecorator" le permite escribir en su lugar:

      @cm()
      def f():
          # Do stuff

   Deja en claro que el "cm" se aplica a toda la función, en lugar de
   solo una parte de ella (y guardar un nivel de sangría también es
   bueno).

   Los gestores de contexto existentes que ya tienen una clase base
   pueden ampliarse utilizando "ContextDecorator" como una clase
   mezcla (*mixin*):

      from contextlib import ContextDecorator

      class mycontext(ContextBaseClass, ContextDecorator):
          def __enter__(self):
              return self

          def __exit__(self, *exc):
              return False

   Nota:

     Como la función decorada debe poder llamarse varias veces, el
     gestor de contexto subyacente debe admitir el uso en múltiples
     declaraciones "with". Si este no es el caso, se debe utilizar la
     construcción original con la declaración explícita "with" dentro
     de la función.

   Added in version 3.2.

class contextlib.AsyncContextDecorator

   Similar a "ContextDecorator" pero solo para funciones asincrónicas.

   Ejemplo de "AsyncContextDecorator":

      from asyncio import run
      from contextlib import AsyncContextDecorator

      class mycontext(AsyncContextDecorator):
          async def __aenter__(self):
              print('Starting')
              return self

          async def __aexit__(self, *exc):
              print('Finishing')
              return False

   La clase se puede usar así:

      >>> @mycontext()
      ... async def function():
      ...     print('The bit in the middle')
      ...
      >>> run(function())
      Starting
      The bit in the middle
      Finishing

      >>> async def function():
      ...    async with mycontext():
      ...         print('The bit in the middle')
      ...
      >>> run(function())
      Starting
      The bit in the middle
      Finishing

   Added in version 3.10.

class contextlib.ExitStack

   Un gestor de contexto que está diseñado para facilitar la
   combinación programática de otros gestores de contexto y funciones
   de limpieza, especialmente aquellas que son opcionales o que de
   otro modo son impulsadas por los datos de entrada.

   Por ejemplo, un conjunto de archivos puede manejarse fácilmente en
   una sola declaración de la siguiente manera:

      with ExitStack() as stack:
          files = [stack.enter_context(open(fname)) for fname in filenames]
          # All opened files will automatically be closed at the end of
          # the with statement, even if attempts to open files later
          # in the list raise an exception

   The "__enter__()" method returns the "ExitStack" instance, and
   performs no additional operations.

   Cada instancia mantiene una pila de retrollamadas registradas que
   se llaman en orden inverso cuando la instancia se cierra (ya sea
   explícita o implícitamente al final de una instrucción "with").
   Tenga en cuenta que las retrollamadas *no* se invocan
   implícitamente cuando la instancia de la pila de contexto se
   recolecta basura.

   Este modelo de pila se utiliza para que los administradores de
   contexto que adquieren sus recursos en su método "__init__" (como
   los objetos de archivo) se puedan manejar correctamente.

   Dado que las retrollamadas registradas se invocan en el orden
   inverso del registro, esto termina comportándose como si se
   hubieran utilizado múltiples instrucciones anidadas "with" con el
   conjunto registrado de retrollamadas. Esto incluso se extiende al
   manejo de excepciones: si una retrollamada interna suprime o
   reemplaza una excepción, las retrollamadas externas se pasarán
   argumentos basados en ese estado actualizado.

   Esta es una API de nivel relativamente bajo que se ocupa de los
   detalles de desenrollar correctamente la pila de retrollamadas de
   salida. Proporciona una base adecuada para administradores de
   contexto de nivel superior que manipulan la pila de salida en
   formas específicas de la aplicación.

   Added in version 3.3.

   enter_context(cm)

      Enters a new context manager and adds its "__exit__()" method to
      the callback stack. The return value is the result of the
      context manager's own "__enter__()" method.

      Estos administradores de contexto pueden suprimir excepciones
      tal como lo harían normalmente si se usaran directamente como
      parte de una declaración "with".

      Distinto en la versión 3.11: Lanza "TypeError" en lugar de
      "AttributeError" si *cm* no es un administrador de contexto.

   push(exit)

      Adds a context manager's "__exit__()" method to the callback
      stack.

      As "__enter__" is *not* invoked, this method can be used to
      cover part of an "__enter__()" implementation with a context
      manager's own "__exit__()" method.

      If passed an object that is not a context manager, this method
      assumes it is a callback with the same signature as a context
      manager's "__exit__()" method and adds it directly to the
      callback stack.

      By returning true values, these callbacks can suppress
      exceptions the same way context manager "__exit__()" methods
      can.

      El objeto pasado se retorna desde la función, lo que permite que
      este método se use como decorador de funciones.

   callback(callback, /, *args, **kwds)

      Acepta una función de retrollamada arbitraria y argumentos y la
      agrega a la pila de retrollamada.

      A diferencia de los otros métodos, las retrollamadas agregadas
      de esta manera no pueden suprimir excepciones (ya que nunca se
      pasan los detalles de excepción).

      La retrollamada pasada se retorna desde la función, lo que
      permite que este método se use como decorador de funciones.

   pop_all()

      Transfiere la pila de retrollamada a una instancia fresca
      "ExitStack" y la retorna. Esta operación no invoca
      retrollamadas; en cambio, ahora se invocarán cuando se cierre la
      nueva pila (ya sea explícita o implícitamente al final de una
      instrucción "with").

      Por ejemplo, un grupo de archivos se puede abrir como una
      operación de "todo o nada" de la siguiente manera:

         with ExitStack() as stack:
             files = [stack.enter_context(open(fname)) for fname in filenames]
             # Hold onto the close method, but don't call it yet.
             close_files = stack.pop_all().close
             # If opening any file fails, all previously opened files will be
             # closed automatically. If all files are opened successfully,
             # they will remain open even after the with statement ends.
             # close_files() can then be invoked explicitly to close them all.

   close()

      Inmediatamente desenrolla la pila de retrollamada, invocando
      retrollamadas en el orden inverso de registro. Para los
      administradores de contexto y las retrollamadas de salida
      registradas, los argumentos pasados indicarán que no se produjo
      ninguna excepción.

class contextlib.AsyncExitStack

   Un gestor de contexto asíncrono, similar a "ExitStack", que admite
   la combinación de gestores de contexto síncrono y asíncrono, además
   de tener rutinas para la lógica de limpieza.

   The "close()" method is not implemented; "aclose()" must be used
   instead.

   async enter_async_context(cm)

      Similar to "ExitStack.enter_context()" but expects an
      asynchronous context manager.

      Distinto en la versión 3.11: Lanza "TypeError" en lugar de
      "AttributeError" si *cm* no es un administrador de contexto
      asíncrono.

   push_async_exit(exit)

      Similar to "ExitStack.push()" but expects either an asynchronous
      context manager or a coroutine function.

   push_async_callback(callback, /, *args, **kwds)

      Similar to "ExitStack.callback()" but expects a coroutine
      function.

   async aclose()

      Similar to "ExitStack.close()" but properly handles awaitables.

   Continuing the example for "@asynccontextmanager":

      async with AsyncExitStack() as stack:
          connections = [await stack.enter_async_context(get_connection())
              for i in range(5)]
          # All opened connections will automatically be released at the end of
          # the async with statement, even if attempts to open a connection
          # later in the list raise an exception.

   Added in version 3.7.

## Ejemplos y recetas

This section describes some examples and recipes for making effective
use of the tools provided by "contextlib".

### Apoyando un número variable de gestores de contexto

El caso de uso principal para "ExitStack" es el que se proporciona en
la documentación de la clase: admite un número variable de gestores de
contexto y otras operaciones de limpieza en una sola "with". La
variabilidad puede provenir de la cantidad de gestores de contexto que
necesitan ser impulsados por la entrada del usuario (como abrir una
colección de archivos especificada por el usuario), o de que algunos
de los gestores de contexto sean opcionales:

   with ExitStack() as stack:
       for resource in resources:
           stack.enter_context(resource)
       if need_special_resource():
           special = acquire_special_resource()
           stack.callback(release_special_resource, special)
       # Perform operations that use the acquired resources

Como se muestra, "ExitStack" también hace que sea bastante fácil de
usar "with" para administrar recursos arbitrarios que no admiten de
forma nativa el protocolo de gestión de contexto.

### Capturando excepciones de los métodos "__enter__"

It is occasionally desirable to catch exceptions from an "__enter__()"
method implementation, *without* inadvertently catching exceptions
from the "with" statement body or the context manager's "__exit__()"
method. By using "ExitStack" the steps in the context management
protocol can be separated slightly in order to allow this:

   stack = ExitStack()
   try:
       x = stack.enter_context(cm)
   except Exception:
       # handle __enter__ exception
   else:
       with stack:
           # Handle normal case

Es probable que la necesidad de hacer esto indique que la API
subyacente debería proporcionar una interfaz de administración de
recursos directa para usar con "try"/"except"/"finally", pero no todas
las API están bien diseñados en ese sentido. Cuando un administrador
de contexto es la única API de administración de recursos
proporcionada, entonces "ExitStack" puede facilitar el manejo de
diversas situaciones que no se pueden manejar directamente en una
declaración "with".

### Limpieza en una implementación "__enter__"

As noted in the documentation of "ExitStack.push()", this method can
be useful in cleaning up an already allocated resource if later steps
in the "__enter__()" implementation fail.

Aquí hay un ejemplo de cómo hacer esto para un administrador de
contexto que acepta funciones de adquisición y liberación de recursos,
junto con una función de validación opcional, y las asigna al
protocolo de administración de contexto:

   from contextlib import contextmanager, AbstractContextManager, ExitStack

   class ResourceManager(AbstractContextManager):

       def __init__(self, acquire_resource, release_resource, check_resource_ok=None):
           self.acquire_resource = acquire_resource
           self.release_resource = release_resource
           if check_resource_ok is None:
               def check_resource_ok(resource):
                   return True
           self.check_resource_ok = check_resource_ok

       @contextmanager
       def _cleanup_on_error(self):
           with ExitStack() as stack:
               stack.push(self)
               yield
               # The validation check passed and didn't raise an exception
               # Accordingly, we want to keep the resource, and pass it
               # back to our caller
               stack.pop_all()

       def __enter__(self):
           resource = self.acquire_resource()
           with self._cleanup_on_error():
               if not self.check_resource_ok(resource):
                   msg = "Failed validation for {!r}"
                   raise RuntimeError(msg.format(resource))
           return resource

       def __exit__(self, *exc_details):
           # We don't need to duplicate any of our resource release logic
           self.release_resource()

### Reemplazar cualquier uso de "try-finally" y marcar variables

Un patrón que a veces verá es una declaración de "try-finally" con una
variable de indicador para indicar si el cuerpo de la cláusula
"finally" debe ejecutarse o no. En su forma más simple (que ya no
puede manejarse simplemente usando una cláusula "except" en su lugar),
se parece a esto:

   cleanup_needed = True
   try:
       result = perform_operation()
       if result:
           cleanup_needed = False
   finally:
       if cleanup_needed:
           cleanup_resources()

Al igual que con cualquier código basado en la declaración "try", esto
puede causar problemas de desarrollo y revisión, porque el código de
configuración y el código de limpieza pueden terminar separados por
secciones de código arbitrariamente largas.

"ExitStack" hace posible registrar una retrollamada para su ejecución
al final de una instrucción "with", y luego decide omitir la ejecución
de esa retrollamada:

   from contextlib import ExitStack

   with ExitStack() as stack:
       stack.callback(cleanup_resources)
       result = perform_operation()
       if result:
           stack.pop_all()

This allows the intended cleanup behaviour to be made explicit up
front, rather than requiring a separate flag variable.

Si una aplicación particular usa mucho este patrón, puede
simplificarse aún más por medio de una pequeña clase auxiliar:

   from contextlib import ExitStack

   class Callback(ExitStack):
       def __init__(self, callback, /, *args, **kwds):
           super().__init__()
           self.callback(callback, *args, **kwds)

       def cancel(self):
           self.pop_all()

   with Callback(cleanup_resources) as cb:
       result = perform_operation()
       if result:
           cb.cancel()

Si la limpieza del recurso no está bien agrupada en una función
independiente, entonces todavía es posible usar la forma decoradora de
"ExitStack.callback()" para declarar la limpieza del recurso por
adelantado:

   from contextlib import ExitStack

   with ExitStack() as stack:
       @stack.callback
       def cleanup_resources():
           ...
       result = perform_operation()
       if result:
           stack.pop_all()

Debido a la forma en que funciona el protocolo decorador, una función
de retrollamada declarada de esta manera no puede tomar ningún
parámetro. En cambio, se debe acceder a los recursos que se liberarán
como variables de cierre.

### Usar un gestor de contexto como decorador de funciones

"ContextDecorator" hace posible usar un gestor de contexto tanto en
una instrucción ordinaria "with" como también como decorador de
funciones.

Por ejemplo, a veces es útil envolver funciones o grupos de
declaraciones con un registrador que puede rastrear la hora de entrada
y la hora de salida. En lugar de escribir tanto un decorador de
funciones como un administrador de contexto para la tarea, heredar de
"ContextDecorator" proporciona ambas capacidades en una sola
definición:

   from contextlib import ContextDecorator
   import logging

   logging.basicConfig(level=logging.INFO)

   class track_entry_and_exit(ContextDecorator):
       def __init__(self, name):
           self.name = name

       def __enter__(self):
           logging.info('Entering: %s', self.name)

       def __exit__(self, exc_type, exc, exc_tb):
           logging.info('Exiting: %s', self.name)

Las instancias de esta clase se pueden usar como un gestor de
contexto:

   with track_entry_and_exit('widget loader'):
       print('Some time consuming activity goes here')
       load_widget()

Y también como decorador de funciones:

   @track_entry_and_exit('widget loader')
   def activity():
       print('Some time consuming activity goes here')
       load_widget()

Note that there is one additional limitation when using context
managers as function decorators: there's no way to access the return
value of "__enter__()". If that value is needed, then it is still
necessary to use an explicit "with" statement.

Ver también:

  **PEP 343** - La declaración "with"
     La especificación, antecedentes y ejemplos de la declaración de
     Python "with".

## Gestores de contexto de uso único, reutilizables y reentrantes

La mayoría de los gestores de contexto están escritos de una manera
que significa que solo se pueden usar de manera efectiva en una
declaración "with" una vez. Estos administradores de contexto de un
solo uso deben crearse de nuevo cada vez que se usan; si intenta
usarlos por segunda vez, se activará una excepción o, de lo contrario,
no funcionará correctamente.

Esta limitación común significa que generalmente es aconsejable crear
gestores de contexto directamente en el encabezado de la palabra clave
"with" donde se usan (como se muestra en todos los ejemplos de uso
anteriores).

Los archivos son un ejemplo de gestores de contexto de un solo uso, ya
que la primera "with" cerrará el archivo, evitando cualquier otra
operación de E/S que use ese objeto de archivo.

Context managers created using "@contextmanager" are also single use
context managers, and will complain about the underlying generator
failing to yield if an attempt is made to use them a second time:

   >>> from contextlib import contextmanager
   >>> @contextmanager
   ... def singleuse():
   ...     print("Before")
   ...     yield
   ...     print("After")
   ...
   >>> cm = singleuse()
   >>> with cm:
   ...     pass
   ...
   Before
   After
   >>> with cm:
   ...     pass
   ...
   Traceback (most recent call last):
       ...
   RuntimeError: generator didn't yield

### Gestores contextuales reentrantes

Los gestores de contexto más sofisticados pueden ser "reentrantes".
Estos administradores de contexto no solo se pueden usar en múltiples
declaraciones "with", sino que también se pueden usar *inside* a
"with" que ya está usando el mismo gestor de contexto.

"threading.RLock" es un ejemplo de administrador de contexto
reentrante, al igual que "suppress()", "redirect_stdout()" y
"chdir()". Aquí hay un ejemplo muy simple de uso de reentrada:

   >>> from contextlib import redirect_stdout
   >>> from io import StringIO
   >>> stream = StringIO()
   >>> write_to_stream = redirect_stdout(stream)
   >>> with write_to_stream:
   ...     print("This is written to the stream rather than stdout")
   ...     with write_to_stream:
   ...         print("This is also written to the stream")
   ...
   >>> print("This is written directly to stdout")
   This is written directly to stdout
   >>> print(stream.getvalue())
   This is written to the stream rather than stdout
   This is also written to the stream

Es más probable que los ejemplos del mundo real de reentrada impliquen
múltiples funciones que se llaman entre sí y, por lo tanto, sean mucho
más complicadas que este ejemplo.

Tenga en cuenta también que ser reentrante *no* es lo mismo que ser
seguro para subprocesos. "redirect_stdout()", por ejemplo,
definitivamente no es seguro para subprocesos, ya que realiza una
modificación global al estado del sistema al vincular "sys.stdout" a
una secuencia diferente.

### Gestores contextuales reutilizables

Distintos de los administradores de contexto de uso único y reentrante
son los administradores de contexto "reutilizables" (o, para ser
completamente explícitos, los administradores de contexto
"reutilizables, pero no reentrantes", ya que los administradores de
contexto reentrantes también son reutilizables). Estos administradores
de contexto admiten que se usen varias veces, pero fallarán (o de lo
contrario no funcionarán correctamente) si la instancia específica del
administrador de contexto ya se ha utilizado en una declaración que
contiene.

"threading.Lock" es un ejemplo de un gestor de contexto reutilizable,
pero no reentrante (para un bloqueo reentrante, es necesario usar
"threading.RLock" en su lugar).

Otro ejemplo de un administrador de contexto reutilizable, pero no
reentrante es "ExitStack", ya que invoca *all* las retrollamadas
registradas actualmente al dejar cualquier con declaración,
independientemente de dónde se agregaron esas retrollamadas:

   >>> from contextlib import ExitStack
   >>> stack = ExitStack()
   >>> with stack:
   ...     stack.callback(print, "Callback: from first context")
   ...     print("Leaving first context")
   ...
   Leaving first context
   Callback: from first context
   >>> with stack:
   ...     stack.callback(print, "Callback: from second context")
   ...     print("Leaving second context")
   ...
   Leaving second context
   Callback: from second context
   >>> with stack:
   ...     stack.callback(print, "Callback: from outer context")
   ...     with stack:
   ...         stack.callback(print, "Callback: from inner context")
   ...         print("Leaving inner context")
   ...     print("Leaving outer context")
   ...
   Leaving inner context
   Callback: from inner context
   Callback: from outer context
   Leaving outer context

Como muestra el resultado del ejemplo, la reutilización de un solo
objeto de pila en múltiples con declaraciones funciona correctamente,
pero intentar anidarlos hará que la pila se borre al final de la
declaración más interna, lo que es poco probable que sea un
comportamiento deseable.

El uso de instancias separadas "ExitStack" en lugar de reutilizar una
sola instancia evita ese problema:

   >>> from contextlib import ExitStack
   >>> with ExitStack() as outer_stack:
   ...     outer_stack.callback(print, "Callback: from outer context")
   ...     with ExitStack() as inner_stack:
   ...         inner_stack.callback(print, "Callback: from inner context")
   ...         print("Leaving inner context")
   ...     print("Leaving outer context")
   ...
   Leaving inner context
   Callback: from inner context
   Leaving outer context
   Callback: from outer context
