---
title: '"test" --- Regression tests package for Python'
source_url: https://docs.python.org/es/3
source_path: library/test.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4100
---

# "test" --- Regression tests package for Python

Nota:

  The "test" package is meant for internal use by Python only. It is
  documented for the benefit of the core developers of Python. Any use
  of this package outside of Python's standard library is discouraged
  as code mentioned here can change or be removed without notice
  between releases of Python.

======================================================================

The "test" package contains all regression tests for Python as well as
the modules "test.support" and "test.regrtest". "test.support" is used
to enhance your tests while "test.regrtest" drives the testing suite.

Each module in the "test" package whose name starts with "test_" is a
testing suite for a specific module or feature. All new tests should
be written using the "unittest" or "doctest" module.  Some older tests
are written using a "traditional" testing style that compares output
printed to "sys.stdout"; this style of test is considered deprecated.

Ver también:

  Módulo "unittest"
     Escritura de pruebas de regresión de PyUnit.

  Módulo "doctest"
     Pruebas integradas en cadenas de caracteres de documentación.

## Writing Unit Tests for the "test" package

Se prefiere que las pruebas que utilizan el módulo "unittest" sigan
algunas pautas. Una es nombrar el módulo de prueba comenzándolo con
"test_" y terminarlo con el nombre del módulo que se está probando.
Los métodos de prueba en el módulo de prueba deben comenzar con
"test_" y terminar con una descripción de lo que el método está
probando. Esto es necesario para que el controlador de prueba
reconozca los métodos como métodos de prueba. Por lo tanto, no se debe
incluir una cadena de caracteres de documentación para el método. Se
debe usar un comentario (como "# Tests function returns only True or
False") para proporcionar documentación para los métodos de prueba.
Esto se hace porque las cadenas de documentación se imprimen si
existen y, por lo tanto, no se indica qué prueba se está ejecutando.

A menudo se usa una plantilla básica:

   import unittest
   from test import support

   class MyTestCase1(unittest.TestCase):

       # Only use setUp() and tearDown() if necessary

       def setUp(self):
           ... code to execute in preparation for tests ...

       def tearDown(self):
           ... code to execute to clean up after tests ...

       def test_feature_one(self):
           # Test feature one.
           ... testing code ...

       def test_feature_two(self):
           # Test feature two.
           ... testing code ...

       ... more test methods ...

   class MyTestCase2(unittest.TestCase):
       ... same structure as MyTestCase1 ...

   ... more test classes ...

   if __name__ == '__main__':
       unittest.main()

Este patrón de código permite que el conjunto de pruebas sea ejecutado
por "test.regrtest", como un script que admite la CLI "unittest", o
mediante la CLI "python -m unittest".

El objetivo de las pruebas de regresión es intentar romper el código.
Esto lleva a algunas pautas a seguir:

* El conjunto de pruebas debe ejercer todas las clases, funciones y
  constantes. Esto incluye no solo la API externa que se presentará al
  mundo exterior sino también el código "privado".

* Se prefiere la prueba de caja blanca (examinar el código que se
  prueba cuando se escriben las pruebas). Las pruebas de caja negra
  (probar solo la interfaz de usuario publicada) no son lo
  suficientemente completas como para garantizar que se prueben todos
  los casos límite y límite.

* Asegúrese de que todos los valores posibles son probados, incluidos
  los no válidos. Esto asegura que no solo todos los valores válidos
  sean aceptables, sino que los valores incorrectos se manejen
  correctamente.

* Agote tantas rutas de código cómo sea posible. Pruebe donde se
  produce la ramificación y, por lo tanto, adapte la entrada para
  asegurarse de que se toman muchas rutas diferentes a través del
  código.

* Añada una prueba explícita para cualquier error descubierto para el
  código probado. Esto asegurará que el error no vuelva a aparecer si
  el código se cambia en el futuro.

* Asegúrese de limpiar después de sus pruebas (así como cerrar y
  eliminar todos los archivos temporales).

* Si una prueba depende de una condición específica del sistema
  operativo, verifique que la condición ya existe antes de intentar la
  prueba.

* Importe la menor cantidad de módulos posible y hágalo lo antes
  posible. Esto minimiza las dependencias externas de las pruebas y
  también minimiza el posible comportamiento anómalo de los efectos
  secundarios de importar un módulo.

* Intente maximizar la reutilización del código. En ocasiones, las
  pruebas variarán en algo tan pequeño como qué tipo de entrada se
  utiliza. Minimice la duplicación de código usando como clase base
  una clase de prueba básica con una clase que especifique la entrada:

     class TestFuncAcceptsSequencesMixin:

         func = mySuperWhammyFunction

         def test_func(self):
             self.func(self.arg)

     class AcceptLists(TestFuncAcceptsSequencesMixin, unittest.TestCase):
         arg = [1, 2, 3]

     class AcceptStrings(TestFuncAcceptsSequencesMixin, unittest.TestCase):
         arg = 'abc'

     class AcceptTuples(TestFuncAcceptsSequencesMixin, unittest.TestCase):
         arg = (1, 2, 3)

  When using this pattern, remember that all classes that inherit from
  "unittest.TestCase" are run as tests.  The
  "TestFuncAcceptsSequencesMixin" class in the example above does not
  have any data and so can't be run by itself, thus it does not
  inherit from "unittest.TestCase".

Ver también:

  Desarrollo dirigido por pruebas (*Test Driven Development*)
     Un libro de *Kent Beck* sobre pruebas de escritura antes del
     código.

## Ejecución de pruebas utilizando la interfaz de línea de comandos

The "test" package can be run as a script to drive Python's regression
test suite, thanks to the "-m" option: **python -m test**. Under the
hood, it uses "test.regrtest"; the call **python -m test.regrtest**
used in previous Python versions still works.  Running the script by
itself automatically starts running all regression tests in the "test"
package. It does this by finding all modules in the package whose name
starts with "test_", importing them, and executing the function
"test_main()" if present or loading the tests via
unittest.TestLoader.loadTestsFromModule if "test_main" does not exist.
The names of tests to execute may also be passed to the script.
Specifying a single regression test (**python -m test test_spam**)
will minimize output and only print whether the test passed or failed.

Running "test" directly allows what resources are available for tests
to use to be set. You do this by using the "-u" command-line option.
Specifying "all" as the value for the "-u" option enables all possible
resources: **python -m test -uall**. If all but one resource is
desired (a more common case), a comma-separated list of resources that
are not desired may be listed after "all". The command **python -m
test -uall,-audio,-largefile** will run "test" with all resources
except the "audio" and "largefile" resources. For a list of all
resources and more command-line options, run **python -m test -h**.

Algunas otras formas de ejecutar las pruebas de regresión dependen de
en qué plataforma se ejecuten las pruebas. En Unix, puede ejecutar
**make test** en el directorio de nivel superior donde se construyó
Python. En Windows, ejecutar **rt.bat** desde su directorio "PCbuild"
ejecutará todas las pruebas de regresión.

Added in version 3.14: Output is colorized by default and can be
controlled using environment variables.

# "test.support" --- Utilities for the Python test suite

The "test.support" module provides support for Python's regression
test suite.

Nota:

  "test.support" is not a public module.  It is documented here to
  help Python developers write tests.  The API of this module is
  subject to change without backwards compatibility concerns between
  releases.

Este módulo define las siguientes excepciones:

exception test.support.TestFailed

   Excepción que se lanzará cuando una prueba falle. Está en desuso a
   favor de pruebas basadas en "unittest"y los métodos de aserción de
   "unittest.TestCase".

exception test.support.ResourceDenied

   La subclase de "unittest.SkipTest". Se lanza cuando un recurso
   (como una conexión de red) no está disponible. Lanzado por la
   función "requires()".

The "test.support" module defines the following constants:

test.support.verbose

   "True" cuando la salida detallada está habilitada. Debe verificarse
   cuando se desea información más detallada sobre una prueba en
   ejecución. *verbose* está establecido por "test.regrtest".

test.support.is_jython

   "True" si el intérprete en ejecución es Jython.

test.support.is_android

   "True" if "sys.platform" is "android".

test.support.is_emscripten

   "True" if "sys.platform" is "emscripten".

test.support.is_wasi

   "True" if "sys.platform" is "wasi".

test.support.is_apple_mobile

   "True" if "sys.platform" is "ios", "tvos", or "watchos".

test.support.is_apple

   "True" if "sys.platform" is "darwin" or "is_apple_mobile" is
   "True".

test.support.unix_shell

   Ruta del shell si no está en Windows; de otra manera "None".

test.support.LOOPBACK_TIMEOUT

   Tiempo de espera en segundos para las pruebas que utilizan un
   servidor de red que escucha en la interfaz local de loopback de la
   red como "127.0.0.1".

   El tiempo de espera es lo suficientemente largo para evitar el
   fracaso de la prueba: tiene en cuenta que el cliente y el servidor
   pueden ejecutarse en diferentes hilos o incluso en diferentes
   procesos.

   El tiempo de espera debe ser lo suficientemente largo para los
   métodos "connect()", "recv()" y "send()" de "socket.socket".

   Su valor por defecto es de 5 segundos.

   Ver también "INTERNET_TIMEOUT".

test.support.INTERNET_TIMEOUT

   Tiempo de espera en segundos para las solicitudes de red que van a
   Internet.

   El tiempo de espera es lo suficientemente corto como para evitar
   que una prueba espere demasiado tiempo si la solicitud de Internet
   se bloquea por cualquier motivo.

   Normalmente, un tiempo de espera utilizando "INTERNET_TIMEOUT" no
   debería marcar una prueba como fallida, sino que debería omitir la
   prueba: ver "transient_internet()".

   Su valor por defecto es de 1 minuto.

   Ver también "LOOPBACK_TIMEOUT".

test.support.SHORT_TIMEOUT

   Tiempo de espera en segundos para marcar una prueba como fallida si
   la prueba tarda "demasiado".

   El valor del tiempo de espera depende de la opción de línea de
   comandos regrtest "--timeout".

   Si una prueba que utiliza "SHORT_TIMEOUT" empieza a fallar
   aleatoriamente en buildbots lentos, utilice en su lugar
   "LONG_TIMEOUT".

   Su valor por defecto es de 30 segundos.

test.support.LONG_TIMEOUT

   Tiempo de espera en segundos para detectar cuando se cuelga una
   prueba.

   Es lo suficientemente largo como para reducir el riesgo de fracaso
   de la prueba en los buildbots de Python más lentos. No debe
   utilizarse para marcar una prueba como fallida si la prueba tarda
   "demasiado".  El valor del tiempo de espera depende de la opción de
   línea de comandos regrtest "--timeout".

   Su valor por defecto es de 5 minutos.

   Ver también "LOOPBACK_TIMEOUT", "INTERNET_TIMEOUT" y
   "SHORT_TIMEOUT".

test.support.PGO

   Establecido cuando se pueden omitir las pruebas cuando no son
   útiles para *PGO*.

test.support.PIPE_MAX_SIZE

   Una constante que probablemente sea más grande que el tamaño del
   búfer de la tubería (*pipe*) del sistema operativo subyacente, para
   bloquear las escrituras.

test.support.Py_DEBUG

   "True" if Python was built with the "Py_DEBUG" macro defined, that
   is, if Python was built in debug mode.

   Added in version 3.12.

test.support.SOCK_MAX_SIZE

   Una constante que probablemente sea más grande que el tamaño del
   búfer del socket del sistema operativo subyacente para bloquear las
   escrituras.

test.support.TEST_SUPPORT_DIR

   Set to the top level directory that contains "test.support".

test.support.TEST_HOME_DIR

   Establecido en el directorio de nivel superior para el paquete de
   prueba.

test.support.TEST_DATA_DIR

   Establecido en el directorio "data" dentro del paquete de prueba.

test.support.MAX_Py_ssize_t

   Establecido "sys.maxsize" para pruebas de gran memoria.

test.support.max_memuse

   Establecido por "set_memlimit()" como límite de memoria para
   pruebas de memoria grande. Limitado por "MAX_Py_ssize_t".

test.support.real_max_memuse

   Establecido por "set_memlimit()" como límite de memoria para
   pruebas de memoria grande. No limitado por "MAX_Py_ssize_t".

test.support.MISSING_C_DOCSTRINGS

   Vale "True" si Python se construye sin cadenas de documentos (la
   macro "WITH_DOC_STRINGS" no está definida). Consulte la opción
   "configure --without-doc-strings".

   Consulte también la variable "HAVE_DOCSTRINGS".

test.support.HAVE_DOCSTRINGS

   Vale "True" si las cadenas de documentación de la función están
   disponibles. Consulte la opción "python -OO", que elimina las
   cadenas de documentación de las funciones implementadas en Python.

   Consulte también la variable "MISSING_C_DOCSTRINGS".

test.support.TEST_HTTP_URL

   Define la URL de un servidor HTTP dedicado para las pruebas de red.

test.support.ALWAYS_EQ

   Objeto que es igual a cualquier cosa. Se utiliza para probar la
   comparación de tipos mixtos.

test.support.NEVER_EQ

   Objeto que no es igual a nada (incluso a "ALWAYS_EQ"). Se utiliza
   para probar la comparación de tipos mixtos.

test.support.LARGEST

   Objeto que es mayor que cualquier cosa (excepto a sí mismo). Se
   utiliza para probar la comparación de tipos mixtos.

test.support.SMALLEST

   Objeto que es menor que cualquier cosa (excepto él mismo). Se
   utiliza para probar la comparación de tipos mixtos.

The "test.support" module defines the following functions:

test.support.busy_retry(timeout, err_msg=None, /, *, error=True)

   Run the loop body until "break" stops the loop.

   After *timeout* seconds, raise an "AssertionError" if *error* is
   true, or just stop the loop if *error* is false.

   Example:

      for _ in support.busy_retry(support.SHORT_TIMEOUT):
          if check():
              break

   Example of error=False usage:

      for _ in support.busy_retry(support.SHORT_TIMEOUT, error=False):
          if check():
              break
      else:
          raise RuntimeError('my custom error')

test.support.sleeping_retry(timeout, err_msg=None, /, *, init_delay=0.010, max_delay=1.0, error=True)

   Wait strategy that applies exponential backoff.

   Run the loop body until "break" stops the loop. Sleep at each loop
   iteration, but not at the first iteration. The sleep delay is
   doubled at each iteration (up to *max_delay* seconds).

   See "busy_retry()" documentation for the parameters usage.

   Example raising an exception after SHORT_TIMEOUT seconds:

      for _ in support.sleeping_retry(support.SHORT_TIMEOUT):
          if check():
              break

   Example of error=False usage:

      for _ in support.sleeping_retry(support.SHORT_TIMEOUT, error=False):
          if check():
              break
      else:
          raise RuntimeError('my custom error')

test.support.is_resource_enabled(resource)

   Retorna "True" si *resource* está habilitado y disponible. La lista
   de recursos disponibles solo se establece cuando "test.regrtest"
   está ejecutando las pruebas.

test.support.get_resource_value(resource)

   Return the value specified for *resource* (as "-u
   *resource*=*value*"). Return "None" if *resource* is disabled or no
   value is specified.

test.support.python_is_optimized()

   Retorna "True" si Python no fue construido con "-O0" o "-Og".

test.support.with_pymalloc()

   Return "_testcapi.WITH_PYMALLOC".

test.support.requires(resource, msg=None)

   Lanza "ResourceDenied" si *resource* no está disponible. *msg* es
   el argumento para "ResourceDenied" si se lanza. Siempre retorna
   "True" si es invocado por una función cuyo "__name__" es
   "'__main__'". Se usa cuando se ejecutan pruebas por
   "test.regrtest".

test.support.sortdict(dict)

   Retorna una representación del *diccionario* con las claves
   ordenadas.

test.support.findfile(filename, subdir=None)

   Retorna la ruta al archivo llamado *filename*. Si no se encuentra
   ninguna coincidencia, se retorna *filename*. Esto no equivale a un
   fallo, ya que podría ser la ruta al archivo.

   La configuración *subdir* indica una ruta relativa a utilizar para
   encontrar el archivo en lugar de buscar directamente en los
   directorios de ruta.

test.support.get_pagesize()

   Get size of a page in bytes.

   Added in version 3.12.

test.support.setswitchinterval(interval)

   Establecido "sys.setswitchinterval()" en el *intervalo* dado.
   Define un intervalo mínimo para los sistemas Android para evitar
   que el sistema se cuelgue.

test.support.check_impl_detail(**guards)

   Use esta verificación para proteger las pruebas específicas de
   implementación de CPython o para ejecutarlas solo en las
   implementaciones protegidas por los argumentos. Esta función
   retorna "True" o "False" según la plataforma del host. Ejemplo de
   uso:

      check_impl_detail()               # Only on CPython (default).
      check_impl_detail(jython=True)    # Only on Jython.
      check_impl_detail(cpython=False)  # Everywhere except CPython.

test.support.set_memlimit(limit)

   Establece los valores para "max_memuse" y "real_max_memuse" para
   pruebas de memoria grande.

test.support.record_original_stdout(stdout)

   Almacene el valor de *stdout*. Está destinado a mantener el
   *stdout* en el momento en que comenzó el regrtest.

test.support.get_original_stdout()

   Retorna el *stdout* original establecido por
   "record_original_stdout()" o "sys.stdout" si no está configurado.

test.support.args_from_interpreter_flags()

   Retorna una lista de argumentos de línea de comandos que reproducen
   la configuración actual en "sys.flags" y "sys.warnoptions".

test.support.optim_args_from_interpreter_flags()

   Retorna una lista de argumentos de línea de comandos que reproducen
   la configuración de optimización actual en "sys.flags".

test.support.captured_stdin()
test.support.captured_stdout()
test.support.captured_stderr()

   Un administrador de contexto que reemplaza temporalmente la
   secuencia nombrada con un objeto "io.StringIO".

   Ejemplo de uso con flujos de salida:

      with captured_stdout() as stdout, captured_stderr() as stderr:
          print("hello")
          print("error", file=sys.stderr)
      assert stdout.getvalue() == "hello\n"
      assert stderr.getvalue() == "error\n"

   Ejemplo de uso con flujo de entrada:

      with captured_stdin() as stdin:
          stdin.write('hello\n')
          stdin.seek(0)
          # call test code that consumes from sys.stdin
          captured = input()
      self.assertEqual(captured, "hello")

test.support.disable_faulthandler()

   Un administrador de contexto que deshabilita temporalmente
   "faulthandler".

test.support.gc_collect()

   Se fuerza la mayor cantidad posible de objetos para ser
   recolectados. Esto es necesario porque el recolector de basura no
   garantiza la desasignación oportuna. Esto significa que los métodos
   "__del__" pueden llamarse más tarde de lo esperado y las
   referencias débiles pueden permanecer vivas por más tiempo de lo
   esperado.

test.support.disable_gc()

   Un administrador de contexto que deshabilita el recolector de
   basura al entrar. Al salir, el recolector de basura se restaura a
   su estado anterior.

test.support.swap_attr(obj, attr, new_val)

   Administrador de contexto para intercambiar un atributo con un
   nuevo objeto.

   Uso:

      with swap_attr(obj, "attr", 5):
          ...

   Esto establecerá "obj.attr" en 5 durante la duración del bloque
   "with", restaurando el valor anterior al final del bloque. Si
   "attr" no existe en "obj", se creará y luego se eliminará al final
   del bloque.

   El valor anterior (o "None" si no existe) se asignará al objetivo
   de la cláusula "como", si existe.

test.support.swap_item(obj, attr, new_val)

   Administrador de contexto para intercambiar un elemento con un
   nuevo objeto.

   Uso:

      with swap_item(obj, "item", 5):
          ...

   Esto establecerá "obj ["item"]" a 5 durante la duración del bloque
   "with", restaurando el valor anterior al final del bloque. Si
   "item" no existe en "obj", se creará y luego se eliminará al final
   del bloque.

   El valor anterior (o "None" si no existe) se asignará al objetivo
   de la cláusula "como", si existe.

test.support.flush_std_streams()

   Llama al método "flush()" en "sys.stdout" y luego en "sys.stderr".
   Se puede usar para asegurarse de que el orden de los registros sea
   consistente antes de escribir en stderr.

   Added in version 3.11.

test.support.print_warning(msg)

   Imprime una advertencia en "sys.__stderr__". Formatea el mensaje
   como: "f "Warning -- {msg}"". Si *msg* se compone de varias líneas,
   añade el prefijo ""Warning --"" a cada línea.

   Added in version 3.9.

test.support.wait_process(pid, *, exitcode, timeout=None)

   Espere hasta que el proceso *pid* termine y comprobará que el
   código de salida del proceso es *exitcode*.

   Lanza un "AssertionError" si el código de salida del proceso no es
   igual a *exitcode*.

   Si el proceso se ejecuta durante más tiempo que *timeout* en
   segundos ("SHORT_TIMEOUT" por defecto), mata el proceso y lanza un
   "AssertionError". La función de tiempo de espera no está disponible
   en Windows.

   Added in version 3.9.

test.support.calcobjsize(fmt)

   Retorna el tamaño del "PyObject" cuyos miembros de estructura están
   definidos por *fmt*. El valor retornado incluye el tamaño del
   encabezado y la alineación del objeto de Python.

test.support.calcvobjsize(fmt)

   Retorna el tamaño del "PyVarObject" cuyos miembros de estructura
   están definidos por *fmt*. El valor retornado incluye el tamaño del
   encabezado y la alineación del objeto de Python.

test.support.checksizeof(test, o, size)

   Para el caso de prueba (*testcase*), se aserciona que el
   "sys.getsizeof" para *o* más el tamaño del encabezado *GC* es igual
   a *size*.

@test.support.anticipate_failure(condition)

   A decorator to conditionally mark tests with
   "@unittest.expectedFailure". Any use of this decorator should have
   an associated comment identifying the relevant tracker issue.

test.support.system_must_validate_cert(f)

   Un decorador que se salta la prueba decorada en los errores de
   validación de la certificación TLS.

@test.support.run_with_locale(catstr, *locales)

   Un decorador para ejecutar una función en una configuración
   regional diferente, restableciéndola correctamente una vez que ha
   finalizado. *catstr* es la categoría de configuración regional como
   una cadena (por ejemplo, ""LC_ALL""). Las *locales* aprobadas se
   probarán secuencialmente y se utilizará la primera configuración
   regional válida.

@test.support.run_with_tz(tz)

   Un decorador para ejecutar una función en una zona horaria
   específica, restableciéndola correctamente una vez que haya
   finalizado.

@test.support.requires_freebsd_version(*min_version)

   Decorador para la versión mínima cuando se ejecuta la prueba en
   FreeBSD. Si la versión de FreeBSD es inferior a la mínima, se salta
   la prueba.

@test.support.requires_linux_version(*min_version)

   Decorador para la versión mínima cuando se ejecuta la prueba en
   Linux. Si la versión de Linux es inferior a la mínima, se omite la
   prueba.

@test.support.requires_mac_version(*min_version)

   Decorador para la versión mínima cuando se ejecuta la prueba en
   macOS. Si la versión de macOS es inferior a la mínima, se omite la
   prueba.

@test.support.requires_gil_enabled

   Decorator for skipping tests on the free-threaded build.  If the
   *GIL* is disabled, the test is skipped.

@test.support.requires_IEEE_754

   Decorador para omitir pruebas en plataformas que no son *IEEE 754*.

@test.support.requires_zlib

   Decorador para omitir pruebas si "zlib" no existe.

@test.support.requires_gzip

   Decorador para omitir pruebas si "gzip" no existe.

@test.support.requires_bz2

   Decorador para omitir pruebas si "bz2" no existe.

@test.support.requires_lzma

   Decorador para omitir pruebas si "lzma" no existe.

@test.support.requires_resource(resource)

   Decorador para omitir pruebas si *resource* no está disponible.

@test.support.requires_docstrings

   Decorador para ejecutar solo la prueba si "HAVE_DOCSTRINGS".

@test.support.requires_limited_api

   Decorator for only running the test if Limited C API is available.

@test.support.cpython_only

   Decorador para pruebas solo aplicable a CPython.

@test.support.impl_detail(msg=None, **guards)

   Decorador para invocar "check_impl_detail()" en *guards*. Si eso
   retorna "False", entonces usa *msg* como la razón para omitir la
   prueba.

@test.support.thread_unsafe(reason=None)

   Decorator for marking tests as thread-unsafe.  This test always
   runs in one thread even when invoked with "--parallel-threads".

@test.support.no_tracing

   Decorador para desactivar temporalmente el seguimiento durante la
   duración de la prueba.

@test.support.refcount_test

   Decorador para pruebas que implican conteo de referencias. El
   decorador no ejecuta la prueba si CPython no la ejecuta. Cualquier
   función de rastreo no se establece durante la duración de la prueba
   para evitar conteos de referencia(*refcounts*) inesperados causados
   por la función de rastreo.

@test.support.bigmemtest(size, memuse, dry_run=True)

   Decorador para pruebas *bigmem*.

   *size* es un tamaño solicitado para la prueba (en unidades
   arbitrarias interpretadas por la prueba). *memuse* es el número de
   bytes por unidad para la prueba, o una buena estimación de la
   misma. Por ejemplo, una prueba que necesita dos búfers de byte, de
   4 *GiB* cada uno, podría decorarse con "@bigmemtest(size=_4G,
   memuse=2)".

   El argumento *size* normalmente se pasa al método de prueba
   decorado como un argumento adicional. Si *dry_run* es "True", el
   valor pasado al método de prueba puede ser menor que el valor
   solicitado. Si *dry_run* es "False", significa que la prueba no
   admite ejecuciones ficticias cuando no se especifica "-M".

@test.support.bigaddrspacetest

   Decorador para pruebas que llenan el espacio de direcciones.

test.support.linked_to_musl()

   Return "False" if there is no evidence the interpreter was compiled
   with "musl", otherwise return a version triple, either "(0, 0, 0)"
   if the version is unknown, or the actual version if it is known.
   Intended for use in "skip" decorators.  "emscripten" and "wasi" are
   assumed to be compiled with "musl"; otherwise "platform.libc_ver"
   is checked.

test.support.check_syntax_error(testcase, statement, errtext='', *, lineno=None, offset=None)

   Prueba los errores de sintaxis en *statement* intentando compilar
   *statement*. *testcase* es la instancia "unittest" para la prueba.
   *errtext* es la expresión regular que debe coincidir con la
   representación de cadena de caracteres que es lanza en
   "SyntaxError". Si *lineno* no es "None", se compara con la línea de
   la excepción. Si *offset* no es "None", se compara con el
   desplazamiento de la excepción.

test.support.open_urlresource(url, *args, **kw)

   Abre *url*. Si la apertura falla, se lanza "TestFailed".

test.support.reap_children()

   Se utiliza esto al final de "test_main" siempre que se inicien
   subprocesos. Esto ayudará a garantizar que ningún proceso hijo
   adicional (zombies) se quede para acumular recursos y crear
   problemas al buscar refleaks.

test.support.get_attribute(obj, name)

   Obtiene un atributo, lanzando "unittest.SkipTest" si
   "AttributeError" está activado.

test.support.catch_unraisable_exception()

   El administrador de contexto detectando excepciones imposibles de
   evaluar usando "sys.unraisablehook()".

   El almacenamiento del valor de excepción
   ("cm.unraisable.exc_value") crea un ciclo de referencia. El ciclo
   de referencia se interrumpe explícitamente cuando sale el
   administrador de contexto.

   El almacenamiento del objeto ("cm.unraisable.object") puede
   resucitarlo si se establece en un objeto que se está finalizando.
   Salir del administrador de contexto borra el objeto almacenado.

   Uso:

      with support.catch_unraisable_exception() as cm:
          # code creating an "unraisable exception"
          ...

          # check the unraisable exception: use cm.unraisable
          ...

      # cm.unraisable attribute no longer exists at this point
      # (to break a reference cycle)

   Added in version 3.8.

test.support.load_package_tests(pkg_dir, loader, standard_tests, pattern)

   La implementación genérica del protocolo "unittest" "load_tests"
   para usar en paquetes de prueba. *pkg_dir* es el directorio raíz
   del paquete; *loader*, *standard_tests* y *pattern* son los
   argumentos esperados por "load_tests". En casos simples, el paquete
   de prueba "__init __. Py" puede ser el siguiente:

      import os
      from test.support import load_package_tests

      def load_tests(*args):
          return load_package_tests(os.path.dirname(__file__), *args)

test.support.detect_api_mismatch(ref_api, other_api, *, ignore=())

   Retorna el conjunto de atributos, funciones o métodos de *ref_api*
   que no se encuentra en *other_api *, excepto por una lista definida
   de elementos que se ignorarán en esta comprobación especificada en
   *ignore*.

   De forma predeterminada, omite los atributos privados que comienzan
   con '_' pero incluye todos los métodos mágicos, es decir, los que
   comienzan y terminan en '__'.

   Added in version 3.5.

test.support.patch(test_instance, object_to_patch, attr_name, new_value)

   Se anula *object_to_patch.attr_name* con *new_value*. Se agrega
   también el procedimiento de limpieza a *test_instance* para
   restaurar *object_to_patch* para *attr_name*. *Attr_name* debe ser
   un atributo válido para *object_to_patch*.

test.support.run_in_subinterp(code)

   Ejecuta *code* en el subinterpretador. Lanza "unittest.SkipTest" si
   "tracemalloc" está habilitado.

@test.support.isolation.runInSubprocess

   Decorator that runs the decorated test in a fresh interpreter
   subprocess, in isolation, so that it does not share global or
   interpreter state with the rest of the test run.  It can decorate a
   test method or a whole "TestCase" subclass.  Decorated methods must
   take no extra arguments.  A failure, error or skip in the
   subprocess is reported for the corresponding test, and individual
   "subtests" that fail or are skipped are reported individually.  A
   reported failure or error shows the original subprocess traceback
   as the cause of the exception.

   When a **method** is decorated, only that method runs in a
   subprocess; all fixtures ("setUp()" / "tearDown()", "setUpClass()"
   / "tearDownClass()" and "setUpModule()" / "tearDownModule()") run
   both in the parent process (as usual) and in the subprocess around
   the method.

   When a **class** is decorated, the whole class runs in a single
   subprocess, and "setUpClass()", "tearDownClass()", "setUp()" and
   "tearDown()" run once each in the subprocess and are skipped in the
   parent process.  A failure or skip of "setUpClass()" in the
   subprocess is reported for the whole class.  "setUpModule()" cannot
   be controlled by a class decorator, so it still runs in the parent
   process too; test it with "runningInSubprocess" if needed.

   The subprocess inherits the enabled resources ("-u"), memory limit
   ("-M") and verbosity ("-v") of the parent test run, so that
   "requires_resource()", "requires()", "bigmemtest()" and the like
   behave consistently in both processes.

   The test is skipped on platforms without subprocess support.

test.support.isolation.runningInSubprocess

   "True" while the code runs in the isolated subprocess spawned by
   "runInSubprocess()", and "False" otherwise (including in the parent
   process and in a normal, non-isolated test run).  Fixtures such as
   "setUp()", "tearDown()", "setUpClass()", "tearDownClass()",
   "setUpModule()" and "tearDownModule()" can test it to choose which
   code to run in the subprocess.

test.support.check_free_after_iterating(test, iter, cls, args=())

   Las instancias de aserción de *cls* se desalojan después de la
   iteración.

test.support.missing_compiler_executable(cmd_names=[])

   Verifica la existencia de los ejecutables del compilador cuyos
   nombres figuran en *cmd_names* o todos los ejecutables del
   compilador cuando *cmd_names* está vacío y retorna el primer
   ejecutable faltante o "None" cuando no se encuentra ninguno.

test.support.check__all__(test_case, module, name_of_module=None, extra=(), not_exported=())

   Aserciona que la variable "_all__" de *module* contiene todos los
   nombres públicos.

   Los nombres públicos del módulo (su API) se detectan
   automáticamente en función de si coinciden con la convención de
   nombres públicos y se definieron en *module*.

   El argumento *name_of_module* puede especificar (como una cadena o
   tupla del mismo) qué módulo(s) se podría definir una API para ser
   detectada como una API pública. Un caso para esto es cuando
   *module* importa parte de su API pública desde otros módulos,
   posiblemente un *backend de C* (como "csv" y su "_csv").

   The *extra* argument can be a set of names that wouldn't otherwise
   be automatically detected as "public", like objects without a
   proper "__module__" attribute. If provided, it will be added to the
   automatically detected ones.

   El argumento *not_exported* puede ser un conjunto de nombres que no
   deben tratarse como parte de la API pública aunque sus nombres
   indiquen lo contrario.

   Ejemplo de uso:

      import bar
      import foo
      import unittest
      from test import support

      class MiscTestCase(unittest.TestCase):
          def test__all__(self):
              support.check__all__(self, foo)

      class OtherTestCase(unittest.TestCase):
          def test__all__(self):
              extra = {'BAR_CONST', 'FOO_CONST'}
              not_exported = {'baz'}  # Undocumented name.
              # bar imports part of its API from _bar.
              support.check__all__(self, bar, ('bar', '_bar'),
                                   extra=extra, not_exported=not_exported)

   Added in version 3.6.

test.support.skip_if_broken_multiprocessing_synchronize()

   Omite las pruebas si el módulo no se encuentra al
   "multiprocessing.synchronize", si no hay una implementación de
   semáforo disponible, o si crear un *lock* lanza un "OSError".

   Added in version 3.10.

test.support.check_disallow_instantiation(test_case, tp, *args, **kwds)

   Se aserciona que el tipo *tp* no pueda ser instanciado usando
   *args* y *kwds*.

   Added in version 3.10.

test.support.adjust_int_max_str_digits(max_digits)

   Esta función devuelve un administrador de contexto que cambiará la
   configuración global de "sys.set_int_max_str_digits()" durante la
   duración del contexto para permitir la ejecución de código de
   prueba que necesita un límite diferente en la cantidad de dígitos
   al convertir entre un número entero y una cadena.

   Added in version 3.11.

The "test.support" module defines the following classes:

class test.support.SuppressCrashReport

   Un administrador de contexto suele intentar evitar ventanas
   emergentes de diálogo de bloqueo en las pruebas que se espera que
   bloqueen un subproceso.

   En Windows, deshabilita los cuadros de diálogo de Informe de
   errores de Windows usando SetErrorMode.

   On UNIX, "resource.setrlimit()" is used to set
   "resource.RLIMIT_CORE"'s soft limit to 0 to prevent coredump file
   creation.

   On both platforms, the old value is restored by "__exit__()".

class test.support.SaveSignals

   Clase para guardar y restaurar manejadores (*handlers*) de señal
   registrados por el manejador de señal Python.

   save(self)

      Guarda los controladores de señales en un diccionario que asigna
      números de señales al controlador de señales actual.

   restore(self)

      Establece los números de señal del diccionario "save()" en el
      controlador guardado.

class test.support.Matcher

   matches(self, d, **kwargs)

      Intenta hacer coincidir una sola sentencia con los argumentos
      proporcionados.

   match_value(self, k, dv, v)

      Intenta hacer coincidir un único valor almacenado (*dv*) con un
      valor proporcionado (*v*).

# "test.support.socket_helper" --- Utilities for socket tests

The "test.support.socket_helper" module provides support for socket
tests.

Added in version 3.9.

test.support.socket_helper.IPV6_ENABLED

   Se establece como "True" si IPv6 está habilitado en este host,
   "False" en caso contrario.

test.support.socket_helper.find_unused_port(family=socket.AF_INET, socktype=socket.SOCK_STREAM)

   Retorna un puerto no utilizado que debería ser adecuado para el
   enlace. Esto se logra creando un *socket* temporal con la misma
   familia y tipo que el parámetro "sock" (el valor predeterminado es
   "AF_INET", "SOCK_STREAM") y vinculándolo a la dirección de host
   especificada (por defecto es "0.0.0.0") con el puerto establecido
   en 0, provocando un puerto efímero no utilizado del sistema
   operativo. El *socket* temporal se cierra y se elimina, y se
   retorna el puerto efímero.

   Este método o "bind_port()" debe usarse para cualquier prueba en la
   que un *socket* del servidor deba estar vinculado a un puerto en
   particular durante la duración de la prueba. Cuál usar depende de
   si el código de llamada está creando un *socket* Python, o si un
   puerto no utilizado debe proporcionarse en un constructor o pasar a
   un programa externo (es decir, el argumento "-accept" al modo
   *s_server de openssl*). Siempre es preferible "bind_port()" sobre
   "find_unused_port()" donde sea posible. Se desaconseja el uso de un
   puerto codificado ya que puede hacer que varias instancias de la
   prueba sean imposibles de ejecutar simultáneamente, lo cual es un
   problema para los *buildbots*.

test.support.socket_helper.bind_port(sock, host=HOST)

   Se enlaza el *socket* a un puerto libre y retorna el número de
   puerto. Se basa en puertos efímeros para garantizar que estemos
   utilizando un puerto independiente. Esto es importante ya que
   muchas pruebas pueden ejecutarse simultáneamente, especialmente en
   un entorno *buildbot*. Este método lanza una excepción si
   "sock.family" es "AF_INET" y "sock.type" es "SOCK_STREAM", y el
   *socket* tiene "SO_REUSEADDR" o "SO_REUSEPORT" establecido en él.
   Las pruebas nunca deben configurar estas opciones de *socket* para
   los *sockets TCP/IP*. El único caso para configurar estas opciones
   es probar la multidifusión (*multicasting*) a través de múltiples
   *sockets UDP*.

   Además, si la opción de *socket* "SO_EXCLUSIVEADDRUSE" está
   disponible (es decir, en Windows), se establecerá en el *socket*.
   Esto evitará que otras personas se vinculen a nuestro host/puerto
   mientras dure la prueba.

test.support.socket_helper.bind_unix_socket(sock, addr)

   Enlaza un socket Unix, lanzando "unittest.SkipTest" si se lanza
   "PermissionError".

@test.support.socket_helper.skip_unless_bind_unix_socket

   Un decorador para ejecutar pruebas que requieren un
   enlace("bind()") funcional para sockets en sistemas Unix.

test.support.socket_helper.transient_internet(resource_name, *, timeout=30.0, errnos=())

   Un gestor de contexto que lanza "ResourceDenied" cuando varios
   problemas con la conexión a Internet se manifiestan como
   excepciones.

# "test.support.script_helper" --- Utilities for the Python execution tests

The "test.support.script_helper" module provides support for Python's
script execution tests.

test.support.script_helper.interpreter_requires_environment()

   Retorna "True" si el "sys.executable interpreter" requiere
   variables de entorno para poder ejecutarse.

   Esto está diseñado para usarse con "@unittest.skipIf()" para anotar
   pruebas que necesitan usar una función "assert_python*()" para
   iniciar un modo aislado ("-I") o sin entorno proceso de
   subinterpretador de modo ("-E").

   Una compilación y prueba normal no se encuentra en esta situación,
   pero puede suceder cuando se intenta ejecutar el conjunto de
   pruebas de biblioteca estándar desde un intérprete que no tiene un
   directorio principal obvio con la lógica de búsqueda de directorio
   principal actual de Python.

   La configuración "PYTHONHOME" es una forma de hacer que la mayoría
   del *testuite* se ejecute en esa situación. "PYTHONPATH" o
   "PYTHONUSERSITE" son otras variables de entorno comunes que pueden
   afectar si el intérprete puede o no comenzar.

test.support.script_helper.run_python_until_end(*args, **env_vars)

   Configura el entorno basado en *env_vars* para ejecutar el
   intérprete en un subproceso. Los valores pueden incluir
   "__isolated", "__cleanenv", "__cwd" y "TERM".

   Distinto en la versión 3.9: La función ya no elimina los espacios
   en blanco de *stderr*.

test.support.script_helper.assert_python_ok(*args, **env_vars)

   Aserción de que ejecutar el intérprete con *arg* y variables de
   entorno opcionales *env_vars* tiene éxito ("rc == 0") y retorna una
   tupla "(código de retorno, stdout, stderr)".

   Si se establece el parámetro de solo palabra clave *__cleanenv*,
   *env_vars* se usa como un entorno nuevo.

   Python se inicia en modo aislado (opción de línea de comando "-I"),
   excepto si el parámetro de solo palabra clave *__isolated* se
   establece en "False".

   Distinto en la versión 3.9: La función ya no elimina los espacios
   en blanco de *stderr*.

test.support.script_helper.assert_python_failure(*args, **env_vars)

   Aserciona que la ejecución del intérprete con *args* y variables de
   entorno opcionales *env_vars* falla ("rc! = 0") y retorna una tupla
   "(return code, stdout, stderr)".

   Consulte "assert_python_ok()" para más opciones.

   Distinto en la versión 3.9: La función ya no elimina los espacios
   en blanco de *stderr*.

test.support.script_helper.spawn_python(*args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, **kw)

   Ejecuta un subproceso de Python con los argumentos dados.

   *kw* es un argumento adicional de palabras clave para pasar a
   "subprocess.Popen()". Retorna un objeto a "subprocess.Popen".

test.support.script_helper.kill_python(p)

   Ejecuta el proceso dado "subprocess.Popen" hasta que finalice y
   retorne *stdout*.

test.support.script_helper.make_script(script_dir, script_basename, source, omit_suffix=False)

   Crea un script que contiene *source* en la ruta *script_dir* y
   *script_basename*. Si *omit_suffix* es "False", agregue ".py" al
   nombre. Retorna la ruta completa del script.

test.support.script_helper.make_zip_script(zip_dir, zip_basename, script_name, name_in_zip=None)

   Crea un archivo zip en *zip_dir* y *zip_basename* con la extensión
   "zip" que contiene los archivos en *script_name*. *name_in_zip* es
   el nombre del archivo. Retorna una tupla que contiene "(ruta
   completa, ruta completa del nombre del archivo)".

test.support.script_helper.make_pkg(pkg_dir, init_source='')

   Crea un directorio llamado *pkg_dir* que contiene un archivo
   "__init__" con *init_source* como su contenido.

test.support.script_helper.make_zip_pkg(zip_dir, zip_basename, pkg_name, script_basename, source, depth=1, compiled=False)

   Crea un directorio de paquete zip con una ruta de *zip_dir* y
   *zip_basename* que contiene un archivo "__init__" vacío y un
   archivo *script_basename* que contiene el *source*. Si *compilado*
   es "True", ambos archivos fuente se compilarán y se agregarán al
   paquete zip. Retorna una tupla de la ruta zip completa y el nombre
   de archivo para el archivo zip.

# "test.support.bytecode_helper" --- Support tools for testing correct bytecode generation

The "test.support.bytecode_helper" module provides support for testing
and inspecting bytecode generation.

Added in version 3.9.

El módulo define la siguiente clase:

class test.support.bytecode_helper.BytecodeTestCase(unittest.TestCase)

   Esta clase tiene métodos de aserción personalizados para
   inspeccionar el código de bytes.

BytecodeTestCase.get_disassembly_as_string(co)

   Retorna el desensamblaje de *co* como cadena.

BytecodeTestCase.assertInBytecode(x, opname, argval=_UNSPECIFIED)

   Retorna instr si se encuentra *opname*, de lo contrario lanza
   "AssertionError".

BytecodeTestCase.assertNotInBytecode(x, opname, argval=_UNSPECIFIED)

   Lanza "AssertionError" si se encuentra *opname*.

# "test.support.threading_helper" --- Utilities for threading tests

The "test.support.threading_helper" module provides support for
threading tests.

Added in version 3.10.

test.support.threading_helper.join_thread(thread, timeout=None)

   Se une un *thread* dentro de *timeout*. Lanza un "AssertionError"
   si el hilo sigue vivo después de unos segundos de *timeout*.

@test.support.threading_helper.reap_threads

   Decorador para garantizar que los hilos se limpien incluso si la
   prueba falla.

test.support.threading_helper.start_threads(threads, unlock=None)

   Administrador de contexto para iniciar *threads*, que es una
   secuencia de subprocesos. *unlock* es una función a la que se llama
   después de que se inician los subprocesos, incluso si se generó una
   excepción; un ejemplo sería "threading.Event.set()".
   "start_threads" intentará unirse a los subprocesos iniciados al
   salir.

test.support.threading_helper.threading_cleanup(*original_values)

   Se limpia los hilos no especificados en *original_values*. Diseñado
   para emitir una advertencia si una prueba deja hilos en ejecución
   en segundo plano.

test.support.threading_helper.threading_setup()

   Retorna el recuento del hilo actual y copia de subprocesos
   colgantes.

test.support.threading_helper.wait_threads_exit(timeout=None)

   El administrador de contexto debe esperar hasta que salgan todos
   los hilos creados en la declaración "with".

test.support.threading_helper.catch_threading_exception()

   El administrador de contexto captura "threading.Thread" excepción
   usando "threading.excepthook()".

   Atributos establecidos cuando se captura una excepción:

   * "exc_type"

   * "exc_value"

   * "exc_traceback"

   * "thread"

   Consulte la documentación para "threading.excepthook()".

   Estos atributos se eliminan en la salida del administrador de
   contexto.

   Uso:

      with threading_helper.catch_threading_exception() as cm:
          # code spawning a thread which raises an exception
          ...

          # check the thread exception, use cm attributes:
          # exc_type, exc_value, exc_traceback, thread
          ...

      # exc_type, exc_value, exc_traceback, thread attributes of cm no longer
      # exists at this point
      # (to avoid reference cycles)

   Added in version 3.8.

test.support.threading_helper.run_concurrently(worker_func, nthreads, args=(), kwargs={})

   Run the worker function concurrently in multiple threads. Re-raises
   an exception if any thread raises one, after all threads have
   finished.

# "test.support.os_helper" --- Utilities for os tests

The "test.support.os_helper" module provides support for os tests.

Added in version 3.10.

test.support.os_helper.FS_NONASCII

   Un carácter no codificable ASCII codificable por "os.fsencode()".

test.support.os_helper.SAVEDCWD

   Establecido "os.getcwd()".

test.support.os_helper.TESTFN

   Establecido a un nombre que sea seguro de usar como nombre de un
   archivo temporal. Cualquier archivo temporal que se cree debe
   cerrarse y desvincularse (eliminarse).

test.support.os_helper.TESTFN_NONASCII

   Establecido en un nombre de archivo que contiene el carácter
   "FS_NONASCII", si existe. Esto garantiza que, si existe el nombre
   de archivo, se puede codificar y decodificar con la codificación
   predeterminada del sistema de archivos. Esto permite omitir
   fácilmente las pruebas que requieren un nombre de archivo que no
   sea ASCII en plataformas donde no pueden funcionar.

test.support.os_helper.TESTFN_UNENCODABLE

   Establecido un nombre de archivo (tipo *str*) que no se pueda
   codificar mediante la codificación del sistema de archivos en modo
   estricto. Puede ser "None" si no es posible generar dicho nombre de
   archivo.

test.support.os_helper.TESTFN_UNDECODABLE

   Establecido un nombre de archivo (tipo de bytes) que no pueda
   descodificarse mediante la codificación del sistema de archivos en
   modo estricto. Puede ser "None" si no es posible generar dicho
   nombre de archivo.

test.support.os_helper.TESTFN_UNICODE

   Establecido un nombre que no sea ASCII para un archivo temporal.

class test.support.os_helper.EnvironmentVarGuard

   Clase utilizada para establecer o deshabilitar temporalmente las
   variables de entorno. Las instancias se pueden usar como un
   administrador de contexto y tienen una interfaz de diccionario
   completa para consultar/modificar el "os.environ" subyacente.
   Después de salir del administrador de contexto, todos los cambios
   en las variables de entorno realizados a través de esta instancia
   se revertirán.

   Distinto en la versión 3.1: Añadido una interfaz de diccionario.

class test.support.os_helper.FakePath(path)

   Simple *path-like object*.  It implements the "__fspath__()" method
   which just returns the *path* argument.  If *path* is an exception,
   it will be raised in "__fspath__()".

EnvironmentVarGuard.set(envvar, value)

   Se establece temporalmente la variable de entorno "envvar" en el
   valor de "value".

EnvironmentVarGuard.unset(envvar, *others)

   Temporarily unset one or more environment variables.

   Distinto en la versión 3.14: More than one environment variable can
   be unset.

test.support.os_helper.can_symlink()

   Retorna "True" si el sistema operativo admite links simbólicos, de
   lo contrario "False".

test.support.os_helper.can_xattr()

   Retorna "True" si el sistema operativo admite *xattr*, de lo
   contrario "False".

test.support.os_helper.change_cwd(path, quiet=False)

   Un administrador de contexto que cambia temporalmente el directorio
   de trabajo actual a *path* y produce el directorio.

   Si *quiet* es "False", el administrador de contexto lanza una
   excepción en caso de error. De lo contrario, solo emite una
   advertencia y mantiene el directorio de trabajo actual igual.

test.support.os_helper.create_empty_file(filename)

   Crea un archivo vacío con *filename*. Si ya existe, truncarlo.

test.support.os_helper.fd_count()

   Cuenta el número de descriptores de archivo abiertos.

test.support.os_helper.fs_is_case_insensitive(directory)

   Retorna "True" si el sistema de archivos para *directory* no
   distingue entre mayúsculas y minúsculas.

test.support.os_helper.make_bad_fd()

   Se crea un descriptor de archivo no válido abriendo y cerrando un
   archivo temporal y retornando su descriptor.

test.support.os_helper.rmdir(filename)

   Llama a "os.rmdir()" en *filename*. En las plataformas Windows,
   esto se envuelve con un ciclo de espera que verifica la existencia
   del archivo, que es necesario debido a los programas antivirus que
   pueden mantener los archivos abiertos y evitar que se eliminen.

test.support.os_helper.rmtree(path)

   Llama a "shutil.rmtree()" en *path* o llama a "os.lstat()" y
   "os.rmdir()" para eliminar una ruta y su contenido. Al igual que
   con "rmdir()", en las plataformas de Windows esto se envuelve con
   un ciclo de espera que verifica la existencia de los archivos.

@test.support.os_helper.skip_unless_symlink

   Un decorador para ejecutar pruebas que requieren soporte para
   enlaces simbólicos.

@test.support.os_helper.skip_unless_xattr

   Un decorador para ejecutar pruebas que requieren soporte para
   *xattr*.

test.support.os_helper.temp_cwd(name='tempcwd', quiet=False)

   Un administrador de contexto que crea temporalmente un nuevo
   directorio y cambia el directorio de trabajo actual (*CWD*).

   El administrador de contexto crea un directorio temporal en el
   directorio actual con el nombre *name* antes de cambiar
   temporalmente el directorio de trabajo actual. Si *name* es "None"
   , el directorio temporal se crea usando "tempfile.mkdtemp()".

   Si *quiet* es "False" y no es posible crear o cambiar el *CWD*, se
   lanza un error. De lo contrario, solo se lanza una advertencia y se
   utiliza el *CWD* original.

test.support.os_helper.temp_dir(path=None, quiet=False)

   Un administrador de contexto que crea un directorio temporal en
   *path* y produce el directorio.

   Si *path* es "None", el directorio temporal se crea usando
   "tempfile.mkdtemp()". Si *quiet* es "False", el administrador de
   contexto lanza una excepción en caso de error. De lo contrario, si
   se especifica *path* y no se puede crear, solo se emite una
   advertencia.

test.support.os_helper.temp_umask(umask)

   Un administrador de contexto que establece temporalmente el proceso
   *umask*.

test.support.os_helper.unlink(filename)

   Llama a "os.unlink()" en *filename*. Al igual que con "rmdir()", en
   las plataformas Windows, esto se envuelve con un ciclo de espera
   que verifica la existencia del archivo.

# "test.support.import_helper" --- Utilities for import tests

The "test.support.import_helper" module provides support for import
tests.

Added in version 3.10.

test.support.import_helper.forget(module_name)

   Elimina el módulo llamado *module_name* de "sys.modules" y elimina
   los archivos compilados por bytes del módulo.

test.support.import_helper.import_fresh_module(name, fresh=(), blocked=(), deprecated=False)

   Esta función importa y retorna una copia nueva del módulo Python
   nombrado eliminando el módulo nombrado de "sys.modules" antes de
   realizar la importación. Tenga en cuenta que a diferencia de
   "reload()", el módulo original no se ve afectado por esta
   operación.

   *fresh* es un iterable de nombres de módulos adicionales que
   también se eliminan del caché "sys.modules" antes de realizar la
   importación.

   *bloqueado* es un iterable de nombres de módulos que se reemplazan
   con "None" en la memoria caché del módulo durante la importación
   para garantizar que los intentos de importarlos generen
   "ImportError".

   El módulo nombrado y los módulos nombrados en los parámetros
   *fresh* y *bloqueado* se guardan antes de comenzar la importación y
   luego se vuelven a insertar en "sys.modules" cuando se completa la
   importación fresca.

   Los mensajes de deprecación de módulos y paquetes se suprimen
   durante esta importación si *deprecated* es "True".

   Esta función lanzará "ImportError" si el módulo nombrado no puede
   importarse.

   Ejemplo de uso:

      # Get copies of the warnings module for testing without affecting the
      # version being used by the rest of the test suite. One copy uses the
      # C implementation, the other is forced to use the pure Python fallback
      # implementation
      py_warnings = import_fresh_module('warnings', blocked=['_warnings'])
      c_warnings = import_fresh_module('warnings', fresh=['_warnings'])

   Added in version 3.1.

test.support.import_helper.import_module(name, deprecated=False, *, required_on=())

   Esta función importa y retorna el módulo nombrado. A diferencia de
   una importación normal, esta función lanza "unittest.SkipTest" si
   el módulo no se puede importar.

   Los mensajes de deprecación de módulos y paquetes se suprimen
   durante esta importación si *deprecated* es "True". Si se requiere
   un módulo en una plataforma pero es opcional para otros, establezca
   *required_on* en un iterable de prefijos de plataforma que se
   compararán con "sys.platform".

   Added in version 3.1.

test.support.import_helper.modules_setup()

   Retorna una copia de "sys.modules".

test.support.import_helper.modules_cleanup(oldmodules)

   Elimina los módulos a excepción de *oldmodules* y "encodings" para
   preservar la memoria caché interna.

test.support.import_helper.unload(name)

   Elimina *name* de "sys.modules".

test.support.import_helper.make_legacy_pyc(source)

   Mueve un archivo *pyc* de **PEP 3147**/**PEP 488** a su ubicación
   heredada y retorna la ruta del sistema de archivos al archivo de
   *pyc* heredado. El valor de origen es la ruta del sistema de
   archivos al archivo fuente. No es necesario que exista, sin
   embargo, debe existir el archivo PEP 3147/488 *pyc*.

class test.support.import_helper.CleanImport(*module_names)

   Un administrador de contexto para forzar la importación para
   retornar una nueva referencia de módulo. Esto es útil para probar
   comportamientos a nivel de módulo, como la emisión de un
   "DeprecationWarning" en la importación. Ejemplo de uso:

      with CleanImport('foo'):
          importlib.import_module('foo')  # New reference.

class test.support.import_helper.DirsOnSysPath(*paths)

   Un administrador de contexto para agregar directorios temporalmente
   a "sys.path".

   Esto hace una copia de "sys.path", agrega cualquier directorio dado
   como argumento posicional, luego revierte "sys.path" a la
   configuración copiada cuando finaliza el contexto.

   Tenga en cuenta que *all* "sys.path" produce modificaciones en el
   cuerpo del administrador de contexto, incluida la sustitución del
   objeto, se revertirán al final del bloque.

# "test.support.warnings_helper" --- Utilities for warnings tests

The "test.support.warnings_helper" module provides support for
warnings tests.

Added in version 3.10.

test.support.warnings_helper.ignore_warnings(*, category)

   Suppress warnings that are instances of *category*, which must be
   "Warning" or a subclass. Roughly equivalent to
   "warnings.catch_warnings()" with "warnings.simplefilter('ignore',
   category=category)". For example:

      @warning_helper.ignore_warnings(category=DeprecationWarning)
      def test_suppress_warning():
          # do something

   Added in version 3.8.

test.support.warnings_helper.check_no_resource_warning(testcase)

   Gestor de contexto para comprobar que no se ha lanzado un
   "ResourceWarning" . Debe eliminar el objeto que puede emitir
   "ResourceWarning" antes del final del administrador de contexto.

test.support.warnings_helper.check_syntax_warning(testcase, statement, errtext='', *, lineno=1, offset=None)

   Prueba la advertencia de sintaxis en *statement* intentando
   compilar *statement*. Pruebe también que "SyntaxWarning" se emite
   solo una vez, y que se convertirá en "SyntaxError" cuando se
   convierta en error. *testcase* es la instancia "unittest" para la
   prueba. *errtext* es la expresión regular que debe coincidir con la
   representación de cadena del emitido "SyntaxWarning" y lanza
   "SyntaxError" . Si *lineno* no es "None", se compara con la línea
   de advertencia y excepción. Si *offset* no es "None", se compara
   con el desplazamiento de la excepción.

   Added in version 3.8.

test.support.warnings_helper.check_warnings(*filters, quiet=True)

   A convenience wrapper for "warnings.catch_warnings()" that makes it
   easier to test that a warning was correctly raised.  It is
   approximately equivalent to calling
   "warnings.catch_warnings(record=True)" with
   "warnings.simplefilter()" set to "always" and with the option to
   automatically validate the results that are recorded.

   "check_warnings" acepta 2 tuplas de la forma "("mensaje regexp",
   WarningCategory)" como argumentos posicionales. Si se proporcionan
   uno o más *filters*, o si el argumento opcional de palabra clave
   *quiet* es "False", se verifica para asegurarse de que las
   advertencias sean las esperadas: cada filtro especificado debe
   coincidir con al menos una de las advertencias lanzadas por el
   código adjunto o la prueba falla, y si se lanzan advertencias que
   no coinciden con ninguno de los filtros especificados, la prueba
   falla. Para deshabilitar la primera de estas comprobaciones,
   configure *quiet* en "True".

   Si no se especifican argumentos, el valor predeterminado es:

      check_warnings(("", Warning), quiet=True)

   En este caso, se capturan todas las advertencias y no se lanzaran
   errores.

   En la entrada al administrador de contexto, se retorna una
   instancia de "WarningRecorder". La lista de advertencias
   subyacentes de "catch_warnings()" está disponible a través del
   atributo "warnings" del objeto del registrador. Como conveniencia,
   también se puede acceder directamente a los atributos del objeto
   que representa la advertencia más reciente a través del objeto
   grabador (vea el ejemplo a continuación). Si no se ha lanzado
   ninguna advertencia, cualquiera de los atributos que de otro modo
   se esperarían en un objeto que representa una advertencia retornará
   "None".

   El objeto grabador (*recorder object*) también tiene un método
   "reset()", que borra la lista de advertencias.

   El administrador de contexto está diseñado para usarse así:

      with check_warnings(("assertion is always true", SyntaxWarning),
                          ("", UserWarning)):
          exec('assert(False, "Hey!")')
          warnings.warn(UserWarning("Hide me!"))

   En este caso, si no se generó ninguna advertencia, o si surgió
   alguna otra advertencia, "check_warnings()" lanzaría un error.

   Cuando una prueba necesita analizar más profundamente las
   advertencias, en lugar de simplemente verificar si ocurrieron o no,
   se puede usar un código como este:

      with check_warnings(quiet=True) as w:
          warnings.warn("foo")
          assert str(w.args[0]) == "foo"
          warnings.warn("bar")
          assert str(w.args[0]) == "bar"
          assert str(w.warnings[0].args[0]) == "foo"
          assert str(w.warnings[1].args[0]) == "bar"
          w.reset()
          assert len(w.warnings) == 0

   Aquí se capturarán todas las advertencias, y el código de prueba
   prueba las advertencias capturadas directamente.

   Distinto en la versión 3.2: Nuevos argumentos opcionales *filters*
   y *quiet*.

class test.support.warnings_helper.WarningsRecorder

   La clase utilizada para registrar advertencias para pruebas
   unitarias. Consulte la documentación de "check_warnings()" arriba
   para obtener más detalles.
