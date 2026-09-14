---
title: La clase SplQueue
source_url: https://www.php.net/manual/es/class.splqueue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splqueue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: 4d17b7b49
order: 85470
---

## Introducción

La clase SplQueue proporciona las principales funcionalidades de una cola implementada usando una lista doblemente enlazada al estableciendo el modo del iterador a `SplDoublyLinkedList::IT_MODE_FIFO`.

## Sinopsis de la clase

SplQueue

extends

SplDoublyLinkedList

Constantes heredadas

Métodos

Métodos heredados

## Ejemplos

`SplQueue` ejemplo

```php
<?php
$q = new SplQueue();
$q[] = 1;
$q[] = 2;
$q[] = 3;
foreach ($q as $elem)  {
 echo $elem."\n";
}
?>

     
```

El ejemplo anterior mostrará:

          
    1
    2
    3

Gestión eficiente de tareas con `SplQueue`

```php
<?php
$q = new SplQueue();
$q->setIteratorMode(SplQueue::IT_MODE_DELETE);
// ... enqueue some tasks on the queue ...
// process them
foreach ($q as $task) {
    // ... process $task ...
    // add new tasks on the queue
    $q[] = $newTask;
    // ...
}
?>

     
```
