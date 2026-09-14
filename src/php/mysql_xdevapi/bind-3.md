---
title: CollectionRemove::bind
description: Liga un valor a un argumento
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionremove.bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionremove/bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53390
---

CollectionRemove::bind

Liga un valor a un argumento

## Descripción

```php
public mysql_xdevapi\CollectionRemove::bind(array $placeholder_values): mysql_xdevapi\CollectionRemove
```php

Liga un argumento al espacio reservado en la condición de búsqueda de la operación de eliminación.

El espacio reservado tiene la forma :NAME donde ':' es un prefijo común que siempre debe existir antes de cualquier NAME donde NAME es el nombre del espacio reservado. El método bind acepta una lista de espacios reservados si varias entidades deben ser sustituidas en la condición de búsqueda de la operación de eliminación.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`placeholder_values`  
El valor del espacio reservado a sustituir en la condición de búsqueda. Se permiten varios valores y deben ser pasados en forma de un array de mapeos NOMBRE_ESPACIO_RESERVADO-\>VALOR_ESPACIO_RESERVADO.

## Valores devueltos

Un objeto CollectionRemove que puede ser utilizado para ejecutar el comando, o para añadir operaciones adicionales.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionRemove::bind`

```
<?php

$res = $coll->remove('age > :age_from and age < :age_to')->bind(['age_from' => 20, 'age_to' => 50])->limit(7)->execute();

?>

   
```php
