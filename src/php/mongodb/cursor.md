---
title: La clase MongoDB\Driver\Cursor
source_url: https://www.php.net/manual/es/class.mongodb-driver-cursor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/cursor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: df78bd1d2
order: 49350
---

## Introducción

La clase `MongoDB\Driver\Cursor` encapsula los resultados de un comando o consulta de MongoDB y puede ser devuelta por MongoDB\Driver\Manager::executeCommand o MongoDB\Driver\Manager::executeQuery, respectivamente.

## Sinopsis de la clase

MongoDB\Driver\Cursor

final

MongoDB\Driver\Cursor

MongoDB\Driver\CursorInterface

Métodos

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 1.9.0 | Implementa Iterator. |
| PECL mongodb 1.6.0 | Implementa MongoDB\Driver\CursorInterface, que extiende Traversable. |

## Ejemplos

Lectura de un conjunto de resultados

MongoDB\Driver\Manager::executeCommand y MongoDB\Driver\Manager::executeQuery devuelven sus resultados como un objeto `MongoDB\Driver\Cursor`. Este objeto puede usarse para iterar sobre el conjunto de resultados del comando o consulta.

Dado que `MongoDB\Driver\Cursor` implementa la interfaz Traversable, puede simplemente iterar sobre el conjunto de resultados con [`foreach`](#control-structures.foreach).

```php
<?php

$manager = new MongoDB\Driver\Manager();

/* Insertar algunos documentos para que nuestra consulta devuelva información */
$bulkWrite = new MongoDB\Driver\BulkWrite;
$bulkWrite->insert(['name' => 'Ceres', 'size' => 946, 'distance' => 2.766]);
$bulkWrite->insert(['name' => 'Vesta', 'size' => 525, 'distance' => 2.362]);
$manager->executeBulkWrite("test.asteroids", $bulkWrite);

/* Consultar todos los elementos de la colección */
$query = new MongoDB\Driver\Query( [] );

/* Consultar la colección "asteroids" de la base de datos "test" */
$cursor = $manager->executeQuery("test.asteroids", $query);

/* $cursor ahora contiene un objeto que envuelve el conjunto de resultados. Usar
 * foreach() para iterar sobre todos los resultados */
foreach($cursor as $document) {
    print_r($document);
}

?>

   
```

Resultado del ejemplo anterior es similar a:

    stdClass Object
    (
        [_id] => MongoDB\BSON\ObjectId Object
            (
                [oid] => 5a4cff2f122d3321565d8cc2
            )

        [name] => Ceres
        [size] => 946
        [distance] => 2.766
    )
    stdClass Object
    (
        [_id] => MongoDB\BSON\ObjectId Object
            (
                [oid] => 5a4cff2f122d3321565d8cc3
            )

        [name] => Vesta
        [size] => 525
        [distance] => 2.362
    )

Lectura de un conjunto de resultados para un cursor rastreable

Los [cursores rastreables](https://www.mongodb.com/docs/manual/core/tailable-cursors) son un tipo especial de cursor de MongoDB que permite al cliente leer algunos resultados y luego esperar hasta que haya más documentos disponibles. Estos cursores se usan principalmente con [colecciones limitadas](https://www.mongodb.com/docs/manual/core/capped-collections) y [flujos de cambios](https://www.mongodb.com/docs/manual/changeStreams).

Mientras que los cursores normales pueden iterarse una vez con `foreach`, ese enfoque no funcionará con cursores rastreables. Cuando se usa `foreach` con un cursor rastreable, el bucle terminará al llegar al final del conjunto de resultados inicial. Intentar continuar la iteración en el cursor con un segundo `foreach` lanzaría una excepción, ya que PHP intenta retroceder el cursor. Al igual que los objetos de resultado en otros controladores de bases de datos, los cursores en MongoDB solo admiten la iteración hacia adelante, lo que significa que no pueden retrocederse.

Para leer de forma continua desde un cursor rastreable, el objeto Cursor debe envolverse con un `IteratorIterator`. Esto permite que la aplicación controle directamente la iteración del cursor, evite retroceder el cursor sin querer y decida cuándo esperar nuevos resultados o detener completamente la iteración.

Para demostrar un cursor rastreable en acción, se usarán dos scripts: un "productor" y un "consumidor". El script productor creará una nueva colección limitada usando el comando [create](https://www.mongodb.com/docs/manual/reference/command/create) e insertará un nuevo documento en esa colección cada segundo.

```php
<?php

$manager = new MongoDB\Driver\Manager;

$manager->executeCommand('test', new MongoDB\Driver\Command([
    'create' => 'asteroids',
    'capped' => true,
    'size' => 1048576,
]));

while (true) {
    $bulkWrite = new MongoDB\Driver\BulkWrite;
    $bulkWrite->insert(['createdAt' => new MongoDB\BSON\UTCDateTime]);
    $manager->executeBulkWrite('test.asteroids', $bulkWrite);

    sleep(1);
}

?>

    
```

Con el script productor aún en ejecución, puede ejecutarse un segundo script consumidor para leer los documentos insertados usando un cursor rastreable, indicado por las opciones `tailable` y `awaitData` en `MongoDB\Driver\Query::__construct`.

```php
<?php

$manager = new MongoDB\Driver\Manager;

$query = new MongoDB\Driver\Query([], [
    'tailable' => true,
    'awaitData' => true,
]);

$cursor = $manager->executeQuery('test.asteroids', $query);

$iterator = new IteratorIterator($cursor);

$iterator->rewind();

while (true) {
    if ($iterator->valid()) {
        $document = $iterator->current();
        printf("Documento consumido creado en: %s\n", $document->createdAt);
    }

    $iterator->next();
}

?>

    
```

El script consumidor comenzará imprimiendo rápidamente todos los documentos disponibles en la colección limitada (como si se hubiera usado `foreach`); sin embargo, no terminará al llegar al final del conjunto de resultados inicial. Dado que el cursor es rastreable, llamar a `IteratorIterator::next` bloqueará y esperará resultados adicionales. `IteratorIterator::valid` también se usa para verificar si hay realmente datos disponibles para leer en cada paso.

> [!NOTE]
> Este ejemplo usa la opción de consulta `awaitData` para instruir al servidor que bloquee durante un breve período (por ejemplo, un segundo) al final del conjunto de resultados antes de devolver una respuesta al controlador. Esto se usa para evitar que el controlador consulte agresivamente al servidor cuando no hay resultados disponibles. La opción `maxAwaitTimeMS` puede usarse junto con `tailable` y `awaitData` para especificar la cantidad de tiempo que el servidor debe bloquearse cuando llega al final del conjunto de resultados.

## Errores/Excepciones

Al iterar sobre el objeto cursor, los datos BSON se convierten en variables PHP. Esta iteración puede causar las siguientes Excepciones:

Lanza

MongoDB\Driver\Exception\InvalidArgumentException

si una clase en el mapa de tipos no puede ser instanciada o no implementa

MongoDB\BSON\Unserializable

.

Lanza una excepción

MongoDB\Driver\Exception\UnexpectedValueException

si la entrada no contiene exactamente un documento BSON. Las razones posibles incluyen, pero no se limitan a, BSON inválido, datos adicionales (después de leer un documento BSON), o un error inesperado de

libbson

.
