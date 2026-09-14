---
title: CollectionAdd::__construct
description: Constructor de CollectionAdd
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionadd.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionadd/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53140
---

CollectionAdd::\_\_construct

Constructor de CollectionAdd

## Descripción

```php
private mysql_xdevapi\CollectionAdd::__construct()
```php

Se utiliza para añadir un documento a una colección; se llama desde un objeto Collection.

## Parámetros

Esta función no contiene ningún parámetro.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionAdd::__construct`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema = $session->getSchema("addressbook");
$create = $schema->createCollection("people");

$collection = $schema->getCollection("people");

// Añade dos documentos
$collection
  ->add('{"name": "Fred",  "age": 21, "job": "Construction"}')
  ->execute();

$collection
  ->add('{"name": "Wilma", "age": 23, "job": "Teacher"}')
  ->execute();

// Añade dos documentos utilizando un solo objeto JSON
$result = $collection
  ->add(
    '{"name": "Bernie",
      "jobs": [{"title":"Cat Herder","Salary":42000}, {"title":"Father","Salary":0}],
      "hobbies": ["Sports","Making cupcakes"]}',
    '{"name": "Jane",
      "jobs": [{"title":"Scientist","Salary":18000}, {"title":"Mother","Salary":0}],
      "hobbies": ["Walking","Making pies"]}')
  ->execute();

// Recupera una lista de ID generados por el último add()
$ids = $result->getGeneratedIds();
print_r($ids);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => 00005b6b53610000000000000056
        [1] => 00005b6b53610000000000000057
    )

## Notas

> [!NOTE]
> Un identificador único \_id es generado por MySQL Server 8.0 o superior, como se demuestra en el ejemplo. El campo \_id debe ser definido manualmente si se utiliza MySQL Server 5.7.
