---
title: La clase parallel\Runtime
source_url: https://www.php.net/manual/es/class.parallel-runtime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parallel/parallel.runtime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parallel
translation_status: ready
translation_reviewed: false
translation_revision: 57c7669a1
order: 60330
---

## Objetos de ejecución

Cada ejecución representa un solo thread PHP, el thread es creado (e inicializado) durante la construcción. El thread espera luego a que se programen tareas: las tareas programadas serán ejecutadas FIFO y luego el thread volverá a esperar hasta que se programen otras tareas, o hasta que sea cerrado, eliminado o destruido por las reglas de ámbito normales de los objetos PHP.

> [!WARNING]
> Cuando una ejecución es destruida por las reglas de ámbito normales de los objetos PHP, primero ejecutará todas las tareas que han sido programadas, y bloqueará durante este tiempo.

## Amortiguación de ejecución

Cuando se crea una nueva ejecución, no comparte código con el thread (o el proceso) que la creó. Esto significa que no tiene las mismas clases y funciones cargadas, ni el mismo cargador automático definido. En algunos casos, una ejecución muy ligera es deseable porque las tareas que serán programadas no necesitan acceder al código del thread padre. En los casos en que las tareas necesitan acceder al mismo código, basta con definir un cargador automático como amortiguación.

> [!NOTE]
> La precarga puede ser utilizada en conjunción con parallel, en este caso el código precargado está disponible sin amortiguación.

## Sinopsis de la clase

parallel\Runtime

final

parallel\Runtime

Crear

Ejecutar

Unir
