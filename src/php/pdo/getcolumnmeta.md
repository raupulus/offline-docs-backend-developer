---
title: PDOStatement::getColumnMeta
description: Devuelve las metadatos para una columna de un conjunto de resultados
source_url: https://www.php.net/manual/es/pdostatement.getcolumnmeta.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdostatement/getcolumnmeta.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_revision: 661e6858a
order: 62150
---

PDOStatement::getColumnMeta

Devuelve las metadatos para una columna de un conjunto de resultados

## Descripción

```php
public PDOStatement::getColumnMeta(int $column): array
```php

Recupera las metadatos para una columna de un conjunto de resultados en un array asociativo.

> [!WARNING]
> Algunos controladores pueden no implementar la función PDOStatement::getColumnMeta, ya que es opcional. Sin embargo, todos los [controladores PDO](#pdo.drivers) documentados en el manual implementan esta función.

## Parámetros

`column`  
El nombre de la columna en el conjunto de resultados.

## Valores devueltos

Devuelve un array asociativo que contiene los siguientes valores representando las metadatos para una columna:

| Nombre | Valor |
|----|----|
| `native_type` | El tipo nativo de PHP utilizado para representar el valor de la columna. |
| `driver:decl_type` | El tipo SQL utilizado para representar el valor de la columna en la base de datos. Si la columna del conjunto de resultados es el resultado de una función, este valor no es devuelto por la función PDOStatement::getColumnMeta. |
| `flags` | Cualquier flag definido para esta columna. |
| `name` | El nombre de esta columna, como es devuelto por la base de datos. |
| `table` | El nombre de la tabla de esta columna, tal como es devuelto por la base de datos. |
| `len` | La longitud de esta columna. Normalmente, `-1` para tipos distintos a los números decimales de punto flotante. |
| `precision` | La precisión numérica para esta columna. Normalmente, `0` para tipos distintos a los números decimales de punto flotante. |
| `pdo_type` | El tipo de esta columna como es representado por la constante [`PDO::PARAM_*`](#pdo.constants). |

Metadatos de una columna

Devuelve `false` si la columna solicitada no existe en el conjunto de resultados, o si no existe ningún conjunto de resultados.

## Ejemplos

Recuperación de las metadatos para una columna

El siguiente ejemplo muestra el resultado de la recuperación de las metadatos para una columna generada por una función (COUNT) en un controlador PDO_SQLITE.

```
<?php
$select = $DB->query('SELECT COUNT(*) FROM fruit');
$meta = $select->getColumnMeta(0);
var_dump($meta);
?>

    
```php

El ejemplo anterior mostrará:

    array(6) {
       ["native_type"]=>
       string(7) "integer"
       ["flags"]=>
          array(0) {
          }
       ["name"]=>
       string(8) "COUNT(*)"
       ["len"]=>
       int(-1)
       ["precision"]=>
       int(0)
       ["pdo_type"]=>
       int(2)
    }

## Véase también

PDOStatement::columnCount, PDOStatement::rowCount
