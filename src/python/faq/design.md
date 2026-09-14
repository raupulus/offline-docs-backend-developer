---
title: Preguntas frecuentes sobre diseño e historia
source_url: https://docs.python.org/es/3
source_path: faq/design.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: faq
order: 1040
---

# Preguntas frecuentes sobre diseño e historia

## ¿Por qué Python usa indentación para agrupar declaraciones?

Guido van Rossum cree que usar indentación para agrupar es
extremadamente elegante y contribuye mucho a la claridad del programa
Python promedio. La mayoría de las personas aprenden a amar esta
característica después de un tiempo.

Como no hay corchetes de inicio/fin, no puede haber un desacuerdo
entre la agrupación percibida por el analizador y el lector humano.
Ocasionalmente, los programadores de C encontrarán un fragmento de
código como este:

   if (x <= y)
           x++;
           y--;
   z++;

Solo se ejecuta la instrucción "x ++" si la condición es verdadera,
pero la indentación lo lleva a creer lo contrario. Incluso los
programadores experimentados de C a veces lo miran durante mucho
tiempo preguntándose por qué "y" se está disminuyendo incluso para "x
> y".

Debido a que no hay corchetes de inicio/fin, Python es mucho menos
propenso a conflictos de estilo de codificación. En C hay muchas
formas diferentes de colocar llaves. Después de acostumbrarse a leer y
escribir código usando un estilo en particular, es normal sentirse
algo incómodo al leer (o tener que escribir) en uno diferente.

Muchos estilos de codificación colocan corchetes de inicio / fin en
una línea por sí mismos. Esto hace que los programas sean
considerablemente más largos y desperdicia un valioso espacio en la
pantalla, lo que dificulta obtener una buena visión general de un
programa. Idealmente, una función debería caber en una pantalla (por
ejemplo, 20-30 líneas). 20 líneas de Python pueden hacer mucho más
trabajo que 20 líneas de C. Esto no se debe únicamente a la falta de
corchetes de inicio/fin -- la falta de declaraciones y los tipos de
datos de alto nivel también son responsables -- sino también la
indentación basada en la sintaxis ciertamente ayuda.

## ¿Por qué obtengo resultados extraños con operaciones aritméticas simples?

Ver la siguiente pregunta.

## ¿Por qué los cálculos de punto flotante son tan inexactos?

Los usuarios a menudo se sorprenden por resultados como este:

   >>> 1.2 - 1.0
   0.19999999999999996

y creo que es un error en Python. No es. Esto tiene poco que ver con
Python, y mucho más con la forma en que la plataforma subyacente
maneja los números de punto flotante.

El tipo "float" en CPython usa una C "double" para el almacenamiento.
Un valor del objeto "float" se almacena en coma flotante binaria con
una precisión fija (típicamente 53 bits) y Python usa operaciones C,
que a su vez dependen de la implementación de hardware en el
procesador, para realizar operaciones de coma flotante. Esto significa
que, en lo que respecta a las operaciones de punto flotante, Python se
comporta como muchos lenguajes populares, incluidos C y Java.

Many numbers that can be written easily in decimal notation cannot be
expressed exactly in binary floating point.  For example, after:

   >>> x = 1.2

el valor almacenado para "x" es una aproximación (muy buena) al valor
decimal "1.2", pero no es exactamente igual a él. En una máquina
típica, el valor real almacenado es:

   1.0011001100110011001100110011001100110011001100110011 (binary)

que es exactamente:

   1.1999999999999999555910790149937383830547332763671875 (decimal)

La precisión típica de 53 bits proporciona flotantes Python con 15--16
dígitos decimales de precisión.

For a fuller explanation, please see the floating-point arithmetic
chapter in the Python tutorial.

## ¿Por qué las cadenas de caracteres de Python son inmutables?

Hay varias ventajas.

Una es el rendimiento: saber que una cadena es inmutable significa que
podemos asignarle espacio en el momento de la creación, y los
requisitos de almacenamiento son fijos e inmutables. Esta es también
una de las razones para la distinción entre tuplas y listas.

Otra ventaja es que las cadenas en Python se consideran tan
"elementales" como los números. Ninguna cantidad de actividad cambiará
el valor 8 a otra cosa, y en Python, ninguna cantidad de actividad
cambiará la cadena "ocho" a otra cosa.

## ¿Por qué debe usarse 'self' explícitamente en las definiciones y llamadas de métodos?

La idea fue tomada de Modula-3. Resulta ser muy útil, por una variedad
de razones.

Primero, es más obvio que está utilizando un método o atributo de
instancia en lugar de una variable local. Leer "self.x" o
"self.meth()" deja absolutamente claro que se usa una variable de
instancia o método incluso si no conoce la definición de clase de
memoria. En C++, puede darse cuenta de la falta de una declaración de
variable local (suponiendo que los globales son raros o fácilmente
reconocibles) -- pero en Python, no hay declaraciones de variables
locales, por lo que debería buscar la definición de clase para estar
seguro. Algunos estándares de codificación de C++ y Java requieren que
los atributos de instancia tengan un prefijo "m_", porque el ser
explícito también es útil en esos lenguajes.

En segundo lugar, significa que no es necesaria una sintaxis especial
si desea hacer referencia explícita o llamar al método desde una clase
en particular. En C++, si desea usar un método de una clase base que
se anula en una clase derivada, debe usar el operador "::" -- en
Python puede escribir "baseclass.methodname(self, <argument list>)".
Esto es particularmente útil para métodos "__init__()", y en general
en los casos en que un método de clase derivada quiere extender el
método de clase base del mismo nombre y, por lo tanto, tiene que
llamar al método de clase base de alguna manera.

Finalmente, para las variables de instancia se resuelve un problema
sintáctico con la asignación: dado que las variables locales en Python
son (¡por definición!) Aquellas variables a las que se asigna un valor
en un cuerpo de función (y que no se declaran explícitamente como
globales), tiene que haber una forma de decirle al intérprete que una
asignación estaba destinada a asignar a una variable de instancia en
lugar de a una variable local, y que preferiblemente debería ser
sintáctica (por razones de eficiencia). C++ hace esto a través de
declaraciones, pero Python no tiene declaraciones y sería una pena
tener que presentarlas solo para este propósito. Usar el "self.var"
explícito resuelve esto muy bien. Del mismo modo, para usar variables
de instancia, tener que escribir "self.var" significa que las
referencias a nombres no calificados dentro de un método no tienen que
buscar en los directorios de la instancia. Para decirlo de otra
manera, las variables locales y las variables de instancia viven en
dos espacios de nombres diferentes, y debe decirle a Python qué
espacio de nombres usar.

## ¿Por qué no puedo usar una tarea en una expresión?

¡A partir de Python 3.8, se puede!

Asignación de expresiones usando el operador walrus ":=" asigna una
variable en una expresión:

   while chunk := fp.read(200):
      print(chunk)

Ver **PEP 572** para más información.

## ¿Por qué Python usa métodos para alguna funcionalidad (por ejemplo, list.index()) pero funciones para otra (por ejemplo, len(list))?

Como dijo Guido:

   (a) For some operations, prefix notation just reads better than
   postfix -- prefix (and infix!) operations have a long tradition in
   mathematics which likes notations where the visuals help the
   mathematician thinking about a problem. Compare the easy with which
   we rewrite a formula like x*(a+b) into x*a + x*b to the clumsiness
   of doing the same thing using a raw OO notation.

   (b) When I read code that says len(x) I *know* that it is asking
   for the length of something. This tells me two things: the result
   is an integer, and the argument is some kind of container. To the
   contrary, when I read x.len(), I have to already know that x is
   some kind of container implementing an interface or inheriting from
   a class that has a standard len(). Witness the confusion we
   occasionally have when a class that is not implementing a mapping
   has a get() or keys() method, or something that isn't a file has a
   write() method.

   -- https://mail.python.org/pipermail/python-3000/2006-November/004
   643.html

## ¿Por qué join() es un método de cadena de caracteres en lugar de un método de lista o tupla?

Las cadenas de caracteres se volvieron mucho más parecidas a otros
tipos estándar a partir de Python 1.6, cuando se agregaron métodos que
brindan la misma funcionalidad que siempre ha estado disponible
utilizando las funciones del módulo de cadenas. La mayoría de estos
nuevos métodos han sido ampliamente aceptados, pero el que parece
hacer que algunos programadores se sientan incómodos es:

   ", ".join(['1', '2', '4', '8', '16'])

que da el resultado:

   "1, 2, 4, 8, 16"

Hay dos argumentos comunes en contra de este uso.

El primero corre a lo largo de las líneas de: "Se ve realmente feo el
uso de un método de un literal de cadena (constante de cadena)", a lo
que la respuesta es que sí, pero un literal de cadena es solo un valor
fijo. Si se permiten los métodos en nombres vinculados a cadenas, no
hay razón lógica para que no estén disponibles en literales.

La segunda objeción generalmente se presenta como: "Realmente estoy
diciéndole a una secuencia que una a sus miembros junto con una
constante de cadena". Lamentablemente, no lo estas haciendo. Por
alguna razón, parece ser mucho menos difícil tener "split()" como
método de cadena, ya que en ese caso es fácil ver que:

   "1, 2, 4, 8, 16".split(", ")

es una instrucción a un literal de cadena para retornar las subcadenas
de caracteres delimitadas por el separador dado (o, por defecto,
ejecuciones arbitrarias de espacio en blanco).

"join()" es un método de cadena de caracteres porque al usarlo le está
diciendo a la cadena de separación que itere sobre una secuencia de
cadenas y se inserte entre elementos adyacentes. Este método se puede
usar con cualquier argumento que obedezca las reglas para los objetos
de secuencia, incluidas las clases nuevas que pueda definir usted
mismo. Existen métodos similares para bytes y objetos bytearray.

## ¿Qué tan rápido van las excepciones?

Un bloque "try"/"except" es extremadamente eficiente si no son lanzada
excepciones. En realidad, capturar una excepción es costoso. En
versiones de Python anteriores a la 2.0, era común usar este modismo:

   try:
       value = mydict[key]
   except KeyError:
       mydict[key] = getvalue(key)
       value = mydict[key]

Esto solo tenía sentido cuando esperaba que el dict tuviera la clave
casi todo el tiempo. Si ese no fuera el caso, lo codificó así:

   if key in mydict:
       value = mydict[key]
   else:
       value = mydict[key] = getvalue(key)

Para este caso específico, también podría usar "value =
dict.setdefault(key, getvalue(key))", pero solo si la llamada
"getvalue()" es lo suficientemente barata porque se evalúa en todos
los casos.

## ¿Por qué no hay un *switch* o una declaración *case* en Python?

In general, structured switch statements execute one block of code
when an expression has a particular value or set of values. Since
Python 3.10 one can easily match literal values, or constants within a
namespace, with a "match ... case" statement. See the specification
and the tutorial for more information about "match" statements. An
older alternative is a sequence of "if... elif... elif... else".

Para los casos en los que necesita elegir entre una gran cantidad de
posibilidades, puede crear un diccionario que asigne valores de casos
a funciones para llamar. Por ejemplo:

   functions = {'a': function_1,
                'b': function_2,
                'c': self.method_1}

   func = functions[value]
   func()

Para invocar métodos en objetos, puede simplificar aún más utilizando
"getattr()" incorporado para recuperar métodos con un nombre
particular:

   class MyVisitor:
       def visit_a(self):
           ...

       def dispatch(self, value):
           method_name = 'visit_' + str(value)
           method = getattr(self, method_name)
           method()

Se sugiere que utilice un prefijo para los nombres de los métodos,
como "visit_" en este ejemplo. Sin dicho prefijo, si los valores
provienen de una fuente no confiable, un atacante podría invocar
cualquier método en su objeto.

Imitating switch with fallthrough, as with C's switch-case-default, is
possible, much harder, and less needed.

## ¿No puede emular hilos en el intérprete en lugar de confiar en una implementación de hilos específica del sistema operativo?

Respuesta 1: Desafortunadamente, el intérprete empuja al menos un
marco de pila C para cada marco de pila de Python. Además, las
extensiones pueden volver a llamar a Python en momentos casi
aleatorios. Por lo tanto, una implementación completa de subprocesos
requiere soporte de subprocesos para C.

Respuesta 2: Afortunadamente, existe Python sin pila, que tiene un
bucle de intérprete completamente rediseñado que evita la pila C.

## ¿Por qué las expresiones lambda no pueden contener sentencias?

Las expresiones lambda de Python no pueden contener declaraciones
porque el marco sintáctico de Python no puede manejar declaraciones
anidadas dentro de expresiones. Sin embargo, en Python, este no es un
problema grave. A diferencia de las formas lambda en otros lenguajes,
donde agregan funcionalidad, las lambdas de Python son solo una
notación abreviada si eres demasiado vago para definir una función.

Las funciones ya son objetos de primera clase en Python, y pueden
declararse en un ámbito local. Por lo tanto, la única ventaja de usar
una lambda en lugar de una función definida localmente es que no es
necesario inventar un nombre para la función -- ¡pero eso es sólo una
variable local a la que se asigna el objeto función (que es
exactamente el mismo tipo de objeto que produce una expresión lambda)!

## ¿Se puede compilar Python en código máquina, C o algún otro lenguaje?

Cython compiles a modified version of Python with optional annotations
into C extensions.  Nuitka is an up-and-coming compiler of Python into
C++ code, aiming to support the full Python language.

## ¿Cómo gestiona Python la memoria?

Los detalles de la administración de memoria de Python dependen de la
implementación. La implementación estándar de Python, *CPython*,
utiliza el recuento de referencias para detectar objetos inaccesibles,
y otro mecanismo para recopilar ciclos de referencia, ejecutando
periódicamente un algoritmo de detección de ciclos que busca ciclos
inaccesibles y elimina los objetos involucrados. El módulo "gc"
proporciona funciones para realizar una recolección de basura, obtener
estadísticas de depuración y ajustar los parámetros del recolector.

Other implementations (such as Jython or PyPy), however, can rely on a
different mechanism such as a full-blown garbage collector.  This
difference can cause some subtle porting problems if your Python code
depends on the behavior of the reference counting implementation.

En algunas implementaciones de Python, el siguiente código (que está
bien en CPython) probablemente se quedará sin descriptores de archivo:

   for file in very_long_list_of_files:
       f = open(file)
       c = f.read(1)

De hecho, utilizando el esquema de conteo de referencias y destructor
de CPython, cada nueva asignación a "f" cierra el archivo anterior.
Sin embargo, con un GC tradicional, esos objetos de archivo solo se
recopilarán (y cerrarán) a intervalos variables y posiblemente largos.

Si desea escribir código que funcione con cualquier implementación de
Python, debe cerrar explícitamente el archivo o utilizar una
declaración "with"; esto funcionará independientemente del esquema de
administración de memoria:

   for file in very_long_list_of_files:
       with open(file) as f:
           c = f.read(1)

## ¿Por qué CPython no utiliza un esquema de recolección de basura más tradicional?

Por un lado, esta no es una característica estándar de C y, por lo
tanto, no es portátil. (Sí, sabemos acerca de la biblioteca Boehm GC.
Tiene fragmentos de código de ensamblador para *la mayoría* de las
plataformas comunes, no para todas ellas, y aunque es principalmente
transparente, no es completamente transparente; se requieren parches
para obtener Python para trabajar con eso)

El GC tradicional también se convierte en un problema cuando Python
está integrado en otras aplicaciones. Mientras que en un Python
independiente está bien reemplazar el estándar "malloc()" y "free()"
con versiones proporcionadas por la biblioteca GC, una aplicación que
incruste Python puede querer tener su *propio* sustituto de "malloc()"
y "free()", y puede no querer el de Python. En este momento, CPython
funciona con todo lo que implementa "malloc()" y "free()"
correctamente.

## ¿Por qué no se libera toda la memoria cuando sale CPython?

Los objetos a los que se hace referencia desde los espacios de nombres
globales de los módulos de Python no siempre se desasignan cuando
Python sale. Esto puede suceder si hay referencias circulares. También
hay ciertos bits de memoria asignados por la biblioteca de C que son
imposibles de liberar (por ejemplo, una herramienta como Purify se
quejará de estos). Python es, sin embargo, agresivo sobre la limpieza
de la memoria al salir e intenta destruir cada objeto.

Si desea forzar a Python a eliminar ciertas cosas en la desasignación,
use el módulo "atexit" para ejecutar una función que obligará a esas
eliminaciones.

## ¿Por qué hay tipos de datos separados de tuplas y listas?

Las listas y las tuplas, si bien son similares en muchos aspectos,
generalmente se usan de maneras fundamentalmente diferentes. Las
tuplas pueden considerarse similares a los "records" de Pascal o a los
"structs" de C; son pequeñas colecciones de datos relacionados que
pueden ser de diferentes tipos que funcionan como un grupo. Por
ejemplo, una coordenada cartesiana se representa adecuadamente como
una tupla de dos o tres números.

Las listas, por otro lado, son más como matrices en otros lenguajes.
Tienden a contener un número variable de objetos, todos los cuales
tienen el mismo tipo y que se operan uno por uno. Por ejemplo,
"os.listdir('.')" retorna una lista de cadenas de caracteres que
representan los archivos en el directorio actual. Las funciones que
operan en esta salida generalmente no se romperían si agregara otro
archivo o dos al directorio.

Las tuplas son inmutables, lo que significa que una vez que se ha
creado una tupla, no puede reemplazar ninguno de sus elementos con un
nuevo valor. Las listas son mutables, lo que significa que siempre
puede cambiar los elementos de una lista. Solo los elementos
inmutables se pueden usar como claves de diccionario y, por lo tanto,
solo las tuplas y no las listas se pueden usar como claves.

## ¿Cómo se implementan las listas en Python?

Las listas de CPython son realmente matrices de longitud variable, no
listas enlazadas al estilo Lisp. La implementación utiliza una matriz
contigua de referencias a otros objetos y mantiene un puntero a esta
matriz y la longitud de la matriz en una estructura de encabezado de
lista.

Esto hace que indexar una lista "a[i]" una operación cuyo costo es
independiente del tamaño de la lista o del valor del índice.

Cuando se añaden o insertan elementos, la matriz de referencias cambia
de tamaño. Se aplica cierta inteligencia para mejorar el rendimiento
de la adición de elementos repetidamente; cuando la matriz debe
crecer, se asigna un espacio extra para que las próximas veces no
requieran un cambio de tamaño real.

## ¿Cómo se implementan los diccionarios en CPython?

Los diccionarios de CPython se implementan como tablas hash
redimensionables. En comparación con los árboles B (*B-trees*), esto
proporciona un mejor rendimiento para la búsqueda (la operación más
común con diferencia) en la mayoría de las circunstancias, y la
implementación es más simple.

Dictionaries work by computing a hash code for each key stored in the
dictionary using the "hash()" built-in function.  The hash code varies
widely depending on the key and a per-process seed; for example,
"'Python'" could hash to "-539294296" while "'python'", a string that
differs by a single bit, could hash to "1142331976".  The hash code is
then used to calculate a location in an internal array where the value
will be stored.  Assuming that you're storing keys that all have
different hash values, this means that dictionaries take constant time
-- *O*(1), in Big-O notation -- to retrieve a key.

## ¿Por qué las claves del diccionario deben ser inmutables?

La implementación de la tabla hash de los diccionarios utiliza un
valor hash calculado a partir del valor clave para encontrar la clave.
Si la clave fuera un objeto mutable, su valor podría cambiar y, por lo
tanto, su hash también podría cambiar. Pero dado que quien cambie el
objeto clave no puede decir que se estaba utilizando como clave de
diccionario, no puede mover la entrada en el diccionario. Luego,
cuando intente buscar el mismo objeto en el diccionario, no se
encontrará porque su valor hash es diferente. Si trató de buscar el
valor anterior, tampoco lo encontraría, porque el valor del objeto que
se encuentra en ese hash bin sería diferente.

Si desea un diccionario indexado con una lista, simplemente convierta
la lista a una tupla primero; La función "tuple(L)" crea una tupla con
las mismas entradas que la lista "L". Las tuplas son inmutables y, por
lo tanto, pueden usarse como claves de diccionario.

Algunas soluciones inaceptables que se han propuesto:

* Listas de hash por su dirección (ID de objeto). Esto no funciona
  porque si construye una nueva lista con el mismo valor, no se
  encontrará; por ejemplo:

     mydict = {[1, 2]: '12'}
     print(mydict[[1, 2]])

  generaría una excepción "KeyError" porque la identificación del "[1,
  2]" usado en la segunda línea difiere de la de la primera línea. En
  otras palabras, las claves del diccionario deben compararse usando
  "==", no usando "is".

* Hacer una copia cuando use una lista como clave. Esto no funciona
  porque la lista, al ser un objeto mutable, podría contener una
  referencia a sí misma, y luego el código de copia se ejecutaría en
  un bucle infinito.

* Permitir listas como claves pero decirle al usuario que no las
  modifique. Esto permitiría una clase de errores difíciles de
  rastrear en los programas cuando olvidó o modificó una lista por
  accidente. También invalida una invariante importante de
  diccionarios: cada valor en "d.keys()" se puede usar como una clave
  del diccionario.

* Marcar las listas como de solo lectura una vez que se usan como
  clave de diccionario. El problema es que no solo el objeto de nivel
  superior puede cambiar su valor; podría usar una tupla que contiene
  una lista como clave. Ingresar cualquier cosa como clave en un
  diccionario requeriría marcar todos los objetos accesibles desde
  allí como de solo lectura -- y nuevamente, los objetos
  autoreferenciados podrían causar un bucle infinito.

Hay un truco para evitar esto si lo necesita, pero úselo bajo su
propio riesgo: Puede envolver una estructura mutable dentro de una
instancia de clase que tenga tanto un método "__eq__()" y un
"__hash__()". Luego debe asegurarse de que el valor hash para todos
los objetos de contenedor que residen en un diccionario (u otra
estructura basada en hash) permanezca fijo mientras el objeto está en
el diccionario (u otra estructura).

   class ListWrapper:
       def __init__(self, the_list):
           self.the_list = the_list

       def __eq__(self, other):
           return self.the_list == other.the_list

       def __hash__(self):
           l = self.the_list
           result = 98767 - len(l)*555
           for i, el in enumerate(l):
               try:
                   result = result + (hash(el) % 9999999) * 1001 + i
               except Exception:
                   result = (result % 7777777) + i * 333
           return result

Tenga en cuenta que el cálculo de hash se complica por la posibilidad
de que algunos miembros de la lista sean inquebrantables y también por
la posibilidad de desbordamiento aritmético.

Además, siempre debe darse el caso de que si "o1 == o2" (es decir,
"o1.__eq__(o2) is True"), entonces "hash(o1) == hash(o2)" (es decir,
"o1.__hash__() == o2.__hash__()"), independientemente de si el objeto
está en un diccionario o no. Si no cumple con estas restricciones, los
diccionarios y otras estructuras basadas en hash se comportarán mal.

En el caso de "ListWrapper", siempre que el objeto contenedor esté en
un diccionario, la lista contenida no debe cambiar para evitar
anomalías. No haga esto a menos que esté preparado para pensar
detenidamente sobre los requisitos y las consecuencias de no
cumplirlos correctamente. Considérese advertido.

## ¿Por qué list.sort() no retorna la lista ordenada?

En situaciones donde el rendimiento es importante, hacer una copia de
la lista solo para ordenarlo sería un desperdicio. Por lo tanto,
"list.sort()" ordena la lista en su lugar. Para recordarle ese hecho,
no retorna la lista ordenada. De esta manera, no se dejará engañar por
sobreescribir accidentalmente una lista cuando necesite una copia
ordenada, pero también deberá mantener la versión sin ordenar.

Si desea retornar una nueva lista, use la función incorporada
"sorted()" en su lugar. Esta función crea una nueva lista a partir de
un iterativo proporcionado, la ordena y la retorna. Por ejemplo, a
continuación se explica cómo iterar sobre las teclas de un diccionario
en orden ordenado:

   for key in sorted(mydict):
       ...  # do whatever with mydict[key]...

## ¿Cómo se especifica y aplica una especificación de interfaz en Python?

Una especificación de interfaz para un módulo proporcionada por
lenguajes como C++ y Java describe los prototipos para los métodos y
funciones del módulo. Muchos sienten que la aplicación en tiempo de
compilación de las especificaciones de la interfaz ayuda en la
construcción de grandes programas.

Python 2.6 agrega un módulo "abc" que le permite definir clases base
abstractas (ABC). Luego puede usar "isinstance()" y "issubclass()"
para verificar si una instancia o una clase implementa un ABC en
particular. El módulo "collections.abc" define un conjunto de ABC
útiles como "Iterable", "Container" y "MutableMapping".

Para Python, muchas de las ventajas de las especificaciones de
interfaz se pueden obtener mediante una disciplina de prueba adecuada
para los componentes.

Un buen conjunto de pruebas para un módulo puede proporcionar una
prueba de regresión y servir como una especificación de interfaz de
módulo y un conjunto de ejemplos. Muchos módulos de Python se pueden
ejecutar como un script para proporcionar una simple
"autocomprobación". Incluso los módulos que usan interfaces externas
complejas a menudo se pueden probar de forma aislada utilizando
emulaciones triviales de "stub" de la interfaz externa. Los módulos
"doctest" y "unittest" o marcos de prueba de terceros se pueden
utilizar para construir conjuntos de pruebas exhaustivas que ejercitan
cada línea de código en un módulo.

An appropriate testing discipline can help build large complex
applications in Python as well as having interface specifications
would.  In fact, it can be better because an interface specification
cannot test certain properties of a program.  For example, the
"list.append()" method is expected to add new elements to the end of
some internal list; an interface specification cannot test that your
"list.append()" implementation will actually do this correctly, but
it's trivial to check this property in a test suite.

Escribir conjuntos de pruebas es muy útil, y es posible que desee
diseñar su código con miras a que sea fácilmente probado. Una técnica
cada vez más popular, el desarrollo dirigido por pruebas, requiere
escribir partes del conjunto de pruebas primero, antes de escribir el
código real. Por supuesto, Python te permite ser descuidado y no
escribir casos de prueba.

## ¿Por qué no hay goto?

En la década de 1970, la gente se dio cuenta de que el goto
irrestricto podía generar un código "espagueti" desordenado que era
difícil de entender y revisar. En un lenguaje de alto nivel, también
es innecesario siempre que haya formas de bifurcar (en Python, con
sentencias "if" y expresiones "or", "and" e "if"/"else") y bucle (con
sentencia "while" y "for", que posiblemente contengan "continue" y
"break").

También se pueden utilizar excepciones para proporcionar un "goto
estructurado" que funcione incluso a través de llamadas a funciones.
Muchos creen que las excepciones pueden emular convenientemente todos
los usos razonables de las construcciones "go" o "goto" de C, Fortran
y otros lenguajes.  Por ejemplo:

   class label(Exception): pass  # declare a label

   try:
       ...
       if condition: raise label()  # goto label
       ...
   except label:  # where to goto
       pass
   ...

Esto no le permite saltar a la mitad de un bucle, pero eso es
generalmente considerado un abuso de "goto" de todos modos. Utilizar
con moderación.

## ¿Por qué las cadenas de caracteres sin formato (r-strings) no pueden terminar con una barra diagonal inversa?

Más precisamente, no pueden terminar con un número impar de barras
invertidas: la barra invertida no emparejada al final escapa el
carácter de comillas de cierre, dejando una cadena sin terminar.

Las cadenas de caracteres sin formato se diseñaron para facilitar la
creación de entradas para procesadores (principalmente motores de
expresión regular) que desean realizar su propio procesamiento de
escape de barra invertida. Tales procesadores consideran que una barra
invertida sin par es un error de todos modos, por lo que las cadenas
de caracteres sin procesar no lo permiten. A cambio, le permiten pasar
el carácter de comillas de cadena escapándolo con una barra invertida.
Estas reglas funcionan bien cuando las cadenas de caracteres r
(*r-strings*) se usan para el propósito previsto.

Si está intentando construir nombres de ruta de Windows, tenga en
cuenta que todas las llamadas al sistema de Windows también aceptan
barras diagonales:

   f = open("/mydir/file.txt")  # works fine!

Si está tratando de construir una ruta para un comando de DOS, intente
por ejemplo uno de los siguientes:

   dir = r"\this\is\my\dos\dir" "\\"
   dir = r"\this\is\my\dos\dir\ "[:-1]
   dir = "\\this\\is\\my\\dos\\dir\\"

## ¿Por qué Python no tiene una declaración "with" para las asignaciones de atributos?

Python tiene una sentencia "with" que envuelve la ejecución de un
bloque, llamando al código en la entrada y salida del bloque. Algunos
lenguajes tienen una construcción que se ve así:

   with obj:
       a = 1               # equivalent to obj.a = 1
       total = total + 1   # obj.total = obj.total + 1

En Python, tal construcción sería ambigua.

Otros lenguajes, como Object Pascal, Delphi y C ++, utilizan tipos
estáticos, por lo que es posible saber, de manera inequívoca, a qué
miembro se le está asignando. Este es el punto principal de la
escritura estática: el compilador *siempre* conoce el alcance de cada
variable en tiempo de compilación.

Python usa tipos dinámicos. Es imposible saber de antemano a qué
atributo se hará referencia en tiempo de ejecución. Los atributos de
los miembros pueden agregarse o eliminarse de los objetos sobre la
marcha. Esto hace que sea imposible saber, a partir de una simple
lectura, a qué atributo se hace referencia: ¿uno local, uno global o
un atributo miembro?

Por ejemplo, tome el siguiente fragmento incompleto:

   def foo(a):
       with a:
           print(x)

El fragmento supone que "a" debe tener un atributo miembro llamado
"x". Sin embargo, no hay nada en Python que le diga esto al
intérprete. ¿Qué debería suceder si "a" es, digamos, un número entero?
Si hay una variable global llamada "x", ¿se usará dentro del bloque
"with"? Como puede ver, la naturaleza dinámica de Python hace que
tales elecciones sean mucho más difíciles.

El principal beneficio de "with" y características de lenguaje
similares (reducción del volumen del código) puede, sin embargo,
lograr fácilmente en Python mediante la asignación. En vez de:

   function(args).mydict[index][index].a = 21
   function(args).mydict[index][index].b = 42
   function(args).mydict[index][index].c = 63

escribe esto:

   ref = function(args).mydict[index][index]
   ref.a = 21
   ref.b = 42
   ref.c = 63

Esto también tiene el efecto secundario de aumentar la velocidad de
ejecución porque los enlaces de nombres se resuelven en tiempo de
ejecución en Python, y la segunda versión solo necesita realizar la
resolución una vez.

Otras propuestas similares que introducían sintaxis para reducir aún
más el volumen del código, como el uso de un 'punto inicial', han sido
rechazadas en favor de la claridad (véase
https://mail.python.org/pipermail/python-ideas/2016-May/040070.html).

## ¿Por qué los generadores no admiten la declaración with?

Por razones técnicas, un generador utilizado directamente como gestor
de contexto no funcionaría correctamente.  Cuando, como es más común,
un generador se utiliza como un iterador ejecutado hasta su
finalización, no es necesario cerrar.  Cuando lo esté, envuélvalo como
"contextlib.closing(generator)" en la sentencia "with".

## ¿Por qué se requieren dos puntos para las declaraciones if/while/def/class?

Los dos puntos se requieren principalmente para mejorar la legibilidad
(uno de los resultados del lenguaje ABC experimental). Considera esto:

   if a == b
       print(a)

versus

   if a == b:
       print(a)

Observe cómo el segundo es un poco más fácil de leer. Observe más a
fondo cómo los dos puntos establecen el ejemplo en esta respuesta de
preguntas frecuentes; Es un uso estándar en inglés.

Otra razón menor es que los dos puntos facilitan a los editores con
resaltado de sintaxis; pueden buscar dos puntos para decidir cuándo se
debe aumentar la indentación en lugar de tener que hacer un análisis
más elaborado del texto del programa.

## ¿Por qué Python permite comas al final de las listas y tuplas?

Python le permite agregar una coma final al final de las listas,
tuplas y diccionarios:

   [1, 2, 3,]
   ('a', 'b', 'c',)
   d = {
       "A": [1, 5],
       "B": [6, 7],  # last trailing comma is optional but good style
   }

Hay varias razones para permitir esto.

Cuando tiene un valor literal para una lista, tupla o diccionario
distribuido en varias líneas, es más fácil agregar más elementos
porque no tiene que recordar agregar una coma a la línea anterior. Las
líneas también se pueden reordenar sin crear un error de sintaxis.

La omisión accidental de la coma puede ocasionar errores difíciles de
diagnosticar. Por ejemplo:

   x = [
     "fee",
     "fie"
     "foo",
     "fum"
   ]

Parece que esta lista tiene cuatro elementos, pero en realidad
contiene tres: "fee", "fiefoo" y "fum". Agregar siempre la coma evita
esta fuente de error.

Permitir la coma final también puede facilitar la generación de código
programático.
