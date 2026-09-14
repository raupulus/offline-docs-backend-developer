---
title: '"graphlib" --- Functionality to operate with graph-like structures'
source_url: https://docs.python.org/es/3
source_path: library/graphlib.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2760
---

# "graphlib" --- Functionality to operate with graph-like structures

**Código fuente:** Lib/graphlib.py

======================================================================

class graphlib.TopologicalSorter(graph=None)

   Provee una funcionalidad para ordenar topológicamente un grafo de
   nodos *hashable*.

   Un ordenamiento topológico es un ordenamiento lineal de los
   vértices en un grafo de modo que para cada arista dirigida u -> v
   desde el vértice u al vértice v, el vértice u viene antes del
   vértice v en el ordenamiento. Por ejemplo, los vértices del grafo
   pueden representar tareas a realizar y las aristas pueden
   representar restricciones de que una tarea debe realizarse antes
   que otra; en este ejemplo, un ordenamiento topológico es solo una
   secuencia válida para las tareas. Es posible un ordenamiento
   topológico completo si y solo si el grafo no tiene ciclos
   dirigidos, es decir, si es un grafo acíclico dirigido.

   Si se proporciona el argumento opcional *graph*, este debe ser un
   diccionario que represente un grafo acíclico dirigido donde las
   claves son nodos y los valores son iterables de todos los
   predecesores de ese nodo en el grafo (los nodos que tienen las
   aristas que apuntan al valor clave). Se pueden agregar nodos
   adicionales al grafo utilizando el "add()" method.

   En el caso general, los pasos necesarios para realizar el
   ordenamiento de un grafo son los siguientes:

   * Cree una instancia "TopologicalSorter" con un grafo inicial
     opcional.

   * Agregue nodos adicionales al grafo.

   * Llame a "prepare()" en el grafo.

   * Mientras "is_active()" is "True", itere sobre los nodos
     retornados por "get_ready()" y procéselos . Llame a "done()" en
     cada nodo a medida que finaliza el procesamiento.

   En caso de que sólo se requiera una ordenación inmediata de los
   nodos del grafo y no haya paralelismo, se puede utilizar
   directamente el método de conveniencia
   "TopologicalSorter.static_order()".

      >>> graph = {"D": {"B", "C"}, "C": {"A"}, "B": {"A"}}
      >>> ts = TopologicalSorter(graph)
      >>> tuple(ts.static_order())
      ('A', 'C', 'B', 'D')

   La clase está diseñada para soportar fácilmente el procesamiento en
   paralelo de los nodos a medida que estén listos. Para la instancia:

      topological_sorter = TopologicalSorter()

      # Add nodes to 'topological_sorter'...

      topological_sorter.prepare()
      while topological_sorter.is_active():
          for node in topological_sorter.get_ready():
              # Worker threads or processes take nodes to work on off the
              # 'task_queue' queue.
              task_queue.put(node)

          # When the work for a node is done, workers put the node in
          # 'finalized_tasks_queue' so we can get more nodes to work on.
          # The definition of 'is_active()' guarantees that, at this point, at
          # least one node has been placed on 'task_queue' that hasn't yet
          # been passed to 'done()', so this blocking 'get()' must (eventually)
          # succeed.  After calling 'done()', we loop back to call 'get_ready()'
          # again, so put newly freed nodes on 'task_queue' as soon as
          # logically possible.
          node = finalized_tasks_queue.get()
          topological_sorter.done(node)

   add(node, *predecessors)

      Añade un nuevo nodo y sus predecesores al grafo. Tanto el *node*
      como todos los elementos de *predecessors* deben ser *hashable*.

      Si se llama varias veces con el mismo argumento del nodo, el
      conjunto de dependencias será la unión de todas las dependencias
      pasadas.

      Es posible añadir un nodo sin dependencias (no se proporciona
      *predecessors*) o proporcionar una dependencia dos veces. Si un
      nodo que no se ha proporcionado antes se incluye entre los
      *predecessors*, se añadirá automáticamente al grafo sin
      predecesores propios.

      Provoca "ValueError" si se llama después de "prepare()".

   prepare()

      Marca el grafo como terminado y comprueba si existen ciclos en
      el grafo. Si se detecta algún ciclo, se lanzará "CycleError",
      pero se puede seguir utilizando "get_ready()" para obtener
      tantos nodos como sea posible hasta que los ciclos bloqueen más
      el progreso. Después de una llamada a esta función, el grafo no
      puede ser modificado, y por lo tanto no se pueden añadir más
      nodos utilizando "add()".

      A "ValueError" will be raised if the sort has been started by
      "static_order()" or "get_ready()".

      Distinto en la versión 3.14: "prepare()" can now be called more
      than once as long as the sort has not started. Previously this
      raised "ValueError".

   is_active()

      Retorna "True" si se puede avanzar más y "False" en caso
      contrario. Se puede avanzar si los ciclos no bloquean la
      resolución y, o bien todavía existen nodos listos que aún no han
      sido retornados por "TopologicalSorter.get_ready()" o el número
      de nodos marcados con "TopologicalSorter.done()" es menor que el
      número que han sido retornados por
      "TopologicalSorter.get_ready()".

      El método "__bool__()" de esta clase defiere a esta función, por
      lo que en lugar de:

         if ts.is_active():
             ...

      es posible hacer simplemente:

         if ts:
             ...

      Lanzar "ValueError" si se llama sin llamar previamente a
      "prepare()".

   done(*nodes)

      Marca un conjunto de nodos retornados por
      "TopologicalSorter.get_ready()" como procesados, desbloqueando
      cualquier sucesor de cada nodo en *nodes* para ser retornado en
      el futuro por una llamada a "TopologicalSorter.get_ready()".

      Lanza "ValueError" si algún nodo de *nodes* ya ha sido marcado
      como procesado por una llamada anterior a este método o si un
      nodo no fue añadido al grafo usando "TopologicalSorter.add()",
      si se llama sin llamar a "prepare()" o si el nodo aún no ha sido
      retornado por "get_ready()".

   get_ready()

      Retorna una "tupla" con todos los nodos que están listos.
      Inicialmente retorna todos los nodos sin predecesores, y una vez
      que éstos se marcan como procesados llamando a
      "TopologicalSorter.done()", las llamadas posteriores devolverán
      todos los nuevos nodos que tengan todos sus predecesores ya
      procesados. Una vez que no se puede avanzar más, se retornan
      tuplas vacías.

      Lanzar "ValueError" si se llama sin llamar previamente a
      "prepare()".

   static_order()

      Retorna un iterable de nodos en un ordenamiento topológico. El
      uso de este método no requiere llamar a
      "TopologicalSorter.prepare()" o "TopologicalSorter.done()". Este
      método es equivalente a:

         def static_order(self):
             self.prepare()
             while self.is_active():
                 node_group = self.get_ready()
                 yield from node_group
                 self.done(*node_group)

      El orden concreto que se retorna puede depender del orden
      específico en que se insertaron los elementos en el grafo. Por
      ejemplo:

         >>> ts = TopologicalSorter()
         >>> ts.add(3, 2, 1)
         >>> ts.add(1, 0)
         >>> print([*ts.static_order()])
         [2, 0, 1, 3]

         >>> ts2 = TopologicalSorter()
         >>> ts2.add(1, 0)
         >>> ts2.add(3, 2, 1)
         >>> print([*ts2.static_order()])
         [0, 2, 1, 3]

      Esto se debe a que "0" y "2" están en el mismo nivel en el
      gráfico (habrían sido retornados en la misma llamada a
      "get_ready()") y el orden entre ellos está determinado por el
      orden de inserción.

      Si se detecta algún ciclo, se lanzará "CycleError".

   Added in version 3.9.

## Excepciones

The "graphlib" module defines the following exception classes:

exception graphlib.CycleError

   Subclase de "ValueError" planteada por
   "TopologicalSorter.prepare()" si existen ciclos en el grafo de
   trabajo. Si existen múltiples ciclos, sólo se informará de una
   elección indefinida entre ellos y se incluirá en la excepción.

   Se puede acceder al ciclo detectado a través del segundo elemento
   del atributo "args" de la instancia de la excepción y consiste en
   una lista de nodos, tal que cada nodo este, en el grafo, un
   predecesor inmediato del siguiente nodo en la lista. En la lista
   reportada, el primer y el último nodo serán el mismo, para dejar
   claro que es cíclico.
