---
title: '"unittest.mock" --- getting started'
source_url: https://docs.python.org/es/3
source_path: library/unittest.mock-examples.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4360
---

# "unittest.mock" --- getting started

Added in version 3.3.

## Usando mock

### Mock patching methods

Usos comunes para objetos "Mock" incluye:

* Métodos de parcheo

* Métodos de grabación de llamadas sobre objetos

Es posible que desee reemplazar un método en un objeto para comprobar
que se llama con los argumentos correctos por otra parte del sistema:

>>> real = SomeClass()
>>> real.method = MagicMock(name='method')
>>> real.method(3, 4, 5, key='value')
<MagicMock name='method()' id='...'>

Una vez que se ha utilizado nuestro mock ("real.method" en este
ejemplo) tiene métodos y atributos que le permiten hacer afirmaciones
sobre cómo se ha utilizado.

Nota:

  En la mayoría de estos ejemplos, las clases "Mock" y "MagicMock" son
  intercambiables. Como el "MagicMock" es la clase más capaz, hace que
  sea sensato usarlo por defecto.

Una vez que el mock ha sido llamado su atributo "called" se establece
en "True". Lo que es más importante, podemos usar el método
"assert_called_with()" o "assert_called_once_with()" para comprobar
que se llamó con los argumentos correctos.

En este ejemplo se prueba que llamar a "ProductionClass().method" da
como resultado una llamada al método "something":

>>> class ProductionClass:
...     def method(self):
...         self.something(1, 2, 3)
...     def something(self, a, b, c):
...         pass
...
>>> real = ProductionClass()
>>> real.something = MagicMock()
>>> real.method()
>>> real.something.assert_called_once_with(1, 2, 3)

### Mock for method calls on an object

En el último ejemplo, parcheamos un método directamente en un objeto
para comprobar que se llamó correctamente. Otro caso de uso común es
pasar un objeto a un método (o a alguna parte del sistema sometido a
prueba) y, a continuación, comprobar que se utiliza de la manera
correcta.

La sencilla "ProductionClass" a continuación tiene un método "closer".
Si se llama con un objeto, entonces llama a "close" en él.

>>> class ProductionClass:
...     def closer(self, something):
...         something.close()
...

Así que para probarlo necesitamos pasar un objeto con un método
"close" y comprobar que se llamó correctamente.

>>> real = ProductionClass()
>>> mock = Mock()
>>> real.closer(mock)
>>> mock.close.assert_called_with()

No tenemos que hacer ningún trabajo para proporcionar el método de
'close' en nuestro mock. El acceso al cierre lo crea. Por lo tanto, si
'close' aún no se ha llamado, entonces acceder a él en la prueba lo
creará, pero "assert_called_with()" lanzará una excepción de error.

### Mocking classes

Un caso de uso común es simular las clases que crea la instancia del
código que se está probando. Cuando se aplica un parche a una clase,
esa clase se reemplaza por un mock. Las instancias se crean *llamando
a la clase*. Esto significa que tiene acceso a la "instancia mock"
examinando el valor devuelto de la clase simulada.

En el ejemplo siguiente tenemos una función "some_function" que crea
una instancia de "Foo" y llama a un método en él. La llamada a
"patch()" reemplaza la clase "Foo" con un mock. La instancia "Foo" es
el resultado de llamar al mock, por lo que se configura modificando el
mock "-Mock.return_value".

   >>> def some_function():
   ...     instance = module.Foo()
   ...     return instance.method()
   ...
   >>> with patch('module.Foo') as mock:
   ...     instance = mock.return_value
   ...     instance.method.return_value = 'the result'
   ...     result = some_function()
   ...     assert result == 'the result'

### Nombrando tus mocks

Puede ser útil poner un nombre a tus mocks. El nombre se muestra en la
reproducción del mock y puede ser útil cuando el mock aparece en los
mensajes de error de la prueba. El nombre también se propaga a los
atributos o métodos del mock:

>>> mock = MagicMock(name='foo')
>>> mock
<MagicMock name='foo' id='...'>
>>> mock.method
<MagicMock name='foo.method' id='...'>

### Tracking all calls

A menudo, desea realizar un seguimiento de más de una llamada a un
método. El atributo "mock_calls" registra todas las llamadas a los
atributos secundarios del mock, y también a sus hijos.

>>> mock = MagicMock()
>>> mock.method()
<MagicMock name='mock.method()' id='...'>
>>> mock.attribute.method(10, x=53)
<MagicMock name='mock.attribute.method()' id='...'>
>>> mock.mock_calls
[call.method(), call.attribute.method(10, x=53)]

Si realiza una afirmación sobre "mock_calls" y se ha llamado a
cualquier método inesperado, la aserción fallará. Esto es útil porque
además de afirmar que se han realizado las llamadas que esperaba,
también está comprobando que se hicieron en el orden correcto y sin
llamadas adicionales:

Utiliza el objeto "call" para construir listas y compararlas con
"mock_calls":

>>> expected = [call.method(), call.attribute.method(10, x=53)]
>>> mock.mock_calls == expected
True

Sin embargo, los parámetros de las llamadas que devuelven mocks no se
registran, lo que significa que no es posible realizar un seguimiento
de las llamadas anidadas donde los parámetros utilizados para crear
ancestros son importantes:

>>> m = Mock()
>>> m.factory(important=True).deliver()
<Mock name='mock.factory().deliver()' id='...'>
>>> m.mock_calls[-1] == call.factory(important=False).deliver()
True

### Setting return values and attributes

Establecer los valores de retorno en un objeto mock es sumamente
fácil:

>>> mock = Mock()
>>> mock.return_value = 3
>>> mock()
3

Por supuesto, puede hacer lo mismo con los métodos en el mock:

>>> mock = Mock()
>>> mock.method.return_value = 3
>>> mock.method()
3

El valor devuelto también se puede establecer en el constructor:

>>> mock = Mock(return_value=3)
>>> mock()
3

Si necesitas una configuración de atributo en su mock, simplemente
haga:

>>> mock = Mock()
>>> mock.x = 3
>>> mock.x
3

A veces desea simular una situación más compleja, como por ejemplo
"mock.connection.cursor().execute("SELECT 1")". Si esperamos que esta
llamada devuelva una lista, entonces tenemos que configurar el
resultado de la llamada anidada.

Podemos usar "call" para construir el conjunto de llamadas en una
"llamada encadenada" como esta para una fácil afirmación después:

>>> mock = Mock()
>>> cursor = mock.connection.cursor.return_value
>>> cursor.execute.return_value = ['foo']
>>> mock.connection.cursor().execute("SELECT 1")
['foo']
>>> expected = call.connection.cursor().execute("SELECT 1").call_list()
>>> mock.mock_calls
[call.connection.cursor(), call.connection.cursor().execute('SELECT 1')]
>>> mock.mock_calls == expected
True

Es la llamada a ".call_list()" la que convierte nuestro objeto de
llamada en una lista de llamadas que representan las llamadas
encadenadas.

### Generar excepciones con mocks

Un atributo útil es "side_effect". Si establece esto en una clase o
instancia de excepción, se producirá la excepción cuando se llame al
mock.

>>> mock = Mock(side_effect=Exception('Boom!'))
>>> mock()
Traceback (most recent call last):
  ...
Exception: Boom!

### Funciones de efectos secundarios e iterables

"side_effect" también se puede asignar en una función o en una
iterable. El caso de uso para "side_effect" como un iterable es donde
se va a llamar a su mock varias veces, y desea que cada llamada
devuelva un valor diferente. Cuando se asigna "side_effect" en un
iterable cada llamada al mock devuelve el siguiente valor de lo
iterable:

>>> mock = MagicMock(side_effect=[4, 5, 6])
>>> mock()
4
>>> mock()
5
>>> mock()
6

Para casos de uso más avanzados, como variar dinámicamente los valores
devueltos en función de cómo se llame al mock, "side_effect" puede ser
una función. Se llamará a la función con los mismos argumentos que el
mock. Lo que sea que la función devuelve es lo que devuelve la
llamada:

>>> vals = {(1, 2): 1, (2, 3): 2}
>>> def side_effect(*args):
...     return vals[args]
...
>>> mock = MagicMock(side_effect=side_effect)
>>> mock(1, 2)
1
>>> mock(2, 3)
2

### Iteradores asincrónicos de Mocking

Desde Python 3.8, "AsyncMock" y "MagicMock" tienen soporte para mock
Iteradores asíncronos through "__aiter__". El "return_value" atributo
de "__aiter__" puede ser usado para asignar los valores de retorno que
podrían ser usados por iteración.

>>> mock = MagicMock()  # AsyncMock also works here
>>> mock.__aiter__.return_value = [1, 2, 3]
>>> async def main():
...     return [i async for i in mock]
...
>>> asyncio.run(main())
[1, 2, 3]

### El gestor de contexto asincrónico de Mocking

Desde Python 3.8, "AsyncMock" y "MagicMock" tienen soporte para mock
Gestores de contexto asíncronos a través de "__aenter__" y
"__aexit__". De forma predeterminada, las instancias "__aenter__" y
"__aexit__" son instancias de "AsyncMock" que devuelven una función
asincrónica.

>>> class AsyncContextManager:
...     async def __aenter__(self):
...         return self
...     async def __aexit__(self, exc_type, exc, tb):
...         pass
...
>>> mock_instance = MagicMock(AsyncContextManager())  # AsyncMock also works here
>>> async def main():
...     async with mock_instance as result:
...         pass
...
>>> asyncio.run(main())
>>> mock_instance.__aenter__.assert_awaited_once()
>>> mock_instance.__aexit__.assert_awaited_once()

### Creating a mock from an existing object

Un problema con el uso excesivo de mocking es que combina sus pruebas
a la implementación de sus mocks en lugar de su código real.
Supongamos que tiene una clase que implementa "some_method". En una
prueba para otra clase, se proporciona un mock de este objeto que
*also* proporciona "some_method". Si más tarde refactoriza la primera
clase, para que ya no tenga "some_method" - entonces sus pruebas
seguirán pasando a pesar de que su código está ahora roto!

"Mock" le permite proporcionar un objeto como especificación para el
mock, utilizando el argumento de palabra clave *spec*. El acceso a
métodos / atributos en el mock que no existen en el objeto de
especificación lanzará inmediatamente un error de atributo. Si cambia
la implementación de la especificación, las pruebas que usan esa clase
comenzarán a fallar inmediatamente sin tener que crear instancias de
la clase en esas pruebas.

>>> mock = Mock(spec=SomeClass)
>>> mock.old_method()
Traceback (most recent call last):
   ...
AttributeError: Mock object has no attribute 'old_method'. Did you mean: 'class_method'?

El uso de una especificación también permite una coincidencia más
inteligente de las llamadas realizadas al mock, independientemente de
si algunos parámetros se pasaron como argumentos posicionales o con
nombre:

   >>> def f(a, b, c): pass
   ...
   >>> mock = Mock(spec=f)
   >>> mock(1, 2, 3)
   <Mock name='mock()' id='140161580456576'>
   >>> mock.assert_called_with(a=1, b=2, c=3)

Si desea que esta coincidencia más inteligente también funcione con
llamadas de método en el mock, puede usar auto-speccing.

Si desea una forma más fuerte de especificación que impida la
configuración de atributos arbitrarios, así como la obtención de
ellos, entonces puede usar *spec_set* en lugar de *spec*.

### Uso de side_effect para devolver el contenido por archivo

"mock_open()" se utiliza para parchear el método "open()".
"side_effect" se puede utilizar para devolver un nuevo objeto Mock por
llamada. Esto puede usarse para devolver diferentes contenidos por
fichero almacenado en un diccionario:

   DEFAULT = "default"
   data_dict = {"file1": "data1",
                "file2": "data2"}

   def open_side_effect(name):
       return mock_open(read_data=data_dict.get(name, DEFAULT))()

   with patch("builtins.open", side_effect=open_side_effect):
       with open("file1") as file1:
           assert file1.read() == "data1"

       with open("file2") as file2:
           assert file2.read() == "data2"

       with open("file3") as file2:
           assert file2.read() == "default"

## Patch decorators

Nota:

  Con "patch()" importa que parchee objetos en el espacio de nombres
  donde se buscan. Esto es normalmente sencillo, pero para una guía
  rápida lea where to patch.

Una necesidad común en las pruebas es aplicar revisiones a un atributo
de clase o a un atributo de módulo, por ejemplo, aplicar revisiones a
una clase integrada o parchear una clase en un módulo para probar que
se crea una instancia. Los módulos y las clases son efectivamente
globales, por lo que el parcheo en ellos tiene que deshacerse después
de la prueba o el parche persistirá en otras pruebas y causará
problemas difíciles de diagnosticar.

mock proporciona tres decoradores convenientes para esto: "patch()",
"patch.object()" y "patch.dict()". "patch" toma una sola cadena del
formulario "package.module.Class.attribute" para especificar el
atributo que está parcheando. También, opcionalmente, toma un valor
con el que desea que se reemplace el atributo (o clase o lo que sea).
'patch.object' toma un objeto y el nombre del atributo con el que
desea parchear, además, opcionalmente, del valor con el que parcharlo.

"patch.object":

   >>> original = SomeClass.attribute
   >>> @patch.object(SomeClass, 'attribute', sentinel.attribute)
   ... def test():
   ...     assert SomeClass.attribute == sentinel.attribute
   ...
   >>> test()
   >>> assert SomeClass.attribute == original

   >>> @patch('package.module.attribute', sentinel.attribute)
   ... def test():
   ...     from package.module import attribute
   ...     assert attribute is sentinel.attribute
   ...
   >>> test()

Si está parcheando un módulo (incluyendo "builtins") entonces use
"patch()" en lugar de "patch.object()":

>>> mock = MagicMock(return_value=sentinel.file_handle)
>>> with patch('builtins.open', mock):
...     handle = open('filename', 'r')
...
>>> mock.assert_called_with('filename', 'r')
>>> assert handle == sentinel.file_handle, "incorrect file handle returned"

EL nombre del módulo puede ser 'dotted', en el formulario
"package.module" si es necesario:

   >>> @patch('package.module.ClassName.attribute', sentinel.attribute)
   ... def test():
   ...     from package.module import ClassName
   ...     assert ClassName.attribute == sentinel.attribute
   ...
   >>> test()

Un buen patrón en realidad es decorar los métodos de pruebas propios:

>>> class MyTest(unittest.TestCase):
...     @patch.object(SomeClass, 'attribute', sentinel.attribute)
...     def test_something(self):
...         self.assertEqual(SomeClass.attribute, sentinel.attribute)
...
>>> original = SomeClass.attribute
>>> MyTest('test_something').test_something()
>>> assert SomeClass.attribute == original

Si desea parchear con un Mock, puede usar "patch()" con un solo
argumento (o "patch.object()" con dos argumentos). El mock se creará
para usted y se pasará a la función de prueba / método:

>>> class MyTest(unittest.TestCase):
...     @patch.object(SomeClass, 'static_method')
...     def test_something(self, mock_method):
...         SomeClass.static_method()
...         mock_method.assert_called_with()
...
>>> MyTest('test_something').test_something()

Puede apilar varios decoradores de parches utilizando este patrón:

   >>> class MyTest(unittest.TestCase):
   ...     @patch('package.module.ClassName1')
   ...     @patch('package.module.ClassName2')
   ...     def test_something(self, MockClass2, MockClass1):
   ...         self.assertIs(package.module.ClassName1, MockClass1)
   ...         self.assertIs(package.module.ClassName2, MockClass2)
   ...
   >>> MyTest('test_something').test_something()

Al anidar decoradores de parches, los mocks se pasan a la función
decorada en el mismo orden en que se aplicaron (el orden normal
*Python* que se aplican los decoradores). Esto significa de abajo
hacia arriba, así que en el ejemplo anterior el simulacro de
"test_module.ClassName2" se pasa primero.

También está "patch.dict()" para establecer valores en un diccionario
solo durante un ámbito y restaurar el diccionario a su estado original
cuando finaliza la prueba:

>>> foo = {'key': 'value'}
>>> original = foo.copy()
>>> with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
...     assert foo == {'newkey': 'newvalue'}
...
>>> assert foo == original

"patch", "patch.object" and "patch.dict" se pueden utilizar como
gestores de contexto.

Donde utilice "patch()" para crear un simulacro para usted, puede
obtener una referencia al simulacro utilizando la forma "as" de la
instrucción with:

>>> class ProductionClass:
...     def method(self):
...         pass
...
>>> with patch.object(ProductionClass, 'method') as mock_method:
...     mock_method.return_value = None
...     real = ProductionClass()
...     real.method(1, 2, 3)
...
>>> mock_method.assert_called_with(1, 2, 3)

Como alternativa "patch", "patch.object" and "patch.dict" se pueden
utilizar como decoradores de clase. Cuando se utiliza de esta manera
es lo mismo que aplicar el decorador individualmente a cada método
cuyo nombre comienza con "test".

## Further examples

Estos son algunos ejemplos más para algunos escenarios ligeramente más
avanzados.

### Mocking de llamadas encadenadas

Mocking de las llamadas encadenadas es en realidad sencillo con mock
una vez que entiende el atributo "return_value" . Cuando se llama a un
mock por primera vez, o se obtiene su "return_value" antes de que se
llame, se crea un nuevo "Mock".

Esto significa que puede ver cómo se ha utilizado el objeto devuelto
de una llamada a un objeto simulado interrogando el simulado
"return_value":

>>> mock = Mock()
>>> mock().foo(a=2, b=3)
<Mock name='mock().foo()' id='...'>
>>> mock.return_value.foo.assert_called_with(a=2, b=3)

Desde aquí es un paso simple para configurar y luego hacer aserciones
sobre llamadas encadenadas. Por supuesto, otra alternativa es escribir
su código de una manera más comprobable en primer lugar...

Por lo tanto, supongamos que tenemos algún código que se ve un poco
como este:

>>> class Something:
...     def __init__(self):
...         self.backend = BackendProvider()
...     def method(self):
...         response = self.backend.get_endpoint('foobar').create_call('spam', 'eggs').start_call()
...         # more code

Suponiendo que "BackendProvider" ya está bien probado, ¿cómo probamos
"method()"? En concreto, queremos probar que la sección de código "#
more code" usa el objeto de respuesta de la manera correcta.

A medida que esta cadena de llamadas se realiza a partir de un
atributo de instancia, podemos parchear el atributo "backend" en una
instancia de "Something". En este caso en particular sólo estamos
interesados en el valor devuelto de la llamada final a "start_call"
por lo que no tenemos mucha configuración que hacer. Supongamos que el
objeto que devuelve es 'similar a un archivo', por lo que nos
aseguraremos de que nuestro objeto de respuesta utilice el compilado
"open()" as its "spec".

Para ello creamos una instancia mock como nuestro back-end simulado y
creamos un objeto de respuesta mock para ella. Para establecer la
respuesta como el valor devuelto de ese "start_call" final podríamos
hacer lo siguiente:

   mock_backend.get_endpoint.return_value.create_call.return_value.start_call.return_value = mock_response

Podemos hacerlo de una manera un poco mejor usando el método
"configure_mock()" para establecer directamente el valor devuelto para
nosotros:

   >>> something = Something()
   >>> mock_response = Mock(spec=open)
   >>> mock_backend = Mock()
   >>> config = {'get_endpoint.return_value.create_call.return_value.start_call.return_value': mock_response}
   >>> mock_backend.configure_mock(**config)

Con estos monkey patch el "backend simulado" en su lugar y puede hacer
la llamada real:

   >>> something.backend = mock_backend
   >>> something.method()

Usando "mock_calls" podemos comprobar la llamada encadenada con una
sola afirmación. Una llamada encadenada es varias llamadas en una
línea de código, por lo que habrá varias entradas en "mock_calls".
Podemos usar "call.call_list()" para crear esta lista de llamadas para
nosotros:

   >>> chained = call.get_endpoint('foobar').create_call('spam', 'eggs').start_call()
   >>> call_list = chained.call_list()
   >>> assert mock_backend.mock_calls == call_list

### Mocking parcial

For some tests, you may want to mock out a call to
"datetime.date.today()" to return a known date, but don't want to
prevent the code under test from creating new date objects.
Unfortunately "datetime.date" is written in C, so you cannot just
monkey-patch out the static "datetime.date.today()" method.

Instead, you can effectively wrap the date class with a mock, while
passing through calls to the constructor to the real class (and
returning real instances).

El "patch decorator" se utiliza aquí como un mock de la clase "date"
en el módulo en pruebas. Entonces, el atributo "side_effect" de la
clase de fecha simulada se establece en una función lambda que
devuelve una fecha real. Cuando la clase de fecha simulada es llamada,
una fecha real se construirá y devolverá por "side_effect".

   >>> import datetime as dt
   >>> with patch('mymodule.date') as mock_date:
   ...     mock_date.today.return_value = dt.date(2010, 10, 8)
   ...     mock_date.side_effect = lambda *args, **kw: dt.date(*args, **kw)
   ...
   ...     assert mymodule.date.today() == dt.date(2010, 10, 8)
   ...     assert mymodule.date(2009, 6, 8) == dt.date(2009, 6, 8)

Tenga en cuenta que no parcheamos "datetime.date" globalmente,
parcheamos "date" en el módulo que *uses*. Consulte where to patch.

Cuando "date.today()" es llamada se retorna una fecha conocida, pero
llama al constructor "date(...)" este constructor todavía devuelve
fechas normales. Sin esto, puede encontrarse teniendo que calcular un
resultado esperado utilizando exactamente el mismo algoritmo que el
código en prueba, que es un anti-patrón de prueba clásico.

Las llamadas al constructor de fecha se registran en los atributos
"mock_date" ("call_count" y amigos) que también pueden ser útiles para
las pruebas.

Una forma alternativa de tratar con fechas de mock, u otras clases
integradas, se discute en esta entrada de blog.

### Mocking a generator method

Un generador de Python es una función o método que utiliza la
instrucción "yield" para devolver una serie de valores cuando se itera
sobre [1].

Se llama a un método / función del generador para devolver el objeto
generador. Es el objeto generador que luego se itera. El método de
protocolo para la iteración es "__iter__()", por lo que podemos hacer
mock de esto usando una "MagicMock".

Aquí hay una clase de ejemplo con un método "iter" implementado como
generador:

>>> class Foo:
...     def iter(self):
...         for i in [1, 2, 3]:
...             yield i
...
>>> foo = Foo()
>>> list(foo.iter())
[1, 2, 3]

¿Cómo haríamos un mock de esta clase y, en particular, de su método
"iter"?

Para configurar los valores devueltos desde la iteración (implícita en
la llamada a "list"), necesitamos configurar el objeto devuelto por la
llamada a "foo.iter()".

>>> mock_foo = MagicMock()
>>> mock_foo.iter.return_value = iter([1, 2, 3])
>>> list(mock_foo.iter())
[1, 2, 3]

[1] También hay expresiones generadoras y más usos avanzados
    <http://www.dabeaz.com/coroutines/index.html>'_ de generadores,
    pero no nos preocupan los que están aquí. Una muy buena
    introducción a los generadores y lo potentes que son es: Generator
    Tricks for Systems Programmers.

### Aplicar el mismo parche a cada método de prueba

Si desea que se coloquen varias revisiones para varios métodos de
prueba, la forma obvia es aplicar los decoradores de parches a cada
método. Esto puede parecer una repetición innecesaria. En cambio,
puede utilizar "patch()" (en todas sus diversas formas) como decorador
de clases. Esto aplica las revisiones a todos los métodos de prueba de
la clase. Un método de prueba se identifica mediante métodos cuyos
nombres comienzan con "test":

   >>> @patch('mymodule.SomeClass')
   ... class MyTest(unittest.TestCase):
   ...
   ...     def test_one(self, MockSomeClass):
   ...         self.assertIs(mymodule.SomeClass, MockSomeClass)
   ...
   ...     def test_two(self, MockSomeClass):
   ...         self.assertIs(mymodule.SomeClass, MockSomeClass)
   ...
   ...     def not_a_test(self):
   ...         return 'something'
   ...
   >>> MyTest('test_one').test_one()
   >>> MyTest('test_two').test_two()
   >>> MyTest('test_two').not_a_test()
   'something'

Una forma alternativa de administrar parches es usar métodos start y
stop de patch. Estos le permiten mover el parche en sus métodos
"setUp" y "tearDown".

   >>> class MyTest(unittest.TestCase):
   ...     def setUp(self):
   ...         self.patcher = patch('mymodule.foo')
   ...         self.mock_foo = self.patcher.start()
   ...
   ...     def test_foo(self):
   ...         self.assertIs(mymodule.foo, self.mock_foo)
   ...
   ...     def tearDown(self):
   ...         self.patcher.stop()
   ...
   >>> MyTest('test_foo').run()

Si utiliza esta técnica, debe asegurarse de que la aplicación de
parches se "undone" llamando a "stop". Esto puede ser más complicado
de lo que podría pensar, porque si se produce una excepción en el
setUp, no se llama a tearDown. "unittest.TestCase.addCleanup()" hace
que esto sea más fácil:

   >>> class MyTest(unittest.TestCase):
   ...     def setUp(self):
   ...         patcher = patch('mymodule.foo')
   ...         self.addCleanup(patcher.stop)
   ...         self.mock_foo = patcher.start()
   ...
   ...     def test_foo(self):
   ...         self.assertIs(mymodule.foo, self.mock_foo)
   ...
   >>> MyTest('test_foo').run()

### Mocking unbound methods

Sometimes a test needs to patch an *unbound method*, which means
patching the method on the class rather than on the instance. In order
to make assertions about which objects were calling this particular
method, you need to pass "self" as the first argument. The issue is
that you can't patch with a mock for this, because if you replace an
unbound method with a mock it doesn't become a bound method when
fetched from the instance, and so it doesn't get "self" passed in. The
workaround is to patch the unbound method with a real function
instead. The "patch()" decorator makes it so simple to patch out
methods with a mock that having to create a real function becomes a
nuisance.

If you pass "autospec=True" to patch then it does the patching with a
*real* function object. This function object has the same signature as
the one it is replacing, but delegates to a mock under the hood. You
still get your mock auto-created in exactly the same way as before.
What it means though, is that if you use it to patch out an unbound
method on a class the mocked function will be turned into a bound
method if it is fetched from an instance. It will have "self" passed
in as the first argument, which is exactly what was needed:

>>> class Foo:
...   def foo(self):
...     pass
...
>>> with patch.object(Foo, 'foo', autospec=True) as mock_foo:
...   mock_foo.return_value = 'foo'
...   foo = Foo()
...   foo.foo()
...
'foo'
>>> mock_foo.assert_called_once_with(foo)

Si no usamos "autospec=True" entonces el método independiente se
parchea con una instancia de Mock en su lugar, y no se llama con
"self".

### Comprobación de varias llamadas con mock

mock tiene una buena API para hacer aserciones sobre cómo se usan sus
objetos ficticios.

>>> mock = Mock()
>>> mock.foo_bar.return_value = None
>>> mock.foo_bar('baz', spam='eggs')
>>> mock.foo_bar.assert_called_with('baz', spam='eggs')

Si su mock solo se llama una vez, puede usar el método
"assert_called_once_with()" que también afirma que "call_count" es
uno.

>>> mock.foo_bar.assert_called_once_with('baz', spam='eggs')
>>> mock.foo_bar()
>>> mock.foo_bar.assert_called_once_with('baz', spam='eggs')
Traceback (most recent call last):
    ...
AssertionError: Expected 'foo_bar' to be called once. Called 2 times.
Calls: [call('baz', spam='eggs'), call()].

Tanto "assert_called_with" como "assert_called_once_with" hacen
afirmaciones sobre la llamada *más reciente*. Si su mock va a ser
llamado varias veces, y desea hacer aserciones sobre *todas* esas
llamadas que puede utilizar "call_args_list":

>>> mock = Mock(return_value=None)
>>> mock(1, 2, 3)
>>> mock(4, 5, 6)
>>> mock()
>>> mock.call_args_list
[call(1, 2, 3), call(4, 5, 6), call()]

El helper "call" facilita la toma de aserciones sobre estas llamadas.
Puede crear una lista de llamadas esperadas y compararla con
"call_args_list". Esto se ve notablemente similar al repr de la
"call_args_list":

>>> expected = [call(1, 2, 3), call(4, 5, 6), call()]
>>> mock.call_args_list == expected
True

### Copiando con argumentos mutables

Otra situación es rara, pero puede morderte, es cuando se llama a tu
mock con argumentos mutables. "call_args" y "call_args_list" almacenan
*referencias* a los argumentos. Si el código sometido a prueba muta
los argumentos ya no puede realizar aserciones sobre cuáles eran los
valores cuando se llamó al mock.

Este es un código de ejemplo que muestra el problema. Imagine las
siguientes funciones definidas en 'mymodule':

   def frob(val):
       pass

   def grob(val):
       "First frob and then clear val"
       frob(val)
       val.clear()

Cuando tratamos de probar que "grob" llama "frob" con el argumento
correcto mira lo que sucede:

   >>> with patch('mymodule.frob') as mock_frob:
   ...     val = {6}
   ...     mymodule.grob(val)
   ...
   >>> val
   set()
   >>> mock_frob.assert_called_with({6})
   Traceback (most recent call last):
       ...
   AssertionError: Expected: (({6},), {})
   Called with: ((set(),), {})

Una posibilidad sería que el mock copiara los argumentos que pasa.
Esto podría causar problemas si realiza aserciones que se basan en la
identidad del objeto para la igualdad.

Aquí hay una solución que utiliza la funcionalidad "side_effect". Si
proporciona una función "side_effect" para un mock, se llamará a
"side_effect" con los mismos argumentos que el mock. Esto nos da la
oportunidad de copiar los argumentos y almacenarlos para aserciones
posteriores. En este ejemplo estoy usando *otro* mock para almacenar
los argumentos de modo que pueda usar los métodos ficticios para hacer
la aserción. Una vez más, una función auxiliar configura esto para mí.

   >>> from copy import deepcopy
   >>> from unittest.mock import Mock, patch, DEFAULT
   >>> def copy_call_args(mock):
   ...     new_mock = Mock()
   ...     def side_effect(*args, **kwargs):
   ...         args = deepcopy(args)
   ...         kwargs = deepcopy(kwargs)
   ...         new_mock(*args, **kwargs)
   ...         return DEFAULT
   ...     mock.side_effect = side_effect
   ...     return new_mock
   ...
   >>> with patch('mymodule.frob') as mock_frob:
   ...     new_mock = copy_call_args(mock_frob)
   ...     val = {6}
   ...     mymodule.grob(val)
   ...
   >>> new_mock.assert_called_with({6})
   >>> new_mock.call_args
   call({6})

"copy_call_args" se llama con el mock que se llamará. Devuelve un
nuevo mock en el que hacemos la aserción. La función "side_effect"
hace una copia de los args y llama a nuestro "new_mock" con la copia.

Nota:

  Si su simulacro solo se va a usar una vez, hay una forma más fácil
  de verificar los argumentos en el punto en que se llaman.
  Simplemente puede hacer la comprobación dentro de una función
  "side_effect".

  >>> def side_effect(arg):
  ...     assert arg == {6}
  ...
  >>> mock = Mock(side_effect=side_effect)
  >>> mock({6})
  >>> mock(set())
  Traceback (most recent call last):
      ...
  AssertionError

Un enfoque alternativo es crear una subclase de "Mock" o "MagicMock"
que copie (usando "copy.deepcopy()") los argumentos. A continuación se
muestra un ejemplo de implementación:

>>> from copy import deepcopy
>>> class CopyingMock(MagicMock):
...     def __call__(self, /, *args, **kwargs):
...         args = deepcopy(args)
...         kwargs = deepcopy(kwargs)
...         return super().__call__(*args, **kwargs)
...
>>> c = CopyingMock(return_value=None)
>>> arg = set()
>>> c(arg)
>>> arg.add(1)
>>> c.assert_called_with(set())
>>> c.assert_called_with(arg)
Traceback (most recent call last):
    ...
AssertionError: expected call not found.
Expected: mock({1})
Actual: mock(set())
>>> c.foo
<CopyingMock name='mock.foo' id='...'>

Cuando subclases "Mock" o "MagicMock" todos los atributos creados
dinámicamente, y el "return_value" usará tu subclase automáticamente.
Eso significa que todos los elementos secundarios de un "CopyingMock"
también tendrán el tipo "CopyingMock".

### Nesting patches

Usar parches como administradores de contexto es bueno, pero si haces
varios parches, puedes terminar con instrucciones anidadas que se
sangran cada vez más a la derecha:

   >>> class MyTest(unittest.TestCase):
   ...
   ...     def test_foo(self):
   ...         with patch('mymodule.Foo') as mock_foo:
   ...             with patch('mymodule.Bar') as mock_bar:
   ...                 with patch('mymodule.Spam') as mock_spam:
   ...                     assert mymodule.Foo is mock_foo
   ...                     assert mymodule.Bar is mock_bar
   ...                     assert mymodule.Spam is mock_spam
   ...
   >>> original = mymodule.Foo
   >>> MyTest('test_foo').test_foo()
   >>> assert mymodule.Foo is original

Con las funciones unittest "cleanup" y métodos start y stop de patch
podemos lograr el mismo efecto sin la sangría anidada. Un método
auxiliar simple, "create_patch", pone el parche en su lugar y devuelve
el mock creado para nosotros:

   >>> class MyTest(unittest.TestCase):
   ...
   ...     def create_patch(self, name):
   ...         patcher = patch(name)
   ...         thing = patcher.start()
   ...         self.addCleanup(patcher.stop)
   ...         return thing
   ...
   ...     def test_foo(self):
   ...         mock_foo = self.create_patch('mymodule.Foo')
   ...         mock_bar = self.create_patch('mymodule.Bar')
   ...         mock_spam = self.create_patch('mymodule.Spam')
   ...
   ...         assert mymodule.Foo is mock_foo
   ...         assert mymodule.Bar is mock_bar
   ...         assert mymodule.Spam is mock_spam
   ...
   >>> original = mymodule.Foo
   >>> MyTest('test_foo').run()
   >>> assert mymodule.Foo is original

### Mocking a un diccionario usando MagickMock

Es posible que desee simular un diccionario u otro objeto contenedor,
registrando todo el acceso a él mientras todavía se comporta como un
diccionario.

Podemos hacer esto con "MagicMock", que se comportará como un
diccionario, y usando "side_effect" para delegar el acceso del
diccionario a un diccionario subyacente real que está bajo nuestro
control.

Cuando se llama a los métodos "__getitem__()" y "__setitem__()" de
nuestro "MagicMock" (acceso normal al diccionario), entonces se llama
a "side_effect" con la clave (y el valor también en el caso de
"__setitem__"). También podemos controlar lo que se devuelve.

Después de que se haya utilizado el "MagicMock" podemos usar atributos
como "call_args_list" para afirmar cómo se usó el diccionario:

>>> my_dict = {'a': 1, 'b': 2, 'c': 3}
>>> def getitem(name):
...      return my_dict[name]
...
>>> def setitem(name, val):
...     my_dict[name] = val
...
>>> mock = MagicMock()
>>> mock.__getitem__.side_effect = getitem
>>> mock.__setitem__.side_effect = setitem

Nota:

  Una alternativa al uso de "MagicMock" es usar "Mock" y *solo*
  proporcionar los métodos mágicos que desea específicamente:

  >>> mock = Mock()
  >>> mock.__getitem__ = Mock(side_effect=getitem)
  >>> mock.__setitem__ = Mock(side_effect=setitem)

  Una *tercera* opción es usar "MagicMock" pero pasando "dict" como el
  argumento *spec* (o *spec_set*) para que el "MagicMock" creado solo
  tenga métodos mágicos de diccionario disponibles:

  >>> mock = MagicMock(spec_set=dict)
  >>> mock.__getitem__.side_effect = getitem
  >>> mock.__setitem__.side_effect = setitem

Con estas funciones de efectos secundarios en su lugar, el "mock" se
comportará como un diccionario normal pero registrando el acceso.
Incluso genera un "KeyError" si intenta acceder a una clave que no
existe.

>>> mock['a']
1
>>> mock['c']
3
>>> mock['d']
Traceback (most recent call last):
    ...
KeyError: 'd'
>>> mock['b'] = 'fish'
>>> mock['d'] = 'eggs'
>>> mock['b']
'fish'
>>> mock['d']
'eggs'

Una vez utilizado, puede realizar aserciones sobre el acceso
utilizando los métodos y atributos mock normales:

>>> mock.__getitem__.call_args_list
[call('a'), call('c'), call('d'), call('b'), call('d')]
>>> mock.__setitem__.call_args_list
[call('b', 'fish'), call('d', 'eggs')]
>>> my_dict
{'a': 1, 'b': 'fish', 'c': 3, 'd': 'eggs'}

### Mock de subclases y sus atributos

Hay varias razones por las que es posible que desee crear subclases
"Mock" Una razón podría ser agregar métodos auxiliares. Aquí hay un
ejemplo simple:

>>> class MyMock(MagicMock):
...     def has_been_called(self):
...         return self.called
...
>>> mymock = MyMock(return_value=None)
>>> mymock
<MyMock id='...'>
>>> mymock.has_been_called()
False
>>> mymock()
>>> mymock.has_been_called()
True

El comportamiento estándar para las instancias "Mock" es que los
atributos y los simulacros de valor devuelto son del mismo tipo que el
simulacro en el que se accede a ellos. Esto garantiza que los
atributos "Mock" son "Mocks" y los atributos "MagicMock" son
"MagicMocks" [2].  Por lo tanto, si está creando subclases para
agregar métodos auxiliares, también estarán disponibles en los
atributos y el valor devuelto mock de las instancias de su subclase.

>>> mymock.foo
<MyMock name='mock.foo' id='...'>
>>> mymock.foo.has_been_called()
False
>>> mymock.foo()
<MyMock name='mock.foo()' id='...'>
>>> mymock.foo.has_been_called()
True

A veces esto es inconveniente. Por ejemplo, un usuario está creando
subclases de mock para crear un Twisted adaptor. Tener esto aplicado a
los atributos también puede causar errores en realidad.

"Mock" (en todos sus sabores) utiliza un método llamado
"_get_child_mock" para crear estos "sub-mocks" para atributos y
valores devueltos. Puede evitar que la subclase se utilice para los
atributos invalidando este método. La firma es que toma argumentos de
palabra clave arbitrarios ("**kwargs") que luego se pasan al
constructor ficticio:

>>> class Subclass(MagicMock):
...     def _get_child_mock(self, /, **kwargs):
...         return MagicMock(**kwargs)
...
>>> mymock = Subclass()
>>> mymock.foo
<MagicMock name='mock.foo' id='...'>
>>> assert isinstance(mymock, Subclass)
>>> assert not isinstance(mymock.foo, Subclass)
>>> assert not isinstance(mymock(), Subclass)

[2] Una excepción a esta regla son los mock no invocables. Los
    atributos usan la variante a la que se puede llamar porque, de lo
    contrario, los simulacros a los que no se puede llamar no podrían
    tener métodos a los que se puede llamar.

### Importaciones de Mocking con patch.dict

Una situación en la que un mocking puede ser difícil es cuando tiene
una importación local dentro de una función. Estos son más difíciles
de simular porque no están usando un objeto del espacio de nombres del
módulo que podemos revisar.

Por lo general, deben evitarse las importaciones locales. A veces se
hacen para evitar dependencias circulares, para las que hay
*generalmente* una manera mucho mejor de resolver el problema
(refactorizar el código) o para evitar "costos iniciales" retrasando
la importación. Esto también se puede resolver de mejores maneras que
una importación local incondicional (almacenar el módulo como una
clase o atributo de módulo y solo hacer la importación en el primer
uso).

Aparte de eso, hay una manera de usar "mock" para afectar los
resultados de una importación. La importación obtiene un *objeto* del
diccionario "sys.modules". Tenga en cuenta que obtiene un *objeto*,
que no tiene por qué ser un módulo. La importación de un módulo por
primera vez da como resultado que un objeto de módulo se coloque en
"sys.modules", por lo que normalmente cuando importe algo devuelve un
modulo. Sin embargo, este no tiene por qué ser el caso.

Esto significa que puede usar "patch.dict()" para *temporalmente*
poner un mock en su lugar sobre "sys.modules". Cualquier importación
mientras este parche está activo recuperará el mock. Cuando el parche
está completo (la función decorada sale, el cuerpo de la instrucción
with está completo o se llama a "patcher.stop()") entonces lo que
había anteriormente se restaurará de forma segura.

Aquí hay un ejemplo de mock del módulo 'fooble'.

>>> import sys
>>> mock = Mock()
>>> with patch.dict('sys.modules', {'fooble': mock}):
...    import fooble
...    fooble.blob()
...
<Mock name='mock.blob()' id='...'>
>>> assert 'fooble' not in sys.modules
>>> mock.blob.assert_called_once_with()

Como puede ver, el "import fooble" tiene éxito, pero al salir no queda
ningún 'fooble' en "sys.modules".

Esto también funciona para el formulario "from module import name":

>>> mock = Mock()
>>> with patch.dict('sys.modules', {'fooble': mock}):
...    from fooble import blob
...    blob.blip()
...
<Mock name='mock.blob.blip()' id='...'>
>>> mock.blob.blip.assert_called_once_with()

Con un poco más de trabajo también puede simular las importaciones de
paquetes:

>>> mock = Mock()
>>> modules = {'package': mock, 'package.module': mock.module}
>>> with patch.dict('sys.modules', modules):
...    from package.module import fooble
...    fooble()
...
<Mock name='mock.module.fooble()' id='...'>
>>> mock.module.fooble.assert_called_once_with()

### Seguimiento del orden de las llamadas y de las aserciones de llamadas menos detalladas

La clase "Mock" le permite realizar un seguimiento del *orden* de las
llamadas a métodos en sus objetos mock a través del atributo
"method_calls". Esto no le permite rastrear el orden de las llamadas
entre objetos simulados separados, sin embargo, podemos usar
"mock_calls" para lograr el mismo efecto.

Debido a que los mocks rastrean las llamadas a mocks secundarios en
"mock_calls", y el acceso a un atributo arbitrario de un mock crea un
mock secundario, podemos crear nuestros mocks separados de uno
primario. Las llamadas a esos mocks hijos se grabarán, en orden, en el
"mock_calls" del padre:

>>> manager = Mock()
>>> mock_foo = manager.foo
>>> mock_bar = manager.bar

>>> mock_foo.something()
<Mock name='mock.foo.something()' id='...'>
>>> mock_bar.other.thing()
<Mock name='mock.bar.other.thing()' id='...'>

>>> manager.mock_calls
[call.foo.something(), call.bar.other.thing()]

A continuación, podemos realizar afirmaciones sobre las llamadas,
incluido el orden, comparando con el atributo "mock_calls" en el mock
administrador:

>>> expected_calls = [call.foo.something(), call.bar.other.thing()]
>>> manager.mock_calls == expected_calls
True

Si "patch" está creando y poniendo en su lugar, sus mocks, puede
adjuntarlos a un mock administrador usando el método "attach_mock()" .
Después de adjuntar las llamadas se registrarán en "mock_calls" del
administrador.

   >>> manager = MagicMock()
   >>> with patch('mymodule.Class1') as MockClass1:
   ...     with patch('mymodule.Class2') as MockClass2:
   ...         manager.attach_mock(MockClass1, 'MockClass1')
   ...         manager.attach_mock(MockClass2, 'MockClass2')
   ...         MockClass1().foo()
   ...         MockClass2().bar()
   <MagicMock name='mock.MockClass1().foo()' id='...'>
   <MagicMock name='mock.MockClass2().bar()' id='...'>
   >>> manager.mock_calls
   [call.MockClass1(),
   call.MockClass1().foo(),
   call.MockClass2(),
   call.MockClass2().bar()]

Si se han realizado muchas llamadas, pero solo está interesado en una
secuencia particular de ellas, entonces una alternativa es usar el
método "assert_has_calls()" . Esto toma una lista de llamadas
(construidas con el objeto "call"). Si esa secuencia de llamadas sobre
"mock_calls", la aserción se realiza correctamente.

>>> m = MagicMock()
>>> m().foo().bar().baz()
<MagicMock name='mock().foo().bar().baz()' id='...'>
>>> m.one().two().three()
<MagicMock name='mock.one().two().three()' id='...'>
>>> calls = call.one().two().three().call_list()
>>> m.assert_has_calls(calls)

Aunque la llamada encadenada "m.one().two().three()" no son las únicas
llamadas que se han realizado al mock, la aserción aún tiene éxito.

A veces, un mock puede tener varias llamadas, y solo le interesa
afirmar sobre *algunas* de esas llamadas. Puede que ni siquiera
importe el pedido. En este caso, puede pasar "any_order=True" a
"assert_has_calls":

>>> m = MagicMock()
>>> m(1), m.two(2, 3), m.seven(7), m.fifty('50')
(...)
>>> calls = [call.fifty('50'), call(1), call.seven(7)]
>>> m.assert_has_calls(calls, any_order=True)

### Coincidencia de argumentos más compleja

Usando el mismo concepto básico que "ANY" podemos implementar
comparadores para hacer afirmaciones más complejas en objetos usados
como argumentos para mocks.

Supongamos que esperamos que algún objeto se pase a un mock que, por
defecto, se compara igual en función de la identidad del objeto (que
es el valor predeterminado de Python para las clases definidas por el
usuario). Para usar "assert_called_with()" tendríamos que pasar
exactamente el mismo objeto. Si solo estamos interesados en algunos de
los atributos de este objeto, podemos crear un comparador que
verifique estos atributos por nosotros.

Puede ver en este ejemplo cómo una llamada 'estándar' a
"assert_called_with" no es suficiente:

>>> class Foo:
...     def __init__(self, a, b):
...         self.a, self.b = a, b
...
>>> mock = Mock(return_value=None)
>>> mock(Foo(1, 2))
>>> mock.assert_called_with(Foo(1, 2))
Traceback (most recent call last):
    ...
AssertionError: expected call not found.
Expected: mock(<__main__.Foo object at 0x...>)
Actual: mock(<__main__.Foo object at 0x...>)

Una función de comparación para nuestra clase "Foo" podría verse así:

>>> def compare(self, other):
...     if not type(self) == type(other):
...         return False
...     if self.a != other.a:
...         return False
...     if self.b != other.b:
...         return False
...     return True
...

Y un objeto comparador que puede usar funciones de comparación como
esta para su operación de igualdad se vería así:

>>> class Matcher:
...     def __init__(self, compare, some_obj):
...         self.compare = compare
...         self.some_obj = some_obj
...     def __eq__(self, other):
...         return self.compare(self.some_obj, other)
...

Poniendo todo esto junto:

>>> match_foo = Matcher(compare, Foo(1, 2))
>>> mock.assert_called_with(match_foo)

El "Matcher" es instanciado con nuestra función de comparación y el
objeto "Foo" con el que queremos comparar. En "assert_called_with" se
llamará al método de igualdad "Matcher", que compara el objeto con el
que se llamó al mock con el que creamos nuestro matcher. Si coinciden,
entonces pasa "assert_called_with", y si no lo hacen, se lanzará un
"AssertionError":

>>> match_wrong = Matcher(compare, Foo(3, 4))
>>> mock.assert_called_with(match_wrong)
Traceback (most recent call last):
    ...
AssertionError: Expected: ((<Matcher object at 0x...>,), {})
Called with: ((<Foo object at 0x...>,), {})

Con un poco de ajuste, podría hacer que la función de comparación
genere el "AssertionError" directamente y proporcione un mensaje de
falla más útil.

A partir de la versión 1.5, la biblioteca de pruebas de Python
PyHamcrest proporciona una funcionalidad similar, que puede ser útil
aquí, en la forma de su comparador de igualdad
(hamcrest.library.integration.match_equality).
