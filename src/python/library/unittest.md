---
title: '"unittest" --- Unit testing framework'
source_url: https://docs.python.org/es/3
source_path: library/unittest.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4380
---

# "unittest" --- Unit testing framework

**Código fuente:** Lib/unittest/__init__.py

======================================================================

(Si ya estás familiarizado con los conceptos básicos de realización de
tests, puedes saltar a la lista de métodos de aserción.)

The "unittest" unit testing framework was originally inspired by JUnit
and has a similar flavor as major unit testing frameworks in other
languages.  It supports test automation, sharing of setup and shutdown
code for tests, aggregation of tests into collections, and
independence of the tests from the reporting framework.

To achieve this, "unittest" supports some important concepts in an
object-oriented way:

configuración de prueba (*fixture*)
   Un *test fixture* representa los preparativos para realizar una o
   más pruebas y las acciones de limpieza asociadas. Esto puede
   incluir, por ejemplo, la creación de bases de datos temporales,
   directorios o el arranque de procesos del servidor.

caso de prueba
   A *test case* is the individual unit of testing.  It checks for a
   specific response to a particular set of inputs.  "unittest"
   provides a base class, "TestCase", which may be used to create new
   test cases.

conjunto de pruebas
   Un *test suite* es una colección de casos de prueba, juegos de
   prueba o ambos. Se usa para agrupar pruebas que se han de ejecutar
   juntas.

ejecutor de pruebas
   Un *test runner* es un componente que dirige la ejecución de las
   pruebas y proporciona un resultado. El ejecutor puede disponer de
   una interfaz gráfica, de texto o devolver un valor especial que
   indique el resultado de la ejecución de las pruebas.

Ver también:

  Módulo "doctest"
     Otro módulo de soporte a pruebas con una solución muy diferente.

  Simple Smalltalk Testing: With Patterns
     Kent Beck's original paper on testing frameworks using the
     pattern shared by "unittest".

  pytest
     Una infraestructura de pruebas unitarias de otro proveedor con
     una sintaxis más ligera de escritura de pruebas, por ejemplo:
     "assert func(10) == 42".

  The Python Testing Tools Taxonomy
     Una lista extensa de herramientas de prueba para Python
     incluyendo infraestructuras de pruebas funcionales y librerías de
     objetos sucedáneos.

  Testing in Python Mailing List
     Grupo especializado en debate sobre las pruebas y las
     herramientas de prueba de Python.

  El script "Tools/unittestgui/unittestgui.py" en la distribución de
  código fuente de Python es una herramienta gráfica para el
  descubrimiento y ejecución de pruebas.  Está orientado
  principalmente a facilitar su uso para aquellos que son nuevos en
  las pruebas unitarias.  Para entornos de producción, se recomienda
  que las pruebas sean ejecutadas por un sistema de integración
  continua como Buildbot, Jenkins, GitHub Actions, o AppVeyor.

## Ejemplo sencillo

The "unittest" module provides a rich set of tools for constructing
and running tests.  This section demonstrates that a small subset of
the tools suffice to meet the needs of most users.

He aquí un breve script para probar estros tres métodos de cadena:

   import unittest

   class TestStringMethods(unittest.TestCase):

       def test_upper(self):
           self.assertEqual('foo'.upper(), 'FOO')

       def test_isupper(self):
           self.assertTrue('FOO'.isupper())
           self.assertFalse('Foo'.isupper())

       def test_split(self):
           s = 'hello world'
           self.assertEqual(s.split(), ['hello', 'world'])
           # check that s.split fails when the separator is not a string
           with self.assertRaises(TypeError):
               s.split(2)

   if __name__ == '__main__':
       unittest.main()

A test case is created by subclassing "unittest.TestCase".  The three
individual tests are defined with methods whose names start with the
letters "test".  This naming convention informs the test runner about
which methods represent tests.

El quid de cada test es la llamada a  "assertEqual()" para verificar
un resultado esperado; "assertTrue()" o "assertFalse()" para verificar
una condición; o "assertRaises()" para asegurar que se lanza una
excepción específica. Se utilizan estos métodos en lugar de la
sentencia "assert" para que el ejecutor de pruebas pueda acumular
todos los resultados de la prueba de cara a realizar un informe.

Los métodos "setUp()" y "tearDown()" permiten definir instrucciones
que han de ser ejecutadas antes y después, respectivamente, de cada
método de prueba. Se describen con mas detalle en la sección
Organización del código de pruebas.

El bloque final muestra un modo sencillo de ejecutar las pruebas.
"unittest.main()" proporciona una interfaz de línea de órdenes para el
script de prueba. Cuando se ejecuta desde la línea de órdenes, el
script anterior produce una salida como:

   ...
   ----------------------------------------------------------------------
   Ran 3 tests in 0.000s

   OK

Si se le pasa una opción "-v" al script de prueba, se establecerá un
nivel mayor de detalle del proceso de "unittest.main()" y se obtendrá
la siguiente salida:

   test_isupper (__main__.TestStringMethods.test_isupper) ... ok
   test_split (__main__.TestStringMethods.test_split) ... ok
   test_upper (__main__.TestStringMethods.test_upper) ... ok

   ----------------------------------------------------------------------
   Ran 3 tests in 0.001s

   OK

The above examples show the most commonly used "unittest" features
which are sufficient to meet many everyday testing needs.  The
remainder of the documentation explores the full feature set from
first principles.

Distinto en la versión 3.11: El comportamiento de retornar un valor de
un método de prueba (que no sea el valor por defecto "None"), ahora
está obsoleto.

## Interfaz de línea de comandos

Se puede usar el módulo *unittest* desde la línea de órdenes para
ejecutar pruebas de módulos, clases o hasta métodos de prueba
individuales:

   python -m unittest test_module1 test_module2
   python -m unittest test_module.TestClass
   python -m unittest test_module.TestClass.test_method

Se puede pasar una lista con cualquier combinación de nombres de
módulo, así como clases o métodos completamente cualificados.

Se puede especificar los módulos de prueba por ruta de fichero
también:

   python -m unittest tests/test_something.py

Esto permite usar el completado automático de nombre de fichero de la
shell para especificar el módulo de pruebas. El fichero especificado
aún debe ser susceptible de importarse como módulo. La ruta se
convierte en nombre de módulo eliminando '.py' y convirtiendo el
separador de directorios por '.'. Si se desea ejecutar un fichero de
prueba que no se puede importar como módulo, se ha de ejecutar el
fichero directamente.

Se pueden ejecutar las pruebas con más nivel de detalle (mayor
verbosidad) pasando el parámetro *-v*:

   python -m unittest -v test_module

Cuando se ejecuta sin argumentos, se inicia Descubrimiento de pruebas:

   python -m unittest

Para obtener una lista de todas las opciones de línea de órdenes:

   python -m unittest -h

Distinto en la versión 3.2: En versiones anteriores sólo era posible
ejecutar métodos de prueba individuales, pero no módulos ni clases.

Added in version 3.14: Output is colorized by default and can be
controlled using environment variables.

### Opciones de la línea de órdenes

**unittest** da soporte a las siguientes opciones de línea de órdenes:

-b, --buffer

   Los flujos de datos de salida estándar y error estándar se acumulan
   en un búfer durante la ejecución de pruebas. La salida de las
   pruebas correctas se descarta. La salida de las pruebas que fallan
   o devuelven un error se añade a los mensajes de fallo.

-c, --catch

   La pulsación de "Control"-"C" durante la ejecución de pruebas
   espera a que termine la prueba en curso y da un informe de los
   resultados hasta ese momento. Una segunda pulsación de
   "Control"-"C" lanza la excepción "KeyboardInterrupt" usual.

   Consultar  en Gestión de señales las funciones que proporcionan
   esta funcionalidad.

-f, --failfast

   Finaliza la ejecución tras el primer error o fallo.

-k

   Ejecutar solamente los métodos y clases de prueba que coincidan con
   el patrón o subcadena de caracteres. Esta opción se puede usar más
   de una vez, en cuyo caso se incluirán todos los casos de prueba que
   coincidan con cualquiera de los patrones dados.

   Los patrones que contengan un comodín ("*") se comprueban contra el
   nombre de la prueba usando "fnmatch.fnmatchcase()"; si no lo
   contienen, se usa una comprobación de contenido simple sensible a
   mayúsculas.

   Los patrones se comprueban contra el nombre del método
   completamente cualificado como lo importa el cargador de pruebas.

   Por ejemplo, "-k foo" coincide con
   "foo_tests.SomeTest.test_something" y con
   "bar_tests.SomeTest.test_foo", pero no con
   "bar_tests.FooTest.test_something".

--locals

   Muestra las variables locales en las trazas.

--durations N

   Muestra los N casos de prueba más lentos (N=0 para todos).

Added in version 3.2: Se añadieron las opciones de línea de órdenes
"-b", "-c" y "-f".

Added in version 3.5: La opción de línea de órdenes "--locals".

Added in version 3.7: La opción de línea de órdenes "-k".

Added in version 3.12: La opción de línea de órdenes "--durations".

La línea de órdenes también se puede usar para descubrimiento de
pruebas, para ejecutar todas las pruebas de un proyecto o un
subconjunto de éstas.

## Descubrimiento de pruebas

Added in version 3.2.

Unittest da soporte al descubrimiento de pruebas simples. Para ser
compatible con el descubrimiento de pruebas, todos los ficheros de
prueba deben ser módulos o paquetes importables desde el directorio
superior del proyecto (por lo que sus nombres han de ser
identificadores válidos).

El descubrimiento de pruebas está implementado en
"TestLoader.discover()", pero también se puede usar desde la línea de
órdenes. La línea de órdenes básica es:

   cd project_directory
   python -m unittest discover

Nota:

  Como atajo, "python -m unittest" es el equivalente de "python -m
  unittest discover". Si se desea pasar argumentos al descubrimiento
  de pruebas, hay que pasar la sub-orden "discover" explícitamente.

La sub-orden "discover" cuenta con las siguientes opciones:

-v, --verbose

   Salida verbosa

-s, --start-directory directory

   Directorio de inicio para el descubrimiento ("." si se omite)

-p, --pattern pattern

   Patrón para la búsqueda de ficheros de prueba ("test*.py" si se
   omite)

-t, --top-level-directory directory

   Directorio superior del proyecto (el directorio inicial si se
   omite)

Las opciones "-s", "-p", y "-t" se pueden pasar por posición en el
orden mostrado. Las siguientes líneas de órdenes son equivalentes:

   python -m unittest discover -s project_directory -p "*_test.py"
   python -m unittest discover project_directory "*_test.py"

Además de pasar una ruta, es posible pasar el nombre de un paquete,
por ejemplo "myproject.subpackage.test", como directorio de inicio. El
nombre de paquete proporcionado será importado y su ubicación en el
sistema de archivos será utilizada como directorio de inicio.

Prudencia:

  El descubrimiento de pruebas carga las pruebas importándolas. Una
  vez que el descubrimiento ha encontrado todos los ficheros de prueba
  a partir del directorio inicial, especificado, convierte las rutas
  en nombres de paquetes a importar. Por ejemplo, "foo/bar/baz.py"
  será importado como "foo.bar.baz".Si hay un paquete instalado
  globalmente y se intenta hacer un descubrimiento sobre una copia
  diferente a la instalada del paquete, *podría* ocurrir que se
  importe la versión incorrecta. Si ocurre esto, el descubrimiento
  lanza una advertencia y abandona.Si se proporciona el directorio de
  inicio como nombre de paquete en lugar de ruta a un directorio, el
  descubrimiento asume que la ubicación importada es la deseada, así
  que no se da la advertencia descrita.

Los módulos y paquetes de prueba pueden personalizar la carta y
descubrimiento de pruebas mediante el protocolo load_tests.

Distinto en la versión 3.4: Test discovery supports *namespace
packages*.

Distinto en la versión 3.11: Test discovery dropped the *namespace
packages* support. It has been broken since Python 3.7. Start
directory and its subdirectories containing tests must be regular
package that have "__init__.py" file.If the start directory is the
dotted name of the package, the ancestor packages can be namespace
packages.

Distinto en la versión 3.14: Test discovery supports *namespace
package* as start directory again. To avoid scanning directories
unrelated to Python, tests are not searched in subdirectories that do
not contain "__init__.py".

## Organización del código de pruebas

The basic building blocks of unit testing are *test cases* --- single
scenarios that must be set up and checked for correctness.  In
"unittest", test cases are represented by "unittest.TestCase"
instances. To make your own test cases you must write subclasses of
"TestCase" or use "FunctionTestCase".

El código de pruebas de una instancia de "TestCase" debería ser
completamente autónomo, de tal modo que se pueda ejecutar aisladamente
o en una combinación arbitraria con otras clases de prueba.

La subclase más simple de "TestCase" se limita a implementar un método
test (o un método que empiece por "test") para realizar código de
prueba específico:

   import unittest

   class DefaultWidgetSizeTestCase(unittest.TestCase):
       def test_default_widget_size(self):
           widget = Widget('The widget')
           self.assertEqual(widget.size(), (50, 50))

Note that in order to test something, we use one of the assert*
methods provided by the "TestCase" base class.  If the test fails, an
exception will be raised with an explanatory message, and "unittest"
will identify the test case as a *failure*.  Any other exceptions will
be treated as *errors*.

Las pruebas pueden ser muchas y su preparación puede ser repetitiva.
Por suerte, se puede "sacar factor común" a la preparación
implementando un método "setUp()", al que la infraestructura de prueba
llamará para cada prueba que se ejecute:

   import unittest

   class WidgetTestCase(unittest.TestCase):
       def setUp(self):
           self.widget = Widget('The widget')

       def test_default_widget_size(self):
           self.assertEqual(self.widget.size(), (50,50),
                            'incorrect default size')

       def test_widget_resize(self):
           self.widget.resize(100,150)
           self.assertEqual(self.widget.size(), (100,150),
                            'wrong size after resize')

Nota:

  El orden en que se ejecutan las diversas pruebas se determina por
  orden alfabético de los nombres de métodos de prueba.

Si el método "setUp()" lanza una excepción mientras se ejecuta la
prueba, la infraestructura considerará que la prueba ha sufrido un
error y no se ejecutará el método de prueba propiamente dicho.

Análogamente, se puede proporcionar un método "tearDown()" que haga
limpieza después de que se ejecute el método de prueba:

   import unittest

   class WidgetTestCase(unittest.TestCase):
       def setUp(self):
           self.widget = Widget('The widget')

       def tearDown(self):
           self.widget.dispose()

Si "setUp()" se ejecuta sin errores, "tearDown()" se ejecutará tanto
si el método de prueba tuvo éxito como si no.

Such a working environment for the testing code is called a *test
fixture*.  A new TestCase instance is created as a unique test fixture
used to execute each individual test method.  Thus "setUp()",
"tearDown()", and "TestCase.__init__()" will be called once per test.

It is recommended that you use TestCase implementations to group tests
together according to the features they test.  "unittest" provides a
mechanism for this: the *test suite*, represented by "unittest"'s
"TestSuite" class.  In most cases, calling "unittest.main()" will do
the right thing and collect all the module's test cases for you and
execute them.

Sin embargo, si se desea personalizar la construcción del paquete de
pruebas, se puede hacer:

   def suite():
       suite = unittest.TestSuite()
       suite.addTest(WidgetTestCase('test_default_widget_size'))
       suite.addTest(WidgetTestCase('test_widget_resize'))
       return suite

   if __name__ == '__main__':
       runner = unittest.TextTestRunner()
       runner.run(suite())

Se puede poner las definiciones de los casos de prueba y de los
paquetes de prueba en los mismos módulos que el código que
prueban.(tal como "widget.py"), pero sacarlos a un módulo aparte como
"test_widget.py" tiene diversas ventajas:

* El módulo de pruebas se puede ejecutar aisladamente desde la línea
  de órdenes.

* El código de pruebas se puede separar con más facilidad del código
  de producción.

* Disminuye la tentación de cambiar el código de prueba para ajustarse
  al código bajo prueba.

* El código de pruebas debería modificarse con mucha menor frecuencia
  que el código bajo prueba.

* Es más sencillo refactorizar el código bajo prueba.

* El código para probar módulos escritos en C ha de estar en módulos
  aparte, así que ¿por qué no mantener la consistencia?

* Si cambia la estrategia de prueba, no hay razón para cambiar el
  código fuente principal.

## Reutilización de código de prueba anterior

Some users will find that they have existing test code that they would
like to run from "unittest", without converting every old test
function to a "TestCase" subclass.

For this reason, "unittest" provides a "FunctionTestCase" class. This
subclass of "TestCase" can be used to wrap an existing test function.
Set-up and tear-down functions can also be provided.

Dada la siguiente función de prueba:

   def testSomething():
       something = makeSomething()
       assert something.name is not None
       # ...

se puede crear una instancia de caso de prueba de la siguiente manera,
con métodos opcionales de preparación y desmontaje:

   testcase = unittest.FunctionTestCase(testSomething,
                                        setUp=makeSomethingDB,
                                        tearDown=deleteSomethingDB)

Nota:

  Even though "FunctionTestCase" can be used to quickly convert an
  existing test base over to a "unittest"-based system, this approach
  is not recommended.  Taking the time to set up proper "TestCase"
  subclasses will make future test refactorings infinitely easier.

In some cases, the existing tests may have been written using the
"doctest" module.  If so, "doctest" provides a "DocTestSuite" class
that can automatically build "unittest.TestSuite" instances from the
existing "doctest"-based tests.

## Omitir tests y fallos esperados

Added in version 3.1.

Unittest soporta omitir métodos individuales de tests e incluso clases
completas de tests. Además, soporta marcar un test como un "fallo
esperado", un test que está roto y va a fallar, pero no debería ser
contado como fallo en "TestResult".

Skipping a test is simply a matter of using the "@skip" *decorator* or
one of its conditional variants, calling "TestCase.skipTest()" within
a "setUp()" or test method, or raising "SkipTest" directly.

La omisión más básica tiene la siguiente forma:

   class MyTestCase(unittest.TestCase):

       @unittest.skip("demonstrating skipping")
       def test_nothing(self):
           self.fail("shouldn't happen")

       @unittest.skipIf(mylib.__version__ < (1, 3),
                        "not supported in this library version")
       def test_format(self):
           # Tests that work for only a certain version of the library.
           pass

       @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
       def test_windows_support(self):
           # windows specific testing code
           pass

       def test_maybe_skipped(self):
           if not external_resource_available():
               self.skipTest("external resource not available")
           # test code that depends on the external resource
           pass

Esta es la salida de ejecutar el ejemplo superior en modo verboso:

   test_format (__main__.MyTestCase.test_format) ... skipped 'not supported in this library version'
   test_nothing (__main__.MyTestCase.test_nothing) ... skipped 'demonstrating skipping'
   test_maybe_skipped (__main__.MyTestCase.test_maybe_skipped) ... skipped 'external resource not available'
   test_windows_support (__main__.MyTestCase.test_windows_support) ... skipped 'requires Windows'

   ----------------------------------------------------------------------
   Ran 4 tests in 0.005s

   OK (skipped=4)

Las clases pueden ser omitidas igual que los métodos:

   @unittest.skip("showing class skipping")
   class MySkippedTestCase(unittest.TestCase):
       def test_not_run(self):
           pass

"TestCase.setUp()" puede omitir también el test. Esto es útil cuando
un recurso que necesita ser puesto a punto no está disponible.

Expected failures use the "@expectedFailure" decorator.

   class ExpectedFailureTestCase(unittest.TestCase):
       @unittest.expectedFailure
       def test_fail(self):
           self.assertEqual(1, 0, "broken")

Es fácil lanzar tus propios decoradores que omitan haciendo un
decorador que llame a "skip()"  en el test cuando quiere ser omitido.
Este decorador omite el test a menos que el objeto pasado tenga un
cierto atributo:

   def skipUnlessHasattr(obj, attr):
       if hasattr(obj, attr):
           return lambda func: func
       return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))

Los siguientes decoradores y la excepción implementan la omisión de
tests y los fallos esperados:

@unittest.skip(reason)

   Omitir incondicionalmente el test decorado. *reason* debe describir
   porqué el test está siendo omitido.

@unittest.skipIf(condition, reason)

   Omitir el test decorado si *condition* es verdadero.

@unittest.skipUnless(condition, reason)

   Omitir el test decorado a menos que *condition* sea verdadero.

@unittest.expectedFailure

   Marca el test como un fallo esperado.  Si falla el test o hay
   errores en la función de test misma (en lugar de en alguno de los
   métodos *test fixture*) será considerado un éxito. Si el test pasa,
   será considerado un fallo.

exception unittest.SkipTest(reason)

   Esta excepción es lanzada para omitir un test.

   Normalmente puedes usar directamente "TestCase.skipTest()" o uno de
   los decoradores de omisión en vez de lanzar esta excepción.

Los tests omitidos no ejecutarán "setUp()" o "tearDown()". Las clases
omitidas no ejecutarán "setUpClass()" o "tearDownClass()". Los módulos
omitidos no ejecutarán "setUpModule()" o "tearDownModule()".

## Distinguiendo iteraciones de tests empleando subtests

Added in version 3.4.

Cuando hay diferencias muy pequeñas entre tus tests, por ejemplo
algunos parámetros, unittest te permite distinguirlos dentro del
cuerpo de un método de test empleando el administrador de contexto
"subTest()" .

Por ejemplo, el siguiente test:

   class NumbersTest(unittest.TestCase):

       def test_even(self):
           """
           Test that numbers between 0 and 5 are all even.
           """
           for i in range(0, 6):
               with self.subTest(i=i):
                   self.assertEqual(i % 2, 0)

producirá la siguiente salida:

   ======================================================================
   FAIL: test_even (__main__.NumbersTest.test_even) (i=1)
   Test that numbers between 0 and 5 are all even.
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "subtests.py", line 11, in test_even
       self.assertEqual(i % 2, 0)
       ^^^^^^^^^^^^^^^^^^^^^^^^^^
   AssertionError: 1 != 0

   ======================================================================
   FAIL: test_even (__main__.NumbersTest.test_even) (i=3)
   Test that numbers between 0 and 5 are all even.
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "subtests.py", line 11, in test_even
       self.assertEqual(i % 2, 0)
       ^^^^^^^^^^^^^^^^^^^^^^^^^^
   AssertionError: 1 != 0

   ======================================================================
   FAIL: test_even (__main__.NumbersTest.test_even) (i=5)
   Test that numbers between 0 and 5 are all even.
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "subtests.py", line 11, in test_even
       self.assertEqual(i % 2, 0)
       ^^^^^^^^^^^^^^^^^^^^^^^^^^
   AssertionError: 1 != 0

Sin usar un subtest, la ejecución se pararía después del primer fallo,
y el error sería más difícil de diagnosticar porque el valor de  "i"
no se mostraría:

   ======================================================================
   FAIL: test_even (__main__.NumbersTest.test_even)
   ----------------------------------------------------------------------
   Traceback (most recent call last):
     File "subtests.py", line 32, in test_even
       self.assertEqual(i % 2, 0)
   AssertionError: 1 != 0

## Clases y funciones

This section describes in depth the API of "unittest".

### Casos de test

class unittest.TestCase(methodName='runTest')

   Instances of the "TestCase" class represent the logical test units
   in the "unittest" universe.  This class is intended to be used as a
   base class, with specific tests being implemented by concrete
   subclasses.  This class implements the interface needed by the test
   runner to allow it to drive the tests, and methods that the test
   code can use to check for and report various kinds of failure.

   Cada instancia de "TestCase"  ejecutará un solo método base: el
   método llamado *methodName*. En la mayoría de usos de "TestCase",
   no tendrás que cambiar el *methodName*  ni reimplementar el método
   por defecto  "runTest()".

   Distinto en la versión 3.2: "TestCase" puede instancias con éxito
   sin dar un *methodName*.  Esto permite experimentar de manera
   sencilla con "TestCase"  en el intérprete interactivo.

   Las instancias de "TestCase"  proveen tres grupos de métodos: un
   grupo empleado para ejecutar el test, otro usado para que la
   implementación del test chequee condiciones y reporte fallos, y
   algunos métodos de indagación que permiten recopilar información
   sobre el test en si mismo.

   Los métodos en el primer grupo (ejecutando el test) son:

   setUp()

      Método llamado para preparar el banco de test. Es invocado
      inmediatamente antes de llamar al método de test; cualquier
      excepción lanzada por este método que no sea "AssertionError" o
      "SkipTest" será considerada un error en vez de un fallo del
      test. La implementación por defecto no hace nada.

   tearDown()

      Método llamado inmediatamente después de que se haya llamado el
      método de prueba y se haya registrado el resultado.  Se llama
      así aunque el método de ensayo haya planteado una excepción, por
      lo que la aplicación en las subclases puede tener que ser
      especialmente cuidadosa en cuanto a la comprobación del estado
      interno.  Cualquier excepción, que no sea  "AssertionError" o
      "SkipTest", planteada por este método se considerará un error
      adicional en lugar de un fallo de la prueba (aumentando así el
      número total de errores reportados). Este método sólo se llamará
      si "setUp()" tiene éxito, independientemente del resultado del
      método de prueba. La implementación por defecto no hace nada.

   setUpClass()

      A class method called before tests in an individual class are
      run. "setUpClass" is called with the class as the only argument
      and must be decorated as a "@classmethod":

         @classmethod
         def setUpClass(cls):
             ...

      Vea  Class and Module Fixtures para más detalles.

      Added in version 3.2.

   tearDownClass()

      A class method called after tests in an individual class have
      run. "tearDownClass" is called with the class as the only
      argument and must be decorated as a "@classmethod":

         @classmethod
         def tearDownClass(cls):
             ...

      Vea  Class and Module Fixtures para más detalles.

      Added in version 3.2.

   run(result=None)

      Ejecutar la prueba, recogiendo el resultado en el objeto
      "TestResult"  pasado como *result*.  Si se omite *result* o
      "None", se crea un objeto resultado temporal (llamando al método
      "defaultTestResult()") y se emplea ese. El objeto resultante se
      devuelve al invocador de "run()".

      El mismo efecto puede conseguirse simplemente llamando a la
      instancia "TestCase".

      Distinto en la versión 3.3: Las versiones previas de "run" no
      retornaban el resultado. Tampoco lo hacía la llamada a una
      instancia.

   skipTest(reason)

      Llamar a esto durante un método de prueba o "setUp()" se salta
      el test actual.  Ver  Omitir tests y fallos esperados para más
      información.

      Added in version 3.1.

   subTest(msg=None, **params)

      Retorna un gestor de contexto que ejecuta el bloque de código
      adjunto como un subtest.  *msg* y *params* son valores
      opcionales y arbitrarios que se muestran cuando falla un
      subtest, permitiéndole identificarlos claramente.

      Un caso de test puede contener cualquier número de declaraciones
      de subtest, y pueden anidarse arbitrariamente.

      Ver Distinguiendo iteraciones de tests empleando subtests para
      más información.

      Added in version 3.4.

   debug()

      Realice el test sin recoger el resultado.  Esto permite que las
      excepciones planteadas por el test se propaguen al invocado, y
      puede utilizarse para apoyar la ejecución de tests bajo un
      depurador.

   La clase "TestCase" proporciona varios métodos de afirmación para
   comprobar y reportar fallos.  En la siguiente tabla se enumeran los
   métodos más utilizados (consulte las tablas siguientes para ver más
   métodos de afirmación):

   +-------------------------------------------+-------------------------------+-----------------+
   | Método                                    | Comprueba que                 | Nuevo en        |
   |===========================================|===============================|=================|
   | "assertEqual(a, b)"                       | "a == b"                      |                 |
   +-------------------------------------------+-------------------------------+-----------------+
   | "assertNotEqual(a, b)"                    | "a != b"                      |                 |
   +-------------------------------------------+-------------------------------+-----------------+
   | "assertTrue(x)"                           | "bool(x) is True"             |                 |
   +-------------------------------------------+-------------------------------+-----------------+
   | "assertFalse(x)"                          | "bool(x) is False"            |                 |
   +-------------------------------------------+-------------------------------+-----------------+
   | "assertIs(a, b)"                          | "a is b"                      | 3.1             |
   +-------------------------------------------+-------------------------------+-----------------+
   | "assertIsNot(a, b)"                       | "a is not b"                  | 3.1             |
   +-------------------------------------------+-------------------------------+-----------------+
   | "assertIsNone(x)"                         | "x is None"                   | 3.1             |
   +-------------------------------------------+-------------------------------+-----------------+
   | "assertIsNotNone(x)"                      | "x is not None"               | 3.1             |
   +-------------------------------------------+-------------------------------+-----------------+
   | "assertIn(a, b)"                          | "a in b"                      | 3.1             |
   +-------------------------------------------+-------------------------------+-----------------+
   | "assertNotIn(a, b)"                       | "a not in b"                  | 3.1             |
   +-------------------------------------------+-------------------------------+-----------------+
   | "assertIsInstance(a, b)"                  | "isinstance(a, b)"            | 3.2             |
   +-------------------------------------------+-------------------------------+-----------------+
   | "assertNotIsInstance(a, b)"               | "not isinstance(a, b)"        | 3.2             |
   +-------------------------------------------+-------------------------------+-----------------+
   | "assertIsSubclass(a, b)"                  | "issubclass(a, b)"            | 3.14            |
   +-------------------------------------------+-------------------------------+-----------------+
   | "assertNotIsSubclass(a, b)"               | "not issubclass(a, b)"        | 3.14            |
   +-------------------------------------------+-------------------------------+-----------------+

   Todos los métodos de aserción aceptan un argumento *msg* que, si se
   especifica, se utiliza como mensaje de error en caso de fallo
   (véase también "longMessage"). Tenga en cuenta que el argumento de
   la palabra clave *msg* puede pasarse a "assertRaises()",
   "assertRaisesRegex()", "assertWarns()", "assertWarnsRegex()" sólo
   cuando se utilizan como gestor de contexto.

   assertEqual(first, second, msg=None)

      Testea que *first* y *second* son iguales. Si los valores no
      comparan como iguales, el test fallará.

      Además, si *first* y *second* son exactamente del mismo tipo y
      uno de lista, tuple, dict, set, frozenset o str o cualquier tipo
      que una subclase registre con "addTypeEqualityFunc()" se llamará
      a la función de igualdad específica del tipo para generar un
      mensaje de error por defecto más útil (véase también la lista de
      métodos específicos del tipo).

      Distinto en la versión 3.1: Añadida la llamada automática de la
      función de igualdad de tipo específico.

      Distinto en la versión 3.2: "assertMultiLineEqual()" añadido
      como la función por defecto para igualdad de tipos cuando se
      comparan cadenas.

   assertNotEqual(first, second, msg=None)

      Testea que *first* y *second* no son iguales.  Si los valores
      son iguales, el test fallará.

   assertTrue(expr, msg=None)
   assertFalse(expr, msg=None)

      Testea que *expr* es verdadero (o falso).

      Note que esto es equivalente a "bool(expr) is True" y no a "expr
      is True" (use "assertIs(expr, True)" para lo último).  Este
      método también debe evitarse cuando se disponga de métodos más
      específicos (por ejemplo, "assertEqual(a, b)" en lugar de
      "assertTrue(a == b)"), porque proporcionan un mejor mensaje de
      error en caso de fallo.

   assertIs(first, second, msg=None)
   assertIsNot(first, second, msg=None)

      Testea si *first* y *second* son (o no) el mismo objeto.

      Added in version 3.1.

   assertIsNone(expr, msg=None)
   assertIsNotNone(expr, msg=None)

      Testea que *expr*  es (o no es) "None".

      Added in version 3.1.

   assertIn(member, container, msg=None)
   assertNotIn(member, container, msg=None)

      Testea que *member* está (o no está) en *container*.

      Added in version 3.1.

   assertIsInstance(obj, cls, msg=None)
   assertNotIsInstance(obj, cls, msg=None)

      Testea que *obj* es (o no es) una instancia de *cls* (que puede
      ser una clase o una tupla de clases, de la misma forma que
      soporta "isinstance()"). Para chequear por el tipo exacto, use
      "assertIs(type(obj), cls)".

      Added in version 3.2.

   assertIsSubclass(cls, superclass, msg=None)
   assertNotIsSubclass(cls, superclass, msg=None)

      Test that *cls* is (or is not) a subclass of *superclass* (which
      can be a class or a tuple of classes, as supported by
      "issubclass()"). To check for the exact type, use "assertIs(cls,
      superclass)".

      Added in version 3.14.

   Es también posible chequear la producción de excepciones,
   advertencias y mensajes de log usando los siguientes métodos:

   +-----------------------------------------------------------+----------------------------------------+--------------+
   | Método                                                    | Comprueba que                          | Nuevo en     |
   |===========================================================|========================================|==============|
   | "assertRaises(exc, fun, *args, **kwds)"                   | "fun(*args, **kwds)" lanza *exc*       |              |
   +-----------------------------------------------------------+----------------------------------------+--------------+
   | "assertRaisesRegex(exc, r, fun, *args, **kwds)"           | "fun(*args, **kwds)" lanza *exc* y el  | 3.1          |
   |                                                           | mensaje coincide con regex *r*         |              |
   +-----------------------------------------------------------+----------------------------------------+--------------+
   | "assertWarns(warn, fun, *args, **kwds)"                   | "fun(*args, **kwds)" lanza *warn*      | 3.2          |
   +-----------------------------------------------------------+----------------------------------------+--------------+
   | "assertWarnsRegex(warn, r, fun, *args, **kwds)"           | "fun(*args, **kwds)" lanza *warn* y el | 3.2          |
   |                                                           | mensaje coincide con regex *r*         |              |
   +-----------------------------------------------------------+----------------------------------------+--------------+
   | "assertLogs(logger, level)"                               | El bloque "with" vuelca sus logs a     | 3.4          |
   |                                                           | *logger* con el *level* mínimo         |              |
   +-----------------------------------------------------------+----------------------------------------+--------------+
   | "assertLogs(logger, level)"                               | El bloque "with" no ingresa El bloque  | 3.10         |
   |                                                           | "with" vuelca sus logs a *logger* con  |              |
   |                                                           | el *level* mínimo                      |              |
   +-----------------------------------------------------------+----------------------------------------+--------------+

   assertRaises(exception, callable, *args, **kwds)
   assertRaises(exception, *, msg=None)

      Testea que se lanza una excepción cuando se llama a *callable*
      con cualquier argumento posicional o de palabra clave que
      también se pasa a  "assertRaises()". El test pasa si se lanza
      *exception*, es un error si se lanza otra excepción, o falla si
      no se lanza ninguna excepción. Para tener en cuenta cualquiera
      de un grupo de excepciones, una tupla que contenga las clases de
      excepción puede ser pasada como *exception*.

      Si sólo se dan los argumentos de *exception* y posiblemente
      *msg*, retorna un administrador de contexto para que el código
      testado pueda ser escrito en línea en lugar de como una función:

         with self.assertRaises(SomeException):
             do_something()

      Cuando se emplea como un administrador de contexto,
      "assertRaises()" acepta el argumento por palabra clave adicional
      *msg*.

      The context manager will store the caught exception object in
      its "exception" attribute.  This can be useful if the intention
      is to perform additional checks on the exception raised:

         with self.assertRaises(SomeException) as cm:
             do_something()

         the_exception = cm.exception
         self.assertEqual(the_exception.error_code, 3)

      Distinto en la versión 3.1: Añadió la capacidad de usar
      "assertRaises()" como gestor de contexto.

      Distinto en la versión 3.2: Added the "exception" attribute.

      Distinto en la versión 3.3: Añadido el argumento por palabra
      clave *msg* cuando se emplea un gestor de contexto.

   assertRaisesRegex(exception, regex, callable, *args, **kwds)
   assertRaisesRegex(exception, regex, *, msg=None)

      Como "assertRaises()" pero también testea que *regex* coincide
      en la representación de la cadena de la excepción planteada.
      *regex* puede ser un objeto de expresión regular o una cadena
      que contiene una expresión regular adecuada para ser usada por
      "re.search()".  Ejemplos:

         self.assertRaisesRegex(ValueError, "invalid literal for.*XYZ'$",
                                int, 'XYZ')

      o:

         with self.assertRaisesRegex(ValueError, 'literal'):
            int('XYZ')

      Added in version 3.1: Añadido bajo el nombre de
      "assertRaisesRegexp".

      Distinto en la versión 3.2: Renombrado a  "assertRaisesRegex()".

      Distinto en la versión 3.3: Añadido el argumento por palabra
      clave *msg* cuando se emplea un gestor de contexto.

   assertWarns(warning, callable, *args, **kwds)
   assertWarns(warning, *, msg=None)

      Testea que una advertencia se activa cuando se llama a
      *callable* con cualquier argumento posicional o de palabra clave
      que también se pasa a "assertWarns()". El test pasa si se activa
      el *warning* y falla si no lo hace.  Cualquier excepción es un
      error. Para considerar cualquiera de un grupo de advertencias,
      una tupla que contenga las clases de advertencia puede ser
      pasada como *warnings*.

      Si sólo se dan los argumentos de *advertencia* y  *msg*, retorna
      un gestor de contexto para que el código testado pueda ser
      escrito en línea en lugar de como una función:

         with self.assertWarns(SomeWarning):
             do_something()

      Cuando se usa como gestor de contexto, "assertWarns()"  acepta
      el argumento de palabra clave adicional *msg*.

      The context manager will store the caught warning object in its
      "warning" attribute, and the source line which triggered the
      warnings in the "filename" and "lineno" attributes. This can be
      useful if the intention is to perform additional checks on the
      warning caught:

         with self.assertWarns(SomeWarning) as cm:
             do_something()

         self.assertIn('myfile.py', cm.filename)
         self.assertEqual(320, cm.lineno)

      Este método funciona independientemente de los filtros de aviso
      que estén en su lugar cuando se llame.

      Added in version 3.2.

      Distinto en la versión 3.3: Añadido el argumento por palabra
      clave *msg* cuando se emplea un gestor de contexto.

   assertWarnsRegex(warning, regex, callable, *args, **kwds)
   assertWarnsRegex(warning, regex, *, msg=None)

      Como "assertWarns()" pero también testea que *regex* coincide en
      el mensaje del aviso disparado.  *regex* puede ser un objeto de
      expresión regular o una cadena que contiene una expresión
      regular adecuada para ser usada por "re.search()".  Ejemplo:

         self.assertWarnsRegex(DeprecationWarning,
                               r'legacy_function\(\) is deprecated',
                               legacy_function, 'XYZ')

      o:

         with self.assertWarnsRegex(RuntimeWarning, 'unsafe frobnicating'):
             frobnicate('/etc/passwd')

      Added in version 3.2.

      Distinto en la versión 3.3: Añadido el argumento por palabra
      clave *msg* cuando se emplea un gestor de contexto.

   assertLogs(logger=None, level=None)

      Un gestor de contexto para comprobar que al menos un mensaje
      está registrado en el *logger* o en uno de sus hijos, con al
      menos el *level* dado.

      Si se da, *logger* debería ser un objeto "logging.Logger" o un
      "str" dando el nombre de un logger.  El valor por defecto es el
      root logger, que captará todos los mensajes.

      Si se da, *level* debería ser un nivel de registro numérico o su
      equivalente en cadena de caracteres (por ejemplo, ya sea
      ""ERROR"" o "logging.ERROR").  El valor predeterminado es
      "logging.INFO".

      El test pasa si al menos un mensaje emitido dentro del bloque
      "with"  coincide con las condiciones de *logger* y *level*, de
      lo contrario falla.

      El objeto devuelto por el gestor de contexto es un ayudante de
      grabación que lleva un registro de los mensajes de registro que
      coinciden.  Tiene dos atributos:

      records

         Una lista de objetos "logging.LogRecord" de los mensajes de
         log coincidentes.

      output

         Una lista de objetos "str" con la salida forrajeada en los
         mensajes coincidentes.

      Ejemplo:

         with self.assertLogs('foo', level='INFO') as cm:
             logging.getLogger('foo').info('first message')
             logging.getLogger('foo.bar').error('second message')
         self.assertEqual(cm.output, ['INFO:foo:first message',
                                      'ERROR:foo.bar:second message'])

      Added in version 3.4.

   assertNoLogs(logger=None, level=None)

      Un gestor de contexto para comprobar que al menos un mensaje
      está registrado en el *logger* o en uno de sus hijos, con al
      menos el *level* dado.

      Si se da, *logger* debería ser un objeto "logging.Logger" o un
      "str" dándole el nombre de un logger.  El valor por defecto es
      el root logger, que captará todos los mensajes.

      Si se da, *level* debería ser un nivel de registro numérico o su
      equivalente en cadena de caracteres (por ejemplo, ya sea
      ""ERROR"" o "logging.ERROR").  El valor predeterminado es
      "logging.INFO".

      A diferencia de "assertLogs()", el gestor de contexto no
      devolverá nada.

      Added in version 3.10.

   Hay también otros métodos empleados para realizar comprobaciones
   más específicas, tales como:

   +-----------------------------------------+----------------------------------+----------------+
   | Método                                  | Comprueba que                    | Nuevo en       |
   |=========================================|==================================|================|
   | "assertAlmostEqual(a, b)"               | "round(a-b, 7) == 0"             |                |
   +-----------------------------------------+----------------------------------+----------------+
   | "assertNotAlmostEqual(a, b)"            | "round(a-b, 7) != 0"             |                |
   +-----------------------------------------+----------------------------------+----------------+
   | "assertGreater(a, b)"                   | "a > b"                          | 3.1            |
   +-----------------------------------------+----------------------------------+----------------+
   | "assertGreaterEqual(a, b)"              | "a >= b"                         | 3.1            |
   +-----------------------------------------+----------------------------------+----------------+
   | "assertLess(a, b)"                      | "a < b"                          | 3.1            |
   +-----------------------------------------+----------------------------------+----------------+
   | "assertLessEqual(a, b)"                 | "a <= b"                         | 3.1            |
   +-----------------------------------------+----------------------------------+----------------+
   | "assertRegex(s, r)"                     | "r.search(s)"                    | 3.1            |
   +-----------------------------------------+----------------------------------+----------------+
   | "assertNotRegex(s, r)"                  | "not r.search(s)"                | 3.2            |
   +-----------------------------------------+----------------------------------+----------------+
   | "assertCountEqual(a, b)"                | *a* contains the same elements   | 3.2            |
   |                                         | as *b*, regardless of their      |                |
   |                                         | order.                           |                |
   +-----------------------------------------+----------------------------------+----------------+
   | "assertStartsWith(a, b)"                | "a.startswith(b)"                | 3.14           |
   +-----------------------------------------+----------------------------------+----------------+
   | "assertNotStartsWith(a, b)"             | "not a.startswith(b)"            | 3.14           |
   +-----------------------------------------+----------------------------------+----------------+
   | "assertEndsWith(a, b)"                  | "a.endswith(b)"                  | 3.14           |
   +-----------------------------------------+----------------------------------+----------------+
   | "assertNotEndsWith(a, b)"               | "not a.endswith(b)"              | 3.14           |
   +-----------------------------------------+----------------------------------+----------------+
   | "assertHasAttr(a, b)"                   | "hasattr(a, b)"                  | 3.14           |
   +-----------------------------------------+----------------------------------+----------------+
   | "assertNotHasAttr(a, b)"                | "not hasattr(a, b)"              | 3.14           |
   +-----------------------------------------+----------------------------------+----------------+

   assertAlmostEqual(first, second, places=7, msg=None, delta=None)
   assertNotAlmostEqual(first, second, places=7, msg=None, delta=None)

      Testea que *first* y *second* son aproximadamente (o no
      aproximadamente) iguales calculando su diferencia, redondeando
      al número dado de puntos *places* decimales (por defecto 7), y
      comparado a cero. Nótese que estos métodos redondean los valores
      al número dado de *puntos decimales* (por ejemplo como la
      función "round()") y no *cifras significativas*.

      Si se suministra *delta* en vez de *places* que entonces la
      diferencia entre *first* y *second* deba ser menor o igual a (o
      mayor que) *delta*.

      Suministrar tanto *delta* como *places* lanza un "TypeError".

      Distinto en la versión 3.2: "assertAlmostEqual()" considera
      automáticamente casi iguales a los objetos que se comparan
      igual. "assertNotAlmostEqual()" falla automáticamente si los
      objetos comparan iguales.  Añadido el argumento de palabra clave
      *delta*.

   assertGreater(first, second, msg=None)
   assertGreaterEqual(first, second, msg=None)
   assertLess(first, second, msg=None)
   assertLessEqual(first, second, msg=None)

      Prueba que *first* es respectivamente >, >=, < o <= que *second*
      dependiendo del nombre del método.  Si no, el test fallará:

         >>> self.assertGreaterEqual(3, 4)
         AssertionError: "3" unexpectedly not greater than or equal to "4"

      Added in version 3.1.

   assertRegex(text, regex, msg=None)
   assertNotRegex(text, regex, msg=None)

      Testea que una búsqueda *regex* coincide (o no coincide) con el
      *text*.  En caso de fallo, el mensaje de error incluirá el
      patrón y el *text* (o el patrón y la parte de *text* que
      coincida inesperadamente).  *regex* puede ser un objeto de
      expresión regular o una cadena que contiene una expresión
      regular adecuada para ser utilizada por "re.search()".

      Added in version 3.1: Añadido bajo el nombre de
      "assertRegexpMatches".

      Distinto en la versión 3.2: El método "assertRegexpMatches()" ha
      sido renombrado a "assertRegex()".

      Added in version 3.2: "assertNotRegex()".

   assertCountEqual(first, second, msg=None)

      Testea que la secuencia *first* contiene los mismos elementos
      que *second*, independientemente de su orden. Cuando no lo
      hagan, se generará un mensaje de error con las diferencias entre
      las secuencias.

      Los elementos duplicados *no* son ignorados cuando se comparan
      *first* y *second*. Verifica si cada elemento tiene la misma
      cuenta en ambas secuencias. Equivalente a:
      "assertEqual(Counter(list(first)), Counter(list(second)))" pero
      funciona también con secuencias de objetos que no son hashable.

      Added in version 3.2.

   assertStartsWith(s, prefix, msg=None)

   assertNotStartsWith(s, prefix, msg=None)

      Test that the Unicode or byte string *s* starts (or does not
      start) with a *prefix*. *prefix* can also be a tuple of strings
      to try.

      Added in version 3.14.

   assertEndsWith(s, suffix, msg=None)

   assertNotEndsWith(s, suffix, msg=None)

      Test that the Unicode or byte string *s* ends (or does not end)
      with a *suffix*. *suffix* can also be a tuple of strings to try.

      Added in version 3.14.

   assertHasAttr(obj, name, msg=None)

   assertNotHasAttr(obj, name, msg=None)

      Test that the object *obj* has (or has not) an attribute *name*.

      Added in version 3.14.

   El método "assertEqual()" envía la comprobación de igualdad de los
   objetos del mismo tipo a diferentes métodos específicos de tipo.
   Estos métodos ya están implementados para la mayoría de los tipos
   incorporados, pero también es posible registrar nuevos métodos
   usando "addTypeEqualityFunc()":

   addTypeEqualityFunc(typeobj, function)

      Registra un método específico de tipo llamado por
      "assertEqual()" para comprobar si dos objetos del mismo
      *typeobj* (no subclases) comparan como iguales.  *function* debe
      tomar dos argumentos posicionales y un tercer argumento de
      palabra clave msg=None tal y como lo hace "assertEqual()".  Debe
      lanzar   "self.failureException(msg)" cuando se detecta una
      desigualdad entre los dos primeros parámetros, posiblemente
      proporcionando información útil y explicando las desigualdades
      en detalle en el mensaje de error.

      Added in version 3.1.

   La lista de métodos específicos de tipo utilizados automáticamente
   por "assertEqual()" se resumen en la siguiente tabla.  Tenga en
   cuenta que normalmente no es necesario invocar estos métodos
   directamente.

   +-------------------------------------------+-------------------------------+----------------+
   | Método                                    | Usado para comparar           | Nuevo en       |
   |===========================================|===============================|================|
   | "assertMultiLineEqual(a, b)"              | strings                       | 3.1            |
   +-------------------------------------------+-------------------------------+----------------+
   | "assertSequenceEqual(a, b)"               | sequences                     | 3.1            |
   +-------------------------------------------+-------------------------------+----------------+
   | "assertListEqual(a, b)"                   | lists                         | 3.1            |
   +-------------------------------------------+-------------------------------+----------------+
   | "assertTupleEqual(a, b)"                  | tuples                        | 3.1            |
   +-------------------------------------------+-------------------------------+----------------+
   | "assertSetEqual(a, b)"                    | sets or frozensets            | 3.1            |
   +-------------------------------------------+-------------------------------+----------------+
   | "assertDictEqual(a, b)"                   | dicts                         | 3.1            |
   +-------------------------------------------+-------------------------------+----------------+

   assertMultiLineEqual(first, second, msg=None)

      Testea que la cadena multilínea *first* es igual a la cadena
      *second*. Cuando no sea igual, una diferencia de las dos cadenas
      que resalte las diferencias se incluirá en el mensaje de error.
      Este método se utiliza por defecto cuando se comparan cadenas
      con "assertEqual()".

      Added in version 3.1.

   assertSequenceEqual(first, second, msg=None, seq_type=None)

      Testea que dos secuencias son iguales.  Si se suministra un
      *seq_type*, tanto *first* como  *second* deben ser instancias de
      *seq_type* o se lanzará un fallo.  Si las secuencias son
      diferentes se construye un mensaje de error que muestra la
      diferencia entre las dos.

      Este método no es llamado directamente por "assertEqual()", pero
      se usa para implementar "assertListEqual()" y
      "assertTupleEqual()".

      Added in version 3.1.

   assertListEqual(first, second, msg=None)
   assertTupleEqual(first, second, msg=None)

      Testea que dos listas o tuplas son iguales.  Si no es así, se
      construye un mensaje de error que muestra sólo las diferencias
      entre las dos.  También se lanza un error si alguno de los
      parámetros es del tipo equivocado. Estos métodos se utilizan por
      defecto cuando se comparan listas o tuplas con "assertEqual()".

      Added in version 3.1.

   assertSetEqual(first, second, msg=None)

      Testea que dos conjuntos son iguales.  Si no es así, se
      construye un mensaje de error que enumera las diferencias entre
      los conjuntos.  Este método se utiliza por defecto cuando se
      comparan los conjuntos o frozensets con "assertEqual()".

      Fails if either of *first* or *second* does not have a
      "difference()" method.

      Added in version 3.1.

   assertDictEqual(first, second, msg=None)

      Testea que dos diccionarios son iguales.  Si no es así, se
      construye un mensaje de error que muestra las diferencias en los
      diccionarios. Este método se usará por defecto para comparar los
      diccionarios en las llamadas a "assertEqual()".

      Added in version 3.1.

   Finalmente, "TestCase" proporciona los siguientes métodos y
   atributos:

   fail(msg=None)

      Señala un fallo del test incondicionalmente, con *msg* o  "None"
      para el mensaje de error.

   failureException

      Este atributo de clase da la excepción lanzada por el método de
      test.  Si un marco de pruebas necesita utilizar una excepción
      especializada, posiblemente para llevar información adicional,
      debe subclasificar esta excepción para "jugar limpio" con el
      marco.  El valor inicial de este atributo es "AssertionError".

   longMessage

      Este atributo de clase determina lo que ocurre cuando se pasa un
      mensaje de fallo personalizado como el argumento msg a una
      llamada assertXYY que falla. "True" es el valor por defecto. En
      este caso, el mensaje personalizado se añade al final del
      mensaje de fallo estándar. Cuando se establece en "False", el
      mensaje personalizado reemplaza al mensaje estándar.

      La configuración de la clase puede ser anulada en los métodos de
      test individuales asignando un atributo de instancia,
      self.longMessage, a "True" o "False" antes de llamar a los
      métodos assert.

      La configuración de la clase se reajusta antes de cada llamada
      de test.

      Added in version 3.1.

   maxDiff

      Este atributo controla la longitud máxima de las diferencias de
      salida de métodos assert que reportan diferencias en caso de
      fallo. El valor predeterminado es de 80*8 caracteres. Los
      métodos assert afectados por este atributo son
      "assertSequenceEqual()" (incluyendo todos los métodos de
      comparación de secuencias que le delegan), "assertDictEqual()" y
      "assertMultiLineEqual()".

      Poner "maxDiff" en "None" significa que no hay una longitud
      máxima de diferencias.

      Added in version 3.2.

   Los marcos de test pueden utilizar los siguientes métodos para
   reunir información sobre el test:

   countTestCases()

      Retorna el número de tests representados por este objeto de
      test.  Para las instancias de "TestCase", este siempre será "1".

   defaultTestResult()

      Retorna una instancia de la clase de resultado de test que
      debería utilizarse para esta clase de caso de test (si no se
      proporciona otra instancia de resultado al método "run()").

      Para las instancias de "TestCase", ésta siempre será una
      instancia de "TestResult"; las subclases de "TestCase" deben
      anular esto según sea necesario.

   id()

      Devuelva una cadena que identifique el caso de test específico.
      Normalmente es el nombre completo del método de test, incluyendo
      el nombre del módulo y de la clase.

   shortDescription()

      Devuelve una descripción de la prueba, o "None" si no se ha
      proporcionado ninguna descripción.  La implementación por
      defecto de este método devuelve la primera línea de la docstring
      del método de test, si está disponible, o  "None" .

      Distinto en la versión 3.1: En 3.1 esto se cambió para añadir el
      nombre del test a la descripción corta incluso en presencia de
      una docstring.  Esto causó problemas de compatibilidad con las
      extensiones de unittest y la adición del nombre de test  fue
      movida a la "TextTestResult" en Python 3.2.

   addCleanup(function, /, *args, **kwargs)

      Añade una función que se llamará después de "tearDown()" a los
      recursos de limpieza utilizados durante el test. Las funciones
      se llamarán en orden inverso al orden en que se agregan (LIFO
      (last-in, first-out)).  Se llaman con cualquier argumento y
      argumentos de palabra clave que se pase a "addCleanup()" cuando
      se agregan.

      Si "setUp()" falla, lo que significa que "tearDown()" no se
      llama, entonces cualquier función de limpieza añadida seguirá
      siendo llamada.

      Added in version 3.1.

   enterContext(cm)

      Introduce el gestor de contexto "context()" suministrado. Si es
      exitoso, añade también su método "__exit__()" como función de
      limpieza mediante "addCleanup()" y retorna el resultado del
      método "__enter__()".

      Added in version 3.11.

   doCleanups()

      Este método se llama incondicionalmente después de
      "tearDown()",  o después de "setUp()"  si "setUp()" lanza una
      excepción.

      Es responsable de llamar a todas las funciones de limpieza
      añadidas por "addCleanup()". Si necesitas que las funciones de
      limpieza se llamen *con anterioridad* a "tearDown()" entonces
      puedes llamar a "doCleanups()" tú mismo.

      "doCleanups()" saca los métodos de la pila de funciones de
      limpieza uno a uno, así que se puede llamar en cualquier
      momento.

      Added in version 3.1.

   classmethod addClassCleanup(function, /, *args, **kwargs)

      Añade una función que se llamará después de "tearDownClass()"
      para limpiar recursos utilizados durante la clase de test. Las
      funciones se llamarán en orden inverso al orden en que se
      agregan (LIFO (last-in, first-out)). Se llaman con cualquier
      argumento y argumento de palabra clave que se pase a
      "addClassCleanup()" cuando se añadan.

      Si "setUpClass()" falla, lo que significa que "tearDownClass()"
      no se invoca, entonces cualquier función de limpieza añadida
      seguirá siendo llamada.

      Added in version 3.8.

   classmethod enterClassContext(cm)

      Introduce el *context manager* suministrado. Si es exitoso,
      añade también su método "__exit__()" como función de limpieza
      mediante "addClassCleanup()" y retorna el resultado del método
      "__enter__()".

      Added in version 3.11.

   classmethod doClassCleanups()

      Este método se llama incondicionalmente después de
      "tearDownClass()", o después de "setUpClass()"  si
      "setUpClass()" lanza una excepción.

      Es responsable de llamar a todas las funciones de limpieza
      añadidas por "addCleanupClass()". Si necesitas que las funciones
      de limpieza se llamen *con anterioridad* a "tearDownClass()"
      entonces puedes llamar a "doCleanupsClass()" tú mismo.

      "doCleanupsClass()" saca los métodos de la pila de funciones de
      limpieza de uno en uno, así que se puede llamar en cualquier
      momento.

      Added in version 3.8.

class unittest.IsolatedAsyncioTestCase(methodName='runTest')

   Esta clase proporciona una API similar a "TestCase" y también
   acepta corutinas como funciones de test.

   Added in version 3.8.

   loop_factory

      The *loop_factory* passed to "asyncio.Runner". Override in
      subclasses with "asyncio.EventLoop" to avoid using the asyncio
      policy system.

      Added in version 3.13.

   async asyncSetUp()

      Method called to prepare the test fixture. This is called after
      "TestCase.setUp()". This is called immediately before calling
      the test method; other than "AssertionError" or "SkipTest", any
      exception raised by this method will be considered an error
      rather than a test failure. The default implementation does
      nothing.

   async asyncTearDown()

      Method called immediately after the test method has been called
      and the result recorded.  This is called before "tearDown()".
      This is called even if the test method raised an exception, so
      the implementation in subclasses may need to be particularly
      careful about checking internal state.  Any exception, other
      than "AssertionError" or "SkipTest", raised by this method will
      be considered an additional error rather than a test failure
      (thus increasing the total number of reported errors). This
      method will only be called if the "asyncSetUp()" succeeds,
      regardless of the outcome of the test method. The default
      implementation does nothing.

   addAsyncCleanup(function, /, *args, **kwargs)

      Este método acepta una corutina que puede ser utilizada como
      función de limpieza.

   async enterAsyncContext(cm)

      Introduce el *asynchronous context manager* suministrado. Si es
      exitoso, añade también su método "__aexit__()" como función de
      limpieza mediante "addAsyncCleanup()" y retorna el resultado del
      método "__aenter__()".

      Added in version 3.11.

   run(result=None)

      Sets up a new event loop to run the test, collecting the result
      into the "TestResult" object passed as *result*.  If *result* is
      omitted or "None", a temporary result object is created (by
      calling the "defaultTestResult()" method) and used. The result
      object is returned to "run()"'s caller. At the end of the test
      all the tasks in the event loop are cancelled.

   Un ejemplo ilustrando el orden:

      from unittest import IsolatedAsyncioTestCase

      events = []

      class Test(IsolatedAsyncioTestCase):

          def setUp(self):
              events.append("setUp")

          async def asyncSetUp(self):
              self._async_connection = await AsyncConnection()
              events.append("asyncSetUp")

          async def test_response(self):
              events.append("test_response")
              response = await self._async_connection.get("https://example.com")
              self.assertEqual(response.status_code, 200)
              self.addAsyncCleanup(self.on_cleanup)

          def tearDown(self):
              events.append("tearDown")

          async def asyncTearDown(self):
              await self._async_connection.close()
              events.append("asyncTearDown")

          async def on_cleanup(self):
              events.append("cleanup")

      if __name__ == "__main__":
          unittest.main()

   Después de ejecutar el test,  "events" contendría  "[“setUp”,
   “asyncSetUp”, “test_response”, “asyncTearDown”, “tearDown”,
   “cleanup”]".

class unittest.FunctionTestCase(testFunc, setUp=None, tearDown=None, description=None)

   This class implements the portion of the "TestCase" interface which
   allows the test runner to drive the test, but does not provide the
   methods which test code can use to check and report errors.  This
   is used to create test cases using legacy test code, allowing it to
   be integrated into a "unittest"-based test framework.

### Agrupando tests

class unittest.TestSuite(tests=())

   Esta clase representa una agregación de casos de test individuales
   y conjuntos de tests. La clase presenta la interfaz que necesita el
   corredor de tests para poder ser ejecutado como cualquier otro caso
   de test.  Ejecutar una instancia "TestSuite" es lo mismo que iterar
   sobre el conjunto, ejecutando cada test individualmente.

   Si se indican *tests*, debe ser un iterable de casos de test
   individuales u otros conjuntos de tests que se usarán para
   construir el conjunto inicialmente. Se proporcionan métodos
   adicionales para añadir casos de test y conjuntos a la colección
   más adelante.

   Los objetos de "TestSuite" se comportan de manera muy parecida a
   los objetos de "TestCase", excepto que no implementan un test.  En
   cambio, se usan para agregar tests en grupos de tests que deben ser
   ejecutados juntos. Existen algunos métodos adicionales para agregar
   tests a las instancias de "TestSuite":

   addTest(test)

      Añade un "TestCase" o "TestSuite" al conjunto.

   addTests(tests)

      Añade todos los tests de un iterable de "TestCase" y "TestSuite"
      a este conjunto de tests.

      Esto equivale a iterar sobre *tests*, llamando a "addTest()"
      para cada elemento.

   "TestSuite" comparte los siguientes métodos con "TestCase":

   run(result)

      Ejecuta los tests asociados a este conjunto, recogiendo el
      resultado en el objeto de resultado del test pasado como
      *result*.  Tenga en cuenta que a diferencia de "TestCase.run()",
      "TestSuite.run()" requiere que se pase el objeto resultado.

   debug()

      Ejecuta los tests asociados con este conjunto sin recoger los
      resultados. Esto permite que las excepciones lanzadas por este
      test sean propagadas al invocador y puedes ser usadas para
      apoyar tests que están ejecutándose con un debugger.

   countTestCases()

      Retorna el numero de tests representados por este objeto de
      test, incluidos todos los test individuales y los sub-conjuntos.

   __iter__()

      Tests grouped by a "TestSuite" are always accessed by iteration.
      Subclasses can lazily provide tests by overriding "__iter__()".
      Note that this method may be called several times on a single
      suite (for example when counting tests or comparing for
      equality) so the tests returned by repeated iterations before
      "TestSuite.run()" must be the same for each call iteration.
      After "TestSuite.run()", callers should not rely on the tests
      returned by this method unless the caller uses a subclass that
      overrides "TestSuite._removeTestAtIndex()" to preserve test
      references.

      Distinto en la versión 3.2: In earlier versions the "TestSuite"
      accessed tests directly rather than through iteration, so
      overriding "__iter__()" wasn't sufficient for providing tests.

      Distinto en la versión 3.4: In earlier versions the "TestSuite"
      held references to each "TestCase" after "TestSuite.run()".
      Subclasses can restore that behavior by overriding
      "TestSuite._removeTestAtIndex()".

   In the typical usage of a "TestSuite" object, the "run()" method is
   invoked by a "TestRunner" rather than by the end-user test harness.

### Cargando y ejecutando tests

class unittest.TestLoader

   The "TestLoader" class is used to create test suites from classes
   and modules.  Normally, there is no need to create an instance of
   this class; the "unittest" module provides an instance that can be
   shared as "unittest.defaultTestLoader".  Using a subclass or
   instance, however, allows customization of some configurable
   properties.

   Los objetos "TestLoader"  tienen los siguientes atributos:

   errors

      Una lista de los errores no fatales encontrados durante la carga
      de tests. No reseteados por el cargador en ningún momento. Los
      errores fatales son señalados por el método relevante que lanza
      una excepción al invocador. Los errores no fatales también son
      indicados por una prueba sintética que lanzará el error original
      cuando se ejecute.

      Added in version 3.5.

   Los objetos "TestLoader" tienen los siguientes métodos:

   loadTestsFromTestCase(testCaseClass)

      Return a suite of all test cases contained in the
      "TestCase"-derived "testCaseClass".

      A test case instance is created for each method named by
      "getTestCaseNames()". By default these are the method names
      beginning with "test". If "getTestCaseNames()" returns no
      methods, but the "runTest()" method is implemented, a single
      test case is created for that method instead.

   loadTestsFromModule(module, *, pattern=None)

      Devuelva un conjunto de todos los casos de test contenidos en el
      módulo dado. Este método busca en *module* clases derivadas de
      "TestCase" y crea una instancia de la clase para cada método de
      test definido para la clase.

      Nota:

        Aunque el uso de una jerarquía de clases derivadas de
        "TestCase"  puede ser conveniente para compartir
        configuraciones y funciones de ayuda, la definición de métodos
        de test en clases base que no están destinadas a ser
        instanciadas directamente no complementa bien con este método.
        Hacerlo, sin embargo, puede ser útil cuando las
        configuraciones son diferentes y están definidas en subclases.

      Si un módulo proporciona una función "load_tests" será llamado
      para cargar los tests. Esto permite a los módulos personalizar
      la carga de los tests. Este es el load_tests protocol.  El
      argumento *pattern* se pasa como tercer argumento a
      "load_tests".

      Distinto en la versión 3.2: Se ha añadido soporte para
      "load_tests".

      Distinto en la versión 3.5: Se ha agregado soporte para un
      argumento *pattern* de solo palabra clave.

      Distinto en la versión 3.12: El parámetro no documentado y no
      oficial *use_load_tests* ha sido eliminado.

   loadTestsFromName(name, module=None)

      Retorna un conjunto de todos los casos de test dado un
      especificador de cadena.

      El especificador *name* es un "nombre punteado" que puede
      resolverse ya sea a un módulo, una clase de caso de test, un
      método de test dentro de una clase de caso de test, una
      instancia "TestSuite", o un objeto invocable que devuelve una
      instancia "TestCase" o "TestSuite".  Estas comprobaciones se
      aplican en el orden que se indica aquí; es decir, un método en
      una posible clase de caso de test se recogerá como "un método de
      test dentro de una clase de caso de test”, en lugar de "un
      objeto invocable”.

      For example, if you have a module "SampleTests" containing a
      "TestCase"-derived class "SampleTestCase" with three test
      methods ("test_one()", "test_two()", and "test_three()"), the
      specifier "'SampleTests.SampleTestCase'" would cause this method
      to return a suite which will run all three test methods. Using
      the specifier "'SampleTests.SampleTestCase.test_two'" would
      cause it to return a test suite which will run only the
      "test_two()" test method. The specifier can refer to modules and
      packages which have not been imported; they will be imported as
      a side-effect.

      El método opcionalmente resuelve *name* relativo al *module*
      dado.

      Distinto en la versión 3.5: Si un "ImportError" o
      "AttributeError" ocurre mientras atraviesa *name* entonces se
      devolverá un test sintético que lanza ese error cuando se
      ejecuta. Estos errores están incluidos en los errores acumulados
      por self.errors.

   loadTestsFromNames(names, module=None)

      Similar a "loadTestsFromName()", pero toma una secuencia de
      nombres en lugar de un solo nombre.  El valor de retorno es una
      suite de tests que soporta todos los test  definidos para cada
      nombre.

   getTestCaseNames(testCaseClass)

      Devuelve una secuencia ordenada de nombres de métodos
      encontrados dentro de *testCaseClass*; esta debería ser una
      subclase de "TestCase".

   discover(start_dir, pattern='test*.py', top_level_dir=None)

      Encuentra todos los módulos de prueba recurriendo a
      subdirectorios del directorio de inicio especificado, y retorna
      un objeto de TestSuite que los contenga. Sólo se cargarán los
      archivos de test que coincidan con el *pattern*. (Utilizando la
      coincidencia de patrones de estilo de shell.) Sólo se cargarán
      los nombres de los módulos que sean importables (es decir, que
      sean identificadores Python válidos).

      All test modules must be importable from the top level of the
      project. If the start directory is not the top level directory
      then *top_level_dir* must be specified separately.

      Si la importación de un módulo falla, por ejemplo debido a un
      error de sintaxis, entonces esto se registrará como un error
      único y el descubrimiento continuará.  Si el fallo en la
      importación se debe a que "SkipTest" se ha lanzado, se
      registrará como un salto en lugar de un error.

      Si se encuentra un paquete (un directorio que contiene un
      archivo llamado "__init__.py"), se comprobará si el paquete
      tiene una función "load_tests". Si existe, entonces se invocará
      "package.load_tests(loader, tests, pattern)". Test discovery se
      encarga de asegurar que un paquete sólo se comprueba una vez
      durante una invocación, incluso si la propia función load_tests
      llama a "loader.discover".

      Si "load_tests" existe, entonces el descubrimiento *no* recurre
      en el paquete, "load_tests" es responsable de cargar todos los
      tests en el paquete.

      The pattern is deliberately not stored as a loader attribute so
      that packages can continue discovery themselves.

      *top_level_dir* is stored internally, and used as a default to
      any nested calls to "discover()". That is, if a package's
      "load_tests" calls "loader.discover()", it does not need to pass
      this argument.

      *start_dir* puede ser un nombre de módulo punteado así como un
      directorio.

      Added in version 3.2.

      Distinto en la versión 3.4: Los módulos que lanzan "SkipTest" en
      la importación se registran como saltos, no como
      errores.*start_dir* puede ser un *paquete de espacios de
      nombres*.Las rutas se ordenan antes de ser importadas para que
      el orden de ejecución sea el mismo, incluso si el orden del
      sistema de archivos subyacente no depende del nombre del
      archivo.

      Distinto en la versión 3.5: Los paquetes encontrados son ahora
      comprobados para "load_tests" sin importar si su ruta coincide
      con el *pattern*, porque es imposible que el nombre de un
      paquete coincida con el patrón por defecto.

      Distinto en la versión 3.11: *start_dir* can not be a *namespace
      packages*. It has been broken since Python 3.7, and Python 3.11
      officially removes it.

      Distinto en la versión 3.13: *top_level_dir* is only stored for
      the duration of *discover* call.

      Distinto en la versión 3.14: *start_dir* can once again be a
      *namespace package*.

   Los siguientes atributos de un "TestLoader" pueden ser configurados
   ya sea por subclasificación o asignación en una instancia:

   testMethodPrefix

      Cadena que da el prefijo de los nombres de métodos que serán
      interpretados como métodos de test.  El valor por defecto es
      "'test'".

      This affects "getTestCaseNames()" and all the "loadTestsFrom*"
      methods.

   sortTestMethodsUsing

      Function to be used to compare method names when sorting them in
      "getTestCaseNames()" and all the "loadTestsFrom*" methods.

   suiteClass

      Objeto invocable que construye un conjunto de pruebas a partir
      de una lista de pruebas. No se necesitan métodos en el objeto
      resultante.  El valor por defecto es la clase "TestSuite".

      This affects all the "loadTestsFrom*" methods.

   testNamePatterns

      Lista de patrones de nombres de test de comodines al estilo del
      shell de Unix que los métodos de test tienen que coincidir con
      para ser incluidos en las suites de test (ver opción "-k").

      Si este atributo no es "None" (el predeterminado), todos los
      métodos de test que se incluyan en los paquetes de test deben
      coincidir con uno de los patrones de esta lista. Tenga en cuenta
      que las coincidencias se realizan siempre utilizando
      "fnmatch.fnmatchcase()", por lo que a diferencia de los patrones
      pasados a la opción "-k", los patrones de subcadena simple
      tendrán que ser convertidos utilizando comodines "*".

      This affects all the "loadTestsFrom*" methods.

      Added in version 3.7.

class unittest.TestResult

   Esta clase se utiliza para recopilar información sobre qué tests
   han tenido éxito y cuáles han fracasado.

   Un objeto  "TestResult"  almacena los resultados de una serie de
   pruebas.  Las clases "TestCase" y "TestSuite" aseguran que los
   resultados se registren correctamente; los autores de los tests no
   tienen que preocuparse de registrar el resultado de las mismas.

   Testing frameworks built on top of "unittest" may want access to
   the "TestResult" object generated by running a set of tests for
   reporting purposes; a "TestResult" instance is returned by the
   "TestRunner.run()" method for this purpose.

   Las instancias de "TestResult" tienen los siguientes atributos que
   serán de interés cuando se inspeccionen los resultados de la
   ejecución de un conjunto de tests:

   errors

      Una lista que contiene tuplas de 2 elementos de instancias
      "TestCase" y cadenas con formato de tracebacks. Cada tupla
      representa una prueba que lanzó una excepción inesperada.

   failures

      A list containing 2-tuples of "TestCase" instances and strings
      holding formatted tracebacks. Each tuple represents a test where
      a failure was explicitly signalled using the assert* methods.

   skipped

      Una lista que contiene tuplas de 2 elementos de instancias de
      "TestCase" y cadenas que contienen la razón para saltarse el
      test.

      Added in version 3.1.

   expectedFailures

      Una lista que contiene tuplas de 2 elementos de instancias
      "TestCase" y cadenas con formato de traceback.  Cada tupla
      representa un fallo esperado del caso de test.

   unexpectedSuccesses

      Una lista que contiene instancias de  "TestCase"  que fueron
      marcadas como fracasos esperados, pero tuvieron éxito.

   collectedDurations

      Una lista que contiene tuplas de 2 elementos con nombres de
      casos de prueba y números flotantes que representan el tiempo
      transcurrido de cada prueba que se ejecutó.

      Added in version 3.12.

   shouldStop

      Puesto en "True" cuando la ejecución de los tests se detenga por
      "stop()".

   testsRun

      El número total de tests realizados hasta ahora.

   buffer

      Si se ajusta a true, "sys.stdout" y "sys.stderr" serán
      almacenados entre "startTest()" y "stopTest()" siendo llamados.
      La salida recolectada sólo tendrá eco en el verdadero
      "sys.stdout" y "sys.stderr" si la prueba falla o se equivoca.
      Cualquier salida también se adjunta al mensaje de fallo / error.

      Added in version 3.2.

   failfast

      Si se ajusta a true "stop()" se llamará al primer fallo o error,
      deteniendo la ejecución de la prueba.

      Added in version 3.2.

   tb_locals

      Si se ajusta a true entonces las variables locales se mostrarán
      en los tracebacks.

      Added in version 3.5.

   wasSuccessful()

      Devuelve "True" si todas las pruebas realizadas hasta ahora han
      pasado, de lo contrario devuelve "False".

      Distinto en la versión 3.4: Returns "False" if there were any
      "unexpectedSuccesses" from tests marked with the
      "@expectedFailure" decorator.

   stop()

      This method can be called to signal that the set of tests being
      run should be aborted by setting the "shouldStop" attribute to
      "True". "TestRunner" objects should respect this flag and return
      without running any additional tests.

      For example, this feature is used by the "TextTestRunner" class
      to stop the test framework when the user signals an interrupt
      from the keyboard.  Interactive tools which provide "TestRunner"
      implementations can use this in a similar manner.

   Los siguientes métodos de la clase "TestResult" se utilizan para
   mantener las estructuras de datos internos, y pueden ampliarse en
   subclases para apoyar los requisitos de información adicionales.
   Esto es particularmente útil para construir herramientas que apoyen
   la presentación de informes interactivos mientras se ejecutan las
   pruebas.

   startTest(test)

      Llamado cuando el caso de prueba *test* está a punto de ser
      ejecutado.

   stopTest(test)

      Llamado después de que el caso de prueba *prueba* haya sido
      ejecutado, independientemente del resultado.

   startTestRun()

      Llamado una vez antes de que se ejecute cualquier prueba.

      Added in version 3.1.

   stopTestRun()

      Llamado una vez después de que se ejecuten todas las pruebas.

      Added in version 3.1.

   addError(test, err)

      Llamado cuando el caso de prueba *test* plantea una excepción
      inesperada. *err* es una tupla de la forma devuelta por
      "sys.exc_info()": "(type, value, traceback)".

      La implementación por defecto añade una tupla "(test,
      formatted_err)" al atributo "errors" de la instancia, donde
      *formatted_err* es una traza formateada derivada de *err*.

   addFailure(test, err)

      Llamado cuando el caso de prueba *test* señala un fallo. *err*
      es una tupla de la forma devuelta por "sys.exc_info()": "(type,
      value, traceback)".

      La implementación por defecto añade una tupla "(test,
      formatted_err)" al atributo "failures" de la instancia, donde
      *formatted_err* es una traza formateada derivada de *err*.

   addSuccess(test)

      Llamado cuando el caso de prueba *test* tenga éxito.

      La implementación por defecto no hace nada.

   addSkip(test, reason)

      Llamado cuando se salta el caso de prueba *test*. *reason* es la
      razón que la prueba dio para saltarse.

      La implementación por defecto añade una tupla "(test, reason)"
      al atributo "skipped" de la instancia.

   addExpectedFailure(test, err)

      Called when the test case *test* fails or errors, but was marked
      with the "@expectedFailure" decorator.

      La implementación por defecto añade una tupla "(test,
      formatted_err)" al atributo "expectedFailures" de la instancia,
      donde *formatted_err* es una traza formateada derivada de *err*.

   addUnexpectedSuccess(test)

      Called when the test case *test* was marked with the
      "@expectedFailure" decorator, but succeeded.

      La implementación por defecto añade la prueba al atributo
      "unexpectedSuccesses" de la instancia.

   addSubTest(test, subtest, outcome)

      Llamado cuando termina una subtest.  *test* es el caso de prueba
      correspondiente al método de test.  *subtest* es una instancia
      personalizada "TestCase" que describe el test.

      Si *outcome* es "None", el subtest tuvo éxito.  De lo contrario,
      falló con una excepción en la que *outcome* es una tupla de la
      forma devuelta por "sys.exc_info()": "(type, value, traceback)".

      La implementación por defecto no hace nada cuando el resultado
      es un éxito, y registra los fallos del subtest como fallos
      normales.

      Added in version 3.4.

   addDuration(test, elapsed)

      Llamado cuando el caso de prueba finaliza.  *elapsed* es el
      tiempo representado en segundos e incluye la ejecución de
      funciones de limpieza.

      Added in version 3.12.

class unittest.TextTestResult(stream, descriptions, verbosity, *, durations=None)

   Una implementación concreta de "TestResult" utilizada por el
   "TextTestRunner". Las subclases deberían aceptar "**kwargs" para
   garantizar la compatibilidad a medida que cambia la interfaz.

   Added in version 3.2.

   Distinto en la versión 3.12: Added the *durations* keyword
   parameter.

unittest.defaultTestLoader

   Instancia de la clase "TestLoader" destinada a ser compartida.  Si
   no es necesario personalizar la clase "TestLoader", esta instancia
   puede utilizarse en lugar de crear repetidamente nuevas instancias.

class unittest.TextTestRunner(stream=None, descriptions=True, verbosity=1, failfast=False, buffer=False, resultclass=None, warnings=None, *, tb_locals=False, durations=None)

   Una implementación básica del test runner que produce resultados en
   una corriente. Si *stream* es "None", el valor por defecto,
   "sys.stderr" se utiliza como flujo de salida. Esta clase tiene unos
   pocos parámetros configurables, pero es esencialmente muy simple.
   Las aplicaciones gráficas que ejecutan las suites de prueba deben
   proporcionar implementaciones alternativas. Tales implementaciones
   deberían aceptar "**kwargs" como interfaz para construir los
   cambios de los corredores cuando se añaden características a
   unittest.

   Por defecto este runner muestra "DeprecationWarning",
   "PendingDeprecationWarning", "ResourceWarning" y "ImportWarning"
   incluso si están ignorados por defecto.  Este comportamiento se
   puede anular utilizando las opciones "-Wd" o "-Wa" de Python
   (consulte Control de advertencias) y dejando *warnings* en "None".

   Distinto en la versión 3.2: Se añadió el argumento *warnings*.

   Distinto en la versión 3.2: El flujo por defecto está configurado
   como "sys.stderr" en tiempo de instanciación en lugar de tiempo de
   importación.

   Distinto en la versión 3.5: Se añadió el parámetro *tb_locals*.

   Distinto en la versión 3.12: Se añadió el parámetro *durations*.

   _makeResult()

      Este método devuelve la instancia de "TestResult" usada por
      "run()". No está destinado a ser llamado directamente, pero
      puede ser anulado en subclases para proporcionar un "TestResult"
      personalizado.

      "_makeResult()" instanciando la clase o el pasaje llamado en el
      constructor "TextTestRunner" como el argumento de "resultclass".
      Por defecto es "TextTestResult" si no se proporciona ninguna
      "resultclass". La clase de resultado se instanciará con los
      siguientes argumentos:

         stream, descriptions, verbosity

   run(test)

      Este método es la principal interfaz pública del
      "TextTestRunner". Este método toma una instancia "TestSuite" o
      "TestCase". Se crea una "TestResult" llamando a "_makeResult()"
      y se ejecuta(n) la(s) prueba(s) y se imprimen los resultados a
      stdout.

unittest.main(module='__main__', defaultTest=None, argv=None, testRunner=None, testLoader=unittest.defaultTestLoader, exit=True, verbosity=1, failfast=None, catchbreak=None, buffer=None, warnings=None)

   Un programa de línea de comandos que carga un conjunto de pruebas
   de *módulo* y las ejecuta; esto es principalmente para hacer los
   módulos de prueba convenientemente ejecutables. El uso más simple
   de esta función es incluir la siguiente línea al final de un guión
   de prueba:

      if __name__ == '__main__':
          unittest.main()

   Puedes hacer pruebas con información más detallada pasando el
   argumento de la verbosity:

      if __name__ == '__main__':
          unittest.main(verbosity=2)

   El argumento *defaultTest* es el nombre de una prueba única o un
   iterable de nombres de pruebas a ejecutar si no se especifican
   nombres de pruebas a través de *argv*.  Si no se especifica o
   "Ninguno" y no se proporcionan nombres de pruebas vía *argv*, se
   ejecutan todas las pruebas encontradas en *modulo*.

   El argumento *argv* puede ser una lista de opciones pasadas al
   programa, siendo el primer elemento el nombre del programa.  Si no
   se especifica o "Ninguno", se utilizan los valores de "sys.argv".

   The *testRunner* argument can either be a test runner class or an
   already created instance of it. By default "main" calls
   "sys.exit()" with an exit code indicating success (0) or failure
   (1) of the tests run. An exit code of 5 indicates that no tests
   were run or skipped.

   El argumento *testLoader* tiene que ser una instancia "TestLoader",
   y por defecto "defaultTestLoader".

   "main" apoya el uso del intérprete interactivo pasando el argumento
   "exit=False". Esto muestra el resultado en la salida estándar sin
   llamar a "sys.exit()":

      >>> from unittest import main
      >>> main(module='test_module', exit=False)

   Los parámetros *failfast*, *catchbreak* y *buffer* tienen el mismo
   efecto que las command-line options del mismo nombre.

   El argumento *warnings* especifica el filtro de aviso que debe ser
   usado mientras se realizan los tests.  Si no se especifica,
   permanecerá como "None" si se pasa una opción "-W" a **python**
   (ver Warning control), de lo contrario se establecerá como
   "’default’".

   Calling "main" returns an object with the "result" attribute that
   contains the result of the tests run as a "unittest.TestResult".

   Distinto en la versión 3.1: El parámetro *exit* fue añadido.

   Distinto en la versión 3.2: Los parámetros *verbosity*, *failfast*,
   *catchbreak*, *buffer* y *warnings* fueron añadidos.

   Distinto en la versión 3.4: El parámetro *defaultTest* fue cambiado
   para aceptar también un iterable de nombres de pruebas.

#### load_tests protocolo

Added in version 3.2.

Los módulos o paquetes pueden personalizar la forma en que se cargan
las pruebas a partir de ellos durante las ejecuciones de prueba
normales o el descubrimiento de pruebas mediante la implementación de
una función llamada "load_tests".

Si un módulo de tests define "load_tests" será llamado por
"TestLoader.loadTestsFromModule()" con los siguientes argumentos:

   load_tests(loader, standard_tests, pattern)

donde *pattern* se pasa directamente desde "loadTestsFromModule".  Por
defecto es "None".

Debe retornar una "TestSuite".

*loader* es la instancia de "TestLoader" haciendo la carga.
*standard_tests* son los tests que se cargarían por defecto desde el
módulo. Es común que los módulos de test sólo quieran añadir o quitar
tests del conjunto de tests estándar. El tercer argumento se usa
cuando se cargan paquetes como parte del descubrimiento de tests.

Una típica función de "load_tests" que carga pruebas de un conjunto
específico de "TestCase`class:`TestCase" puede ser como:

   test_cases = (TestCase1, TestCase2, TestCase3)

   def load_tests(loader, tests, pattern):
       suite = TestSuite()
       for test_class in test_cases:
           tests = loader.loadTestsFromTestCase(test_class)
           suite.addTests(tests)
       return suite

Si discovery se inicia en un directorio que contiene un paquete, ya
sea desde la línea de comandos o llamando a "TestLoader.discover()",
entonces el paquete "__init__.py" se comprobará por "load_tests".  Si
esa función no existe, discover se reincorporará al paquete como si
fuera un directorio más.  De lo contrario, el descubrimiento de los
tests del paquete se dejará en "load_tests" que se llama con los
siguientes argumentos:

   load_tests(loader, standard_tests, pattern)

Esto debería devolver un "TestSuite" que represente todas las pruebas
del paquete. ("test_estándar" sólo contendrá las pruebas recogidas de
"__init__.py".)

Debido a que el patrón se pasa a "load_tests" el paquete es libre de
continuar (y potencialmente modificar) el descubrimiento de pruebas.
Una función de 'no hace nada' "load_test" para un paquete de pruebas
se vería como:

   def load_tests(loader, standard_tests, pattern):
       # top level directory cached on loader instance
       this_dir = os.path.dirname(__file__)
       package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
       standard_tests.addTests(package_tests)
       return standard_tests

Distinto en la versión 3.5: Discovery ya no comprueba si los nombres
de los paquetes coinciden con el *patrón* debido a la imposibilidad de
que los nombres de los paquetes coincidan con el patrón por defecto.

## Instalaciones para clases y módulos

Class and module level fixtures are implemented in "TestSuite". When
the test suite encounters a test from a new class then
"tearDownClass()" from the previous class (if there is one) is called,
followed by "setUpClass()" from the new class.

Del mismo modo, si una prueba es de un módulo diferente de la prueba
anterior, entonces se ejecuta "DesmontarMódulo" del módulo anterior,
seguido de "DesmontarMódulo" del nuevo módulo.

Después de todas las pruebas, se ejecutan los últimos "tearDownClass"
y "tearDownModule".

Tenga en cuenta que los accesorios compartidos no juegan bien con las
características [potenciales] como la paralelización de la prueba y
rompen el aislamiento de la prueba. Deben ser usados con cuidado.

El orden por defecto de las pruebas creadas por los cargadores de
pruebas unitarias es agrupar todas las pruebas de los mismos módulos y
clases. Esto llevará a que "setUpClass" / "setUpModule" (etc) sea
llamado exactamente una vez por clase y módulo. Si se aleatoriza el
orden, de manera que las pruebas de diferentes módulos y clases sean
adyacentes entre sí, entonces estas funciones compartidas de fixture
pueden ser llamadas varias veces en una sola ejecución de prueba.

Los accesorios compartidos no están pensados para trabajar con suites
con pedidos no estándar. Todavía existe una "BaseTestSuite" para los
marcos de trabajo que no quieren soportar accesorios compartidos.

Si hay alguna excepción planteada durante una de las funciones
compartidas del aparato, la prueba se notifica como un error. Debido a
que no hay una instancia de prueba correspondiente, se crea un objeto
"_ErrorHolder" (que tiene la misma interfaz que un "TestCase") para
representar el error. Si sólo estás usando el standard unittest test
runner entonces este detalle no importa, pero si eres un autor de
marcos de trabajo puede ser relevante.

### setUpClass y tearDownClass

Estos deben ser implementados como métodos de clase:

   import unittest

   class Test(unittest.TestCase):
       @classmethod
       def setUpClass(cls):
           cls._connection = createExpensiveConnectionObject()

       @classmethod
       def tearDownClass(cls):
           cls._connection.destroy()

Si quieres que se invoque a "SetUpClass" y "BreakdownClass" en clases
base, debes llamarlos tú mismo. Las implementaciones en  "TestCase"
están vacías.

Si se lanza una excepción durante una "setUpClass", entonces los tests
de la clase no se ejecutan y la "tearDownClass" no se ejecuta. Las
clases que se salten no tendrán "setUpClass" o "tearDownClass". Si la
excepción es una "SkipTest"  entonces la clase será reportada como
salteada en lugar de como un error.

### setUpModule y tearDownModule

Estos deben ser implementados como funciones:

   def setUpModule():
       createConnection()

   def tearDownModule():
       closeConnection()

Si se lanza una excepción en un  "setUpModule", entonces no se
ejecutará ninguna de las pruebas del módulo y no se ejecutará el
"tearDownModule". Si la excepción es una "SkipTest"   entonces el
módulo será reportado como saltado en lugar de como un error.

Para agregar código de limpieza que se debe ejecutar incluso en el
caso de una excepción, utilice "addModuleCleanup":

unittest.addModuleCleanup(function, /, *args, **kwargs)

   Añade una función que se llamará después de "tearDownModule()" para
   limpiar los recursos utilizados durante la clase de test. Las
   funciones se llamarán en orden inverso al orden en que se agregan
   (LIFO (last-in, first-out)). Se llaman con cualquier argumento y
   palabra clave que se pase a "addModuleCleanup()" cuando se añadan.

   Si "setUpModule()" falla, lo que significa que "tearDownModule()"
   no se invoca, entonces cualquier función de limpieza añadida
   seguirá siendo invocada.

   Added in version 3.8.

unittest.enterModuleContext(cm)

   Introduce el *context manager* suministrado. Si es exitoso, añade
   también su método "__exit__()" como función de limpieza mediante
   "addModuleCleanup()" y retorna el resultado del método
   "__enter__()".

   Added in version 3.11.

unittest.doModuleCleanups()

   Esta función se llama incondicionalmente después de
   "tearDownModule()", o después de "setUpModule()" si "setUpModule()"
   lanza una excepción.

   Es responsable de invocar a todas las funciones de limpieza
   añadidas por "addCleanupModule()". Si necesitas que las funciones
   de limpieza se llamen *previamente* a "tearDownModule()" entonces
   puedes invocar a "doModuleCleanups()" tú mismo.

   "doModuleCleanups()" saca los métodos de la pila de funciones de
   limpieza uno a uno, así que se puede llamar en cualquier momento.

   Added in version 3.8.

## Manejo de señales

Added in version 3.2.

The "-c/--catch" command-line option to unittest, along with the
"catchbreak" parameter to "unittest.main()", provide more friendly
handling of control-C during a test run. With catch break behavior
enabled control-C will allow the currently running test to complete,
and the test run will then end and report all the results so far. A
second control-c will raise a "KeyboardInterrupt" in the usual way.

El manejador de señales de manejo de control-c intenta permanecer
compatible con el código o las pruebas que instalan su propio
manejador "signal.SIGINT" . Si se llama al manejador "unittest" pero
*no es* el manejador "signal.SIGINT" instalado, es decir, ha sido
reemplazado por el sistema bajo test y delegado, entonces llama al
manejador por defecto. Este será normalmente el comportamiento
esperado por el código que reemplaza un manejador instalado y delega
en él. Para las pruebas individuales que necesiten el manejo de
control-c de "unittest" deshabilitado se puede usar el decorador
"removeHandler()".

Hay algunas funciones de utilidad para que los autores de marcos de
trabajo habiliten la funcionalidad de control de control-c dentro de
los marcos de prueba.

unittest.installHandler()

   Instala el controlador de control-c. Cuando se recibe una
   "signal.SIGINT"  (normalmente en respuesta a que el usuario
   presione control-c) todos los resultados registrados tienen
   "stop()" llamado.

unittest.registerResult(result)

   Registrar un objeto  "TestResult"  para el manejo de control-c. El
   registro de un resultado almacena una referencia débil a él, por lo
   que no evita que el resultado sea recogido por el recolector de
   basura.

   El registro de un objeto "TestResult" no tiene efectos secundarios
   si el manejo de control-c no está habilitado, por lo que los marcos
   de pruebas pueden registrar incondicionalmente todos los resultados
   que crean independientemente de si el manejo está habilitado o no.

unittest.removeResult(result)

   Elimine un resultado registrado. Una vez que un resultado ha sido
   eliminado, "stop()" ya no se llamará en ese objeto de resultado en
   respuesta a un control-c.

unittest.removeHandler(function=None)

   Cuando se llama sin argumentos, esta función quita el gestor
   control-c si se ha instalado. Esta función también se puede
   utilizar como decorador de tests para quitar temporalmente el
   controlador mientras se ejecuta el test:

      @unittest.removeHandler
      def test_signal_handling(self):
          ...
