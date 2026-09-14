---
title: Collection::add
description: Añade un documento a la colección
source_url: https://www.php.net/manual/es/mysql-xdevapi-collection.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collection/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: f1e951b98
order: 52980
---

Collection::add

Añade un documento a la colección

## Descripción

```php
public mysql_xdevapi\Collection::add(mixed $document): mysql_xdevapi\CollectionAdd
```php

Desencadena la inserción del o de los documentos dados en la colección, y se admiten varias variantes de este método. Las opciones incluyen:

1.  Añadir un solo documento en forma de string JSON.

2.  Añadir un solo documento en forma de array como: `[ 'field' => 'value', 'field2' => 'value2' ... ]`

3.  Una mezcla de ambos, y varios documentos pueden ser añadidos en la misma operación.

## Parámetros

`document`  
Uno o varios documentos, y esto puede ser tanto JSON como un array de campos con sus valores asociados. No puede ser un array vacío.

El servidor MySQL genera automáticamente valores `_id` únicos para cada documento (recomendado), aunque esto también puede ser añadido manualmente. Este valor debe ser único, de lo contrario la operación de adición fallará.

## Valores devueltos

Una colección de objetos. Utilizar execute() para devolver un resultado que puede ser utilizado para consultar el número de elementos afectados, el número de advertencias generadas por la operación, o para recuperar una lista de identificadores generados para los documentos insertados.

## Ejemplos

Ejemplo de `mysql_xdevapi\Collection::add`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");
$session->sql("DROP DATABASE IF EXISTS addressbook")->execute();
$session->sql("CREATE DATABASE addressbook")->execute();

$schema = $session->getSchema("addressbook");
$create = $schema->createCollection("people");

$collection = $schema->getCollection("people");

// Añade dos documentos
$collection->add('{"name": "Fred",  "age": 21, "job": "Construction"}')->execute();
$collection->add('{"name": "Wilma", "age": 23, "job": "Teacher"}')->execute();

// Añade dos documentos utilizando un solo objeto JSON
$result = $collection->add(
  '{"name": "Bernie",
    "jobs": [{"title":"Cat Herder","Salary":42000}, {"title":"Father","Salary":0}],
    "hobbies": ["Sports","Making cupcakes"]}',
  '{"name": "Jane",
    "jobs": [{"title":"Scientist","Salary":18000}, {"title":"Mother","Salary":0}],
    "hobbies": ["Walking","Making pies"]}')->execute();

// Recupera una lista de identificadores generados a partir del último add()
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
