---
title: Preguntas frecuentes de programación
source_url: https://docs.python.org/es/3
source_path: faq/programming.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: faq
order: 1110
---

# Preguntas frecuentes de programación

## General questions

### Is there a source code-level debugger with breakpoints and single-stepping?

Sí.

Debajo se describen algunos depuradores para Python y la función
integrada "breakpoint()" te permite ejecutar alguno de ellos.

El módulo pdb es en depurador en modo consola simple pero conveniente
para Python. Es parte de la biblioteca estándar de Python y está
"documentado en el manual de referencia de la biblioteca". Puedes
escribir tu propio depurador usando el código de pdb como ejemplo.

The IDLE interactive development environment, which is part of the
standard Python distribution (normally available as "idlelib"),
includes a graphical debugger.

PythonWin es un IDE Python que incluye un depurador con GUI basado en
pdb. El depurador PythonWin colorea los puntos de interrupción y
dispone de características geniales como la depuración de programas no
modificados mediante PythonWin. PythonWin está disponible como parte
del proyecto Las extensiones de Python para Windows y como parte de la
distribución ActivePython.

Eric is an IDE built on PyQt and the Scintilla editing component.

trepan3k es un depurador similar a *gdb*.

Visual Studio Code es un IDE con herramientas de depuración que se
integra con software de control de versiones.

Existen varios IDEs comerciales para Python que incluyen depuradores
gráficos. Entre ellos tenemos:

* IDE Wing

* PyCharm

### ¿Existe alguna herramienta que ayude a encontrar errores o realizar análisis estático?

Sí.

Ruff, Pylint and Pyflakes do basic checking that will help you catch
bugs sooner.

Static type checkers such as mypy, ty, Pyrefly, and pytype can check
type hints in Python source code.

### ¿Cómo puedo crear un binario independiente a partir de un programa Python?

No necesitas tener la habilidad de compilar Python a código C si lo
único que necesitas es un programa independiente que los usuarios
puedan descargar y ejecutar sin necesidad de instalar primero una
distribución Python. Existe una serie de herramientas que determinan
el conjunto de módulos que necesita un programa y une estos módulos
conjuntamente con un binario Python para generar un único ejecutable.

One is to use the freeze tool, which is included in the Python source
tree as Tools/freeze. It converts Python byte code to C arrays; with a
C compiler you can embed all your modules into a new program, which is
then linked with the standard Python modules.

Funciona escaneando su fuente de forma recursiva en busca de
declaraciones de importación (en ambas formas) y buscando los módulos
en la ruta estándar de Python, así como en el directorio de la fuente
(para los módulos incorporados).  Luego convierte el *bytecode* de los
módulos escritos en Python en código C (inicializadores de arrays que
pueden ser convertidos en objetos de código usando el módulo marshal)
y crea un archivo de configuración a medida que sólo contiene aquellos
módulos incorporados que se usan realmente en el programa.  A
continuación, compila el código C generado y lo enlaza con el resto
del intérprete de Python para formar un binario autónomo que actúa
exactamente igual que su script.

Los siguientes paquetes pueden ayudar con la creación de ejecutables
de consola y GUI:

* Nuitka (Multiplataforma)

* PyInstaller (Cross-platform)

* PyOxidizer (Multiplataforma)

* cx_Freeze (Multiplataforma)

* py2app (macOS solamente)

* py2exe (Windows only)

### ¿Existen estándares de código o una guía de estilo para programas Python?

Sí. El estilo de código requerido para los módulos de la biblioteca
estándar se encuentra documentado como **PEP 8**.

## Core language

### ¿Por qué obtengo un *UnboundLocalError* cuando la variable tiene un valor?

It can be a surprise to get the "UnboundLocalError" in previously
working code when it is modified by adding an assignment statement
somewhere in the body of a function.

Este código:

>>> x = 10
>>> def bar():
...     print(x)
...
>>> bar()
10

funciona, pero este código:

>>> x = 10
>>> def foo():
...     print(x)
...     x += 1

results in an "UnboundLocalError":

>>> foo()
Traceback (most recent call last):
  ...
UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

Esto es debido a que cuando realizas una asignación a una variable en
un  ámbito de aplicación, esa variable se convierte en local y
enmascara cualquier variable llamada de forma similar en un ámbito de
aplicación exterior. Desde la última declaración en foo asigna un
nuevo valor a "x", el compilador la reconoce como una variable local.
Consecuentemente, cuando el "print(x)" más próximo intenta mostrar la
variable local no inicializada se muestra un error.

En el ejemplo anterior puedes acceder al ámbito de aplicación exterior
a la variable declarándola como global:

>>> x = 10
>>> def foobar():
...     global x
...     print(x)
...     x += 1
...
>>> foobar()
10

Esta declaración explícita es necesaria de cara a recordarte que (a
diferencia de la situación superficialmente análoga con las variables
de clase e instancia) estás modificando el valor de la variable en un
ámbito de aplicación más externo:

>>> print(x)
11

Puedes hacer algo similar en un ámbito de aplicación anidado usando la
palabra clave "nonlocal":

>>> def foo():
...    x = 10
...    def bar():
...        nonlocal x
...        print(x)
...        x += 1
...    bar()
...    print(x)
...
>>> foo()
10
11

### ¿Cuáles son las reglas para las variables locales y globales en Python?

En Python, las variables que solo se encuentran referenciadas dentro
de una función son globales implícitamente.  Si a una variable se le
asigna un valor en cualquier lugar dentro del cuerpo de una función,
se asumirá que es local a no ser que explícitamente se la declare como
global.

Aunque, inicialmente, puede parecer sorprendente, un momento de
consideración permite explicar esto.  Por una parte, requerir "global"
para variables asignadas proporciona una barrera frente a efectos
secundarios indeseados.  Por otra parte, si "global" es requerido para
todas las referencias globales, deberás usar "global" en todo momento.
Deberías declarar como global cualquier referencia a una función
integrada o a un componente de un módulo importado. Este embrollo
arruinaría la utilidad de la declaración "global" para identificar los
efectos secundarios.

### ¿Por qué las funciones lambda definidas en un bucle con diferentes valores devuelven todas el mismo resultado?

Assume you use a for loop to define a few different lambdas (or even
plain functions), for example:

   >>> squares = []
   >>> for x in range(5):
   ...     squares.append(lambda: x**2)

Lo siguiente proporciona una lista que contiene 5 funciones lambda que
calculan "x**2". Esperarías que, cuando se les invoca, retornaran,
respectivamente, "0", "1", "4", "9" y "16". Sin embargo, cuando lo
ejecutes verás que todas devuelven "16":

   >>> squares[2]()
   16
   >>> squares[4]()
   16

This happens because "x" is not local to the lambdas, but is defined
in the outer scope, and it is accessed when the lambda is called ---
not when it is defined.  At the end of the loop, the value of "x" is
"4", so all the functions now return "4**2", that is "16".  You can
also verify this by changing the value of "x" and see how the results
of the lambdas change:

   >>> x = 8
   >>> squares[2]()
   64

De cara a evitar esto necesitas guardar los valores en variables
locales a las funciones lambda de tal forma que no dependan del valor
de la  "x" global:

   >>> squares = []
   >>> for x in range(5):
   ...     squares.append(lambda n=x: n**2)

Aquí, "n=x" crea una nueva variable "n" local a la función lambda y
ejecutada cuando la función lambda se define de tal forma que tiene el
mismo valor que tenía "x" en ese punto en el bucle.  Esto significa
que el valor de "n" será "0" en la primera función lambda, "1" en la
segunda, "2" en la tercera y así sucesivamente. Por tanto, ahora cada
lambda retornará el resultado correcto:

   >>> squares[2]()
   4
   >>> squares[4]()
   16

Es de destacar que este comportamiento no es peculiar de las funciones
lambda sino que aplica también a las funciones regulares.

### ¿Cómo puedo compartir variables globales entre módulos?

La forma canónica de compartir información entre módulos dentro de un
mismo programa sería creando un módulo especial (a menudo llamado
config o cfg).  Simplemente importa el módulo config  en todos los
módulos de tu aplicación; el módulo estará disponible como un nombre
global.  Debido a que solo hay una instancia de cada módulo, cualquier
cambio hecho en el objeto módulo se reflejará en todos los sitios.
Por ejemplo:

config.py:

   x = 0   # Default value of the 'x' configuration setting

mod.py:

   import config
   config.x = 1

main.py:

   import config
   import mod
   print(config.x)

Note that using a module is also the basis for implementing the
singleton design pattern, for the same reason.

### ¿Cuáles son las "buenas prácticas" para usar import en un módulo?

En general, no uses "from modulename import *".  Haciendo eso
embarulla el espacio de nombres del importador y hace que sea más
difícil para los *linters* el detectar los nombres sin definir.

Importar los módulos en la parte inicial del fichero. Haciéndolo así
deja claro los módulos que son necesarios para tu código y evita
preguntas sobre si el nombre del módulo se encuentra en el ámbito de
la aplicación. Usar una importación por línea hace que sea sencillo
añadir y eliminar módulos importados pero usar múltiples importaciones
por línea usa menos espacio de pantalla.

Es una buena práctica si importas los módulos en el orden siguiente:

1. standard library modules -- such as "sys", "os", "argparse", "re"

2. third-party library modules (anything installed in Python's site-
   packages directory) -- such as dateutil, requests, tzdata

3. locally developed modules

Hay veces en que es necesario mover las importaciones a una función o
clase para evitar problemas de importaciones circulares.  Gordon
McMillan dice:

   No hay problema con las importaciones circulares cuando ambos
   módulos usan la forma de importación "import <module>".  Fallará
   cuando el segundo módulo quiera coger un nombre del primer módulo
   ("from module import name") y la importación se encuentre en el
   nivel superior.  Esto sucede porque los nombres en el primero
   todavía no se encuentran disponibles debido a que el primer módulo
   se encuentra ocupado importando al segundo.

En este caso, si el segundo módulo se usa solamente desde una función,
la importación se puede mover de forma sencilla dentro de la función.
En el momento en que se invoca a la importación el primer módulo habrá
terminado de inicializarse y el segundo módulo podrá hacer la
importación.

También podría ser necesario mover importaciones fuera del nivel
superior del código si alguno de loa módulos son específicos a la
plataforma. En ese caso podría, incluso, no ser posible importar todos
los módulos en la parte superior del fichero. Para esos casos, la
importación correcta de los módulos en el código correspondiente
específico de la plataforma es una buena opción.

Solo debes mover importaciones a un ámbito de aplicación local, como
dentro de la definición de una función, si es necesario resolver
problemas como una importación circular o al intentar reducir el
tiempo de inicialización de un módulo. Esta técnica es especialmente
útil si muchas de las importaciones no son necesarias dependiendo de
cómo se ejecute el programa. También podrías mover importaciones a una
función si los módulos solo se usan dentro de esa función. Nótese que
la primera carga de un módulo puede ser costosa debido al tiempo
necesario para la inicialización del módulo,pero la carga de un módulo
múltiples veces está prácticamente libre de coste ya que solo es
necesario hacer búsquedas en un diccionario. Incluso si el nombre del
módulo ha salido del ámbito de aplicación el módulo se encuentre,
probablemente, en "sys.modules".

### ¿Por qué los valores por defecto se comparten entre objetos?

Este tipo de error golpea a menudo a programadores novatos. Considera
esta función:

   def foo(mydict={}):  # Danger: shared reference to one dict for all calls
       ... compute something ...
       mydict[key] = value
       return mydict

La primera vez que llamas a esta función, "mydict" solamente contiene
un único elemento. La segunda vez, "mydict" contiene dos elementos
debido a que cuando comienza la ejecución de "foo()", "mydict"
comienza conteniendo un elemento de partida.

A menudo se esperaría que una invocación a una función cree nuevos
objetos para valores por defecto. Eso no es lo que realmente sucede.
Los valores por defecto se crean exactamente una sola vez, cuando se
define la función. Se se cambia el objeto, como el diccionario en este
ejemplo, posteriores invocaciones a la función estarán referidas al
objeto cambiado.

Por definición, los objetos inmutables como números, cadenas, tuplas y
"None" están asegurados frente al cambio. Cambios en objetos mutables
como diccionarios, listas e instancias de clase pueden llevar a
confusión.

Debido a esta característica es una buena práctica de programación el
no usar valores mutables como valores por defecto. En su lugar usa
"None" como valor por defecto dentro de la función, comprueba si el
parámetro es "None" y crea una nueva lista/un nuevo
diccionario/cualquier otras cosa que necesites.  Por ejemplo, no
escribas:

   def foo(mydict={}):
       ...

pero:

   def foo(mydict=None):
       if mydict is None:
           mydict = {}  # create a new dict for local namespace

Esta característica puede ser útil. Cuando tienes una función que es
muy costosa de ejecutar, una técnica común es *cachear* sus parámetros
y el valor resultante de cada invocación a la función y retornar el
valor *cacheado* si se solicita nuevamente el mismo valor.  A esto se
le llama "memoizing" y se puede implementar de la siguiente forma:

   # Callers can only provide two parameters and optionally pass _cache by keyword
   def expensive(arg1, arg2, *, _cache={}):
       if (arg1, arg2) in _cache:
           return _cache[(arg1, arg2)]

       # Calculate the value
       result = ... expensive computation ...
       _cache[(arg1, arg2)] = result           # Store result in the cache
       return result

Podrías usar una variable global conteniendo un diccionario en lugar
de un valor por defecto; es una cuestión de gustos.

### ¿Cómo puedo pasar parámetros por palabra clave u opcionales de una función a otra?

Recopila los argumentos usando los especificadores "*" y "**" en la
lista de parámetros de la función; esto te proporciona los argumentos
posicionales como una tupla y los argumentos con palabras clave como
un diccionario.  Puedes, entonces, pasar estos argumentos cuando
invoques a otra función usando "*" y "**":

   def f(x, *args, **kwargs):
       ...
       kwargs['width'] = '14.3c'
       ...
       g(x, *args, **kwargs)

### ¿Cuál es la diferencia entre argumentos y parámetros?

*Parameters* are defined by the names that appear in a function
definition, whereas *arguments* are the values actually passed to a
function when calling it.  Parameters define what *kind of arguments*
a function can accept.  For example, given the function definition:

   def func(foo, bar=None, **kwargs):
       pass

*foo*, *bar* y *kwargs* son parámetros de "func".  Sin embargo, cuando
invocamos a "func", por ejemplo:

   func(42, bar=314, extra=somevar)

los valores "42", "314" y "somevar" son argumentos.

### ¿Por qué cambiando la lista 'y' cambia, también, la lista 'x'?

Si escribes código como:

   >>> x = []
   >>> y = x
   >>> y.append(10)
   >>> y
   [10]
   >>> x
   [10]

te estarás preguntando porque añadir un elemento a "y" ha cambiado
también a "x".

Hay dos factores que provocan este resultado:

1. Las variables son simplemente nombres que referencian a objetos.
   Haciendo "y = x" no crea una copia de la lista -- crea una nueva
   variable "y" que referencia al mismo objeto al que referencia "x" .
   Esto significa que solo existe un objeto (la lista) y tanto "x"
   como "y" hacen referencia al mismo.

2. Las listas son *mutable*, lo que significa que puedes cambiar su
   contenido.

After the call to "append()", the content of the mutable object has
changed from "[]" to "[10]".  Since both the variables refer to the
same object, using either name accesses the modified value "[10]".

Si, por otra parte, asignamos un objeto inmutable a "x":

   >>> x = 5  # ints are immutable
   >>> y = x
   >>> x = x + 1  # 5 can't be mutated, we are creating a new object here
   >>> x
   6
   >>> y
   5

podemos ver que "x" e "y" ya no son iguales.  Esto es debido a que los
enteros son *immutable*, y cuando hacemos "x = x + 1" no estamos
mutando el entero "5" incrementando su valor; en su lugar, estamos
creando un nuevo objeto (el entero "6") y se lo asignamos a "x" (esto
es, cambiando el objeto al cual referencia "x").  Después de esta
asignación tenemos dos objetos (los enteros "6" y "5") y dos variables
que referencian a ellos ("x" ahora referencia a  "6" pero "y" todavía
referencia a "5").

Some operations (for example "y.append(10)" and "y.sort()") mutate the
object, whereas superficially similar operations (for example "y = y +
[10]" and "sorted(y)") create a new object.  In general in Python (and
in all cases in the standard library) a method that mutates an object
will return "None" to help avoid getting the two types of operations
confused.  So if you mistakenly write "y.sort()" thinking it will give
you a sorted copy of "y", you'll instead end up with "None", which
will likely cause your program to generate an easily diagnosed error.

Sin embargo, existe una clase de operaciones en las cuales la misma
operación tiene, a veces, distintos comportamientos con diferentes
tipos:  los operadores de asignación aumentada.  Por ejemplo, "+="
muta listas pero no tuplas o enteros ("a_list += [1, 2, 3]" es
equivalente a "a_list.extend([1, 2, 3])" y muta "a_list", mientras que
"some_tuple += (1, 2, 3)" y "some_int += 1" crea nuevos objetos).

En otras palabras:

* If we have a mutable object (such as "list", "dict", "set"), we can
  use some specific operations to mutate it and all the variables that
  refer to it will see the change.

* If we have an immutable object (such as "str", "int", "tuple"), all
  the variables that refer to it will always see the same value, but
  operations that transform that value into a new value always return
  a new object.

Si deseas saber si dos variables referencian o no al mismo objeto
puedes usar el operador "is" o la función incorporada "id()".

### ¿Cómo puedo escribir una función sin parámetros (invocación mediante referencia)?

Remember that arguments are passed by assignment in Python.  Since
assignment just creates references to objects, there's no alias
between an argument name in the caller and callee, and consequently no
call-by-reference.  You can achieve the desired effect in a number of
ways.

1. Mediante el retorno de una tupla de resultados:

      >>> def func1(a, b):
      ...     a = 'new-value'        # a and b are local names
      ...     b = b + 1              # assigned to new objects
      ...     return a, b            # return new values
      ...
      >>> x, y = 'old-value', 99
      >>> func1(x, y)
      ('new-value', 100)

   Esta es, casi siempre, la solución más clara.

2. Mediante el uso de variables globales.  No es thread-safe y no se
   recomienda.

3. Pasando un objeto mutable (intercambiable en el mismo sitio):

      >>> def func2(a):
      ...     a[0] = 'new-value'     # 'a' references a mutable list
      ...     a[1] = a[1] + 1        # changes a shared object
      ...
      >>> args = ['old-value', 99]
      >>> func2(args)
      >>> args
      ['new-value', 100]

4. Pasando un diccionario que muta:

      >>> def func3(args):
      ...     args['a'] = 'new-value'     # args is a mutable dictionary
      ...     args['b'] = args['b'] + 1   # change it in-place
      ...
      >>> args = {'a': 'old-value', 'b': 99}
      >>> func3(args)
      >>> args
      {'a': 'new-value', 'b': 100}

5. O empaquetar valores en una instancia de clase:

      >>> class Namespace:
      ...     def __init__(self, /, **args):
      ...         for key, value in args.items():
      ...             setattr(self, key, value)
      ...
      >>> def func4(args):
      ...     args.a = 'new-value'        # args is a mutable Namespace
      ...     args.b = args.b + 1         # change object in-place
      ...
      >>> args = Namespace(a='old-value', b=99)
      >>> func4(args)
      >>> vars(args)
      {'a': 'new-value', 'b': 100}

   Casi nunca existe una buena razón para hacer esto tan complicado.

Tu mejor opción es retornar una tupla que contenga los múltiples
resultados.

### ¿Cómo se puede hacer una función de orden superior en Python?

Tienes dos opciones: puedes usar ámbitos de aplicación anidados o
puedes usar objetos invocables. Por ejemplo, supón que querías definir
"linear(a,b)" que devuelve una función "f(x)" que calcula el valor
"a*x+b".  Usar ámbitos de aplicación anidados:

   def linear(a, b):
       def result(x):
           return a * x + b
       return result

O usar un objeto invocable:

   class linear:

       def __init__(self, a, b):
           self.a, self.b = a, b

       def __call__(self, x):
           return self.a * x + self.b

En ambos casos,

   taxes = linear(0.3, 2)

nos da un objeto invocable donde "taxes(10e6) == 0.3 * 10e6 + 2".

El enfoque del objeto invocable tiene la desventaja que es un
ligeramente más lento y el resultado es un código levemente más largo.
Sin embargo, destacar que una colección de invocables pueden compartir
su firma vía herencia:

   class exponential(linear):
       # __init__ inherited
       def __call__(self, x):
           return self.a * (x ** self.b)

Los objetos pueden encapsular el estado de varios métodos:

   class counter:

       value = 0

       def set(self, x):
           self.value = x

       def up(self):
           self.value = self.value + 1

       def down(self):
           self.value = self.value - 1

   count = counter()
   inc, dec, reset = count.up, count.down, count.set

Aquí "inc()", "dec()" y "reset()" se comportan como funciones las
cuales comparten la misma variable de conteo.

### ¿Cómo copio un objeto en Python?

En general, prueba "copy.copy()" o "copy.deepcopy()" para el caso
general. No todos los objetos se pueden copiar pero la mayoría sí que
pueden copiarse.

Algunas objetos se pueden copiar de forma más sencilla. Los
diccionarios disponen de un método "copy()":

   newdict = olddict.copy()

Las secuencias se pueden copiar usando un rebanado:

   new_l = l[:]

### ¿Cómo puedo encontrar los métodos o atributos de un objeto?

For an instance "x" of a user-defined class, "dir(x)" returns an
alphabetized list of the names containing the instance attributes and
methods and attributes defined by its class.

### ¿Cómo puede mi código descubrir el nombre de un objeto?

Hablando de forma general no podrían puesto que los objetos no
disponen, realmente, de un nombre. Esencialmente, las asignaciones
relacionan un nombre con su valor; Lo mismo se cumple con las
declaraciones "def" y "class" pero, en este caso, el valor es un
invocable. Considera el siguiente código:

   >>> class A:
   ...     pass
   ...
   >>> B = A
   >>> a = B()
   >>> b = a
   >>> print(b)
   <__main__.A object at 0x16D07CC>
   >>> print(a)
   <__main__.A object at 0x16D07CC>

Arguably the class has a name: even though it is bound to two names
and invoked through the name "B" the created instance is still
reported as an instance of class "A".  However, it is impossible to
say whether the instance's name is "a" or "b", since both names are
bound to the same value.

En términos generales, no debería ser necesario que tu código "conozca
los nombres" de determinados valores. A menos que estés escribiendo
deliberadamente programas introspectivos, esto suele ser una
indicación de que un cambio de enfoque podría ser beneficioso.

En comp.lang.python, Fredrik Lundh proporcionó una vez una excelente
analogía en respuesta a esta pregunta:

   De la misma forma que obtienes el nombre de ese gato que te has
   encontrado en tu porche el propio gato (objeto) no te puede indicar
   su nombre y, realmente, no importa -- por tanto, la única forma de
   encontrar cómo se llama sería preguntando a todos los vecinos
   (espacios de nombres) si es su gato (objeto)...

   ...y no te sorprendas si encuentras que se le conoce mediante
   diferentes nombres o ¡nadie conoce su nombre!

### ¿Qué ocurre con la precedencia del operador coma?

La coma no es un operador en Python. Considera la sesión:

   >>> "a" in "b", "a"
   (False, 'a')

Debido a que la coma no es un operador sino un  separador entre
expresiones lo anterior se evalúe como se ha introducido:

   ("a" in "b"), "a"

no:

   "a" in ("b", "a")

The same is true of the various assignment operators ("=", "+=", and
so on). They are not truly operators but syntactic delimiters in
assignment statements.

### ¿Existe un equivalente al operador ternario de C "?:"?

Sí, existe. La sintaxis es como sigue:

   [on_true] if [expression] else [on_false]

   x, y = 50, 25
   small = x if x < y else y

Antes de que esta sintaxis se introdujera en Python 2.5 una expresión
común fue el uso de operadores lógicos:

   [expression] and [on_true] or [on_false]

Sin embargo, esa expresión no es segura ya que puede retornar valores
erróneos cuando *on_true* tiene un valor booleano falso.  Por tanto,
siempre es mejor usar la forma "... if ... else ...".

### ¿Es posible escribir expresiones en una línea de forma ofuscada en Python?

Yes.  Usually this is done by nesting "lambda" within "lambda".  See
the following three examples, slightly adapted from Ulf Bartelt:

   from functools import reduce

   # Primes < 1000
   print(list(filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0,
   map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(2,1000)))))

   # First 10 Fibonacci numbers
   print(list(map(lambda x,f=lambda x,f:(f(x-1,f)+f(x-2,f)) if x>1 else 1:
   f(x,f), range(10))))

   # Mandelbrot set
   print((lambda Ru,Ro,Iu,Io,IM,Sx,Sy:reduce(lambda x,y:x+'\n'+y,map(lambda y,
   Iu=Iu,Io=Io,Ru=Ru,Ro=Ro,Sy=Sy,L=lambda yc,Iu=Iu,Io=Io,Ru=Ru,Ro=Ro,i=IM,
   Sx=Sx,Sy=Sy:reduce(lambda x,y:x+y,map(lambda x,xc=Ru,yc=yc,Ru=Ru,Ro=Ro,
   i=i,Sx=Sx,F=lambda xc,yc,x,y,k,f=lambda xc,yc,x,y,k,f:(k<=0)or (x*x+y*y
   >=4.0) or 1+f(xc,yc,x*x-y*y+xc,2.0*x*y+yc,k-1,f):f(xc,yc,x,y,k,f):chr(
   64+F(Ru+x*(Ro-Ru)/Sx,yc,0,0,i)),range(Sx))):L(Iu+y*(Io-Iu)/Sy),range(Sy
   ))))(-2.1, 0.7, -1.2, 1.2, 30, 80, 24))
   #    \___ ___/  \___ ___/  |   |   |__ lines on screen
   #        V          V      |   |______ columns on screen
   #        |          |      |__________ maximum of "iterations"
   #        |          |_________________ range on y axis
   #        |____________________________ range on x axis

¡No probéis esto en casa, personitas!

### ¿Qué hace la barra (/) en medio de la lista de parámetros de una función?

A slash in the argument list of a function denotes that the parameters
prior to it are positional-only.  Positional-only parameters are the
ones without an externally usable name.  Upon calling a function that
accepts positional-only parameters, arguments are mapped to parameters
based solely on their position. For example, "divmod()" is a function
that accepts positional-only parameters. Its documentation looks like
this:

   >>> help(divmod)
   Help on built-in function divmod in module builtins:

   divmod(x, y, /)
       Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.

El *slash* al final de la lista de parámetros indica que los tres
parámetros son únicamente posicionales. Por tanto, invocar a  "pow()"
con argumentos con palabra clave podría derivar en un error:

   >>> divmod(x=3, y=4)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: divmod() takes no keyword arguments

## Números y cadenas

### ¿Cómo puedo especificar enteros hexadecimales y octales?

Para especificar un dígito octal, prefija el valor octal con un cero y
una "o" en minúscula o mayúscula.  Por ejemplo, para definir la
variable "a" con el valor octal "10" (8 en decimal), escribe:

   >>> a = 0o10
   >>> a
   8

Un hexadecimal es igual de simple.  Simplemente añade un cero y una
"x", en minúscula o mayúscula, antes del número hexadecimal . Los
dígitos hexadecimales se pueden especificar en minúsculas o
mayúsculas.  Por ejemplo, en el intérprete de Python:

   >>> a = 0xa5
   >>> a
   165
   >>> b = 0XB2
   >>> b
   178

### ¿Por qué -22 // 10 devuelve -3?

Es debido, principalmente al deseo que "i % j" tenga el mismo signo
que "j". Si quieres eso y, además, quieres:

   i == (i // j) * j + (i % j)

entonces la división entera a la baja debe retornar el valor base más
bajo. C también requiere que esa identidad se mantenga de tal forma
que cuando los compiladores truncan "i // j" necesitan que "i % j"
tenga el mismo signo que "i".

Existen unos pocos casos para "i % j" cuando "j" es negativo.  Cuando
"j" es positivo, existen muchos casos y, virtualmente, en todos ellos
es más útil para "i % j" que sea ">= 0".  Si el reloj dice que ahora
son las 10, ¿qué dijo hace 200 horas?  "-190 % 12 == 2" es útil; "-190
% 12 == -10" es un error listo para morderte.

### ¿Cómo puedo obtener un atributo int literal en lugar de SyntaxError?

Trying to lookup an "int" literal attribute in the normal manner gives
a "SyntaxError" because the period is seen as a decimal point:

   >>> 1.__class__
     File "<stdin>", line 1
     1.__class__
      ^
   SyntaxError: invalid decimal literal

La solución es separar el literal del punto con un espacio o un
paréntesis.

>>> 1 .__class__
<class 'int'>
>>> (1).__class__
<class 'int'>

### ¿Cómo convierto una cadena a un número?

For integers, use the built-in "int()" type constructor, for example,
"int('144') == 144".  Similarly, "float()" converts to a floating-
point number, for example, "float('144') == 144.0".

Por defecto, estas interpretan el número como decimal de tal forma que
"int('0144') == 144" y "int('0x144')" lanzará "ValueError".
"int(string, base)" toma la base para convertirlo desde un segundo
parámetro opcional, por tanto "int('0x144', 16) == 324". Si la base se
especifica como 0, el número se interpreta usando las reglas de
Python's rules: un prefijo '0o' indica octal y un prefijo '0x' indica
un número hexadecimal.

No uses la función incorporada "eval()" si todo lo que necesitas es
convertir cadenas a números.  "eval()" será considerablemente más
lento y presenta riesgos de seguridad: cualquiera podría introducir
una expresión Python que presentara efectos indeseados.  Por ejemplo,
alguien podría pasar "__import__('os').system("rm -rf $HOME")" lo cual
borraría el directorio home al completo.

"eval()" also has the effect of interpreting numbers as Python
expressions, so that, for example, "eval('09')" gives a syntax error
because Python does not allow leading '0' in a decimal number (except
'0').

### ¿Cómo puedo convertir un número a una cadena?

For example, to convert the number "144" to the string "'144'", use
the built-in type constructor "str()".  If you want a hexadecimal or
octal representation, use the built-in functions "hex()" or "oct()".
For fancy formatting, see the f-strings and Format string syntax
sections. For example, ""{:04d}".format(144)" yields "'0144'" and
""{:.3f}".format(1.0/3.0)" yields "'0.333'".

### ¿Cómo puedo modificar una cadena in situ?

You can't, because strings are immutable.  In most situations, you
should simply construct a new string from the various parts you want
to assemble it from.  However, if you need an object with the ability
to modify in-place Unicode data, try using an "io.StringIO" object or
the "array" module:

   >>> import io
   >>> s = "Hello, world"
   >>> sio = io.StringIO(s)
   >>> sio.getvalue()
   'Hello, world'
   >>> sio.seek(7)
   7
   >>> sio.write("there!")
   6
   >>> sio.getvalue()
   'Hello, there!'

   >>> import array
   >>> a = array.array('w', s)
   >>> print(a)
   array('w', 'Hello, world')
   >>> a[0] = 'y'
   >>> print(a)
   array('w', 'yello, world')
   >>> a.tounicode()
   'yello, world'

### ¿Cómo puedo usar cadenas para invocar funciones/métodos?

Existen varias técnicas.

* Lo mejor sería usar un diccionario que mapee cadenas a funciones.
  La principal ventaja de esta técnica es que las cadenas no necesitan
  ser iguales que los nombres de las funciones.  Esta es también la
  principal técnica que se usa para emular un constructo *case*:

     def a():
         pass

     def b():
         pass

     dispatch = {'go': a, 'stop': b}  # Note lack of parens for funcs

     dispatch[get_input()]()  # Note trailing parens to call function

* Usa la función incorporada "getattr()":

     import foo
     getattr(foo, 'bar')()

  Nótese que "getattr()" funciona en cualquier objeto, incluido
  clases, instancias de clases, módulos, etc.

  Esto se usa en varios lugares de la biblioteca estándar, como esto:

     class Foo:
         def do_foo(self):
             ...

         def do_bar(self):
             ...

     f = getattr(foo_instance, 'do_' + opname)
     f()

* Use "locals()" para resolver el nombre de la función:

     def myFunc():
         print("hello")

     fname = "myFunc"

     f = locals()[fname]
     f()

### Is there an equivalent to Perl's "chomp()" for removing trailing newlines from strings?

Puedes usar "S.rstrip("\r\n")" para eliminar todas las ocurrencias de
cualquier terminación de línea desde el final de la cadena "S" sin
eliminar el resto de espacios en blanco que le siguen. Si la cadena
"S" representa más de una línea con varias líneas vacías al final, las
terminaciones de línea para todas las líneas vacías se eliminarán:

   >>> lines = ("line 1 \r\n"
   ...          "\r\n"
   ...          "\r\n")
   >>> lines.rstrip("\n\r")
   'line 1 '

Ya que esto solo sería deseable, típicamente, cuando lees texto línea
a línea, usar "S.rstrip()" de esta forma funcionaría bien.

### Is there a "scanf()" or "sscanf()" equivalent?

No de la misma forma.

For simple input parsing, the easiest approach is usually to split the
line into whitespace-delimited words using the "split()" method of
string objects and then convert decimal strings to numeric values
using "int()" or "float()".  "split()" supports an optional "sep"
parameter which is useful if the line uses something other than
whitespace as a separator.

For more complicated input parsing, regular expressions are more
powerful than C's "sscanf" and better suited for the task.

### What does "UnicodeDecodeError" or "UnicodeEncodeError" error mean?

Ver CÓMO (HOWTO) Unicode.

### Can I end a raw string with an odd number of backslashes?

A raw string ending with an odd number of backslashes will escape the
string's quote:

   >>> r'C:\this\will\not\work\'
     File "<stdin>", line 1
       r'C:\this\will\not\work\'
       ^
   SyntaxError: unterminated string literal (detected at line 1)

There are several workarounds for this. One is to use regular strings
and double the backslashes:

   >>> 'C:\\this\\will\\work\\'
   'C:\\this\\will\\work\\'

Another is to concatenate a regular string containing an escaped
backslash to the raw string:

   >>> r'C:\this\will\work' '\\'
   'C:\\this\\will\\work\\'

It is also possible to use "os.path.join()" to append a backslash on
Windows:

   >>> os.path.join(r'C:\this\will\work', '')
   'C:\\this\\will\\work\\'

Note that while a backslash will "escape" a quote for the purposes of
determining where the raw string ends, no escaping occurs when
interpreting the value of the raw string. That is, the backslash
remains present in the value of the raw string:

   >>> r'backslash\'preserved'
   "backslash\\'preserved"

Also see the specification in the language reference.

## Rendimiento

### Mi programa es muy lento. ¿Cómo puedo acelerarlo?

That's a tough one, in general.  First, here is a list of things to
remember before diving further:

* Las características del rendimiento varían entre las distintas
  implementaciones de Python.  Estas preguntas frecuentes se enfocan
  en *CPython*.

* El comportamiento puede variar entre distintos sistemas operativos,
  especialmente cuando se habla de tareas I/O o multi-tarea.

* Siempre deberías encontrar las partes importantes en tu programa
  *antes* de intentar optimizar el código (ver el módulo "profile").

* Escribir programas de comparación del rendimiento te permitirá
  iterar rápidamente cuando te encuentres buscando mejoras (ver el
  módulo "timeit").

* Es altamente recomendable disponer de una buena cobertura de código
  (a partir de pruebas unitarias o cualquier otra técnica) antes de
  introducir potenciales regresiones ocultas en sofisticadas
  optimizaciones.

Dicho lo anterior, existen muchos trucos para acelerar código Python.
Aquí tienes algunos principios generales que te permitirán llegar a
alcanzar niveles de rendimiento aceptables:

* El hacer más rápido tu algoritmo (o cambiarlo por alguno más rápido)
  puede provocar mayores beneficios que intentar unos pocos trucos de
  micro-optimización a través de todo tu código.

* Utiliza las estructuras de datos correctas.  Estudia la
  documentación para los Tipos integrados y el módulo "collections".

* Cuando la biblioteca estándar proporciona una primitiva de hacer
  algo, esta supuestamente será (aunque no se garantiza) más rápida
  que cualquier otra alternativa que se te ocurra.  Esto es doblemente
  cierto si las primitivas han sido escritas en C, como los *builtins*
  y algunos tipos extendidos.  Por ejemplo, asegúrate de usar el
  método integrado "list.sort()" o la función relacionada "sorted()"
  para ordenar (y ver Sorting Techniques para ver ejemplos de uso
  moderadamente avanzados).

* Las abstracciones tienden a crear rodeos y fuerzan al intérprete a
  trabajar más.  Si el nivel de rodeos sobrepasa el trabajo útil
  realizado tu programa podría ser más lento.  Deberías evitar
  abstracciones excesivas, especialmente, en forma de pequeñas
  funciones o métodos (que también va en detrimento de la
  legibilidad).

If you have reached the limit of what pure Python can allow, there are
tools to take you further away.  For example, Cython can compile a
slightly modified version of Python code into a C extension, and can
be used on many different platforms.  Cython can take advantage of
compilation (and optional type annotations) to make your code
significantly faster than when interpreted.  If you are confident in
your C programming skills, you can also write a C extension module
yourself.

Ver también: La página de la wiki dedicada a trucos de rendimiento.

### ¿Cuál es la forma más eficiente de concatenar muchas cadenas conjuntamente?

Los objetos "str" y "bytes" son inmutables, por tanto, concatenar
muchas cadenas en una sola es ineficiente debido a que cada
concatenación crea un nuevo objeto. En el caso más general, el coste
total en tiempo de ejecución es cuadrático en relación a la longitud
de la cadena final.

Para acumular muchos objetos "str", la forma recomendada sería
colocarlos en una lista y llamar al método "str.join()" al final:

   chunks = []
   for s in my_strings:
       chunks.append(s)
   result = ''.join(chunks)

(Another reasonably efficient idiom is to use "io.StringIO".)

Para acumular muchos objetos "bytes", la forma recomendada sería
extender un objeto "bytearray" usando el operador de concatenación
in situ (el operador "+="):

   result = bytearray()
   for b in my_bytes_objects:
       result += b

## Sequences (tuples/lists)

### ¿Cómo convertir entre tuplas y listas?

El constructor "tuple(seq)" convierte cualquier secuencia (en
realidad, cualquier iterable) en una tupla con los mismos elementos y
en el mismo orden.

Por ejemplo, "tuple([1, 2, 3])" lo convierte en "(1, 2, 3)" y
"tuple('abc')" lo convierte en "('a', 'b', 'c')".  Si el argumento es
una tupla no creará una nueva copia y retornará el mismo objeto, por
tanto, llamar a "tuple()" no tendrá mucho coste si no estás seguro si
un objeto ya es una tupla.

El constructor "list(seq)" convierte cualquier secuencia o iterable en
una lista con los mismos elementos y en el mismo orden.  Por ejemplo,
"list((1, 2, 3))" lo convierte a "[1, 2, 3]" y "list('abc')" lo
convierte a "['a', 'b', 'c']".  Si el argumento es una lista, hará una
copia como lo haría "seq[:]".

### ¿Qué es un índice negativo?

Las secuencias en Python están indexadas con números positivos y
negativos.  Para los números positivos el  0 será el primer índice, el
1 el segundo y así en adelante.  Para los índices negativos el -1 el
último índice, el -2 el penúltimo, etc.  Piensa en "seq[-n]" como si
fuera "seq[len(seq)-n]".

El uso de índices negativos puede ser muy conveniente.  Por ejemplo
"S[:-1]" se usa para todo la cadena excepto para su último carácter,
lo cual es útil para eliminar el salto de línea final de una cadena.

### ¿Cómo puedo iterar sobre una secuencia en orden inverso?

Usa la función incorporada "reversed()":

   for x in reversed(sequence):
       ...  # do something with x ...

Esto no transformará la secuencia original sino que creará una nueva
copia en orden inverso por la que se puede iterar.

### ¿Cómo eliminar duplicados de una lista?

Puedes echar un vistazo al recetario de Python para ver una gran
discusión mostrando muchas formas de hacer esto:

   https://code.activestate.com/recipes/52560/

Si no te preocupa que la lista se reordene la puedes ordenar y,
después, y después escanearla desde el final borrando duplicados a
medida que avanzas:

   if mylist:
       mylist.sort()
       last = mylist[-1]
       for i in range(len(mylist)-2, -1, -1):
           if last == mylist[i]:
               del mylist[i]
           else:
               last = mylist[i]

If all elements of the list may be used as set keys (that is, they are
all *hashable*) this is often faster:

   mylist = list(set(mylist))

Esto convierte la lista en un conjunto eliminando, por tanto, los
duplicados y, posteriormente, puedes volver a una lista.

### How do you remove multiple items from a list?

As with removing duplicates, explicitly iterating in reverse with a
delete condition is one possibility.  However, it is easier and faster
to use slice replacement with an implicit or explicit forward
iteration. Here are three variations:

   mylist[:] = filter(keep_function, mylist)
   mylist[:] = (x for x in mylist if keep_condition)
   mylist[:] = [x for x in mylist if keep_condition]

Esta comprensión de lista puede ser la más rápida.

### ¿Cómo se puede hacer un array en Python?

Usa una lista:

   ["this", 1, "is", "an", "array"]

Las listas son equivalentes en complejidad temporal a arrays en C o
Pascal; La principal diferencia es que una lista en Python puede
contener objetos de diferentes tipos.

The "array" module also provides methods for creating arrays of fixed
types with compact representations, but they are slower to index than
lists.  Also note that NumPy and other third-party packages define
array-like structures with various characteristics as well.

To get Lisp-style linked lists, you can emulate *cons cells* using
tuples:

   lisp_list = ("like",  ("this",  ("example", None) ) )

If mutability is desired, you could use lists instead of tuples.  Here
the analogue of a Lisp *car* is "lisp_list[0]" and the analogue of
*cdr* is "lisp_list[1]".  Only do this if you're sure you really need
to, because it's usually a lot slower than using Python lists.

### ¿Cómo puedo crear una lista multidimensional?

Seguramente hayas intentado crear un array multidimensional de la
siguiente forma:

   >>> A = [[None] * 2] * 3

Esto parece correcto si lo muestras en pantalla:

   >>> A
   [[None, None], [None, None], [None, None]]

Pero cuando asignas un valor, se muestra en múltiples sitios:

   >>> A[0][0] = 5
   >>> A
   [[5, None], [5, None], [5, None]]

La razón es que replicar una lista con "*" no crea copias, solo crea
referencias a los objetos existentes.  El "*3" crea una lista
conteniendo 3 referencias a la misma lista de longitud dos.  Cambios a
una fila se mostrarán en todas las filas, lo cual, seguramente, no es
lo que deseas.

El enfoque recomendado sería crear, primero, una lista de la longitud
deseada y, después, rellenar cada elemento con una lista creada en ese
momento:

   A = [None] * 3
   for i in range(3):
       A[i] = [None] * 2

Esto genera una lista conteniendo 3 listas distintas de longitud dos.
También puedes usar una comprensión de lista:

   w, h = 2, 3
   A = [[None] * w for i in range(h)]

Or, you can use an extension that provides a matrix datatype; NumPy is
the best known.

### How do I apply a method or function to a sequence of objects?

To call a method or function and accumulate the return values in a
list, a *list comprehension* is an elegant solution:

   result = [obj.method() for obj in mylist]

   result = [function(obj) for obj in mylist]

To just run the method or function without saving the return values, a
plain "for" loop will suffice:

   for obj in mylist:
       obj.method()

   for obj in mylist:
       function(obj)

### ¿Por qué hacer lo siguiente, "a_tuple[i] += ['item']", lanza una excepción cuando la suma funciona?

Esto es debido a la combinación del hecho de que un operador de
asignación aumentada es un operador de *asignación* y a la diferencia
entre objetos mutables e inmutable en Python.

Esta discusión aplica, en general, cuando los operadores de asignación
aumentada se aplican a elementos de una tupla que apuntan a objetos
mutables. Pero vamos a usar una "lista" y "+=" para el ejemplo.

Si escribes:

   >>> a_tuple = (1, 2)
   >>> a_tuple[0] += 1
   Traceback (most recent call last):
      ...
   TypeError: 'tuple' object does not support item assignment

La razón por la que se produce la excepción debería ser evidente: "1"
se añade al objeto "a_tuple[0]" que apunta a ("1"), creando el objeto
resultante, "2", pero cuando intentamos asignar el resultado del
cálculo, "2", al elemento "0" de la tupla, obtenemos un error debido a
que no podemos cambiar el elemento al que apunta la tupla.

En realidad, lo que esta declaración de asignación aumentada está
haciendo es, aproximadamente, lo siguiente:

   >>> result = a_tuple[0] + 1
   >>> a_tuple[0] = result
   Traceback (most recent call last):
     ...
   TypeError: 'tuple' object does not support item assignment

Es la parte de asignación de la operación la que provoca el error,
debido a que una tupla es inmutable.

Cuando escribes algo como lo siguiente:

   >>> a_tuple = (['foo'], 'bar')
   >>> a_tuple[0] += ['item']
   Traceback (most recent call last):
     ...
   TypeError: 'tuple' object does not support item assignment

La excepción es un poco más sorprendente e, incluso, más sorprendente
es el hecho que aunque hubo un error, la agregación funcionó:

   >>> a_tuple[0]
   ['foo', 'item']

To see why this happens, you need to know that (a) if an object
implements an "__iadd__()" magic method, it gets called when the "+="
augmented assignment is executed, and its return value is what gets
used in the assignment statement; and (b) for lists, "__iadd__()" is
equivalent to calling "extend()" on the list and returning the list.
That's why we say that for lists, "+=" is a "shorthand" for
"list.extend()":

   >>> a_list = []
   >>> a_list += [1]
   >>> a_list
   [1]

Esto es equivalente a

   >>> result = a_list.__iadd__([1])
   >>> a_list = result

El objeto al que apunta a_list ha mutado y el puntero al objeto mutado
es asignado de vuelta a "a_list".  El resultado final de la asignación
no es opción debido a que es un puntero al mismo objeto al que estaba
apuntando "a_list"  pero la asignación sí que ocurre.

Por tanto, en nuestro ejemplo con tupla lo que está pasando es
equivalente a:

   >>> result = a_tuple[0].__iadd__(['item'])
   >>> a_tuple[0] = result
   Traceback (most recent call last):
     ...
   TypeError: 'tuple' object does not support item assignment

The "__iadd__()" succeeds, and thus the list is extended, but even
though "result" points to the same object that "a_tuple[0]" already
points to, that final assignment still results in an error, because
tuples are immutable.

### Quiero hacer una ordenación compleja: ¿Puedes hacer una transformada Schwartziana (Schwartzian Transform) en Python?

La técnica, atribuida a Randal Schwartz, miembro de la comunidad Perl,
ordena los elementos de una lista mediante una métrica que mapea cada
elemento a su "valor orden". En Python, usa el argumento "key" par el
método "list.sort()":

   Isorted = L[:]
   Isorted.sort(key=lambda s: int(s[10:15]))

### ¿Cómo puedo ordenar una lista a partir de valores de otra lista?

Merge them into an iterator of tuples, sort the resulting list, and
then pick out the element you want.

>>> list1 = ["what", "I'm", "sorting", "by"]
>>> list2 = ["something", "else", "to", "sort"]
>>> pairs = zip(list1, list2)
>>> pairs = sorted(pairs)
>>> pairs
[("I'm", 'else'), ('by', 'sort'), ('sorting', 'to'), ('what', 'something')]
>>> result = [x[1] for x in pairs]
>>> result
['else', 'sort', 'to', 'something']

## Objetos

### ¿Qué es una clase?

Una clase es un tipo de objeto particular creado mediante la ejecución
de la declaración class. Los objetos class se usan como plantillas
para crear instancias de objetos que son tanto los datos (atributos)
como el código (métodos) específicos para un tipo de dato.

Una clase puede estar basada en una o más clases diferentes, llamadas
su(s) clase(s). Hereda los atributos y métodos de sus clases base.
Esto permite que se pueda refinar un objeto modelo de forma sucesiva
mediante herencia.  Puedes tener una clase genérica "Mailbox"  que
proporciona métodos de acceso básico para un buzón de correo y
subclases como "MboxMailbox", "MaildirMailbox", "OutlookMailbox" que
gestionan distintos formatos específicos de buzón de correos.

### ¿Qué es un método?

Un método es una función de un objeto "x" que puedes llamar,
normalmente, de la forma "x.name(arguments...)".  Los métodos  se
definen como funciones dentro de la definición de la clase:

   class C:
       def meth(self, arg):
           return arg * 2 + self.attribute

### ¿Qué es self?

Self es, básicamente, un nombre que se usa de forma convencional como
primer argumento de un método.  Un método definido como "meth(self, a,
b, c)" se le llama como "x.meth(a, b, c)" para una instancia "x" de la
clase es que se definió; el método invocado pensará que se le ha
invocado como "meth(x, a, b, c)".

Ver también ¿Por qué debe usarse 'self' explícitamente en las
definiciones y llamadas de métodos?.

### ¿Cómo puedo comprobar si un objeto es una instancia de una clase dada o de una subclase de la misma?

Use the built-in function "isinstance(obj, cls)".  You can check if an
object is an instance of any of a number of classes by providing a
tuple instead of a single class, for example, "isinstance(obj,
(class1, class2, ...))", and can also check whether an object is one
of Python's built-in types, for example, "isinstance(obj, str)" or
"isinstance(obj, (int, float, complex))".

Note that "isinstance()" also checks for virtual inheritance from an
*abstract base class*.  So, the test will return "True" for a
registered class even if hasn't directly or indirectly inherited from
it.  To test for "true inheritance", scan the *method resolution
order* (MRO) of the class:

   from collections.abc import Mapping

   class P:
        pass

   class C(P):
       pass

   Mapping.register(P)

   >>> c = C()
   >>> isinstance(c, C)        # direct
   True
   >>> isinstance(c, P)        # indirect
   True
   >>> isinstance(c, Mapping)  # virtual
   True

   # Actual inheritance chain
   >>> type(c).__mro__
   (<class 'C'>, <class 'P'>, <class 'object'>)

   # Test for "true inheritance"
   >>> Mapping in type(c).__mro__
   False

Destacar que muchos programas no necesitan usar "isinstance()" de
forma frecuente en clases definidas por el usuario.  Si estás
desarrollando clases un mejor estilo orientado a objetos sería el de
definir los métodos en las clases que encapsulan un comportamiento en
particular en lugar de ir comprobando la clase del objeto e ir
haciendo cosas en base a la clase que es.  Por ejemplo, si tienes una
función que hace lo siguiente:

   def search(obj):
       if isinstance(obj, Mailbox):
           ...  # code to search a mailbox
       elif isinstance(obj, Document):
           ...  # code to search a document
       elif ...

Un enfoque más adecuado sería definir un método "search()" en todas
las clases e invocarlo:

   class Mailbox:
       def search(self):
           ...  # code to search a mailbox

   class Document:
       def search(self):
           ...  # code to search a document

   obj.search()

### ¿Qué es la delegación?

Delegation is an object-oriented technique (also called a design
pattern). Let's say you have an object "x" and want to change the
behaviour of just one of its methods.  You can create a new class that
provides a new implementation of the method you're interested in
changing and delegates all other methods to the corresponding method
of "x".

Los programadores Python pueden implementar la delegación de forma muy
sencilla.  Por ejemplo, la siguiente clase implementa una clase que se
comporta como un fichero pero convierte todos los datos escritos a
mayúsculas:

   class UpperOut:

       def __init__(self, outfile):
           self._outfile = outfile

       def write(self, s):
           self._outfile.write(s.upper())

       def __getattr__(self, name):
           return getattr(self._outfile, name)

Here the "UpperOut" class redefines the "write()" method to convert
the argument string to uppercase before calling the underlying
"self._outfile.write()" method.  All other methods are delegated to
the underlying "self._outfile" object.  The delegation is accomplished
via the "__getattr__()" method; consult the language reference for
more information about controlling attribute access.

Note that for more general cases delegation can get trickier. When
attributes must be set as well as retrieved, the class must define a
"__setattr__()" method too, and it must do so carefully.  The basic
implementation of "__setattr__()" is roughly equivalent to the
following:

   class X:
       ...
       def __setattr__(self, name, value):
           self.__dict__[name] = value
       ...

Many "__setattr__()" implementations call "object.__setattr__()" to
set an attribute on self without causing infinite recursion:

   class X:
       def __setattr__(self, name, value):
           # Custom logic here...
           object.__setattr__(self, name, value)

Alternatively, it is possible to set attributes by inserting entries
into "self.__dict__" directly.

### ¿Cómo invoco a un método definido en una clase base desde una clase derivada que la extiende?

Usa la función incorporada "super()":

   class Derived(Base):
       def meth(self):
           super().meth()  # calls Base.meth

En el ejemplo, "super()" automáticamente determinará la instancia
desde la cual ha sido llamada (el valor "self`"), busca el *method
resolution order* (MRO) con "type(self).__mro__", y devuelve el
siguiente en línea después de "Derived" en el MRO: "Base".

### ¿Cómo puedo organizar mi código para hacer que sea más sencillo modificar la clase base?

You could assign the base class to an alias and derive from the alias.
Then all you have to change is the value assigned to the alias.
Incidentally, this trick is also handy if you want to decide
dynamically (such as depending on availability of resources) which
base class to use.  Example:

   class Base:
       ...

   BaseAlias = Base

   class Derived(BaseAlias):
       ...

### ¿Cómo puedo crear datos estáticos de clase y métodos estáticos de clase?

Tanto los datos estáticos como los métodos estáticos (en el sentido de
C++ o Java) están permitidos en Python.

Para datos estáticos simplemente define un atributo de clase.  Para
asignar un nuevo valor al atributo debes usar de forma explícita el
nombre de la clase en la asignación:

   class C:
       count = 0   # number of times C.__init__ called

       def __init__(self):
           C.count = C.count + 1

       def getcount(self):
           return C.count  # or return self.count

"c.count" también se refiere a "C.count" para cualquier "c" de tal
forma que se cumpla "isinstance(c, C)", a no ser que "c" sea
sobreescrita por si misma o por alguna clase contenida en la búsqueda
de clases base desde "c.__class__" hasta "C".

Debes tener cuidado: dentro de un método de C, una asignación como
"self.count = 42" creará una nueva instancia sin relación con la
original que se llamará "count" en el propio diccionario de "self".
El reunificar el nombre de datos estáticos de una clase debería
llevar, siempre, a especificar la clase tanto si se produce desde
dentro de un método como si no:

   C.count = 314

Los métodos estáticos son posibles:

   class C:
       @staticmethod
       def static(arg1, arg2, arg3):
           # No 'self' parameter!
           ...

Sin embargo, una forma más directa de obtener el efecto de un método
estático sería mediante una simple función a nivel de módulo:

   def getcount():
       return C.count

Si has estructurado tu código para definir una clase única (o una
jerarquía de clases altamente relacionadas) por módulo, esto
proporcionará la encapsulación deseada.

### ¿Como puedo sobrecargar constructores (o métodos) en Python?

Esta respuesta es aplicable, en realidad, a todos los métodos pero la
pregunta suele surgir primero en el contexto de los constructores.

In C++ you'd write:

   class C {
       C() { cout << "No arguments\n"; }
       C(int i) { cout << "Argument is " << i << "\n"; }
   }

En Python solo debes escribir un único constructor que tenga en cuenta
todos los casos usando los argumentos por defecto.  Por ejemplo:

   class C:
       def __init__(self, i=None):
           if i is None:
               print("No arguments")
           else:
               print("Argument is", i)

Esto no es totalmente equivalente pero, en la práctica, es muy
similar.

You could also try a variable-length argument list, for example:

   def __init__(self, *args):
       ...

El mismo enfoque funciona para todas las definiciones de métodos.

### Intento usar __spam y obtengo un error sobre _SomeClassName__spam.

Nombres de variable con doble guión prefijado se convierten, con una
modificación de nombres, para proporcionar una forma simple pero
efectiva de definir variables de clase privadas. Cualquier
identificador de la forma "__spam" (como mínimo dos guiones bajos como
prefijo, como máximo un guión bajo como sufijo) se reemplaza con
"_classname__spam", donde "classname" es el nombre de la clase
eliminando cualquier guión bajo prefijado.

The identifier can be used unchanged within the class, but to access
it outside the class, the mangled name must be used:

   class A:
       def __one(self):
           return 1
       def two(self):
           return 2 * self.__one()

   class B(A):
       def three(self):
           return 3 * self._A__one()

   four = 4 * A()._A__one()

In particular, this does not guarantee privacy since an outside user
can still deliberately access the private attribute; many Python
programmers never bother to use private variable names at all.

Ver también:

  The private name mangling specifications for details and special
  cases.

### Mi clase define __del__ pero no se le invoca cuando borro el objeto.

Existen varias razones posibles para que suceda así.

The "del" statement does not necessarily call "__del__()" -- it simply
decrements the object's reference count, and if this reaches zero
"__del__()" is called.

If your data structures contain circular links (for example, a tree
where each child has a parent reference and each parent has a list of
children) the reference counts will never go back to zero.  Once in a
while Python runs an algorithm to detect such cycles, but the garbage
collector might run some time after the last reference to your data
structure vanishes, so your "__del__()" method may be called at an
inconvenient and random time. This is inconvenient if you're trying to
reproduce a problem. Worse, the order in which object's "__del__()"
methods are executed is arbitrary.  You can run "gc.collect()" to
force a collection, but there *are* pathological cases where objects
will never be collected.

Despite the cycle collector, it's still a good idea to define an
explicit "close()" method on objects to be called whenever you're done
with them.  The "close()" method can then remove attributes that refer
to subobjects.  Don't call "__del__()" directly -- "__del__()" should
call "close()" and "close()" should make sure that it can be called
more than once for the same object.

Otra forma de evitar referencias cíclicas sería usando el módulo
"weakref", que permite apuntar hacia objetos sin incrementar su conteo
de referencias. Las estructuras de datos en árbol, por ejemplo,
deberían usar referencias débiles para las referencias del padre y
hermanos (¡si es que las necesitan!).

Finally, if your "__del__()" method raises an exception, a warning
message is printed to "sys.stderr".

### ¿Cómo puedo obtener una lista de todas las instancias de una clase dada?

Python no hace seguimiento de todas las instancias de una clase (o de
los tipos incorporados). Puedes programar el constructor de una clase
para que haga seguimiento de todas sus instancias manteniendo una
lista de referencias débiles a cada instancia.

### ¿Por qué el resultado de "id()" no parece ser único?

La función incorporada "id()" devuelve un entero que se garantiza que
sea único durante la vida del objeto.  Debido a que en CPython esta es
la dirección en memoria del objeto, sucede que, frecuentemente,
después de que un objeto se elimina de la memoria el siguiente objeto
recién creado se localiza en la misma posición en memoria.  Esto se
puede ver ilustrado en este ejemplo:

>>> id(1000)
13901272
>>> id(2000)
13901272

Las dos ids pertenecen a dos objetos 'entero' diferentes que se crean
antes y se eliminan inmediatamente después de la ejecución de la
invocación a "id()".  Para estar seguro que los objetos cuya id
quieres examinar siguen vivos crea otra referencia al objeto:

>>> a = 1000; b = 2000
>>> id(a)
13901272
>>> id(b)
13891296

### ¿Cuándo puedo fiarme de pruebas de identidad con el operador *is*?

El operador "is" verifica la identidad de un objeto. La prueba "a is
b" es equivalente a "id(a) == id(b)".

La propiedad más importante de una prueba de identidad es que un
objeto siempre es idéntico a si mismo, "a is a" siempre devuelve
"True".  Las pruebas de identidad suelen ser más rápidas que pruebas
de igualdad.  Y a diferencia de las pruebas de igualdad, las pruebas
de identidad están garantizadas de devolver un booleano "True" o
"False".

Sin embargo, las pruebas de identidad *solo* pueden ser sustituidas
por pruebas de igualdad cuando la identidad de objeto está asegurada.
Generalmente hay tres circunstancias en las que la identidad está
garantizada:

1. Assignments create new names but do not change object identity.
   After the assignment "new = old", it is guaranteed that "new is
   old".

2. Putting an object in a container that stores object references does
   not change object identity.  After the list assignment "s[0] = x",
   it is guaranteed that "s[0] is x".

3. If an object is a singleton, it means that only one instance of
   that object can exist.  After the assignments "a = None" and "b =
   None", it is guaranteed that "a is b" because "None" is a
   singleton.

En la mayoría de las demás circunstancias, no se recomiendan las
pruebas de identidad y las pruebas de igualdad son preferidas.  En
particular, las pruebas de identidad no deben ser usadas para
verificar constantes como "int" y "str" que no están garantizadas a
ser singletons:

   >>> a = 10_000_000
   >>> b = 5_000_000
   >>> c = b + 5_000_000
   >>> a is c
   False

   >>> a = 'Python'
   >>> b = 'Py'
   >>> c = b + 'thon'
   >>> a is c
   False

De la misma manera, nuevas instancias de contenedores mutables nunca
son idénticas:

   >>> a = []
   >>> b = []
   >>> a is b
   False

En la librería estándar de código, verás varios patrones comunes para
usar correctamente pruebas de identidad:

1. As recommended by **PEP 8**, an identity test is the preferred way
   to check for "None".  This reads like plain English in code and
   avoids confusion with other objects that may have boolean values
   that evaluate to false.

2. Detecting optional arguments can be tricky when "None" is a valid
   input value.  In those situations, you can create a singleton
   sentinel object guaranteed to be distinct from other objects.  For
   example, here is how to implement a method that behaves like
   "dict.pop()":

      _sentinel = object()

      def pop(self, key, default=_sentinel):
          if key in self:
              value = self[key]
              del self[key]
              return value
          if default is _sentinel:
              raise KeyError(key)
          return default

3. Container implementations sometimes need to augment equality tests
   with identity tests.  This prevents the code from being confused by
   objects such as "float('NaN')" that are not equal to themselves.

For example, here is the implementation of
"collections.abc.Sequence.__contains__()":

   def __contains__(self, value):
       for v in self:
           if v is value or v == value:
               return True
       return False

### ¿Cómo puede una subclase controlar qué datos se almacenan en una instancia inmutable?

When subclassing an immutable type, override the "__new__()" method
instead of the "__init__()" method.  The latter only runs *after* an
instance is created, which is too late to alter data in an immutable
instance.

Todas estas clases inmutables tienen una firma distinta que su clase
padre:

   import datetime as dt

   class FirstOfMonthDate(dt.date):
       "Always choose the first day of the month"
       def __new__(cls, year, month, day):
           return super().__new__(cls, year, month, 1)

   class NamedInt(int):
       "Allow text names for some numbers"
       xlat = {'zero': 0, 'one': 1, 'ten': 10}
       def __new__(cls, value):
           value = cls.xlat.get(value, value)
           return super().__new__(cls, value)

   class TitleStr(str):
       "Convert str to name suitable for a URL path"
       def __new__(cls, s):
           s = s.lower().replace(' ', '-')
           s = ''.join([c for c in s if c.isalnum() or c == '-'])
           return super().__new__(cls, s)

Las clases pueden ser utilizadas así:

   >>> FirstOfMonthDate(2012, 2, 14)
   FirstOfMonthDate(2012, 2, 1)
   >>> NamedInt('ten')
   10
   >>> NamedInt(20)
   20
   >>> TitleStr('Blog: Why Python Rocks')
   'blog-why-python-rocks'

### ¿Cómo cacheo llamadas de método?

The two principal tools for caching methods are
"@functools.cached_property" and "@functools.lru_cache".  The former
stores results at the instance level and the latter at the class
level.

The "cached_property" approach only works with methods that do not
take any arguments.  It does not create a reference to the instance.
The cached method result will be kept only as long as the instance is
alive.

The advantage is that when an instance is no longer used, the cached
method result will be released right away.  The disadvantage is that
if instances accumulate, so too will the accumulated method results.
They can grow without bound.

The "lru_cache" approach works with methods that have *hashable*
arguments.  It creates a reference to the instance unless special
efforts are made to pass in weak references.

La ventaja del algoritmo usado menos recientemente es que el cache
está limitado por el *maxsize* especificado.  La desventaja es que las
instancias se mantienen activas hasta que sean eliminadas del cache
por edad o que el cache sea borrado.

Este ejemplo muestra las diversas técnicas:

   class Weather:
       "Lookup weather information on a government website"

       def __init__(self, station_id):
           self._station_id = station_id
           # The _station_id is private and immutable

       def current_temperature(self):
           "Latest hourly observation"
           # Do not cache this because old results
           # can be out of date.

       @cached_property
       def location(self):
           "Return the longitude/latitude coordinates of the station"
           # Result only depends on the station_id

       @lru_cache(maxsize=20)
       def historic_rainfall(self, date, units='mm'):
           "Rainfall on a given date"
           # Depends on the station_id, date, and units.

The above example assumes that the *station_id* never changes.  If the
relevant instance attributes are mutable, the "cached_property"
approach can't be made to work because it cannot detect changes to the
attributes.

To make the "lru_cache" approach work when the *station_id* is
mutable, the class needs to define the "__eq__()" and "__hash__()"
methods so that the cache can detect relevant attribute updates:

   class Weather:
       "Example with a mutable station identifier"

       def __init__(self, station_id):
           self.station_id = station_id

       def change_station(self, station_id):
           self.station_id = station_id

       def __eq__(self, other):
           return self.station_id == other.station_id

       def __hash__(self):
           return hash(self.station_id)

       @lru_cache(maxsize=20)
       def historic_rainfall(self, date, units='cm'):
           'Rainfall on a given date'
           # Depends on the station_id, date, and units.

## Módulos

### ¿Cómo creo un fichero .pyc?

Cuando se importa un módulo por primera vez (o cuando el código fuente
ha cambiado desde que el fichero compilado se creó) un fichero ".pyc"
que contiene el código compilado se debería crear en la subcarpeta
"__pycache__" del directorio que contiene al fichero ".py".  El
fichero ".pyc" tendrá un nombre que empezará con el mismo nombre que
el del fichero  ".py" y terminará con ".pyc", con un componente
intermedio que dependerá del binario "python" en particular que lo
creó.  (Ver **PEP 3147** para detalles.)

Una razón por la que no se cree un fichero ".pyc" podría ser debido a
un problema de permisos del directorio que contiene al fichero fuente,
lo que significa que el subdirectorio "__pycache__" no se puede crear.
Esto puede suceder, por ejemplo, si desarrollas como un usuario pero
lo ejecutas como otro, como si estuvieras probando en un servidor web.

Unless the "PYTHONDONTWRITEBYTECODE" environment variable is set,
creation of a .pyc file is automatic if you're importing a module and
Python has the ability (permissions, free space, and so on) to create
a "__pycache__" subdirectory and write the compiled module to that
subdirectory.

Running Python on a top-level script is not considered an import and
no ".pyc" will be created.  For example, if you have a top-level
module "foo.py" that imports another module "xyz.py", when you run
"foo" (by typing "python foo.py" as a shell command), a ".pyc" will be
created for "xyz" because "xyz" is imported, but no ".pyc" file will
be created for "foo" since "foo.py" isn't being imported.

Si necesitas crear un fichero ".pyc" también para "foo" -- es decir,
crear un fichero ".pyc" para un módulo que no ha sido importado --
puedes usar los módulos "py_compile" y "compileall".

El módulo "py_compile" puede compilar manualmente cualquier módulo.
Una forma sería usando la función "compile()" de ese módulo de forma
interactiva:

   >>> import py_compile
   >>> py_compile.compile('foo.py')

This will write the ".pyc" to a "__pycache__" subdirectory in the same
location as "foo.py" (or you can override that with the optional
parameter *cfile*).

Puedes compilar automáticamente todos los ficheros en un directorio o
directorios usando el módulo "compileall".  Lo puedes hacer desde la
línea de comandos ejecutando "compileall.py" y proporcionando una ruta
al directorio que contiene los ficheros Python a compilar:

   python -m compileall .

### ¿Cómo puedo encontrar el nombre del módulo en uso?

Un módulo puede encontrar su propio nombre mirando en la variable
global predeterminada "__name__".  Si tiene el valor "'__main__'", el
programa se está ejecutando como un script.  Muchos módulos que se
usan, generalmente, importados en otro script proporcionan, además,
una interfaz para la línea de comandos o para probarse a si mismos y
solo ejecutan código después de comprobar "__name__":

   def main():
       print('Running test...')
       ...

   if __name__ == '__main__':
       main()

### ¿Cómo podría tener módulos que se importan mutuamente entre ellos?

Supón que tienes los siguientes módulos:

"foo.py":

   from bar import bar_var
   foo_var = 1

"bar.py":

   from foo import foo_var
   bar_var = 2

El problema es que el intérprete realizará los siguientes pasos:

* main importa a "foo"

* Se crean *globals* vacíos para foo

* "foo" se compila y se comienza a ejecutar

* "foo" importa a "bar"

* Se crean *globals* vacíos para "bar"

* "bar" se compila y se comienza a ejecutar

* "bar" importa a "foo" (lo cual es un no-op ya que ya hay un módulo
  que se llama "foo")

* El mecanismo de importado intenta leer "foo_var" de globales de
  "foo", para establecer "bar.foo_var = foo.foo_var"

El último paso falla debido a que Python todavía no ha terminado de
interpretar a "foo" y el diccionario de símbolos global para "foo"
todavía se encuentra vacío.

Lo mismo ocurre cuando usas "import foo" y luego tratas de acceder a
"foo.foo_var" en un código global.

Existen (al menos) tres posibles soluciones para este problema.

Guido van Rossum recomienda evitar todos los usos de "from <module>
import ...", y colocar todo el código dentro de funciones.  La
inicialización de variables globales y variables de clase debería usar
únicamente constantes o funciones incorporadas .  Esto significa que
todo se referenciará como "<module>.<name>" desde un módulo importado.

Jim Roskind sugiere realizar los siguientes pasos en el siguiente
orden en cada módulo:

* exportar (*globals*, funciones y clases que no necesitan clases
  bases importadas)

* "import" declaraciones

* código activo (incluyendo *globals* que han sido inicializados desde
  valores importados).

Van Rossum doesn't like this approach much because the imports appear
in a strange place, but it does work.

Matthias Urlichs recomienda reestructurar tu código de tal forma que
un import recursivo no sea necesario.

Estas soluciones no son mutuamente excluyentes.

### __import__('x.y.z') devuelve <module 'x'>; ¿cómo puedo obtener z?

Considera, en su lugar, usa la función de conveniencia
"import_module()" de "importlib":

   z = importlib.import_module('x.y.z')

### Cuando edito un módulo importado y lo reimporto los cambios no tienen efecto. ¿Por qué sucede esto?

Por razones de eficiencia además de por consistencia, Python solo lee
el fichero del módulo la primera vez que el módulo se importa.  Si no
lo hiciera así, un programa escrito en muchos módulos donde cada
módulo importa al mismo módulo básico estaría analizando
sintácticamente el mismo módulo básico muchas veces.  Para forzar una
relectura de un módulo que ha sido modificado haz lo siguiente:

   import importlib
   import modname
   importlib.reload(modname)

Warning: this technique is not 100% fool-proof.  In particular,
modules containing statements like:

   from modname import some_objects

continuarán funcionando con la versión antigua de los objetos
importados.  Si el módulo contiene definiciones de clase, instancias
de clase ya existentes *no* se actualizarán para usar la nueva
definición de la clase.  Esto podría resultar en el comportamiento
paradójico siguiente:

   >>> import importlib
   >>> import cls
   >>> c = cls.C()                # Create an instance of C
   >>> importlib.reload(cls)
   <module 'cls' from 'cls.py'>
   >>> isinstance(c, cls.C)       # isinstance is false?!?
   False

La naturaleza del problema se hace evidente si muestras la "identity"
de los objetos clase:

   >>> hex(id(c.__class__))
   '0x7352a0'
   >>> hex(id(cls.C))
   '0x4198d0'
