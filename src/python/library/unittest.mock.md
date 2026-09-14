---
title: '"unittest.mock" --- mock object library'
source_url: https://docs.python.org/es/3
source_path: library/unittest.mock.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4370
---

# "unittest.mock" --- mock object library

Added in version 3.3.

**Source code:** Lib/unittest/mock.py

======================================================================

"unittest.mock" is a library for testing in Python. It allows you to
replace parts of your system under test with mock objects and make
assertions about how they have been used.

"unittest.mock" provides a core "Mock" class removing the need to
create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were
used and arguments they were called with. You can also specify return
values and set needed attributes in the normal way.

Además, mock proporciona un decorador "patch()" que puede manejar el
parcheo de atributos a nivel de clase y de módulo dentro del ámbito de
una prueba, junto con "sentinel" para crear objetos únicos. Consulta
quick guide para ver algunos ejemplos de cómo utilizar "Mock",
"MagicMock" y "patch()".

Mock está diseñado para ser utilizado junto a "unittest". Mock se basa
en el patrón 'acción -> aserción' en lugar de usar el patrón
'grabación -> reproducción' utilizado por muchos frameworks de
simulación.

There is a backport of "unittest.mock" for earlier versions of Python,
available as mock on PyPI.

## Guía rápida

Los objetos de las clases "Mock" y "MagicMock" van creando todos los
atributos y métodos a medida que se accede a ellos y almacenan
detalles de cómo se han utilizado. Puedes configurarlos para
especificar valores de retorno o limitar qué atributos están
disponibles y posteriormente hacer aserciones sobre cómo han sido
utilizados:

>>> from unittest.mock import MagicMock
>>> thing = ProductionClass()
>>> thing.method = MagicMock(return_value=3)
>>> thing.method(3, 4, 5, key='value')
3
>>> thing.method.assert_called_with(3, 4, 5, key='value')

"side_effect" allows you to perform side effects, including raising an
exception when a mock is called:

>>> from unittest.mock import Mock
>>> mock = Mock(side_effect=KeyError('foo'))
>>> mock()
Traceback (most recent call last):
 ...
KeyError: 'foo'

>>> values = {'a': 1, 'b': 2, 'c': 3}
>>> def side_effect(arg):
...     return values[arg]
...
>>> mock.side_effect = side_effect
>>> mock('a'), mock('b'), mock('c')
(1, 2, 3)
>>> mock.side_effect = [5, 4, 3, 2, 1]
>>> mock(), mock(), mock()
(5, 4, 3)

Existen muchas otras formas de configurar y controlar el
comportamiento de Mock. Por ejemplo, el argumento *spec* configura el
objeto simulado para que tome su especificación de otro objeto.
Cualquier intento de acceder a atributos o métodos en el objeto
simulado que no existan en la especificación fallará lanzando una
excepción "AttributeError".

El decorador / gestor de contexto "patch()" facilita la simulación de
clases u objetos en un módulo bajo prueba. El objeto que especifiques
será reemplazado por un objeto simulado (u otro objeto) durante la
prueba y será restaurado cuando esta finalice:

   >>> from unittest.mock import patch
   >>> @patch('module.ClassName2')
   ... @patch('module.ClassName1')
   ... def test(MockClass1, MockClass2):
   ...     module.ClassName1()
   ...     module.ClassName2()
   ...     assert MockClass1 is module.ClassName1
   ...     assert MockClass2 is module.ClassName2
   ...     assert MockClass1.called
   ...     assert MockClass2.called
   ...
   >>> test()

Nota:

  Cuando anidas decoradores patch, los objetos simulados se pasan a la
  función decorada en el mismo orden en el que fueron aplicados (el
  orden normal en el que se aplican los decoradores en *Python*). Esto
  significa de abajo hacia arriba, por lo que en el ejemplo anterior
  se pasa primero el objeto simulado para "module.ClassName1".Al usar
  "patch()" es importante que parchees los objetos en el espacio de
  nombres donde son buscados. Esto normalmente es sencillo, pero para
  una guía rápida, lee dónde parchear.

Además de decorador, la función "patch()" se puede usar como gestor de
contexto en una declaración with:

>>> with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
...     thing = ProductionClass()
...     thing.method(1, 2, 3)
...
>>> mock_method.assert_called_once_with(1, 2, 3)

También existe la función "patch.dict()" que permite establecer
valores en un diccionario dentro de un ámbito y restaurar el
diccionario a su estado original cuando finaliza la prueba:

>>> foo = {'key': 'value'}
>>> original = foo.copy()
>>> with patch.dict(foo, {'newkey': 'newvalue'}, clear=True):
...     assert foo == {'newkey': 'newvalue'}
...
>>> assert foo == original

Mock admite la simulación de los métodos mágicos de Python. La forma
más sencilla de utilizar métodos mágicos es mediante la clase
"MagicMock". Te permite hacer cosas como:

>>> mock = MagicMock()
>>> mock.__str__.return_value = 'foobarbaz'
>>> str(mock)
'foobarbaz'
>>> mock.__str__.assert_called_with()

Mock también permite asignar funciones (u otras instancias de Mock) a
métodos mágicos y se asegura de que serán llamadas de forma apropiada.
La clase "MagicMock" es solo una variante de Mock con la diferencia de
que tiene todos los métodos mágicos previamente creados para ti
(bueno, todos los que son útiles).

El siguiente es un ejemplo de uso de métodos mágicos utilizando la
clase Mock ordinaria:

>>> mock = Mock()
>>> mock.__str__ = Mock(return_value='wheeeeee')
>>> str(mock)
'wheeeeee'

Para asegurarte de que los objetos simulados en tus pruebas tienen
exactamente la misma API que los objetos que están reemplazando,
puedes usar autoespecificación. La autoespecificación se puede
realizar a través del argumento *autospec* de patch, o mediante la
función "create_autospec()". La autoespecificación crea objetos
simulados que tienen los mismos atributos y métodos que los objetos
que están reemplazando, y todas las función y métodos (incluidos los
constructores) tienen la misma firma de llamada que los objetos
reales.

Esto asegura que tus simulaciones fallarán, si se utilizan
incorrectamente, de la misma manera que lo haría tu código en
producción:

>>> from unittest.mock import create_autospec
>>> def function(a, b, c):
...     pass
...
>>> mock_function = create_autospec(function, return_value='fishy')
>>> mock_function(1, 2, 3)
'fishy'
>>> mock_function.assert_called_once_with(1, 2, 3)
>>> mock_function('wrong arguments')
Traceback (most recent call last):
 ...
TypeError: missing a required argument: 'b'

"create_autospec()" también se puede usar en clases, donde copia la
firma del método "__init__", y en objetos invocables, donde copia la
firma del método "__call__".

## La clase Mock

"Mock" es un objeto simulado flexible, destinado a reemplazar el uso
de stubs y dobles de prueba en todo tu código. Los objetos Mock son
invocables y crean atributos en el mismo momento que se accede a ellos
como nuevos objetos Mock [1]. Acceder al mismo atributo siempre
retornará el mismo objeto Mock. Además, registran cómo los usas, lo
que te permite hacer aserciones sobre cómo tu código ha interaccionado
con ellos.

"MagicMock" es una subclase de "Mock" con todos los métodos mágicos
creados previamente y listos para ser usados. También hay variantes no
invocables, útiles cuando se están simulando objetos que no se pueden
llamar: "NonCallableMock" y "NonCallableMagicMock"

Los decoradores "patch()" facilitan la sustitución temporal de clases
en un módulo en particular con un objeto "Mock". Por defecto,
"patch()" creará un objeto "MagicMock" automáticamente. Se puede
especificar una clase alternativa a "Mock" usando el argumento
*new_callable* de "patch()".

class unittest.mock.Mock(spec=None, side_effect=None, return_value=DEFAULT, wraps=None, name=None, spec_set=None, unsafe=False, **kwargs)

   Crea un nuevo objeto "Mock". "Mock" toma varios argumentos
   opcionales que especifican el comportamiento del objeto Mock:

   * *spec*: Puede ser una lista de cadenas de caracteres o un objeto
     existente previamente (una clase o una instancia) que actúa como
     la especificación del objeto simulado. Si pasas un objeto, se
     forma una lista de cadenas llamando a la función *dir* en el
     objeto (excluyendo los métodos y atributos mágicos no admitidos).
     Acceder a cualquier atributo que no esté en esta lista lanzará
     una excepción "AttributeError".

     If *spec* is an object (rather than a list of strings) then
     "__class__" returns the class of the spec object. This allows
     mocks to pass "isinstance()" tests.

   * *spec_set*: Una variante más estricta de *spec*. Si se utiliza,
     cualquier intento de *establecer* u obtener un atributo del
     objeto simulado que no esté en el objeto pasado como *spec_set*
     lanzará una excepción "AttributeError".

   * *side_effect*: Una función que se llamará cada vez que el objeto
     simulado sea invocado. Consultar el atributo "side_effect" para
     más información. Es útil para lanzar excepciones o para cambiar
     dinámicamente valores de retorno. La función se llama con los
     mismos argumentos que el objeto simulado, y a menos que retorne
     "DEFAULT", su valor de retorno se utiliza como valor de retorno
     del propio objeto simulado.

     Alternativamente *side_effect* puede ser una clase o instancia de
     excepción. En este caso, se lanza la excepción cuando se llama al
     objeto simulado.

     Si *side_effect* es un iterable, cada llamada al objeto simulado
     retornará el siguiente valor del iterable.

     Un *side_effect* se puede desactivar estableciéndolo en "None".

   * *return_value*: El valor retornado cuando se llama al objeto
     simulado. Por defecto, este es una nueva instancia de la clase
     Mock (creada en el primer acceso). Consultar el atributo
     "return_value" para más detalles.

   * *unsafe*: Por defecto, el acceso a cualquier atributo cuyo nombre
     comience por *assert*, *assret*, *asert*, *aseert* o *assrt*
     generará un error "AttributeError". Si se pasa "unsafe=True" se
     permitirá el acceso a estos atributos.

     Added in version 3.5.

   * *wraps*: objeto a envolver (simular) por la instancia de Mock. Si
     *wraps* no es "None", al llamar al objeto Mock se pasa la llamada
     a través del objeto envuelto (retornando el resultado real).
     Acceder a un atributo del objeto simulado retornará otro objeto
     Mock que envuelve al atributo correspondiente del objeto real
     envuelto (de modo que intentar acceder a un atributo que no
     existe lanzará una excepción "AttributeError").

     Si el objeto simulado tiene un *return_value* explícito
     establecido, las llamadas no se pasan al objeto envuelto y
     *return_value* se retorna en su lugar.

   * *name*: Si el objeto simulado tiene un nombre, será utilizado en
     la representación imprimible del mismo. Esto puede ser útil para
     la depuración. El nombre se propaga a los objetos simulados
     hijos.

   Los objetos simulados también pueden ser invocados con argumentos
   por palabra clave arbitrarios. Estos serán utilizados para
   establecer atributos en el objeto simulado una vez creado.
   Consultar el método "configure_mock()" para más detalles.

   assert_called()

      Assert cuando el objeto simulado se ha invocado al menos una
      vez.

      >>> mock = Mock()
      >>> mock.method()
      <Mock name='mock.method()' id='...'>
      >>> mock.method.assert_called()

      Added in version 3.6.

   assert_called_once()

      Assert si el objeto simulado se ha invocado exactamente una vez.

      >>> mock = Mock()
      >>> mock.method()
      <Mock name='mock.method()' id='...'>
      >>> mock.method.assert_called_once()
      >>> mock.method()
      <Mock name='mock.method()' id='...'>
      >>> mock.method.assert_called_once()
      Traceback (most recent call last):
      ...
      AssertionError: Expected 'method' to have been called once. Called 2 times.
      Calls: [call(), call()].

      Added in version 3.6.

   assert_called_with(*args, **kwargs)

      Este método es una manera apropiada de asertar si la última
      llamada se ha realizado de una manera particular:

      >>> mock = Mock()
      >>> mock.method(1, 2, 3, test='wow')
      <Mock name='mock.method()' id='...'>
      >>> mock.method.assert_called_with(1, 2, 3, test='wow')

   assert_called_once_with(*args, **kwargs)

      Assert si el objeto simulado se ha invocado exactamente una vez
      y si esa llamada se realizó con los argumentos especificados.

      >>> mock = Mock(return_value=None)
      >>> mock('foo', bar='baz')
      >>> mock.assert_called_once_with('foo', bar='baz')
      >>> mock('other', bar='values')
      >>> mock.assert_called_once_with('other', bar='values')
      Traceback (most recent call last):
        ...
      AssertionError: Expected 'mock' to be called once. Called 2 times.
      Calls: [call('foo', bar='baz'), call('other', bar='values')].

   assert_any_call(*args, **kwargs)

      assert si el objeto simulado se ha invocado con los argumentos
      especificados.

      La aserción pasa si el objeto simulado se ha invocado *en algún
      momento*, a diferencia de "assert_called_with()" y
      "assert_called_once_with()", con los que solo pasa la aserción
      si la llamada es la más reciente, y en el caso de
      "assert_called_once_with()" también debe ser la única llamada
      realizada.

      >>> mock = Mock(return_value=None)
      >>> mock(1, 2, arg='thing')
      >>> mock('some', 'thing', 'else')
      >>> mock.assert_any_call(1, 2, arg='thing')

   assert_has_calls(calls, any_order=False)

      assert si el objeto simulado se ha invocado con las llamadas
      especificadas. La lista "mock_calls" se compara con la lista de
      llamadas.

      Si *any_order* es falso entonces las llamadas deben ser
      secuenciales. No puede haber llamadas adicionales antes o
      después de las llamadas especificadas.

      Si *any_order* es verdadero, las llamadas pueden estar en
      cualquier orden, pero deben aparecer todas en "mock_calls".

      >>> mock = Mock(return_value=None)
      >>> mock(1)
      >>> mock(2)
      >>> mock(3)
      >>> mock(4)
      >>> calls = [call(2), call(3)]
      >>> mock.assert_has_calls(calls)
      >>> calls = [call(4), call(2), call(3)]
      >>> mock.assert_has_calls(calls, any_order=True)

   assert_not_called()

      Assert si el objeto simulado nunca fue invocado.

      >>> m = Mock()
      >>> m.hello.assert_not_called()
      >>> obj = m.hello()
      >>> m.hello.assert_not_called()
      Traceback (most recent call last):
        ...
      AssertionError: Expected 'hello' to not have been called. Called 1 times.
      Calls: [call()].

      Added in version 3.5.

   reset_mock(*, return_value=False, side_effect=False)

      El método *reset_mock* restablece todos los atributos de llamada
      en un objeto simulado:

         >>> mock = Mock(return_value=None)
         >>> mock('hello')
         >>> mock.called
         True
         >>> mock.reset_mock()
         >>> mock.called
         False

      This can be useful where you want to make a series of assertions
      that reuse the same object.

      *return_value* parameter when set to "True" resets
      "return_value":

         >>> mock = Mock(return_value=5)
         >>> mock('hello')
         5
         >>> mock.reset_mock(return_value=True)
         >>> mock('hello')
         <Mock name='mock()' id='...'>

      *side_effect* parameter when set to "True" resets "side_effect":

         >>> mock = Mock(side_effect=ValueError)
         >>> mock('hello')
         Traceback (most recent call last):
           ...
         ValueError
         >>> mock.reset_mock(side_effect=True)
         >>> mock('hello')
         <Mock name='mock()' id='...'>

      Note that "reset_mock()" *doesn't* clear the "return_value",
      "side_effect" or any child attributes you have set using normal
      assignment by default.

      Child mocks are reset as well.

      Distinto en la versión 3.6: Se añadieron dos argumentos de
      palabra clave a la función *reset_mock*.

   mock_add_spec(spec, spec_set=False)

      Agrega una especificación a un objeto simulado. *spec* puede ser
      un objeto o una lista de cadenas de caracteres. Solo los
      atributos presentes en *spec* pueden ser obtenidos desde el
      objeto simulado.

      Si *spec_set* es verdadero, solo los atributos de la
      especificación pueden ser establecidos.

   attach_mock(mock, attribute)

      Adjunta otro objeto simulado como un atributo de la instancia
      actual, substituyendo su nombre y su padre. Las llamadas al
      objeto simulado adjuntado se registrarán en los atributos
      "method_calls" y "mock_calls" del padre.

   configure_mock(**kwargs)

      Establece los atributos del objeto simulado por medio de
      argumentos por palabra clave.

      Los atributos, los valores de retorno y los efectos de
      colaterales se pueden configurar en los objetos simulados hijos
      usando la notación de punto estándar y desempaquetando un
      diccionario en la llamada al método:

      >>> mock = Mock()
      >>> attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
      >>> mock.configure_mock(**attrs)
      >>> mock.method()
      3
      >>> mock.other()
      Traceback (most recent call last):
        ...
      KeyError

      Lo mismo se puede lograr en la llamada al constructor de los
      objetos simulados:

      >>> attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
      >>> mock = Mock(some_attribute='eggs', **attrs)
      >>> mock.some_attribute
      'eggs'
      >>> mock.method()
      3
      >>> mock.other()
      Traceback (most recent call last):
        ...
      KeyError

      "configure_mock()" existe con el fin de facilitar la
      configuración después de que el objeto simulado haya sido
      creado.

   __dir__()

      Los objetos "Mock" limitan los resultados de "dir(some_mock)" a
      resultados útiles. Para los objetos simulados con una
      especificación (*spec*), esto incluye todos los atributos
      permitidos para el mismo.

      Consultar "FILTER_DIR" para conocer que hace este filtrado y la
      forma de desactivarlo.

   _get_child_mock(**kw)

      Crea los objetos simulados hijos para los atributos y el valor
      de retorno. Por defecto los objetos simulados hijos serán del
      mismo tipo que el padre. Las subclases de Mock pueden redefinir
      este método para personalizar la forma en la que se construye el
      objeto simulado hijo.

      Para objetos simulados no invocables la variante invocable será
      utilizada (en lugar de cualquier subclase personalizada).

   called

      Un booleano que representa si el objeto simulado ha sido
      invocado o no:

      >>> mock = Mock(return_value=None)
      >>> mock.called
      False
      >>> mock()
      >>> mock.called
      True

   call_count

      Un entero que le indica cuántas veces el objeto simulado ha sido
      invocado:

      >>> mock = Mock(return_value=None)
      >>> mock.call_count
      0
      >>> mock()
      >>> mock()
      >>> mock.call_count
      2

   return_value

      Establece este atributo para configurar el valor a retornar
      cuando se llama al objeto simulado:

      >>> mock = Mock()
      >>> mock.return_value = 'fish'
      >>> mock()
      'fish'

      El valor de retorno por defecto es otro objeto simulado y se
      puede configurar de forma habitual:

      >>> mock = Mock()
      >>> mock.return_value.attribute = sentinel.Attribute
      >>> mock.return_value()
      <Mock name='mock()()' id='...'>
      >>> mock.return_value.assert_called_with()

      "return_value" también se puede establecer directamente en el
      constructor:

      >>> mock = Mock(return_value=3)
      >>> mock.return_value
      3
      >>> mock()
      3

   side_effect

      Este atributo puede ser una función a ser llamada cuando se
      llame al objeto simulado, un iterable o una excepción (clase o
      instancia) para ser lanzada.

      Si pasas una función, será llamada con los mismos argumentos que
      el objeto simulado y, a menos que la función retorne el
      singleton "DEFAULT", la llamada al objeto simulado retornará lo
      mismo que retorna la función. En cambio, si la función retorna
      "DEFAULT", entonces el objeto simulado retornará su valor normal
      (el del atributo "return_value").

      Si pasas un iterable, se utiliza para obtener un iterador a
      partir del mismo que debe producir un valor en cada llamada.
      Este valor puede ser una instancia de la excepción a ser lanzada
      o un valor a retornar al llamar al objeto simulado (el manejo de
      "DEFAULT" es igual que en el caso en el que se pasa una
      función).

      Un ejemplo de un objeto simulado que genera una excepción (para
      probar el manejo de excepciones de una API):

      >>> mock = Mock()
      >>> mock.side_effect = Exception('Boom!')
      >>> mock()
      Traceback (most recent call last):
        ...
      Exception: Boom!

      Usando "side_effect" para retornar una secuencia de valores:

      >>> mock = Mock()
      >>> mock.side_effect = [3, 2, 1]
      >>> mock(), mock(), mock()
      (3, 2, 1)

      Usando un objeto invocable:

      >>> mock = Mock(return_value=3)
      >>> def side_effect(*args, **kwargs):
      ...     return DEFAULT
      ...
      >>> mock.side_effect = side_effect
      >>> mock()
      3

      "side_effect" se puede establecer en el constructor. Aquí hay un
      ejemplo que suma uno al valor del objeto simulado invocado y lo
      retorna:

      >>> side_effect = lambda value: value + 1
      >>> mock = Mock(side_effect=side_effect)
      >>> mock(3)
      4
      >>> mock(-8)
      -7

      Establecer "side_effect" en "None" lo desactiva:

      >>> m = Mock(side_effect=KeyError, return_value=3)
      >>> m()
      Traceback (most recent call last):
       ...
      KeyError
      >>> m.side_effect = None
      >>> m()
      3

   call_args

      This is either "None" (if the mock hasn't been called), or the
      arguments that the mock was last called with. This will be in
      the form of a tuple: the first member, which can also be
      accessed through the "args" property, is any positional
      arguments the mock was called with (or an empty tuple) and the
      second member, which can also be accessed through the "kwargs"
      property, is any keyword arguments (or an empty dictionary).

      >>> mock = Mock(return_value=None)
      >>> print(mock.call_args)
      None
      >>> mock()
      >>> mock.call_args
      call()
      >>> mock.call_args == ()
      True
      >>> mock(3, 4)
      >>> mock.call_args
      call(3, 4)
      >>> mock.call_args == ((3, 4),)
      True
      >>> mock.call_args.args
      (3, 4)
      >>> mock.call_args.kwargs
      {}
      >>> mock(3, 4, 5, key='fish', next='w00t!')
      >>> mock.call_args
      call(3, 4, 5, key='fish', next='w00t!')
      >>> mock.call_args.args
      (3, 4, 5)
      >>> mock.call_args.kwargs
      {'key': 'fish', 'next': 'w00t!'}

      El atributo "call_args", junto con los miembros de las listas
      "call_args_list", "method_calls" y "mock_calls" son objetos
      "call". Estos objetos son tuplas, con la finalidad de que puedan
      ser desempaquetadas para acceder a los argumentos individuales y
      hacer aserciones más complejas. Consultar objetos call como
      tuplas para más información.

      Distinto en la versión 3.8: Propiedades "args" y "kwargs"
      agregadas.

   call_args_list

      Este argumento es una lista de todas las llamadas consecutivas
      realizadas al objeto simulado (por lo que la longitud de la
      lista es el número de veces que se ha invocado). Previamente a
      que se hayan realizado llamadas es una lista vacía. El objeto
      "call" se puede utilizar para construir convenientemente las
      listas de llamadas a comparar con "call_args_list".

      >>> mock = Mock(return_value=None)
      >>> mock()
      >>> mock(3, 4)
      >>> mock(key='fish', next='w00t!')
      >>> mock.call_args_list
      [call(), call(3, 4), call(key='fish', next='w00t!')]
      >>> expected = [(), ((3, 4),), ({'key': 'fish', 'next': 'w00t!'},)]
      >>> mock.call_args_list == expected
      True

      Los miembros de "call_args_list" son objetos "call". Estos
      pueden ser desempaquetados como tuplas para acceder a los
      argumentos individuales. Consultar objetos call como tuplas para
      más información.

   method_calls

      Igual que realizan un seguimiento de las llamadas hechas a sí
      mismos, los objetos simulados también realizan un seguimiento a
      *sus* métodos y atributos, así como de las llamadas hechas a los
      mismos:

      >>> mock = Mock()
      >>> mock.method()
      <Mock name='mock.method()' id='...'>
      >>> mock.property.method.attribute()
      <Mock name='mock.property.method.attribute()' id='...'>
      >>> mock.method_calls
      [call.method(), call.property.method.attribute()]

      Los miembros de "method_calls" son objetos "call". Estos pueden
      ser desempaquetados como tuplas para acceder a los atributos
      individuales. Consultar objetos call como tuplas para más
      información.

   mock_calls

      "mock_calls" registra *todas* las llamadas al objeto simulado,
      sus métodos, métodos mágicos *y* objetos simulados del valor de
      retorno.

      >>> mock = MagicMock()
      >>> result = mock(1, 2, 3)
      >>> mock.first(a=3)
      <MagicMock name='mock.first()' id='...'>
      >>> mock.second()
      <MagicMock name='mock.second()' id='...'>
      >>> int(mock)
      1
      >>> result(1)
      <MagicMock name='mock()()' id='...'>
      >>> expected = [call(1, 2, 3), call.first(a=3), call.second(),
      ... call.__int__(), call()(1)]
      >>> mock.mock_calls == expected
      True

      Los miembros de "mock_calls" son objetos "call". Estos pueden
      ser desempaquetados como tuplas para acceder a los argumentos
      individuales. Consultar objetos call como tuplas para más
      información.

      Nota:

        La forma como se registra el atributo "mock_calls" implica que
        cuando se realizan llamadas anidadas, los parámetros de las
        llamadas previas no se registran, por lo que siempre resultan
        iguales al comparar:

        >>> mock = MagicMock()
        >>> mock.top(a=3).bottom()
        <MagicMock name='mock.top().bottom()' id='...'>
        >>> mock.mock_calls
        [call.top(a=3), call.top().bottom()]
        >>> mock.mock_calls[-1] == call.top(a=-1).bottom()
        True

   __class__

      Normally the "__class__" attribute of an object will return its
      type. For a mock object with a "spec", "__class__" returns the
      spec class instead. This allows mock objects to pass
      "isinstance()" tests for the object they are replacing /
      masquerading as:

      >>> mock = Mock(spec=3)
      >>> isinstance(mock, int)
      True

      "__class__" is assignable to, this allows a mock to pass an
      "isinstance()" check without forcing you to use a spec:

      >>> mock = Mock()
      >>> mock.__class__ = dict
      >>> isinstance(mock, dict)
      True

class unittest.mock.NonCallableMock(spec=None, wraps=None, name=None, spec_set=None, **kwargs)

   Una versión no invocable de "Mock". Los parámetros del constructor
   tienen el mismo significado que en "Mock", con la excepción de
   *return_value* y *side_effect* que no tienen sentido en un objeto
   simulado no invocable.

Mock objects that use a class or an instance as a "spec" or "spec_set"
are able to pass "isinstance()" tests:

>>> mock = Mock(spec=SomeClass)
>>> isinstance(mock, SomeClass)
True
>>> mock = Mock(spec_set=SomeClass())
>>> isinstance(mock, SomeClass)
True

Las clases "Mock" tienen soporte para simular los métodos mágicos.
Consultar la sección dedicada a los métodos mágicos para ver los
detalles.

Las clases simuladas y los decoradores "patch()" aceptan todas
argumentos por palabra clave arbitrarios para la configuración. En los
decoradores "patch()" los argumentos por palabra clave se pasan al
constructor del objeto simulado creado. Estos argumentos se usan para
configurar los atributos del propio objeto simulado:

>>> m = MagicMock(attribute=3, other='fish')
>>> m.attribute
3
>>> m.other
'fish'

Tanto el valor de retorno como el efecto colateral del objeto simulado
pueden ser establecidos de la misma manera, mediante notación de
punto. En cambio, si se quieren establecer mediante el constructor,
dado que no se puede utilizar notación de punto directamente en una
llamada, se tiene que crear un diccionario y desempaquetarlo usando
"**":

>>> attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
>>> mock = Mock(some_attribute='eggs', **attrs)
>>> mock.some_attribute
'eggs'
>>> mock.method()
3
>>> mock.other()
Traceback (most recent call last):
  ...
KeyError

Un objeto simulado invocable que fue creado con un *spec* (o un
*spec_set*) introspeccionará la firma del objeto de la especificación
en el momento de emparejar las llamadas al objeto simulado. Esto le
permite hacer coincidir sus argumentos con los argumentos de la
llamada real, independientemente de si se pasaron por posición o por
nombre:

   >>> def f(a, b, c): pass
   ...
   >>> mock = Mock(spec=f)
   >>> mock(1, 2, c=3)
   <Mock name='mock()' id='140161580456576'>
   >>> mock.assert_called_with(1, 2, 3)
   >>> mock.assert_called_with(a=1, b=2, c=3)

Esto se aplica a "assert_called_with()", "assert_called_once_with()",
"assert_has_calls()" y "assert_any_call()". Cuando se hace uso de
Autoespecificación, también se aplicará a las llamadas a los métodos
del objeto simulado.

Distinto en la versión 3.4: Se añadió introspección de firma en
objetos simulados especificados y autoespecificados.

class unittest.mock.PropertyMock(*args, **kwargs)

   A mock intended to be used as a "property", or other *descriptor*,
   on a class. "PropertyMock" provides "__get__()" and "__set__()"
   methods so you can specify a return value when it is fetched.

   La obtención de una instancia "PropertyMock" desde un objeto
   ocasiona una llamada al objeto simulado, sin argumentos. Establecer
   su valor también llama al objeto simulado, con el valor a
   establecer como argumento.

      >>> class Foo:
      ...     @property
      ...     def foo(self):
      ...         return 'something'
      ...     @foo.setter
      ...     def foo(self, value):
      ...         pass
      ...
      >>> with patch('__main__.Foo.foo', new_callable=PropertyMock) as mock_foo:
      ...     mock_foo.return_value = 'mockity-mock'
      ...     this_foo = Foo()
      ...     print(this_foo.foo)
      ...     this_foo.foo = 6
      ...
      mockity-mock
      >>> mock_foo.mock_calls
      [call(), call(6)]

Debido a la forma en que se almacenan los atributos simulados, no es
posible conectar directamente un "PropertyMock" a un objeto simulado.
En su lugar se puede conectar al tipo (type) del objeto simulado:

   >>> m = MagicMock()
   >>> p = PropertyMock(return_value=3)
   >>> type(m).foo = p
   >>> m.foo
   3
   >>> p.assert_called_once_with()

Prudencia:

  If an "AttributeError" is raised by "PropertyMock", it will be
  interpreted as a missing descriptor and "__getattr__()" will be
  called on the parent mock:

     >>> m = MagicMock()
     >>> no_attribute = PropertyMock(side_effect=AttributeError)
     >>> type(m).my_property = no_attribute
     >>> m.my_property
     <MagicMock name='mock.my_property' id='140165240345424'>

  See "__getattr__()" for details.

class unittest.mock.AsyncMock(spec=None, side_effect=None, return_value=DEFAULT, wraps=None, name=None, spec_set=None, unsafe=False, **kwargs)

   Una versión asíncrona de "Mock". El objeto "AsyncMock" se
   comportará de tal modo que el objeto es reconocido como una función
   asíncrona y el resultado de su llamada es un objeto aguardable
   (awaitable).

   >>> mock = AsyncMock()
   >>> inspect.iscoroutinefunction(mock)
   True
   >>> inspect.isawaitable(mock())
   True

   El resultado de "mock()" es una función asíncrona que proporcionará
   el resultado de "side_effect" o de "return_value" después de haber
   sido aguardada:

   * si "side_effect" es una función, la función asíncrona retornará
     el resultado de esa función,

   * si "side_effect" es una excepción, la función asíncrona lanzará
     la excepción,

   * si "side_effect" es un iterable, la función asíncrona retornará
     el siguiente valor del iterable, sin embargo, si se agota la
     secuencia de resultados, se lanza una excepción
     "StopAsyncIteration" inmediatamente,

   * si "side_effect" no está definido, la función asíncrona retornará
     el valor definido por "return_value", por lo tanto, la función
     asíncrona retorna un nuevo objeto "AsyncMock" por defecto.

   Establecer el argumento *spec* de un objeto "Mock" o "MagicMock" en
   una función asíncrona resultará en que un objeto corrutina será
   retornado después de la llamada al objeto.

   >>> async def async_func(): pass
   ...
   >>> mock = MagicMock(async_func)
   >>> mock
   <MagicMock spec='function' id='...'>
   >>> mock()
   <coroutine object AsyncMockMixin._mock_call at ...>

   Establecer el argumento *spec* de un objeto "Mock", "MagicMock" o
   "AsyncMock" en una clase que tiene simultáneamente funciones
   asíncronas y síncronas hará que se detecten automáticamente las
   funciones sincrónicas y las establecerá como "MagicMock" (si el
   objeto simulado padre es "AsyncMock" o "MagicMock") o "Mock" (si el
   objeto simulado padre es "Mock") . Todas las funciones asíncronas
   serán "AsyncMock".

   >>> class ExampleClass:
   ...     def sync_foo():
   ...         pass
   ...     async def async_foo():
   ...         pass
   ...
   >>> a_mock = AsyncMock(ExampleClass)
   >>> a_mock.sync_foo
   <MagicMock name='mock.sync_foo' id='...'>
   >>> a_mock.async_foo
   <AsyncMock name='mock.async_foo' id='...'>
   >>> mock = Mock(ExampleClass)
   >>> mock.sync_foo
   <Mock name='mock.sync_foo' id='...'>
   >>> mock.async_foo
   <AsyncMock name='mock.async_foo' id='...'>

   Added in version 3.8.

   assert_awaited()

      Assert si el objeto simulado fue aguardado al menos una vez. Ten
      en cuenta que, independientemente del objeto que ha sido
      invocado, la palabra clave "await" debe ser utilizada:

      >>> mock = AsyncMock()
      >>> async def main(coroutine_mock):
      ...     await coroutine_mock
      ...
      >>> coroutine_mock = mock()
      >>> mock.called
      True
      >>> mock.assert_awaited()
      Traceback (most recent call last):
      ...
      AssertionError: Expected mock to have been awaited.
      >>> asyncio.run(main(coroutine_mock))
      >>> mock.assert_awaited()

   assert_awaited_once()

      Assert si el objeto simulado fue aguardado exactamente una vez.

      >>> mock = AsyncMock()
      >>> async def main():
      ...     await mock()
      ...
      >>> asyncio.run(main())
      >>> mock.assert_awaited_once()
      >>> asyncio.run(main())
      >>> mock.assert_awaited_once()
      Traceback (most recent call last):
      ...
      AssertionError: Expected mock to have been awaited once. Awaited 2 times.

   assert_awaited_with(*args, **kwargs)

      Assert si el último aguardo (await) fue con los argumentos
      especificados.

      >>> mock = AsyncMock()
      >>> async def main(*args, **kwargs):
      ...     await mock(*args, **kwargs)
      ...
      >>> asyncio.run(main('foo', bar='bar'))
      >>> mock.assert_awaited_with('foo', bar='bar')
      >>> mock.assert_awaited_with('other')
      Traceback (most recent call last):
      ...
      AssertionError: expected await not found.
      Expected: mock('other')
      Actual: mock('foo', bar='bar')

   assert_awaited_once_with(*args, **kwargs)

      Assert si que el objeto simulado se ha aguardado exactamente una
      vez y con los argumentos especificados.

      >>> mock = AsyncMock()
      >>> async def main(*args, **kwargs):
      ...     await mock(*args, **kwargs)
      ...
      >>> asyncio.run(main('foo', bar='bar'))
      >>> mock.assert_awaited_once_with('foo', bar='bar')
      >>> asyncio.run(main('foo', bar='bar'))
      >>> mock.assert_awaited_once_with('foo', bar='bar')
      Traceback (most recent call last):
      ...
      AssertionError: Expected mock to have been awaited once. Awaited 2 times.

   assert_any_await(*args, **kwargs)

      Assert si el objeto simulado nunca se ha aguardado con los
      argumentos especificados.

      >>> mock = AsyncMock()
      >>> async def main(*args, **kwargs):
      ...     await mock(*args, **kwargs)
      ...
      >>> asyncio.run(main('foo', bar='bar'))
      >>> asyncio.run(main('hello'))
      >>> mock.assert_any_await('foo', bar='bar')
      >>> mock.assert_any_await('other')
      Traceback (most recent call last):
      ...
      AssertionError: mock('other') await not found

   assert_has_awaits(calls, any_order=False)

      Assert si el objeto simulado ha sido aguardado con las llamadas
      especificadas. Para comprobar los aguardos (awaits) se utiliza
      la lista "await_args_list".

      Si *any_order* es falso, los aguardos (awaits) deben ser
      secuenciales. No puede haber llamadas adicionales antes o
      después de los aguardos especificados.

      Si *any_order* es verdadero, entonces los aguardos (awaits)
      pueden estar en cualquier orden, pero deben aparecer todos en
      "await_args_list".

      >>> mock = AsyncMock()
      >>> async def main(*args, **kwargs):
      ...     await mock(*args, **kwargs)
      ...
      >>> calls = [call("foo"), call("bar")]
      >>> mock.assert_has_awaits(calls)
      Traceback (most recent call last):
      ...
      AssertionError: Awaits not found.
      Expected: [call('foo'), call('bar')]
      Actual: []
      >>> asyncio.run(main('foo'))
      >>> asyncio.run(main('bar'))
      >>> mock.assert_has_awaits(calls)

   assert_not_awaited()

      Assert si el objeto simulado nunca ha sido aguardado.

      >>> mock = AsyncMock()
      >>> mock.assert_not_awaited()

   reset_mock(*args, **kwargs)

      Consultar "Mock.reset_mock()". Además, también establece
      "await_count" a 0, "await_args" a None y borra
      "await_args_list".

   await_count

      Un registro entero de cuántas veces se ha aguardado el objeto
      simulado.

      >>> mock = AsyncMock()
      >>> async def main():
      ...     await mock()
      ...
      >>> asyncio.run(main())
      >>> mock.await_count
      1
      >>> asyncio.run(main())
      >>> mock.await_count
      2

   await_args

      Este atributo es "None" (si el objeto simulado no se ha
      aguardado) o los argumentos con los que fue aguardado la última
      vez. Su funcionamiento es idéntico al de "Mock.call_args".

      >>> mock = AsyncMock()
      >>> async def main(*args):
      ...     await mock(*args)
      ...
      >>> mock.await_args
      >>> asyncio.run(main('foo'))
      >>> mock.await_args
      call('foo')
      >>> asyncio.run(main('bar'))
      >>> mock.await_args
      call('bar')

   await_args_list

      Es una lista de todas los aguardos (awaits) realizados en el
      objeto simulado de forma secuencial (por lo que la longitud de
      la lista es el número de veces que se ha aguardado el objeto).
      Si no se han realizado aguardos previos, es una lista vacía.

      >>> mock = AsyncMock()
      >>> async def main(*args):
      ...     await mock(*args)
      ...
      >>> mock.await_args_list
      []
      >>> asyncio.run(main('foo'))
      >>> mock.await_args_list
      [call('foo')]
      >>> asyncio.run(main('bar'))
      >>> mock.await_args_list
      [call('foo'), call('bar')]

class unittest.mock.ThreadingMock(spec=None, side_effect=None, return_value=DEFAULT, wraps=None, name=None, spec_set=None, unsafe=False, *, timeout=UNSET, **kwargs)

   A version of "MagicMock" for multithreading tests. The
   "ThreadingMock" object provides extra methods to wait for a call to
   be invoked, rather than assert on it immediately.

   The default timeout is specified by the "timeout" argument, or if
   unset by the "ThreadingMock.DEFAULT_TIMEOUT" attribute, which
   defaults to blocking ("None").

   You can configure the global default timeout by setting
   "ThreadingMock.DEFAULT_TIMEOUT".

   wait_until_called(*, timeout=UNSET)

      Waits until the mock is called.

      If a timeout was passed at the creation of the mock or if a
      timeout argument is passed to this function, the function raises
      an "AssertionError" if the call is not performed in time.

      >>> mock = ThreadingMock()
      >>> thread = threading.Thread(target=mock)
      >>> thread.start()
      >>> mock.wait_until_called(timeout=1)
      >>> thread.join()

   wait_until_any_call_with(*args, **kwargs)

      Waits until the mock is called with the specified arguments.

      If a timeout was passed at the creation of the mock the function
      raises an "AssertionError" if the call is not performed in time.

      >>> mock = ThreadingMock()
      >>> thread = threading.Thread(target=mock, args=("arg1", "arg2",), kwargs={"arg": "thing"})
      >>> thread.start()
      >>> mock.wait_until_any_call_with("arg1", "arg2", arg="thing")
      >>> thread.join()

   DEFAULT_TIMEOUT

      Global default timeout in seconds to create instances of
      "ThreadingMock".

   Added in version 3.13.

### Llamar a los objetos simulados

Los objetos Mock son invocables. La llamada a uno retornará el valor
establecido en el atributo "return_value". El valor de retorno por
defecto es un nuevo objeto Mock, el cual se crea la primera vez que se
accede al valor de retorno (ya sea explícitamente o llamando al objeto
Mock). Una vez creado, se almacena y el mismo objeto es retornado cada
vez que se solicita.

Las llamadas realizadas al objeto serán registradas en los atributos
"call_args" y "call_args_list".

If "side_effect" is set then it will be called after the call has been
recorded, so if "side_effect" raises an exception the call is still
recorded.

La forma más sencilla de hacer que un objeto simulado lance de una
excepción cuando sea invocado es establecer su atributo "side_effect"
como una clase o instancia de excepción:

>>> m = MagicMock(side_effect=IndexError)
>>> m(1, 2, 3)
Traceback (most recent call last):
  ...
IndexError
>>> m.mock_calls
[call(1, 2, 3)]
>>> m.side_effect = KeyError('Bang!')
>>> m('two', 'three', 'four')
Traceback (most recent call last):
  ...
KeyError: 'Bang!'
>>> m.mock_calls
[call(1, 2, 3), call('two', 'three', 'four')]

If "side_effect" is a function then whatever that function returns is
what calls to the mock return. The "side_effect" function is called
with the same arguments as the mock. This allows you to vary the
return value of the call dynamically, based on the input:

>>> def side_effect(value):
...     return value + 1
...
>>> m = MagicMock(side_effect=side_effect)
>>> m(1)
2
>>> m(2)
3
>>> m.mock_calls
[call(1), call(2)]

If you want the mock to still return the default return value (a new
mock), or any set return value, then there are two ways of doing this.
Either return "return_value" from inside "side_effect", or return
"DEFAULT":

>>> m = MagicMock()
>>> def side_effect(*args, **kwargs):
...     return m.return_value
...
>>> m.side_effect = side_effect
>>> m.return_value = 3
>>> m()
3
>>> def side_effect(*args, **kwargs):
...     return DEFAULT
...
>>> m.side_effect = side_effect
>>> m()
3

To remove a "side_effect", and return to the default behaviour, set
the "side_effect" to "None":

>>> m = MagicMock(return_value=6)
>>> def side_effect(*args, **kwargs):
...     return 3
...
>>> m.side_effect = side_effect
>>> m()
3
>>> m.side_effect = None
>>> m()
6

The "side_effect" can also be any iterable object. Repeated calls to
the mock will return values from the iterable (until the iterable is
exhausted and a "StopIteration" is raised):

>>> m = MagicMock(side_effect=[1, 2, 3])
>>> m()
1
>>> m()
2
>>> m()
3
>>> m()
Traceback (most recent call last):
  ...
StopIteration

Si cualquier miembro del iterable es una excepción, se lanzará en
lugar de retornarse:

   >>> iterable = (33, ValueError, 66)
   >>> m = MagicMock(side_effect=iterable)
   >>> m()
   33
   >>> m()
   Traceback (most recent call last):
    ...
   ValueError
   >>> m()
   66

### Eliminar atributos

Los objetos simulados crean atributos en demanda. Esto les permite
hacerse pasar por objetos de cualquier tipo.

You may want a mock object to return "False" to a "hasattr()" call, or
raise an "AttributeError" when an attribute is fetched. You can do
this by providing an object as a "spec" for a mock, but that isn't
always convenient.

Puedes "bloquear" atributos eliminándolos. Una vez eliminado, el
acceso a un atributo lanzará una excepción "AttributeError".

>>> mock = MagicMock()
>>> hasattr(mock, 'm')
True
>>> del mock.m
>>> hasattr(mock, 'm')
False
>>> del mock.f
>>> mock.f
Traceback (most recent call last):
    ...
AttributeError: f

### Los nombres de los objetos simulados y el atributo *name*

Dado que "name" es un argumento para el constructor de la clase
"Mock", si quieres que tu objeto simulado tenga un atributo "name", no
puedes simplemente pasarlo al constructor en tiempo de creación. Hay
dos alternativas. Una opción es usar el método "configure_mock()":

   >>> mock = MagicMock()
   >>> mock.configure_mock(name='my_name')
   >>> mock.name
   'my_name'

Una opción más sencilla es simplemente establecer el atributo "name"
después de la creación del objeto simulado:

   >>> mock = MagicMock()
   >>> mock.name = "foo"

### Adjuntar objetos simulados como atributos

Cuando se adjunta un objeto simulado como un atributo de otro objeto
simulado (o como su valor de retorno) se convierte en un "hijo" del
mismo. Las llamadas a los hijos se registran en los atributos
"method_calls" y "mock_calls" del padre. Esto es útil para configurar
objetos simulados hijos para después adjuntarlos al padre, o para
adjuntar objetos simulados a un padre que se encargará de registrar
todas las llamadas a los hijos, permitiéndote hacer aserciones sobre
el orden de las llamadas entre objetos simulados:

>>> parent = MagicMock()
>>> child1 = MagicMock(return_value=None)
>>> child2 = MagicMock(return_value=None)
>>> parent.child1 = child1
>>> parent.child2 = child2
>>> child1(1)
>>> child2(2)
>>> parent.mock_calls
[call.child1(1), call.child2(2)]

La excepción a lo anterior es si el objeto simulado tiene un nombre.
Esto te permite evitar el comportamiento de "parentesco" explicado
previamente, si por alguna razón no deseas que suceda.

>>> mock = MagicMock()
>>> not_a_child = MagicMock(name='not-a-child')
>>> mock.attribute = not_a_child
>>> mock.attribute()
<MagicMock name='not-a-child()' id='...'>
>>> mock.mock_calls
[]

Los objetos simulados creados automáticamente por la función "patch()"
también reciben nombres automáticamente. Para adjuntar un objeto
simulado con nombre a un padre debes utilizar el método
"attach_mock()":

   >>> thing1 = object()
   >>> thing2 = object()
   >>> parent = MagicMock()
   >>> with patch('__main__.thing1', return_value=None) as child1:
   ...     with patch('__main__.thing2', return_value=None) as child2:
   ...         parent.attach_mock(child1, 'child1')
   ...         parent.attach_mock(child2, 'child2')
   ...         child1('one')
   ...         child2('two')
   ...
   >>> parent.mock_calls
   [call.child1('one'), call.child2('two')]

[1] Las únicas excepciones son los métodos y atributos mágicos
    (aquellos que tienen doble subrayado al principio y al final).
    Mock no los crea automáticamente, sino que lanza una excepción
    "AttributeError". Esto se debe a que el intérprete a menudo
    solicitará implícitamente estos métodos y terminaría *muy*
    confundido si obtiene un nuevo objeto Mock cuando espera un método
    mágico. Si necesitas soporte para métodos mágicos, consulta
    métodos mágicos.

## Parcheadores

Los decoradores patch se utilizan para parchear los objetos solo
dentro del ámbito de la función que decoran. Se encargan
automáticamente de desparchear una vez terminada la prueba, incluso si
se lanzan excepciones. Todas estas funciones también se pueden
utilizar con declaraciones o como decoradores de clase.

### patch

Nota:

  La clave es realizar el parche en el mismo espacio de nombre. Para
  más detalles consultar la sección where to patch.

unittest.mock.patch(target, new=DEFAULT, spec=None, create=False, spec_set=None, autospec=None, new_callable=None, **kwargs)

   "patch()" actúa como decorador de función, decorador de clase o
   como gestor de contexto. Ya sea en el interior del cuerpo de una
   función o dentro de una declaración with, *target* es parcheado con
   un objeto *new*. Cuando la función / declaración with termina su
   ejecución el parche se deshace automáticamente.

   Si se omite *new*, entonces el objetivo se reemplaza por un objeto
   "AsyncMock" si el objeto parcheado es una función asíncrona, o con
   un objeto "MagicMock" en caso contrario. Si se utiliza "patch()"
   como decorador y se omite *new*, el objeto simulado creado se pasa
   como un argumento adicional a la función decorada. Si se utiliza
   "patch()" como un gestor de contexto, el objeto simulado creado es
   retornado por el gestor de contexto.

   *target* debe ser una cadena de la forma
   "'paquete.modulo.NombreDeLaClase'". *target* es importado y el
   objeto especificado reemplazado por el objeto *new*, por lo que
   *target* debe ser importable desde el entorno desde el cual estás
   llamando a "patch()". Hay que tener presente que *target* es
   importado cuando se ejecuta la función decorada, no en tiempo de
   decoración.

   Los argumentos *spec* y *spec_set* se pasan a "MagicMock" si patch
   está creando automáticamente uno para ti.

   Además, puedes pasar "spec=True" o "spec_set=True", lo que causa
   que patch pase el objeto que está siendo simulado como el objeto
   spec/spec_set.

   *new_callable* te permite especificar una clase diferente, o un
   objeto invocable, que será invocada para crear el objeto *new*. Por
   defecto se utiliza "AsyncMock" para las funciones asíncronas y
   "MagicMock" para el resto.

   Una variante más poderosa de *spec* es *autospec*. Si estableces
   "autospec=True" el objeto simulado se creará con una especificación
   del objeto que está siendo reemplazado. Todos los atributos del
   objeto simulado también tendrán la especificación del atributo
   correspondiente del objeto que está siendo reemplazado. Los
   argumentos de los métodos y funciones simulados son comprobados y
   se lanzará una excepción "TypeError" si se les llama con la firma
   incorrecta. Para los objetos simulados que sustituyen a una clase,
   su valor de retorno (la 'instancia') tendrá la misma especificación
   que la clase. Consultar la función "create_autospec()" y
   Autoespecificación para más detalles.

   En lugar de "autospec=True", puedes pasar "autospec=some_object"
   para utilizar un objeto arbitrario como especificación en lugar del
   objeto reemplazado.

   Por defecto, "patch()" fallará al intentar reemplazar atributos que
   no existen. Si pasas "create=True" y no existe el atributo, patch
   crea el atributo cuando la función se llama y lo elimina de nuevo
   en cuanto termina de ejecutarse . Esto es útil para implementar
   pruebas para atributos que tu código de producción crea en tiempo
   de ejecución. Está desactivado por defecto, ya que puede ser
   peligroso. ¡Al activarlo se pueden implementar pruebas que validen
   APIs que en realidad no existen!

   Nota:

     Distinto en la versión 3.5: Si estás parcheando objetos
     incorporados (builtins) en un módulo, no es necesario pasar
     "create=True", ya que en este caso se agrega de forma
     predeterminada.

   Patch can be used as a "TestCase" class decorator. It works by
   decorating each test method in the class. This reduces the
   boilerplate code when your test methods share a common patchings
   set. "patch()" finds tests by looking for method names that start
   with "patch.TEST_PREFIX". By default this is "'test'", which
   matches the way "unittest" finds tests. You can specify an
   alternative prefix by setting "patch.TEST_PREFIX".

   Patch puede ser usado como un gestor de contexto, con la
   declaración with. En este caso el parcheo se aplica al bloque
   sangrado inmediatamente después de la declaración with. Si utilizas
   "as", el objeto parcheado será enlazado al nombre especificado
   después de "as"; muy útil si "patch()" está creando un objeto
   simulado automáticamente.

   "patch()" toma argumentos por palabra clave arbitrarios. Estos
   serán pasados a "AsyncMock" si el objeto parcheado es asincrónico,
   si es de otra forma "MagicMock" o a un *new_callable* si es
   especificado.

   "patch.dict(...)", "patch.multiple(...)" y "patch.object(...)"
   están disponibles para casos de uso alternativos.

"patch()" como decorador de función, crea el objeto simulado por ti y
lo pasa a la función decorada:

   >>> @patch('__main__.SomeClass')
   ... def function(normal_argument, mock_class):
   ...     print(mock_class is SomeClass)
   ...
   >>> function(None)
   True

Parchear una clase sustituye a la clase por una *instancia* de
"MagicMock". Si la clase se instancia en el código bajo prueba, el
atributo "return_value" del objeto simulado será el utilizado.

Si la clase se instancia en múltiples ocasiones, puedes utilizar el
atributo "side_effect" para retornar un nuevo objeto simulado cada
vez. O también puedes establecer *return_value* para que sea lo que tu
quieras.

To configure return values on methods of *instances* on the patched
class you must do this on the "return_value". For example:

   >>> class Class:
   ...     def method(self):
   ...         pass
   ...
   >>> with patch('__main__.Class') as MockClass:
   ...     instance = MockClass.return_value
   ...     instance.method.return_value = 'foo'
   ...     assert Class() is instance
   ...     assert Class().method() == 'foo'
   ...

Si utilizas *spec* o *spec_set* y "patch()" está reemplazando una
*clase*, el valor de retorno del objeto simulado creado tendrá las
mismas especificaciones:

   >>> Original = Class
   >>> patcher = patch('__main__.Class', spec=True)
   >>> MockClass = patcher.start()
   >>> instance = MockClass()
   >>> assert isinstance(instance, Original)
   >>> patcher.stop()

El argumento *new_callable* es útil cuando deseas utilizar una clase
por defecto alternativa a "MagicMock" para el objeto simulado creado.
Por ejemplo, si quieres que se use una clase "NonCallableMock" por
defecto:

   >>> thing = object()
   >>> with patch('__main__.thing', new_callable=NonCallableMock) as mock_thing:
   ...     assert thing is mock_thing
   ...     thing()
   ...
   Traceback (most recent call last):
     ...
   TypeError: 'NonCallableMock' object is not callable

Otro caso de uso podría ser la sustitución de un objeto por una
instancia de "io.StringIO":

   >>> from io import StringIO
   >>> def foo():
   ...     print('Something')
   ...
   >>> @patch('sys.stdout', new_callable=StringIO)
   ... def test(mock_stdout):
   ...     foo()
   ...     assert mock_stdout.getvalue() == 'Something\n'
   ...
   >>> test()

Cuando "patch()" crea un objeto simulado para ti, a menudo lo primero
que tienes que hacer es configurar el objeto simulado recién creado.
Parte de la configuración se puede hacer en la propia llamada a patch.
Cualquier palabra clave arbitraria que pases a la llamada será
utilizada para establecer los atributos del objeto simulado creado:

   >>> patcher = patch('__main__.thing', first='one', second='two')
   >>> mock_thing = patcher.start()
   >>> mock_thing.first
   'one'
   >>> mock_thing.second
   'two'

Los atributos de los objetos simulados hijos, como "return_value" y
"side_effect", también puede ser configurados en la llamada, dado que
los objetos simulados hijos son atributos en si mismos del objeto
simulado padre creado. Eso si, estos no son sintácticamente válidos
para ser pasados directamente como argumentos por palabras clave a la
función patch, pero un diccionario con ellos como claves si que puede
ser expandido en una llama a "patch()" usando "**":

   >>> config = {'method.return_value': 3, 'other.side_effect': KeyError}
   >>> patcher = patch('__main__.thing', **config)
   >>> mock_thing = patcher.start()
   >>> mock_thing.method()
   3
   >>> mock_thing.other()
   Traceback (most recent call last):
     ...
   KeyError

Por defecto, el intento de parchear una función en un módulo (o un
método o atributo en una clase) que no existe fallará lanzando una
excepción "AttributeError":

   >>> @patch('sys.non_existing_attribute', 42)
   ... def test():
   ...     assert sys.non_existing_attribute == 42
   ...
   >>> test()
   Traceback (most recent call last):
     ...
   AttributeError: <module 'sys' (built-in)> does not have the attribute 'non_existing_attribute'

pero añadir "create=True" en la llamada a "patch()" hará que el
ejemplo previo funcione como se esperaba:

   >>> @patch('sys.non_existing_attribute', 42, create=True)
   ... def test(mock_stdout):
   ...     assert sys.non_existing_attribute == 42
   ...
   >>> test()

Distinto en la versión 3.8: "patch()" ahora retorna una instancia de
"AsyncMock" si el objetivo es una función asíncrona.

### patch.object

patch.object(target, attribute, new=DEFAULT, spec=None, create=False, spec_set=None, autospec=None, new_callable=None, **kwargs)

   parchea el miembro *attribute* invocado de un objeto *target* con
   un objeto simulado.

   "patch.object()" se puede utilizar como un decorador, decorador de
   clase o un gestor de contexto. Los argumentos *new*, *spec*,
   *create*, *spec_set*, *autospec* y *new_callable* tienen el mismo
   significado que en la función "patch()". Al igual que "patch()",
   "patch.object()" toma argumentos por palabras clave arbitrarios
   para la configuración del objeto simulado que crea.

   Cuando se utiliza como un decorador de clase "patch.object()" se
   rige por "patch.TEST_PREFIX" a la hora de elegir los métodos a
   envolver.

Puedes llamar a "patch.object()" con tres argumentos o con dos
argumentos. La forma de tres argumento toma el objeto a parchear, el
nombre del atributo y el objeto con el que reemplazar el atributo.

Al llamar usando la variante de dos argumento se omite el objeto de
sustitución, por lo tanto se crea un objeto simulado automáticamente y
se pasa como argumento adicional a la función decorada:

>>> @patch.object(SomeClass, 'class_method')
... def test(mock_method):
...     SomeClass.class_method(3)
...     mock_method.assert_called_with(3)
...
>>> test()

*spec*, *create* y el resto de argumentos de "patch.object()" tienen
el mismo significado que en la función "patch()".

### patch.dict

patch.dict(in_dict, values=(), clear=False, **kwargs)

   Patch a dictionary, or dictionary like object, and restore the
   dictionary to its original state after the test, where the restored
   dictionary is a copy of the dictionary as it was before the test.

   *in_dict* puede ser un diccionario o un contenedor similar a uno.
   Si se trata de un objeto similar a un diccionario, debe soportar
   como mínimo el establecimiento, la obtención y la eliminación de
   elementos, además de permitir la iteración sobre las claves.

   *in_dict* también puede ser una cadena que especifique el nombre
   del diccionario a parchear, el nombre es usado para obtener el
   diccionario mediante importación.

   *values* puede ser otro diccionario con valores para ser añadidos
   al diccionario. *values* también puede ser un iterable de parejas
   "(clave, valor)".

   Si *clear* es verdadero, el contenido del diccionario se borrará
   antes de establecer los nuevos valores.

   La función "patch.dict()" también puede ser invocada con argumentos
   por palabra clave arbitrarios para establecer los valores en el
   diccionario.

   Distinto en la versión 3.8: La función "patch.dict()" ahora retorna
   el diccionario parcheado cuando se utiliza como gestor de contexto.

"patch.dict()" se puede utilizar como gestor de contexto, decorador o
decorador de clase:

>>> foo = {}
>>> @patch.dict(foo, {'newkey': 'newvalue'})
... def test():
...     assert foo == {'newkey': 'newvalue'}
...
>>> test()
>>> assert foo == {}

Cuando se utiliza "patch.dict()" como decorador de clase, se rige por
"patch.TEST_PREFIX" (por defecto "'test'") a la hora de elegir qué
métodos envolver:

>>> import os
>>> import unittest
>>> from unittest.mock import patch
>>> @patch.dict('os.environ', {'newkey': 'newvalue'})
... class TestSample(unittest.TestCase):
...     def test_sample(self):
...         self.assertEqual(os.environ['newkey'], 'newvalue')

Si deseas utilizar un prefijo diferente para tu prueba, puede informar
a los parcheadores del nuevo prefijo a usar estableciendo
"patch.TEST_PREFIX". Para más detalles sobre cómo cambiar el valor del
atributo consultar TEST_PREFIX.

"patch.dict()" puede utilizarse para agregar miembros a un
diccionario, o simplemente para dejar que una prueba modifique un
diccionario y asegurarte de que el diccionario será restablecido
cuando finalice la misma.

>>> foo = {}
>>> with patch.dict(foo, {'newkey': 'newvalue'}) as patched_foo:
...     assert foo == {'newkey': 'newvalue'}
...     assert patched_foo == {'newkey': 'newvalue'}
...     # You can add, update or delete keys of foo (or patched_foo, it's the same dict)
...     patched_foo['spam'] = 'eggs'
...
>>> assert foo == {}
>>> assert patched_foo == {}

>>> import os
>>> with patch.dict('os.environ', {'newkey': 'newvalue'}):
...     print(os.environ['newkey'])
...
newvalue
>>> assert 'newkey' not in os.environ

Se pueden utilizar argumentos por palabra clave en la llamada a
"patch.dict()" para establecer valores en el diccionario:

>>> mymodule = MagicMock()
>>> mymodule.function.return_value = 'fish'
>>> with patch.dict('sys.modules', mymodule=mymodule):
...     import mymodule
...     mymodule.function('some', 'args')
...
'fish'

"patch.dict()" can be used with dictionary like objects that aren't
actually dictionaries. At the very minimum they must support item
getting, setting, deleting and either iteration or membership test.
This corresponds to the magic methods "__getitem__()",
"__setitem__()", "__delitem__()" and either "__iter__()" or
"__contains__()".

>>> class Container:
...     def __init__(self):
...         self.values = {}
...     def __getitem__(self, name):
...         return self.values[name]
...     def __setitem__(self, name, value):
...         self.values[name] = value
...     def __delitem__(self, name):
...         del self.values[name]
...     def __iter__(self):
...         return iter(self.values)
...
>>> thing = Container()
>>> thing['one'] = 1
>>> with patch.dict(thing, one=2, two=3):
...     assert thing['one'] == 2
...     assert thing['two'] == 3
...
>>> assert thing['one'] == 1
>>> assert list(thing) == ['one']

### patch.multiple

patch.multiple(target, spec=None, create=False, spec_set=None, autospec=None, new_callable=None, **kwargs)

   Realiza múltiples parches en una sola llamada. Se toma el objeto a
   ser parcheado (ya sea como un objeto o una cadena de caracteres con
   el nombre del mismo para obtener el objeto mediante importación) y
   los argumentos por palabras clave para los parches:

      with patch.multiple(settings, FIRST_PATCH='one', SECOND_PATCH='two'):
          ...

   Usa "DEFAULT" como valor si deseas que la función
   "patch.multiple()" cree objetos simulados automáticamente por ti.
   En este caso, los objetos simulados creados son pasados a la
   función decorada mediante palabra clave y se retorna un diccionario
   cuando "patch.multiple()" se utiliza como gestor de contexto.

   La función "patch.multiple()" se puede utilizar como un decorador,
   decorador de clase o como gestor de contexto. La argumentos *spec*,
   *spec_set*, *create*, *autospec* y *new_callable* tienen el mismo
   significado que en la función "patch()". Estos argumentos se
   aplicarán a *todos* los parches realizados por "patch.multiple()".

   Cuando se utiliza como decorador de clase, "patch.multiple()" se
   rige por "patch.TEST_PREFIX" a la hora de elegir qué métodos
   envolver.

Si deseas que "patch.multiple()" cree objetos simulados
automáticamente por ti, puedes utilizar "DEFAULT" como valor. Si
utilizas "patch.multiple()" como decorador, entonces los objetos
simulados creados se pasan a la función decorada por palabra clave:

   >>> thing = object()
   >>> other = object()

   >>> @patch.multiple('__main__', thing=DEFAULT, other=DEFAULT)
   ... def test_function(thing, other):
   ...     assert isinstance(thing, MagicMock)
   ...     assert isinstance(other, MagicMock)
   ...
   >>> test_function()

"patch.multiple()" se puede anidar junto a otros decoradores "patch",
pero los argumentos pasados por palabra clave se deben agregar
*después* de cualquier argumento estándar creado por "patch()":

   >>> @patch('sys.exit')
   ... @patch.multiple('__main__', thing=DEFAULT, other=DEFAULT)
   ... def test_function(mock_exit, other, thing):
   ...     assert 'other' in repr(other)
   ...     assert 'thing' in repr(thing)
   ...     assert 'exit' in repr(mock_exit)
   ...
   >>> test_function()

Si "patch.multiple()" se utiliza como un gestor de contexto, el valor
retornado por el mismo es un diccionario en el que los objetos
simulados creados son almacenados, usando sus nombres como claves:

   >>> with patch.multiple('__main__', thing=DEFAULT, other=DEFAULT) as values:
   ...     assert 'other' in repr(values['other'])
   ...     assert 'thing' in repr(values['thing'])
   ...     assert values['thing'] is thing
   ...     assert values['other'] is other
   ...

### métodos start y stop de patch

All the patchers have "start()" and "stop()" methods. These make it
simpler to do patching in "setUp" methods or where you want to do
multiple patches without nesting decorators or with statements.

To use them call "patch()", "patch.object()" or "patch.dict()" as
normal and keep a reference to the returned "patcher" object. You can
then call "start()" to put the patch in place and "stop()" to undo it.

Si estás utilizando "patch()" para crear un objeto simulado
automáticamente, este será retornado por la llamada a "patcher.start":

   >>> patcher = patch('package.module.ClassName')
   >>> from package import module
   >>> original = module.ClassName
   >>> new_mock = patcher.start()
   >>> assert module.ClassName is not original
   >>> assert module.ClassName is new_mock
   >>> patcher.stop()
   >>> assert module.ClassName is original
   >>> assert module.ClassName is not new_mock

A typical use case for this might be for doing multiple patches in the
"setUp" method of a "TestCase":

   >>> class MyTest(unittest.TestCase):
   ...     def setUp(self):
   ...         self.patcher1 = patch('package.module.Class1')
   ...         self.patcher2 = patch('package.module.Class2')
   ...         self.MockClass1 = self.patcher1.start()
   ...         self.MockClass2 = self.patcher2.start()
   ...
   ...     def tearDown(self):
   ...         self.patcher1.stop()
   ...         self.patcher2.stop()
   ...
   ...     def test_something(self):
   ...         assert package.module.Class1 is self.MockClass1
   ...         assert package.module.Class2 is self.MockClass2
   ...
   >>> MyTest('test_something').run()

Prudencia:

  Si se utiliza esta técnica debes asegurarte de que el parcheo está
  "sin aplicar" llamando a "stop". Esto puede ser más complicado de lo
  que parece, ya que si se produce una excepción en el "setUp" no se
  llama a "tearDown" a continuación. "unittest.TestCase.addCleanup()"
  hace que esto sea más fácil:

     >>> class MyTest(unittest.TestCase):
     ...     def setUp(self):
     ...         patcher = patch('package.module.Class')
     ...         self.MockClass = patcher.start()
     ...         self.addCleanup(patcher.stop)
     ...
     ...     def test_something(self):
     ...         assert package.module.Class is self.MockClass
     ...

  Como beneficio adicional, ya no es necesario mantener una referencia
  al objeto "patcher".

También es posible detener todos los parches que han sido iniciados
usando "patch.stopall()".

patch.stopall()

   Detiene todos los parches activos. Solo se detienen parches
   iniciados con "start".

### parchear objetos incorporados (builtins)

Puedes parchear cualquier objeto incorporado dentro de un módulo. El
siguiente ejemplo parchea la función incorporada "ord()":

   >>> @patch('__main__.ord')
   ... def test(mock_ord):
   ...     mock_ord.return_value = 101
   ...     print(ord('c'))
   ...
   >>> test()
   101

### TEST_PREFIX

Todos los parcheadores se puede utilizar como decoradores de clase.
Cuando se usan de esta forma, todos los métodos a probar en la clase
son envueltos. Los parcheadores reconocen los métodos que comienzan
con "'test'" como métodos a probar. Esta es la misma forma que la
clase "unittest.TestLoader" usa para encontrar métodos de prueba por
defecto.

Cabe la posibilidad de que desees utilizar un prefijo diferente para
las pruebas. Puedes informar a los parcheadores del cambio de prefijo
estableciendo el atributo "patch.TEST_PREFIX":

   >>> patch.TEST_PREFIX = 'foo'
   >>> value = 3
   >>>
   >>> @patch('__main__.value', 'not three')
   ... class Thing:
   ...     def foo_one(self):
   ...         print(value)
   ...     def foo_two(self):
   ...         print(value)
   ...
   >>>
   >>> Thing().foo_one()
   not three
   >>> Thing().foo_two()
   not three
   >>> value
   3

### Anidando decoradores patch

Si deseas aplicar múltiples parches, solo tienes que apilar los
decoradores.

Puede apilar múltiples decoradores patch usando el siguiente patrón:

>>> @patch.object(SomeClass, 'class_method')
... @patch.object(SomeClass, 'static_method')
... def test(mock1, mock2):
...     assert SomeClass.static_method is mock1
...     assert SomeClass.class_method is mock2
...     SomeClass.static_method('foo')
...     SomeClass.class_method('bar')
...     return mock1, mock2
...
>>> mock1, mock2 = test()
>>> mock1.assert_called_once_with('foo')
>>> mock2.assert_called_once_with('bar')

Ten en cuenta que los decoradores se aplican desde abajo hacia arriba.
Esta es la manera estándar de Python para aplicar decoradores. El
orden en el que los objetos simulados generados se pasan a la función
de prueba coincide con este orden.

### Dónde parchear

"patch()" funciona cambiando (temporalmente) el objeto al que apunta
*name* con otro. Puede haber muchos nombres apuntando a cualquier
objeto individual, por lo que para que el parcheo funcione, debes
asegurarte de parchear el nombre utilizado para el objeto por el
sistema concreto bajo prueba.

El principio básico es parchear donde un objeto es *buscado*, que no
es necesariamente el mismo lugar donde está definido. Un par de
ejemplos ayudarán a aclarar esto.

Imaginemos que tenemos un proyecto, que queremos probar, con la
siguiente estructura:

   a.py
       -> Defines SomeClass

   b.py
       -> from a import SomeClass
       -> some_function instantiates SomeClass

Now we want to test "some_function" but we want to mock out
"SomeClass" using "patch()". The problem is that when we import module
b, which we will have to do when it imports "SomeClass" from module a.
If we use "patch()" to mock out "a.SomeClass" then it will have no
effect on our test; module b already has a reference to the *real*
"SomeClass" and it looks like our patching had no effect.

La clave es parchear "SomeClass" donde se utiliza (o donde es
buscado). En este caso "some_function" realmente va a buscar
"SomeClass" en el módulo b, donde lo hemos importado. La aplicación de
parches debe ser similar a:

   @patch('b.SomeClass')

Sin embargo, ten en cuenta el escenario alternativo donde en el módulo
b en lugar de "from a import SomeClass" se hace "import a" y
"some_function" usa "a.SomeClass". Ambas formas de importación son
comunes. En este caso, la clase que queremos parchear está siendo
buscada en el módulo, por lo que tenemos que parchear "a.SomeClass":

   @patch('a.SomeClass')

### Parcheando descriptores y objetos proxy

Tanto patch como patch.object parchean y restauran correctamente los
descriptores: métodos de clase, métodos estáticos y propiedades. Debe
parcharlos en el *class* en lugar de una instancia. También funcionan
con objetos *some* que acceden a atributos de proxy, como django
settings object.

## MagicMock y el soporte de métodos mágicos

### Simular métodos mágicos

"Mock" supports mocking the Python protocol methods, also known as
*"magic methods"*. This allows mock objects to replace containers or
other objects that implement Python protocols.

Dado que los métodos mágicos se buscan de manera diferente a los
métodos normales [2], este soporte ha sido especialmente implementado.
Esto significa que solo es compatible con métodos mágicos específicos.
La lista de métodos soportados incluye *casi* todos los existentes. Si
hay alguno que falta y que consideras necesario, por favor háznoslo
saber.

Puedes simular métodos mágicos estableciendo el método que te interesa
en una función o en una instancia simulada. Si utilizas una función,
*debe* aceptar "self" como primer argumento [3].

>>> def __str__(self):
...     return 'fooble'
...
>>> mock = Mock()
>>> mock.__str__ = __str__
>>> str(mock)
'fooble'

>>> mock = Mock()
>>> mock.__str__ = Mock()
>>> mock.__str__.return_value = 'fooble'
>>> str(mock)
'fooble'

>>> mock = Mock()
>>> mock.__iter__ = Mock(return_value=iter([]))
>>> list(mock)
[]

Un caso de uso para esto es simular objetos usados como gestores de
contexto en una declaración "with":

>>> mock = Mock()
>>> mock.__enter__ = Mock(return_value='foo')
>>> mock.__exit__ = Mock(return_value=False)
>>> with mock as m:
...     assert m == 'foo'
...
>>> mock.__enter__.assert_called_with()
>>> mock.__exit__.assert_called_with(None, None, None)

Las llamadas a métodos mágicos no aparecen registradas en
"method_calls", aunque si se registran en "mock_calls".

Nota:

  Si se utiliza el argumento por palabra clave *spec* para crear un
  objeto simulado, intentar después establecer un método mágico que no
  está en la especificación lanzará una excepción "AttributeError".

La lista completa de los métodos mágicos soportados es la siguiente:

* "__hash__", "__sizeof__", "__repr__" y "__str__"

* "__dir__", "__format__" y "__subclasses__"

* "__round__", "__floor__", "__trunc__" y "__ceil__"

* Comparaciones: "__lt__", "__gt__", "__le__", "__ge__", "__eq__" y
  "__ne__"

* Métodos de contenedores: "__getitem__", "__setitem__",
  "__delitem__", "__contains__", "__len__", "__iter__", "__reversed__"
  y "__missing__"

* Administrador de contexto: "__enter__", "__exit__", "__aenter__" y
  "__aexit__"

* Métodos numéricos unarios: "__neg__", "__pos__" y "__invert__"

* Los métodos numéricos (incluidas las variantes de mano derecha e in
  situ): "__add__", "__sub__", "__mul__", "__matmul__", "__truediv__",
  "__floordiv__", "__mod__", "__divmod__", "__lshift__", "__rshift__",
  "__and__", "__xor__", "__or__" y "__pow__"

* Métodos de conversión numérica: "__complex__", "__int__",
  "__float__" y "__index__"

* Métodos de descriptores: "__get__", "__set__" y "__delete__"

* Pickling: "__reduce__", "__reduce_ex__", "__getinitargs__",
  "__getnewargs__", "__getstate__" y "__setstate__"

* Representación de rutas del sistema de archivos: "__fspath__"

* Métodos de iteración asíncronos: "__aiter__" y "__anext__"

Distinto en la versión 3.8: Se añadió soporte para
"os.PathLike.__fspath__()".

Distinto en la versión 3.8: Se añadió soporte para "__aenter__",
"__aexit__", "__aiter__" y "__anext__".

Los siguientes métodos existen pero *no* están soportados, ya sea
porque son usados por el propio objeto simulado, porque no se pueden
establecer dinámicamente o porque pueden causar problemas:

* "__getattr__", "__setattr__", "__init__" y "__new__"

* "__prepare__", "__instancecheck__", "__subclasscheck__" y "__del__"

### Magic Mock

Hay dos variantes de "MagicMock": "MagicMock" y
"NonCallableMagicMock".

class unittest.mock.MagicMock(*args, **kw)

   "MagicMock" is a subclass of "Mock" with default implementations of
   most of the *magic methods*. You can use "MagicMock" without having
   to configure the magic methods yourself.

   Los parámetros del constructor tienen el mismo significado que en
   "Mock".

   Si utilizas los argumentos *spec* o *spec_set* entonces *solo* los
   métodos mágicos que existan en la especificación serán creados.

class unittest.mock.NonCallableMagicMock(*args, **kw)

   Una versión no invocable de "MagicMock".

   Los parámetros del constructor tienen el mismo significado que en
   "MagicMock", con la excepción de *return_value* y *side_effect* que
   no tienen significado en un objeto simulado no invocable.

Los métodos mágicos están implementados mediante objetos "MagicMock",
por lo que puedes configurarlos y utilizarlos de la forma habitual:

>>> mock = MagicMock()
>>> mock[3] = 'fish'
>>> mock.__setitem__.assert_called_with(3, 'fish')
>>> mock.__getitem__.return_value = 'result'
>>> mock[2]
'result'

Por defecto, muchos de los métodos de protocolo están obligados a
retornar objetos de un tipo específico. Estos métodos están
preconfigurados con un valor de retorno por defecto, de manera que
puedan ser utilizados sin tener que hacer nada más, siempre que no
estés interesado en el valor de retorno. En todo caso, puedes
*establecer* el valor de retorno de forma manual si deseas cambiar el
valor predeterminado.

Métodos y sus valores por defecto:

* "__lt__": "NotImplemented"

* "__gt__": "NotImplemented"

* "__le__": "NotImplemented"

* "__ge__": "NotImplemented"

* "__int__": "1"

* "__contains__": "False"

* "__len__": "0"

* "__iter__": "iter([])"

* "__exit__": "False"

* "__aexit__": "False"

* "__complex__": "1j"

* "__float__": "1.0"

* "__bool__": "True"

* "__index__": "1"

* "__hash__": hash predeterminado del objeto simulado

* "__str__": str predeterminado del objeto simulado

* "__sizeof__": sizeof predeterminado del objeto simulado

Por ejemplo:

>>> mock = MagicMock()
>>> int(mock)
1
>>> len(mock)
0
>>> list(mock)
[]
>>> object() in mock
False

The two equality methods, "__eq__()" and "__ne__()", are special. They
do the default equality comparison on identity, using the
"side_effect" attribute, unless you change their return value to
return something else:

   >>> MagicMock() == 3
   False
   >>> MagicMock() != 3
   True
   >>> mock = MagicMock()
   >>> mock.__eq__.return_value = True
   >>> mock == 3
   True

The return value of "__iter__()" can be any iterable object and isn't
required to be an iterator:

>>> mock = MagicMock()
>>> mock.__iter__.return_value = ['a', 'b', 'c']
>>> list(mock)
['a', 'b', 'c']
>>> list(mock)
['a', 'b', 'c']

Si el valor de retorno *es* un iterador, iterar sobre él una vez que
se consume, y cualquier iteración posterior, resultará en una lista
vacía:

>>> mock.__iter__.return_value = iter(['a', 'b', 'c'])
>>> list(mock)
['a', 'b', 'c']
>>> list(mock)
[]

"MagicMock" tiene todos los métodos mágicos soportados configurados a
excepción de algunos de los más oscuros y obsoletos. De todas formas,
puedes configurar estos también si lo deseas.

Los métodos mágicos que son compatibles, pero que no están
configurados por defecto en "MagicMock" son:

* "__subclasses__"

* "__dir__"

* "__format__"

* "__get__", "__set__" y "__delete__"

* "__reversed__" y "__missing__"

* "__reduce__", "__reduce_ex__", "__getinitargs__", "__getnewargs__",
  "__getstate__" y "__setstate__"

* "__getformat__"

[2] Los métodos mágicos *deben* ser buscados en la clase en lugar de
    en la instancia. Diferentes versiones de Python son inconsistentes
    sobre la aplicación de esta regla. Los métodos de protocolo
    soportados deben trabajar con todas las versiones de Python.

[3] La función está básicamente conectada a la clase, pero cada
    instancia "Mock" se mantiene aislada de las demás.

## Ayudantes

### sentinel

unittest.mock.sentinel

   El objeto "sentinel" proporciona una manera conveniente de
   proporcionar objetos únicos para tus pruebas.

   Los atributos se crean a demanda, en el instante en el que se
   accede a ellos por su nombre por primera vez. El acceso al mismo
   atributo siempre retornará el mismo objeto. Los objetos retornados
   tienen una reproducción (repr) apropiada para que los mensajes de
   error de la prueba sean legibles.

   Distinto en la versión 3.7: Los atributos "sentinel" ahora
   preservan su identidad cuando son "copiados" o "serializados con
   pickle".

A veces, cuando implementas pruebas, necesitas probar que un
determinado objeto se pasa como argumento a otro método, o se retorna.
Crear objetos centinela con un nombre para probar esto puede ser una
práctica común. "sentinel" proporciona una manera conveniente de crear
y probar la identidad de este tipo de objetos.

En el siguiente ejemplo, parcheamos "method" para retornar
"sentinel.some_object":

>>> real = ProductionClass()
>>> real.method = Mock(name="method")
>>> real.method.return_value = sentinel.some_object
>>> result = real.method()
>>> assert result is sentinel.some_object
>>> result
sentinel.some_object

### DEFAULT

unittest.mock.DEFAULT

   El objeto "DEFAULT" es un centinela pre-creado (actualmente
   "sentinel.DEFAULT"). Puede ser usado por las funciones
   "side_effect" para indicar que el valor de retorno normal debe ser
   utilizado.

### call

unittest.mock.call(*args, **kwargs)

   "call()" es un objeto ayudante que puede usarse para hacer
   aserciones simples, para comparar con "call_args",
   "call_args_list", "mock_calls" y "method_calls". "call()" y también
   se puede utilizar con "assert_has_calls()".

   >>> m = MagicMock(return_value=None)
   >>> m(1, 2, a='foo', b='bar')
   >>> m()
   >>> m.call_args_list == [call(1, 2, a='foo', b='bar'), call()]
   True

call.call_list()

   Para un objeto call que representa múltiples llamadas, el método
   "call_list()" retorna una lista con todas las llamadas intermedias,
   así como la llamada final.

"call_list" es particularmente útil para hacer aserciones sobre
"llamadas encadenadas". Una llamada encadenada es varias llamadas en
una sola línea de código. Esto resulta en múltiples entradas en el
atributo "mock_calls" de un objeto simulado. Construir manualmente la
secuencia de llamadas puede ser tedioso.

"call_list()" puede construir la secuencia de llamadas desde la misma
llamada encadenada:

>>> m = MagicMock()
>>> m(1).method(arg='foo').other('bar')(2.0)
<MagicMock name='mock().method().other()()' id='...'>
>>> kall = call(1).method(arg='foo').other('bar')(2.0)
>>> kall.call_list()
[call(1),
 call().method(arg='foo'),
 call().method().other('bar'),
 call().method().other()(2.0)]
>>> m.mock_calls == kall.call_list()
True

Un objeto "call", dependiendo de cómo fuera construido, puede ser una
tupla de la forma (argumentos posicionales, argumentos por palabras
clave) o bien de la forma (nombre, argumentos posicionales, argumentos
por palabras clave). Esto no es particularmente interesante cuando los
construyes por ti mismo, pero la introspección de los objetos "call"
que conforman los atributos "Mock.call_args", "Mock.call_args_list" y
"Mock.mock_calls" si pueden ser de utilidad para para acceder a los
argumentos individuales que contienen.

Los objetos "call" en "Mock.call_args" y "Mock.call_args_list" están
conformados por dos tuplas (argumentos posicionales, argumentos por
palabra clave) mientras que los objetos "call" en "Mock.mock_calls",
junto con los que construyas por ti mismo, constan de tres tuplas
(nombre, argumentos posicionales, argumentos por palabra clave).

Puedes utilizar esta presentación en forma de tuplas para obtener los
argumentos individuales, con la finalidad de llevar a cabo
introspección y aserciones más complejas. Los argumentos posicionales
son una tupla (vacía si no hay ninguno) y los argumentos por palabra
clave son un diccionario:

>>> m = MagicMock(return_value=None)
>>> m(1, 2, 3, arg='one', arg2='two')
>>> kall = m.call_args
>>> kall.args
(1, 2, 3)
>>> kall.kwargs
{'arg': 'one', 'arg2': 'two'}
>>> kall.args is kall[0]
True
>>> kall.kwargs is kall[1]
True

>>> m = MagicMock()
>>> m.foo(4, 5, 6, arg='two', arg2='three')
<MagicMock name='mock.foo()' id='...'>
>>> kall = m.mock_calls[0]
>>> name, args, kwargs = kall
>>> name
'foo'
>>> args
(4, 5, 6)
>>> kwargs
{'arg': 'two', 'arg2': 'three'}
>>> name is m.mock_calls[0][0]
True

### create_autospec

unittest.mock.create_autospec(spec, spec_set=False, instance=False, **kwargs)

   Crea un nuevo objeto simulado utilizando otro objeto (*spec*) como
   especificación. Los atributos del objeto simulado utilizarán el
   atributo correspondiente del objeto *spec* como su especificación.

   Los argumentos de las funciones o métodos simulados se validarán
   para asegurarse de que son invocados con la firma correcta.

   Si *spec_set* es "True", tratar de establecer atributos que no
   existen en el objeto especificado lanzará una excepción
   "AttributeError".

   Si se utiliza una clase como especificación, el valor de retorno
   del objeto simulado (la instancia de la clase) tendrá la misma
   especificación. Se puede utilizar una clase como especificación de
   una instancia pasando "instance=True". El objeto simulado retornado
   solo será invocable si las instancias del objeto simulado son
   también invocables.

   "create_autospec()" también acepta argumentos por palabra clave
   arbitrarios, que son pasados al constructor del objeto simulado
   creado.

Consultar Autoespecificación para ver ejemplos de cómo utilizar la
autoespecificación mediante "create_autospec()" y el argumento
*autospec* de "patch()".

Distinto en la versión 3.8: "create_autospec()" ahora retorna un
objeto "AsyncMock" si el objetivo a simular es una función asíncrona.

### ANY

unittest.mock.ANY

A veces puede que necesites hacer aserciones sobre *algunos* de los
argumentos de una llamada al objeto simulado, pero sin preocuparte por
el resto, o puede que quieras hacer uso de ellos de forma individual
fuera de "call_args" y hacer aserciones más complejas con ellos.

Para ignorar ciertos argumentos puedes pasar objetos que se comparan
como iguales con *cualquier cosa*. En este caso, las llamadas a
"assert_called_with()" y "assert_called_once_with()" tendrán éxito sin
importar lo que se haya pasado realmente.

>>> mock = Mock(return_value=None)
>>> mock('foo', bar=object())
>>> mock.assert_called_once_with('foo', bar=ANY)

"ANY" también se puede utilizar en las comparaciones con las listas de
llamadas, como "mock_calls":

>>> m = MagicMock(return_value=None)
>>> m(1)
>>> m(1, 2)
>>> m(object())
>>> m.mock_calls == [call(1), call(1, 2), ANY]
True

"ANY" is not limited to comparisons with call objects and so can also
be used in test assertions:

   class TestStringMethods(unittest.TestCase):

       def test_split(self):
           s = 'hello world'
           self.assertEqual(s.split(), ['hello', ANY])

### FILTER_DIR

unittest.mock.FILTER_DIR

"FILTER_DIR" es una variable de nivel de módulo que controla la forma
en que los objetos simulados responden a "dir()". El valor
predeterminado es "True", que utiliza el filtrado que se describe a
continuación para mostrar solo los miembros útiles. Si no le gusta
este filtrado o necesita desactivarlo con fines de diagnóstico,
configure "mock.FILTER_DIR = False".

Con el filtrado activado, "dir(some_mock)" mostrará solo atributos
útiles y además incluirá cualquier atributo creado dinámicamente, que
normalmente no se mostraría. Si el objeto simulado fue creado con un
*spec* (o *autospec*) se muestran todos los atributos del objeto
original, incluso si no se ha accedido a ellos todavía:

   >>> dir(Mock())
   ['assert_any_call',
    'assert_called',
    'assert_called_once',
    'assert_called_once_with',
    'assert_called_with',
    'assert_has_calls',
    'assert_not_called',
    'attach_mock',
    ...
   >>> from urllib import request
   >>> dir(Mock(spec=request))
   ['AbstractBasicAuthHandler',
    'AbstractDigestAuthHandler',
    'AbstractHTTPHandler',
    'BaseHandler',
    ...

Muchos de los atributos con subrayado y doble subrayado no muy útiles
(atributos privados de "Mock" y no del objeto real que se está
simulando) se han filtrado del resultado de llamar a "dir()" en un
objeto "Mock". Si no te gusta este comportamiento, puedes desactivarlo
estableciendo el modificador a nivel de módulo "FILTER_DIR":

   >>> from unittest import mock
   >>> mock.FILTER_DIR = False
   >>> dir(mock.Mock())
   ['_NonCallableMock__get_return_value',
    '_NonCallableMock__get_side_effect',
    '_NonCallableMock__return_value_doc',
    '_NonCallableMock__set_return_value',
    '_NonCallableMock__set_side_effect',
    '__call__',
    '__class__',
    ...

Alternatively you can just use "vars(my_mock)" (instance members) and
"dir(type(my_mock))" (type members) to bypass the filtering
irrespective of "FILTER_DIR".

### mock_open

unittest.mock.mock_open(mock=None, read_data='')

   Una función auxiliar que permite crear un objeto simulado con la
   finalidad de reemplazar el uso de "open()". Funciona para simular
   llamadas directas a "open()" y para aquellos casos en los que es
   utilizada como gestor de contexto.

   El argumento *mock* es el objeto simulado a configurar. Si es
   "None" (por defecto) un objeto "MagicMock" se creará para ti, con
   la API limitada a métodos o atributos disponibles en los gestores
   de fichero estándares.

   *read_data* is a string for the "read()", "readline()", and
   "readlines()" methods of the file handle to return.  Calls to those
   methods will take data from *read_data* until it is depleted.  The
   mock of these methods is pretty simplistic: every time the *mock*
   is called, the *read_data* is rewound to the start.  If you need
   more control over the data that you are feeding to the tested code
   you will need to customize this mock for yourself.  When that is
   insufficient, one of the in-memory filesystem packages on PyPI can
   offer a realistic filesystem for testing.

   Distinto en la versión 3.4: Added "readline()" and "readlines()"
   support. The mock of "read()" changed to consume *read_data* rather
   than returning it on each call.

   Distinto en la versión 3.5: *read_data* ahora es restablecido en
   cada llamada al *mock*.

   Distinto en la versión 3.8: Added "__iter__()" to implementation so
   that iteration (such as in for loops) correctly consumes
   *read_data*.

Usar "open()" como gestor de contexto es una buena manera de
asegurarse de que los gestores de archivos se cierren correctamente al
terminar y se está convirtiendo en una práctica común:

   with open('/some/path', 'w') as f:
       f.write('something')

The issue is that even if you mock out the call to "open()" it is the
*returned object* that is used as a context manager (and has
"__enter__()" and "__exit__()" called).

Simular gestores de contexto con un "MagicMock" es lo suficientemente
común y complicado como para que una función auxiliar sea útil:

   >>> m = mock_open()
   >>> with patch('__main__.open', m):
   ...     with open('foo', 'w') as h:
   ...         h.write('some stuff')
   ...
   >>> m.mock_calls
   [call('foo', 'w'),
    call().__enter__(),
    call().write('some stuff'),
    call().__exit__(None, None, None)]
   >>> m.assert_called_once_with('foo', 'w')
   >>> handle = m()
   >>> handle.write.assert_called_once_with('some stuff')

Y para la lectura de archivos:

   >>> with patch('__main__.open', mock_open(read_data='bibble')) as m:
   ...     with open('foo') as h:
   ...         result = h.read()
   ...
   >>> m.assert_called_once_with('foo')
   >>> assert result == 'bibble'

### Autoespecificación

Autospeccing is based on the existing "spec" feature of mock. It
limits the api of mocks to the api of an original object (the spec),
but it is recursive (implemented lazily) so that attributes of mocks
only have the same api as the attributes of the spec. In addition
mocked functions / methods have the same call signature as the
original so they raise a "TypeError" if they are called incorrectly.

Antes de explicar cómo funciona la autoespecificación, he aquí por qué
se necesita.

"Mock" is a very powerful and flexible object, but it suffers from a
flaw which is general to mocking. If you refactor some of your code,
rename members and so on, any tests for code that is still using the
*old api* but uses mocks instead of the real objects will still pass.
This means your tests can all pass even though your code is broken.

Distinto en la versión 3.5: Before 3.5, tests with a typo in the word
assert would silently pass when they should raise an error. You can
still achieve this behavior by passing "unsafe=True" to Mock.

Ten en cuenta que esta es otra razón por la que necesitas pruebas de
integración además de pruebas unitarias. Probar todo de forma aislada
está muy bien, pero si no pruebas cómo están "conectadas entre sí" tus
unidades, todavía hay mucho espacio para errores que las pruebas
deberían haber detectado.

"unittest.mock" already provides a feature to help with this, called
speccing. If you use a class or instance as the "spec" for a mock then
you can only access attributes on the mock that exist on the real
class:

>>> from urllib import request
>>> mock = Mock(spec=request.Request)
>>> mock.assret_called_with  # Intentional typo!
Traceback (most recent call last):
 ...
AttributeError: Mock object has no attribute 'assret_called_with'

La especificación solo se aplica al propio objeto simulado, por lo que
aún tenemos el mismo problema con cualquiera de los métodos del mismo:

   >>> mock.header_items()
   <mock.Mock object at 0x...>
   >>> mock.header_items.assret_called_with()  # Intentional typo!

La autoespecificación resuelve este problema. Puedes pasar
"autospec=True" a "patch()" / "patch.object()" o utilizar la función
"create_autospec()" para crear un objeto simulado con una
especificación. Si utilizas el argumento "autospec=True" de "patch()",
el objeto que se va a reemplazar se utiliza como objeto de
especificación. Debido a que la especificación se hace "perezosamente"
(la especificación se crea en el instante en el que se accede a los
atributos del objeto simulado, no antes), se puede utilizar con
objetos muy complejos o anidadas (como módulos que importan módulos
que, a su vez, importan otros módulos) sin un gran impacto en el
rendimiento.

He aquí un ejemplo de ello en acción:

   >>> from urllib import request
   >>> patcher = patch('__main__.request', autospec=True)
   >>> mock_request = patcher.start()
   >>> request is mock_request
   True
   >>> mock_request.Request
   <MagicMock name='request.Request' spec='Request' id='...'>

You can see that "request.Request" has a spec. "request.Request" takes
two arguments in the constructor (one of which is *self*). Here's what
happens if we try to call it incorrectly:

   >>> req = request.Request()
   Traceback (most recent call last):
    ...
   TypeError: <lambda>() takes at least 2 arguments (1 given)

La especificación también se aplica a las clases instanciadas (es
decir, el valor de retorno de los objetos simulados especificados):

   >>> req = request.Request('foo')
   >>> req
   <NonCallableMagicMock name='request.Request()' spec='Request' id='...'>

"Request" objects are not callable, so the return value of
instantiating our mocked out "request.Request" is a non-callable mock.
With the spec in place any typos in our asserts will raise the correct
error:

   >>> req.add_header('spam', 'eggs')
   <MagicMock name='request.Request().add_header()' id='...'>
   >>> req.add_header.assret_called_with  # Intentional typo!
   Traceback (most recent call last):
    ...
   AttributeError: Mock object has no attribute 'assret_called_with'
   >>> req.add_header.assert_called_with('spam', 'eggs')

En muchos casos, podrás simplemente añadir "autospec=True" a tus
llamadas "patch()" existentes y así estar protegido contra errores
tipográficos y cambios de la API.

Además de poder usar *autospec* a través de "patch()", existe la
función "create_autospec()" para crear directamente objetos simulados
autoespecificados:

>>> from urllib import request
>>> mock_request = create_autospec(request)
>>> mock_request.Request('foo', 'bar')
<NonCallableMagicMock name='mock.Request()' spec='Request' id='...'>

Sin embargo, este no es el comportamiento predeterminado, ya que no
está exento de advertencias y restricciones. Con el fin de conocer qué
atributos están disponibles en el objeto especificado, autospec tiene
que hacer uso de introspección sobre la especificación (acceder a los
atributos). A medida que recorres los atributos en el objeto simulado,
se produce paralelamente y de forma soterrada un recorrido del objeto
original. Si alguno de tus objetos especificados tienen propiedades o
descriptores que puedan desencadenar la ejecución de código, quizás no
deberías utilizar la autoespecificación. De todas formas, es siempre
mucho mejor diseñar tus objetos de modo que la introspección sea
segura [4].

A more serious problem is that it is common for instance attributes to
be created in the "__init__()" method and not to exist on the class at
all. *autospec* can't know about any dynamically created attributes
and restricts the api to visible attributes.

   >>> class Something:
   ...   def __init__(self):
   ...     self.a = 33
   ...
   >>> with patch('__main__.Something', autospec=True):
   ...   thing = Something()
   ...   thing.a
   ...
   Traceback (most recent call last):
     ...
   AttributeError: Mock object has no attribute 'a'

Hay diferentes formas de resolver este problema. La forma más
sencilla, pero no necesariamente la menos molesta, es simplemente
establecer los atributos necesarios en el objeto simulado después de
la creación del mismo. El hecho de que *autospec* no te permita buscar
atributos que no existen en la especificación no impide que los
establezcas manualmente después:

   >>> with patch('__main__.Something', autospec=True):
   ...   thing = Something()
   ...   thing.a = 33
   ...

Existe una versión más agresiva de *spec* y *autospec* que impide
establecer atributos inexistentes. Esto es útil si deseas asegurarte
de que tu código solo *establece* atributos válidos, pero obviamente
evitando este escenario en particular:

>>> with patch('__main__.Something', autospec=True, spec_set=True):
...   thing = Something()
...   thing.a = 33
...
Traceback (most recent call last):
 ...
AttributeError: Mock object has no attribute 'a'

Probably the best way of solving the problem is to add class
attributes as default values for instance members initialised in
"__init__()". Note that if you are only setting default attributes in
"__init__()" then providing them via class attributes (shared between
instances of course) is faster too. e.g.

   class Something:
       a = 33

Esto nos plantea otro problema. Es relativamente común proporcionar un
valor predeterminado de "None" para los miembros que posteriormente se
convertirán en objetos de un tipo diferente. "None" es inútil como
especificación dado que no permite acceder a *ningún* atributo o
método. Como "None" *nunca* será útil como especificación, y
probablemente indica un miembro que normalmente será de algún otro
tipo en el futuro, la autoespecificación no usa una especificación
para aquellos miembros configurados con "None" como valor. Estos serán
simplemente objetos simulados ordinarios (MagicMocks en realidad):

>>> class Something:
...     member = None
...
>>> mock = create_autospec(Something)
>>> mock.member.foo.bar.baz()
<MagicMock name='mock.member.foo.bar.baz()' id='...'>

Si modificar tus clases en producción para agregar valores
predeterminados no es de tu agrado, dispones de otras opciones. Una de
ellas es simplemente usar una instancia como especificación en lugar
de la clase. La otra es crear una subclase de la clase en producción y
agregar los valores predeterminados a la subclase, sin afectar a la
clase en producción. Ambas alternativas requieren que uses un objeto
alternativo como especificación. Afortunadamente "patch()" admite
esto, simplemente tienes que pasar el objeto alternativo mediante el
argumento *autospec*:

   >>> class Something:
   ...   def __init__(self):
   ...     self.a = 33
   ...
   >>> class SomethingForTest(Something):
   ...   a = 33
   ...
   >>> p = patch('__main__.Something', autospec=SomethingForTest)
   >>> mock = p.start()
   >>> mock.a
   <NonCallableMagicMock name='Something.a' spec='int' id='...'>

[4] Esto solo se aplica a las clases u objetos ya instanciados. Llamar
    a una clase simulada para crear una instancia simulada *no* crea
    una instancia real. Solo se llevan a cabo las búsqueda de
    atributos (mediante llamadas a "dir()").

### Sellar objetos simulados

unittest.mock.seal(mock)

   Seal desactivará la creación automática de objetos simulados al
   acceder a un atributo del objeto simulado que está siendo sellado,
   o a cualquiera de sus atributos que ya sean objetos simulados de
   forma recursiva.

   Si una instancia simulada con un nombre o una especificación es
   asignada a un atributo no será considerada en la cadena de sellado.
   Esto permite evitar que seal fije partes del objeto simulado.

      >>> mock = Mock()
      >>> mock.submock.attribute1 = 2
      >>> mock.not_submock = mock.Mock(name="sample_name")
      >>> seal(mock)
      >>> mock.new_attribute  # This will raise AttributeError.
      >>> mock.submock.attribute2  # This will raise AttributeError.
      >>> mock.not_submock.attribute2  # This won't raise.

   Added in version 3.7.

## Order of precedence of "side_effect", "return_value" and *wraps*

The order of their precedence is:

1. "side_effect"

2. "return_value"

3. *wraps*

If all three are set, mock will return the value from "side_effect",
ignoring "return_value" and the wrapped object altogether. If any two
are set, the one with the higher precedence will return the value.
Regardless of the order of which was set first, the order of
precedence remains unchanged.

>>> from unittest.mock import Mock
>>> class Order:
...     @staticmethod
...     def get_value():
...         return "third"
...
>>> order_mock = Mock(spec=Order, wraps=Order)
>>> order_mock.get_value.side_effect = ["first"]
>>> order_mock.get_value.return_value = "second"
>>> order_mock.get_value()
'first'

As "None" is the default value of "side_effect", if you reassign its
value back to "None", the order of precedence will be checked between
"return_value" and the wrapped object, ignoring "side_effect".

>>> order_mock.get_value.side_effect = None
>>> order_mock.get_value()
'second'

If the value being returned by "side_effect" is "DEFAULT", it is
ignored and the order of precedence moves to the successor to obtain
the value to return.

>>> from unittest.mock import DEFAULT
>>> order_mock.get_value.side_effect = [DEFAULT]
>>> order_mock.get_value()
'second'

When "Mock" wraps an object, the default value of "return_value" will
be "DEFAULT".

>>> order_mock = Mock(spec=Order, wraps=Order)
>>> order_mock.return_value
sentinel.DEFAULT
>>> order_mock.get_value.return_value
sentinel.DEFAULT

The order of precedence will ignore this value and it will move to the
last successor which is the wrapped object.

As the real call is being made to the wrapped object, creating an
instance of this mock will return the real instance of the class. The
positional arguments, if any, required by the wrapped object must be
passed.

>>> order_mock_instance = order_mock()
>>> isinstance(order_mock_instance, Order)
True
>>> order_mock_instance.get_value()
'third'

>>> order_mock.get_value.return_value = DEFAULT
>>> order_mock.get_value()
'third'

>>> order_mock.get_value.return_value = "second"
>>> order_mock.get_value()
'second'

But if you assign "None" to it, this will not be ignored as it is an
explicit assignment. So, the order of precedence will not move to the
wrapped object.

>>> order_mock.get_value.return_value = None
>>> order_mock.get_value() is None
True

Even if you set all three at once when initializing the mock, the
order of precedence remains the same:

>>> order_mock = Mock(spec=Order, wraps=Order,
...                   **{"get_value.side_effect": ["first"],
...                      "get_value.return_value": "second"}
...                   )
...
>>> order_mock.get_value()
'first'
>>> order_mock.get_value.side_effect = None
>>> order_mock.get_value()
'second'
>>> order_mock.get_value.return_value = DEFAULT
>>> order_mock.get_value()
'third'

If "side_effect" is exhausted, the order of precedence will not cause
a value to be obtained from the successors. Instead, "StopIteration"
exception is raised.

>>> order_mock = Mock(spec=Order, wraps=Order)
>>> order_mock.get_value.side_effect = ["first side effect value",
...                                     "another side effect value"]
>>> order_mock.get_value.return_value = "second"

>>> order_mock.get_value()
'first side effect value'
>>> order_mock.get_value()
'another side effect value'

>>> order_mock.get_value()
Traceback (most recent call last):
 ...
StopIteration
