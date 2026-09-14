---
title: Ejemplos
source_url: https://www.php.net/manual/es/mysql-xdevapi.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 8deee9585
order: 52550
---

## Ejemplos

El punto de entrada central de la API X es la función `mysql_xdevapi\getSession`, que recibe una URI hacia un servidor MySQL 8.0 y devuelve un objeto `mysql_xdevapi\Session`.

Conectar a un Servidor MySQL

```php
<?php
try {
    $session = mysql_xdevapi\getSession("mysqlx://user:password@host");
} catch(Exception $e) {
    die("La conexión no pudo ser establecida: " . $e->getMessage());
}

// ... usar $session
?>

  
```

La sesión proporciona acceso completo a la API. Para una nueva instalación de servidor MySQL, el primer paso es crear un esquema de base de datos con una colección para almacenar datos:

Crear un Esquema y una Colección en el Servidor MySQL

```php
<?php
$schema = $session->createSchema("test");
$collection = $schema->createCollection("example");
?>

  
```

Al almacenar datos, generalmente `json_encode` se utiliza para codificar los datos en JSON, que luego pueden ser almacenados en una colección.

Los siguientes ejemplos almacenan datos en la colección que hemos creado anteriormente, y luego recuperan partes de estos datos nuevamente.

Almacenar y Recuperar Datos

```php
<?php
$marco = [
  "name" => "Marco",
  "age"  => 19,
  "job"  => "Programmer"
];
$mike = [
  "name" => "Mike",
  "age"  => 39,
  "job"  => "Manager"
];

$schema = $session->getSchema("test");
$collection = $schema->getCollection("example");

$collection->add($marco, $mike)->execute();

var_dump($collection->find("name = 'Mike'")->execute()->fetchOne());
?>

  
```

Resultado del ejemplo anterior es similar a:

       
    array(4) {
      ["_id"]=>
      string(28) "00005ad66aaf0000000000000003"
      ["age"]=>
      int(39)
      ["job"]=>
      string(7) "Manager"
      ["name"]=>
      string(4) "Mike"
    }

Este ejemplo demuestra que el servidor MySQL añade un campo adicional llamado `_id`, que sirve como clave primaria del documento.

Este ejemplo también demuestra que los datos recuperados están ordenados alfabéticamente. Este orden específico proviene del almacenamiento binario eficiente dentro del servidor MySQL, pero no debe confiarse en él. Consulte la documentación del tipo de datos JSON de MySQL para más detalles.

Opcionalmente, utilice los iteradores de PHP para recuperar múltiples documentos:

Recuperar e Iterar sobre Múltiples Documentos

```php
<?php
$result = $collection->find()->execute();
foreach ($result as $doc) {
  echo "{$doc["name"]} es un {$doc["job"]}.\n";
}
?>

  
```

Resultado del ejemplo anterior es similar a:

       
    Marco es un Programmer.
    Mike es un Manager.
