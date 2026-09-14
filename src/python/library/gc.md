---
title: '"gc" --- Garbage Collector interface'
source_url: https://docs.python.org/es/3
source_path: library/gc.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2710
---

# "gc" --- Garbage Collector interface

======================================================================

Este módulo proporciona una interfaz para el recolector de basura
opcional (recolector de basura cíclico generacional). Proporciona la
capacidad de deshabilitar el recolector, ajustar la frecuencia de
recolección y establecer opciones de depuración. También proporciona
acceso a objetos inaccesibles (*unreachables*) que el recolector
encontró pero no pudo liberar. Dado que el recolector de basura
complementa el conteo de referencias, que ya se utiliza en Python, es
posible desactivarlo siempre que se esté seguro de que el programa no
crea referencias cíclicas. La recolección automática se puede
desactivar llamando a "gc.disable()". Para depurar un programa con
fugas de memoria, se debe llamar a "gc.set_debug(gc.DEBUG_LEAK)". Se
debe tener en cuenta que la llamada anterior incluye
"gc.DEBUG_SAVEALL", lo que hace que los objetos recolectados se
guarden en *gc.garbage* para su inspección.

The "gc" module provides the following functions:

gc.enable()

   Habilita la recolección automática de basura.

gc.disable()

   Deshabilita la recolección automática de basura.

gc.isenabled()

   Retorna "True" si la recolección automática está habilitada.

gc.collect(generation=2)

   With no arguments, run a full collection.  The optional argument
   *generation* may be an integer specifying which generation to
   collect (from 0 to 2).  A "ValueError" is raised if the generation
   number is invalid. The sum of collected objects and uncollectable
   objects is returned.

   Las listas libres mantenidas para varios tipos incorporados son
   borradas cada vez que se ejecuta una recolección completa o una
   recolección de la generación más alta (2). No obstante, no todos
   los elementos de algunas listas libres pueden ser liberados,
   particularmente "float", debido a su implementación particular.

   El efecto de llamar a "gc.collect()" mientras el intérprete ya está
   realizando una recolección es indefinido.

   Distinto en la versión 3.14: "generation=1" performs an increment
   of collection.

   Distinto en la versión 3.14.5: "generation=1" performs collection
   of the middle generation.

gc.set_debug(flags)

   Establece las flags de depuración para la recolección de basura. La
   información de depuración se escribirá en "sys.stderr". A
   continuación se puede consultar una lista con las flags de
   depuración disponibles, que se pueden combinar mediante operaciones
   de bits para controlar la depuración.

gc.get_debug()

   Retorna las flags de depuración actualmente establecidas.

gc.get_objects(generation=None)

   Returns a list of all objects tracked by the collector, excluding
   the list returned. If *generation* is not "None", return only the
   objects tracked by the collector that are in that generation.

   Distinto en la versión 3.8: Se agregó el parámetro *generation*.

   Distinto en la versión 3.14: Generation 1 is removed

   Distinto en la versión 3.14.5: Generation 1 is reintroduced to
   maintain GC behavior from 3.13.

   Lanza un evento de auditoría "gc.get_objects" con el argumento
   "generation".

gc.get_stats()

   Retorna una lista de tres diccionarios, uno por cada generación,
   que contienen estadísticas de recolección desde el inicio del
   intérprete. El número de claves puede cambiar en el futuro, pero
   actualmente cada diccionario contendrá los siguientes elementos:

   * "collections" es el número de veces que se recolectó esta
     generación;

   * "collected" es el número total de objetos recolectados dentro de
     esta generación;

   * "uncollectable" es el número total de objetos que se consideraron
     no recolectables (y por lo tanto, se movieron a la lista
     "garbage") dentro de esta generación.

   Added in version 3.4.

gc.set_threshold(threshold0[, threshold1[, threshold2]])

   Establece los umbrales de recolección (la frecuencia de
   recolección). Si se establece *threshold0* en cero se deshabilita
   la recolección.

   The GC classifies objects into three generations depending on how
   many collection sweeps they have survived.  New objects are placed
   in the youngest generation (generation "0").  If an object survives
   a collection it is moved into the next older generation.  Since
   generation "2" is the oldest generation, objects in that generation
   remain there after a collection.  In order to decide when to run,
   the collector keeps track of the number object allocations and
   deallocations since the last collection.  When the number of
   allocations minus the number of deallocations exceeds *threshold0*,
   collection starts.  Initially only generation "0" is examined.  If
   generation "0" has been examined more than *threshold1* times since
   generation "1" has been examined, then generation "1" is examined
   as well. With the third generation, things are a bit more
   complicated, see Collecting the oldest generation for more
   information.

   In the free-threaded build, the increase in process memory usage is
   also checked before running the collector.  If the memory usage has
   not increased by 10% since the last collection and the net number
   of object allocations has not exceeded 40 times *threshold0*, the
   collection is not run.

   See Garbage collector design for more information.

   Distinto en la versión 3.14: *threshold2* is ignored

   Distinto en la versión 3.14.5: *threshold2* is restored to match
   Python 3.13 behavior.

gc.get_count()

   Retorna los recuentos de la recolección actual como una tupla de la
   forma "(count0, count1, count2)".

gc.get_threshold()

   Retorna los umbrales de la recolección actual como una tupla de la
   forma "(threshold0, threshold1, threshold2)".

gc.get_referrers(*objs)

   Retorna la lista de objetos que referencian de forma directa a
   cualquiera de *objs*. Esta función solo localizará aquellos
   contenedores que admitan la recolección de basura; no se
   localizarán los tipos de extensión que referencian a otros objetos
   pero que no admiten la recolección de basura.

   Téngase en cuenta que los objetos que ya se han desreferenciado,
   pero que tienen referencias cíclicas y aún no han sido recolectados
   por el recolector de basura pueden enumerarse entre las referencias
   resultantes. Para obtener solo los objetos activos actualmente,
   llame a "collect()" antes de llamar a "get_referrers()".

   Advertencia:

     Se debe tener un especial cuidado cuando se usan objetos
     retornados por "get_referrers()" dado que algunos de ellos aún
     podrían estar en construcción y por tanto en un estado
     temporalmente inválido. Debe evitarse el uso de "get_referrers()"
     para cualquier propósito que no sea la depuración.

   Lanza un evento de auditoría "gc.get_referrers" con el argumento
   "objs".

gc.get_referents(*objs)

   Retorna una lista de objetos a los que hace referencia directamente
   cualquiera de los argumentos. Las referencias retornadas son
   aquellos objetos visitados por los métodos "tp_traverse" a nivel de
   C de los argumentos (si los hay) y es posible que no todos los
   objetos sean directamente accesibles realmente. Los métodos
   "tp_traverse" solo son compatibles con los objetos que admiten
   recolección de basura y solo se requieren para visitar objetos que
   pueden estar involucrados en un ciclo de referencias. Lo que quiere
   decir que, por ejemplo, si se puede acceder directamente a un
   número entero desde uno de los argumento, ese objeto entero puede
   aparecer o no en la lista de resultados.

   Lanza un evento de auditoría "gc.get_referents" con el argumento
   "objs".

gc.is_tracked(obj)

   Retorna "True" si el recolector de basura rastrea actualmente el
   objeto y "False" en caso contrario. Como regla general, las
   instancias de tipos atómicos no se rastrean y las instancias de
   tipos no atómicos (contenedores, objetos definidos por el usuario
   ...) sí. Sin embargo, algunas optimizaciones específicas de tipo
   pueden estar presentes para suprimir el impacto del recolector de
   basura en instancias simples (por ejemplo, diccionarios que
   contienen solo claves y valores atómicos):

      >>> gc.is_tracked(0)
      False
      >>> gc.is_tracked("a")
      False
      >>> gc.is_tracked([])
      True
      >>> gc.is_tracked({})
      False
      >>> gc.is_tracked({"a": 1})
      True

   Added in version 3.1.

gc.is_finalized(obj)

   Retorna "True" si el objeto dado ha sido finalizado por el
   recolector de basura, "False" en caso contrario.

      >>> x = None
      >>> class Lazarus:
      ...     def __del__(self):
      ...         global x
      ...         x = self
      ...
      >>> lazarus = Lazarus()
      >>> gc.is_finalized(lazarus)
      False
      >>> del lazarus
      >>> gc.is_finalized(x)
      True

   Added in version 3.9.

gc.freeze()

   Congela todos los objetos rastreados por el recolector de basura;
   los mueve a una generación permanente y los ignora en todas las
   recolecciones futuras.

   Si un proceso va a llamar a "fork()" sin llamar a "exec()", evitar
   la copia en escritura innecesaria en procesos secundarios
   maximizará el intercambio de memoria y reducirá el uso general de
   la memoria. Esto requiere tanto evitar la creación de "agujeros"
   liberados en las páginas de memoria del proceso principal y
   garantizar que las colecciones de GC en los procesos secundarios no
   tocarán el contador "gc_refs" de objetos de larga duración que se
   originan en el proceso principal. Para lograr ambas cosas, llame a
   "gc.disable()" al principio del proceso principal, a "gc.freeze()"
   justo antes de "fork()" y a "gc.enable()" al principio. en procesos
   secundarios.

   Added in version 3.7.

gc.unfreeze()

   Descongela los objetos de la generación permanente y vuelve a
   colocarlos en la generación más antigua.

   Added in version 3.7.

gc.get_freeze_count()

   Retorna el número de objetos de la generación permanente.

   Added in version 3.7.

Las siguientes variables se proporcionan para acceso de solo lectura
(se pueden mutar los valores pero no se deben vincular de nuevo):

gc.garbage

   Una lista de objetos que el recolector consideró inaccesibles pero
   que no pudieron ser liberados (objetos que no se pueden
   recolectar). A partir de Python 3.4, esta lista debe estar vacía la
   mayor parte del tiempo, excepto cuando se utilizan instancias de
   tipos de extensión C en los que la ranura (*slot*) "tp_del" no sea
   "NULL".

   Si se establece "DEBUG_SAVEALL", todos los objetos inaccesibles se
   agregarán a esta lista en lugar de ser liberados.

   Distinto en la versión 3.2: Si la lista no está vacía en el momento
   del *interpreter shutdown*, se emite un "ResourceWarning", que es
   silencioso de forma predeterminada. Si se establece
   "DEBUG_UNCOLLECTABLE", además se imprimen todos los objetos no
   recolectables.

   Distinto en la versión 3.4: Siguiendo con **PEP 442**, los objetos
   con un método "__del__()" ya no terminan en "gc.garbage".

gc.callbacks

   Una lista de retrollamadas que el recolector de basura invocará
   antes y después de la recolección. Las retrollamadas serán llamadas
   con dos argumentos, *phase* e *info*.

   *phase* puede tomar uno de estos valores:

      "start": la recolección de basura está a punto de comenzar.

      "stop": la recolección de basura ha terminado.

   *info* es un diccionario que proporciona información adicional para
   la retrollamada. Las siguientes claves están definidas actualmente:

      "generation": la generación más antigua que ha sido recolectada.

      "collected": cuando *phase* es "stop", el número de objetos
      recolectados satisfactoriamente.

      "uncollectable": cuando *phase* es "stop", el número de objetos
      que no pudieron ser recolectados y fueron ubicados en "garbage".

   Las aplicaciones pueden agregar sus propias retrollamadas a esta
   lista. Los principales casos de uso son:

      Recopilar estadísticas sobre la recolección de basura, como la
      frecuencia con la que se recolectan varias generaciones y cuánto
      tiempo lleva la recolección.

      Permitir que las aplicaciones identifiquen y borren sus propios
      tipos no recolectables cuando aparecen en "garbage".

   Added in version 3.3.

Las siguientes constantes son proporcionadas para ser usadas con
"set_debug()":

gc.DEBUG_STATS

   Imprime estadísticas durante la recolección. Esta información puede
   resultar útil para ajustar la frecuencia de recolección.

gc.DEBUG_COLLECTABLE

   Imprime información sobre los objetos recolectables encontrados.

gc.DEBUG_UNCOLLECTABLE

   Imprime información sobre los objetos no recolectables encontrados
   (objetos inaccesibles, pero que el recolector no puede liberar).
   Estos objetos se agregarán a la lista "garbage".

   Distinto en la versión 3.2: También imprime el contenido de la
   lista "garbage" durante *interpreter shutdown*, si no está vacía.

gc.DEBUG_SAVEALL

   Cuando se establece, todos los objetos inaccesibles encontrados se
   agregarán a *garbage* en lugar de ser liberados. Esto puede
   resultar útil para depurar un programa con fugas de memoria.

gc.DEBUG_LEAK

   Las flags de depuración necesarias para que el recolector imprima
   información sobre un programa con fugas de memoria (igual a
   "DEBUG_COLLECTABLE | DEBUG_UNCOLLECTABLE | DEBUG_SAVEALL").
