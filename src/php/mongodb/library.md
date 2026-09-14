---
title: Utilizar la biblioteca PHP para MongoDB (PHPLIB)
source_url: https://www.php.net/manual/es/mongodb.tutorial.library.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/tutorial/library.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 51780
---

## Utilizar la biblioteca PHP para MongoDB (PHPLIB)

Después de la configuración inicial de la extensión, se continuará explicando cómo comenzar con la biblioteca de usuario correspondiente para escribir nuestro primer proyecto.

## Instalar la biblioteca PHP con Composer

La última cosa que se debe instalar para comenzar la aplicación en sí es la biblioteca PHP.

La biblioteca debe ser instalada con [Composer](https://getcomposer.org/), un gestor de paquetes para PHP. Las instrucciones para instalar Composer en diferentes plataformas pueden encontrarse en su sitio web.

Instalar la biblioteca ejecutando:

```php
$ composer require mongodb/mongodb

    
```

Esto producirá una salida similar a:

```php
./composer.json has been created
Loading composer repositories with package information
Updating dependencies (including require-dev)
  - Installing mongodb/mongodb (1.0.0)
    Downloading: 100%

Writing lock file
Generating autoload files

    
```

Composer creará varios ficheros: `composer.json`, `composer.lock`, y un directorio `vendor` que contendrá la biblioteca y todas las otras dependencias que su proyecto podría necesitar.

## Utilizar la biblioteca PHP

Además de gestionar sus dependencias, Composer también le proporcionará un autocargador (para las clases de estas dependencias). Asegúrese de que esté incluido al inicio de su script o en el código de arranque de su aplicación:

```php
<?php
// Esta ruta debe apuntar al autocargador de Composer
require 'vendor/autoload.php';

    
```

Con esto hecho, ahora puede utilizar cualquier funcionalidad como se describe en la [documentación de la biblioteca](https://www.mongodb.com/docs/php-library/current/).

Si ha utilizado controladores MongoDB en otros lenguajes, la API de la biblioteca debería resultarle familiar. Contiene una clase [Client](https://www.mongodb.com/docs/php-library/current/reference/class/MongoDBClient/) para conectarse a MongoDB, una clase [Database](https://www.mongodb.com/docs/php-library/current/reference/class/MongoDBDatabase/) para las operaciones a nivel de la base de datos (por ejemplo, los comandos, la gestión de las colecciones), y una clase [Collection](https://www.mongodb.com/docs/php-library/current/reference/class/MongoDBCollection) para las operaciones a nivel de la colección (por ejemplo, los métodos [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete), la gestión de los índices).

Como ejemplo, aquí se muestra cómo insertar un documento en la colección *beers* de la base de datos *demo*:

```php
<?php
require 'vendor/autoload.php'; // incluir el autocargador de Composer

$client = new MongoDB\Client("mongodb://localhost:27017");
$collection = $client->demo->beers;

$result = $collection->insertOne( [ 'name' => 'Hinterland', 'brewery' => 'BrewDog' ] );

echo "Inserted with Object ID '{$result->getInsertedId()}'";
?>

    
```

Dado que el documento insertado no contenía un campo `_id`, la extensión generará un `MongoDB\BSON\ObjectId` para que el servidor lo utilice como `_id`. Este valor también está disponible para el llamador a través del objeto de resultado devuelto por el método `insertOne`.

Después de la inserción, se pueden consultar los datos que acaba de insertar. Para ello, se utiliza el método `find`, que devuelve un cursor iterable:

```php
<?php
require 'vendor/autoload.php'; // incluir el autocargador de Composer

$client = new MongoDB\Client("mongodb://localhost:27017");
$collection = $client->demo->beers;

$result = $collection->find( [ 'name' => 'Hinterland', 'brewery' => 'BrewDog' ] );

foreach ($result as $entry) {
    echo $entry['_id'], ': ', $entry['name'], "\n";
}
?>

    
```

Aunque los ejemplos no lo muestran, los documentos BSON y los arrays son deserializados como clases especiales en la biblioteca por defecto. Estas clases extienden `ArrayObject` para facilidad de uso e implementan las interfaces MongoDB\BSON\Serializable y MongoDB\BSON\Unserializable de la extensión para garantizar que los valores conserven su tipo cuando se serializan nuevamente en BSON. Esto evita un inconveniente de la antigua extensión `mongo` donde los arrays podrían convertirse en documentos, y viceversa. Ver la especificación [???](#mongodb.persistence) para más información sobre cómo se convierten los valores entre PHP y BSON.
