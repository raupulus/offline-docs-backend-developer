---
title: Estructuras de datos
source_url: https://www.php.net/manual/es/spl.datastructures.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/datastructures.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: e93feee28
order: 81800
---

## Estructuras de datos

SPL proporciona un conjunto de estructuras de datos estándar. Estas están agrupadas por su implementación subyacente la cual usualmente define su campo de aplicación general.

## Listas doblemente enlazadas

Una Lista Doblemente Enlazada (DLL en inglés) es una lista de nodos enlazados entre ellos en ambas direcciones. Las operaciones de iteración, acceso a ambos extremos, adición o remoción de nodos tienen un costo de O(1) cuando la estructura subyacente es una DLL. Por lo tanto, proporciona una implementación decente para pilas y colas.

- `SplDoublyLinkedList`

  - `SplStack`

  - `SplQueue`

## Montículos

Los montículos son estructuras de árboles que siguen la propiedad de los montículos: cada nodo es mayor o igual que sus hijos, cuando son comparados utilizando el método de comparación implementado, el cual es global al montículo.

- `SplHeap`

  - `SplMaxHeap`

  - `SplMinHeap`

- `SplPriorityQueue`

## Arrays

Los array son estructuras que almacenan datos de una forma continua y accesible mediante índices.

> [!NOTE]
> No deben confundirse con los `array`s nativos de PHP. Los array de PHP son en realidad tablas hash ordenadas. Mientras que, SPL proporciona la clase `ArrayObject` que envuelven los arrays de PHP en un objeto.

- `SplFixedArray`

## Mapa

Un mapa es una estructura de datos que contiene parejas de clave-valor. Los array de PHP pueden ser vistos como correspondencias (mapas) de enteros/string a valores. SPL proporciona una correspondencia de objetos a datos. Este mapa puede ser utilizado además como un conjunto de objetos.

- `SplObjectStorage`
