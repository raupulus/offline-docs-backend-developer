---
title: '"weakref" --- Weak references'
source_url: https://docs.python.org/es/3
source_path: library/weakref.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4500
---

# "weakref" --- Weak references

**Código Fuente:** Lib/weakref.py

======================================================================

The "weakref" module allows the Python programmer to create *weak
references* to objects.

En lo consecutivo, el término *referente* aludirá al objeto que es
referenciado por una referencia débil.

Una referencia débil a un objeto no es suficiente para mantener al
objeto con vida: cuando las únicas referencias que le queden a un
referente son referencias débiles, la (*recolección de basura*) es
libre de destruir al referente y reusar su memoria para algo más.  Sin
embargo, hasta que el objeto no sea realmente destruido, la referencia
débil puede retornar el objeto incluso si no tiene referencias
fuertes.

Un uso principal para las referencias débiles es para implementar
caches o mapeados que mantienen objetos grandes, cuando no se desea
que un objeto grande no sea mantenido con vida sólo porque aparece en
un cache o mapeado.

For example, if you have a number of large binary image objects, you
may wish to associate a name with each.  If you used a Python
dictionary to map names to images, or images to names, the image
objects would remain alive just because they appeared as values or
keys in the dictionaries.  The "WeakKeyDictionary" and
"WeakValueDictionary" classes supplied by the "weakref" module are an
alternative, using weak references to construct mappings that don't
keep objects alive solely because they appear in the mapping objects.
If, for example, an image object is a value in a
"WeakValueDictionary", then when the last remaining references to that
image object are the weak references held by weak mappings, garbage
collection can reclaim the object, and its corresponding entries in
weak mappings are simply deleted.

"WeakKeyDictionary" y "WeakValueDictionary" usan referencias débiles
en sus implementaciones, estableciendo retrollamadas (*callback*) en
las referencias débiles que notifiquen a los diccionarios débiles
cuando una llave o valor ha sido reclamado por la recolección de
basura. "WeakSet" implementa la interfaz "set", pero mantiene
referencias débiles de sus elementos, justo como lo hace
"WeakKeyDictionary".

"finalize" provee una forma directa de registrar una función de
limpieza que se llame cuando un objeto es recogido por la recolección
de basura. Esto es más simple que configurar una retrollamada en una
referencia débil pura, ya que el módulo automáticamente se asegura que
el finalizador se mantenga con vida hasta que el objeto sea
recolectado.

Most programs should find that using one of these weak container types
or "finalize" is all they need -- it's not usually necessary to create
your own weak references directly.  The low-level machinery is exposed
by the "weakref" module for the benefit of advanced uses.

No todos los objetos pueden ser débilmente referenciados. Objetos que
soportan referencias débiles pueden incluir instancias de clases,
funciones escritas en Python (pero no en C), métodos de instancia,
conjuntos, frozensets, algunos *objetos archivo*, *generadores*,
objetos de tipo, sockets, arreglos, deques, objetos de patrones de
expresiones regulares, y objetos código.

Distinto en la versión 3.2: Se añadió el soporte para thread.lock,
threading.Lock, y objetos código.

Varios tipos incorporados como "list" y "dict" no soportan
directamente referencias débiles pero pueden añadir soporte al crear
una subclase:

   class Dict(dict):
       pass

   obj = Dict(red=1, green=2, blue=3)   # this object is weak referenceable

Otros tipos incorporados como "tuple" y "int" no soportan referencias
débiles incluso cuando son usadas como clase base.

Los tipos de extensiones se pueden hacer para soportar referencias
débiles; véase Soporte de referencia débil.

Cuando "__slots__" es definido para un tipo específico, el soporte
para referencia débil es deshabilitado a menos que una cadena
"'__weakref__'" también esté presente en la secuencia de cadenas en la
declaración "__slots__". Véase __slots__ documentation para más
detalles.

class weakref.ref(object[, callback])

   Retorna una referencia débil de *object*.  El objeto original puede
   ser recuperado al llamar la referencia del objeto si el referente
   sigue con vida; si el referente ya no está con vida, llamar a la
   referencia del objeto causará que se retorne un "None".  Si se
   proporciona *callback* y no "None", y el objeto weakref retornado
   aún sigue con vida, la retrollamada (*callback*) será llamado
   cuando el objeto esté a punto de ser finalizado; el objeto de la
   referencia débil será pasado como el único parámetro a la
   retrollamada, el referente ya no estará disponible.

   Se permite que muchas referencias débiles sean construidas por el
   mismo objeto. Las retrollamadas registradas por cada referencia
   débil serán llamados desde la retrollamada registrada más
   recientemente hasta la retrollamada registrada más antigua.

   Las excepciones lanzadas por la retrollamada serán visibles en la
   salida de error estándar pero no pueden ser propagadas; son
   manejadas de la misma forma que las excepciones lanzadas por el
   método "__del__()" de un objeto.

   Las referencias débiles son *hashable* si el *object* es mapeable.
   Ellos mantendrán su valor del hash incluso cuando el *objet* haya
   sido eliminado.  Si "hash()" es llamado por primera vez sólo
   después de que *object* sea eliminado, la llamada lanzará un
   "TypeError".

   Las referencias débiles soportan pruebas para igualdad, pero no
   para ordenación.  Si los referentes están todavía con vida, dos
   referencias tiene la misma relación de igualdad como sus referentes
   (sin importar el *callback*).  Si un referente ha sido eliminado,
   las referencias son iguales sólo si el objetos de referencia son el
   mismo objeto.

   Es un tipo del que se puede crear una subclase en vez de una
   función de fábrica.

   Weak references are generic over the type of the object they
   reference.

   __callback__

      Este atributo de sólo lectura retorna la llamada que está
      asociada actualmente con el weakref.  Si no hay retrollamadas o
      si el referente del weakref no está con vida entonces este
      atributo tendrá de valor "None".

   Distinto en la versión 3.4: Se añadió el atributo "__callback__".

weakref.proxy(object[, callback])

   Retorna un proxy a *object* que usa una referencia débil.  Esto
   soporta el uso del proxy en la mayoría de los contextos en vez de
   requerir la dereferencia explícita usada con los objetos de
   referencia débil. El objeto retornado tendrá un tipo "ProxyType" o
   "CallableProxyType", dependiendo si *object* es invocable. Objetos
   Proxy no son *hashable* independiente de la referencia; esto evita
   un número de problemas relacionados a su naturaleza mutable
   fundamental, y evita su uso como clave de diccionario. *callback*
   corresponde al parámetro del mismo nombre de la función "ref()".

   Acceder al atributo de un objeto proxy después de que el objeto
   referenciado haya sido recolectado por el recolector de basura
   lanza "ReferenceError".

   Distinto en la versión 3.8: Se extendió el soporto de operadores en
   objetos proxy para incluir los operadores de multiplicación de
   matrices "@" and "@=".

weakref.getweakrefcount(object)

   Retorna el número de referencias débiles y proxies que refieren a
   *object*.

weakref.getweakrefs(object)

   Retorna una lista de todas las referencias débiles y objetos proxy
   que refieren a *object*.

class weakref.WeakKeyDictionary([dict])

   Clase de mapeado que referencia llaves débilmente.  Las entradas en
   el diccionario serán descartadas cuando no haya una referencia
   fuerte a la llave.  Esto puede ser usado para asociar datos con un
   objeto apropiado por otras partes de una aplicación sin añadir
   atributos a esos objetos.  Esto puede ser especialmente útil con
   objetos que sobre escriben atributos de acceso.

   Nótese que cuando una clave cuyo valor es igual a una clave ya
   existente (pero no tienen igual identidad) es insertado en el
   diccionario, el valor es reemplazado pero no se reemplaza la clave
   existente. Debido a esto, cuando la referencia a la clave original
   es eliminada, se elimina la entrada en el diccionario:

      >>> class T(str): pass
      ...
      >>> k1, k2 = T(), T()
      >>> d = weakref.WeakKeyDictionary()
      >>> d[k1] = 1   # d = {k1: 1}
      >>> d[k2] = 2   # d = {k1: 2}
      >>> del k1      # d = {}

   Una solución alternativa sería remover la clave antes de la
   reasignación:

      >>> class T(str): pass
      ...
      >>> k1, k2 = T(), T()
      >>> d = weakref.WeakKeyDictionary()
      >>> d[k1] = 1   # d = {k1: 1}
      >>> del d[k1]
      >>> d[k2] = 2   # d = {k2: 2}
      >>> del k1      # d = {k2: 2}

   Distinto en la versión 3.9: Se agregó soporte para los operadores
   "|" y "|=", como se especifica en **PEP 584**.

Los objetos "WeakKeyDictionary" tiene un método adicional que expone
las referencias internas directamente.  Las referencias no tienen
garantía de estar con "vida" en el momento en que son usadas, por lo
que el resultado de llamar las referencias necesita ser revisado antes
de ser usado. Esto puede ser usado para evitar crear referencias que
causen que recolector de basura mantenga las llaves en existencia más
tiempo del que necesitan.

WeakKeyDictionary.keyrefs()

   Retorna un iterable de las referencias débiles a las llaves.

class weakref.WeakValueDictionary([dict])

   Clase de mapeado que referencia valores débilmente.  Las entradas
   en el diccionario serán descartadas cuando ya no existan las
   referencias fuertes a los valores.

   Distinto en la versión 3.9: Se agregó soporte para los operadores
   "|" y "|=", como se especifica en **PEP 584**.

Los objetos "WeakValueDictionary" tienen un método adicional que posee
los mismos problemas que el método "WeakKeyDictionary.keyrefs()".

WeakValueDictionary.valuerefs()

   Retorna un iterable de las referencias débiles a los valores.

class weakref.WeakSet([elements])

   Clase Conjunto que mantiene referencias débiles a sus elementos.
   Un elemento será descartado cuando ya no existan referencias
   fuertes.

class weakref.WeakMethod(method[, callback])

   Una subclase "ref" personalizada que simula una referencia débil a
   un método vinculado (i.e., un método definido en una clase y visto
   en una instancia). Ya que un método atado es efímero, una
   referencia débil estándar no puede mantenerlo.  El "WeakMethod"
   tiene un código especial para recrear el método atado hasta que o
   el objeto o la función original muera:

      >>> class C:
      ...     def method(self):
      ...         print("method called!")
      ...
      >>> c = C()
      >>> r = weakref.ref(c.method)
      >>> r()
      >>> r = weakref.WeakMethod(c.method)
      >>> r()
      <bound method C.method of <__main__.C object at 0x7fc859830220>>
      >>> r()()
      method called!
      >>> del c
      >>> gc.collect()
      0
      >>> r()
      >>>

   *callback* corresponde al parámetro del mismo nombre de la función
   "ref()".

   Added in version 3.4.

class weakref.finalize(obj, func, /, *args, **kwargs)

   Retorna un objeto finalizador invocable que será llamado cuando
   *obj* sea recolectado por el recolector de basura. A diferencia de
   referencias débiles ordinarias, un finalizador siempre sobrevivirá
   hasta que el objeto de referencia sea recolectado, simplificando
   enormemente la gestión del ciclo de vida.

   Se considera a un finalizador como *vivo* hasta que sea llamado (o
   explícitamente o en la recolección de basura), y después que esté
   *muerto*.  Llamar a un finalizador vivo retorna el resultado de
   evaluar "func(*arg, **kwargs)", mientras que llamar a un
   finalizador muerto retorna "None".

   Las excepciones lanzadas por retrollamadas de finalizadores durante
   la recolección de basura serán mostradas en la salida de error
   estándar, pero no pueden ser propagadas.  Son gestionados de la
   misma forma que las excepciones lanzadas por el método "__del__()"
   de un objeto o la retrollamada de una referencia débil.

   Cuando el programa sale, cada finalizador vivo que quede es llamado
   a menos que su atributo "atexit" sea falso.  Son llamados en el
   orden reverso de creación.

   Un finalizador nunca invocará su retrollamada durante la última
   parte del *apagado del intérprete* cuando las variables globales
   del módulo (globals) están sujetos a ser reemplazados por "None".

   __call__()

      Si *self* está vivo entonces lo marca como muerto y retorna el
      resultado de llamar a "func(*args, **kwargs)".  Si *self* está
      muerto entonces retorna "None".

   detach()

      Si *self* está vivo entonces lo marca como muerto y retorna la
      tupla "(obj, func, args, kwargs)".  Si *self* está muerto
      entonces retorna "None".

   peek()

      Si *self* está vivo entonces retorna la tupla "(obj, func, args,
      kwargs)".  Si *self* está muerto entonces retorna "None".

   alive

      Propiedad que es verdadera si el finalizador está vivo, caso
      contrario, falso.

   atexit

      Una propiedad booleana con permisos de escritura que por defecto
      es verdadero.  Cuando el programa sale, llama a todos los
      finalizadores vivos que queden para los cuales "atexit" es
      verdadero.  Ellos son llamados en el orden reverso de creación.

   Nota:

     Es importante asegurar que *func*, *args* y *kwargs* no sean
     dueños de ninguna referencia a *obj*, o directamente o
     indirectamente, ya que de otra manera *obj* nunca será
     recolectado por el recolector de basura.  En particular, *func*
     no debe ser un método vinculado de *obj*.

   Added in version 3.4.

class weakref.ReferenceType

   El objeto de tipo para objetos de referencias débiles.

class weakref.ProxyType

   El objeto de tipo para proxies de objetos que no son invocables.

class weakref.CallableProxyType

   El objeto de tipo para proxies de objetos invocables.

weakref.ProxyTypes

   Una secuencia que contiene todos los objetos de tipo para los
   proxies. Esto puede hacerlo más simple para pruebas si un objeto es
   un proxy sin ser dependiente en nombrar a ambos tipos proxy.

Ver también:

  **PEP 205** - Referencias Débiles
     La propuesta y lógica de esta característica, incluyendo los
     enlaces a implementaciones tempranas e información acerca de
     características similares en otros lenguajes.

## Objetos de referencias débiles

Los objetos de referencias débiles no tiene métodos y atributos aparte
de "ref.__calback__". Un objeto de referencia débil permite que el
referente sea obtenido, si todavía existe, al llamarlo:

>>> import weakref
>>> class Object:
...     pass
...
>>> o = Object()
>>> r = weakref.ref(o)
>>> o2 = r()
>>> o is o2
True

Si el referente no existe, llamar al objeto de referencia retorna
"None":

>>> del o, o2
>>> print(r())
None

Probar que un objeto de referencia débil está todavía con vida debe
ser hecho usando la expresión "ref() is not None".  Normalmente, el
código de aplicación que necesite usar un objeto de referencia debe
seguir este patrón:

   # r is a weak reference object
   o = r()
   if o is None:
       # referent has been garbage collected
       print("Object has been deallocated; can't frobnicate.")
   else:
       print("Object is still live!")
       o.do_something_useful()

Usar una prueba separada para "vivacidad" crea una condición de
carrera en aplicaciones con hilos; otro hilo puede hacer que una
referencia débil sea invalidada antes de que la referencia débil sea
llamada; El modismo mostrado arriba es seguro en aplicaciones con
hilos también como aplicaciones de un sólo hilo.

Versiones especializadas de objetos "ref" pueden ser creadas a través
de creación por subclase. Esto es usado en la implementación de
"WeakValueDictionary" para reducir la memoria elevada por cada entrada
en el mapeado.  Esto puede ser lo más útil para asociar información
adicional con un referencia, pero también puede ser usado para
insertar procesamiento adicional en llamadas para recuperar el
referente.

Este ejemplo muestra como una subclase de "ref" puede ser usado para
guardar información adicional sobre un objeto y afectar el valor que
se retorna cuando el referente es accedido:

   import weakref

   class ExtendedRef(weakref.ref):
       def __init__(self, ob, callback=None, /, **annotations):
           super().__init__(ob, callback)
           self.__counter = 0
           for k, v in annotations.items():
               setattr(self, k, v)

       def __call__(self):
           """Return a pair containing the referent and the number of
           times the reference has been called.
           """
           ob = super().__call__()
           if ob is not None:
               self.__counter += 1
               ob = (ob, self.__counter)
           return ob

## Ejemplo

Este simple ejemplo muestra como una aplicación puede usar objetos ID
para recuperar objetos que han sido visto antes.  Los ID de los
objetos pueden ser usados en otras estructuras de datos sin forzar que
los objetos permanezcan con vida, pero los objetos pueden aún pueden
ser recuperados por el ID si lo hacen.

   import weakref

   _id2obj_dict = weakref.WeakValueDictionary()

   def remember(obj):
       oid = id(obj)
       _id2obj_dict[oid] = obj
       return oid

   def id2obj(oid):
       return _id2obj_dict[oid]

## Objetos finalizadores

El principal beneficio de usar "finalize" es que hace simple registrar
una retrollamada sin necesitar preservar el objeto finalizador
retornado.  Por ejemplo

>>> import weakref
>>> class Object:
...     pass
...
>>> kenny = Object()
>>> weakref.finalize(kenny, print, "You killed Kenny!")
<finalize object at ...; for 'Object' at ...>
>>> del kenny
You killed Kenny!

El finalizador puede ser llamado directamente también.  Sin embargo,
el finalizador invocará la retrollamada como máximo una vez.

>>> def callback(x, y, z):
...     print("CALLBACK")
...     return x + y + z
...
>>> obj = Object()
>>> f = weakref.finalize(obj, callback, 1, 2, z=3)
>>> assert f.alive
>>> assert f() == 6
CALLBACK
>>> assert not f.alive
>>> f()                     # callback not called because finalizer dead
>>> del obj                 # callback not called because finalizer dead

Puedes de-registrar un finalizador usando su método "detach()". Esto
mata el finalizador y retorna los argumentos pasados al constructor
cuando fue creado.

>>> obj = Object()
>>> f = weakref.finalize(obj, callback, 1, 2, z=3)
>>> f.detach()
(<...Object object ...>, <function callback ...>, (1, 2), {'z': 3})
>>> newobj, func, args, kwargs = _
>>> assert not f.alive
>>> assert newobj is obj
>>> assert func(*args, **kwargs) == 6
CALLBACK

A menos que pongas el atributo "atexit" a "False", un finalizador será
llamado cuando el programa salga si todavía está con vida.  Por
ejemplo

   >>> obj = Object()
   >>> weakref.finalize(obj, print, "obj dead or exiting")
   <finalize object at ...; for 'Object' at ...>
   >>> exit()
   obj dead or exiting

## Comparando finalizadores con los métodos "__del__()"

Suponga que queremos crear una clase cuyas instancias representan
directorios temporales.  Los directorios deben ser eliminados con sus
contenidos cuando el primero de los siguiente eventos ocurre:

* el objeto es recolectado por el recolector de basura,

* el método "remove()" del objeto es llamado, o

* el programa sale.

Podemos intentar implementar la clase usando un método "__del__()"
como se muestra a continuación:

   class TempDir:
       def __init__(self):
           self.name = tempfile.mkdtemp()

       def remove(self):
           if self.name is not None:
               shutil.rmtree(self.name)
               self.name = None

       @property
       def removed(self):
           return self.name is None

       def __del__(self):
           self.remove()

A partir de Python 3.4, los métodos "__del__()" ya no impiden que los
ciclos de referencia sean recolectados como basura y las variables
globales del módulo (globals) ya no son forzados a "None" durante el
*apagado del intérprete*. Por lo tanto, este código debería funcionar
sin ningún problema en CPython.

Sin embargo, la gestión de métodos "__del__()" es notoriamente
específica a la implementación, ya que depende de detalles internos de
la implementación del recolector de basura del intérprete.

Una alternativa más robusta puede ser para definir un finalizador que
sólo hace referencia a funciones específicas y objetos que necesite,
en vez de tener acceso al estado completo del objeto:

   class TempDir:
       def __init__(self):
           self.name = tempfile.mkdtemp()
           self._finalizer = weakref.finalize(self, shutil.rmtree, self.name)

       def remove(self):
           self._finalizer()

       @property
       def removed(self):
           return not self._finalizer.alive

Definido así, nuestro finalizador sólo recibe una referencia a los
detalles que necesita limpiar los directorios apropiadamente. Si el
objeto nueva llega a ser recolectado como basura el finalizador aún
será llamado al salir.

La otra ventaja de weakref basados en finalizadores es que ellos
pueden ser usados para registrar finalizadores para clases donde la
definición es controlado por terceros, como un código que corre cuando
un módulo es descargado:

   import weakref, sys
   def unloading_module():
       # implicit reference to the module globals from the function body
   weakref.finalize(sys.modules[__name__], unloading_module)

Nota:

  Si creas un objeto finalizador en un hilo daemon sólo como el
  programa sale entonces hay la posibilidad de que el finalizador no
  llegue a ser llamado. Sin embargo, en un hilo daemonic
  "atexit.register()", "try: ... finally: ..." y "with: ..." no
  garantizan que la limpieza ocurra tampoco.
