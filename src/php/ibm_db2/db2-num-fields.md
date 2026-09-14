---
title: db2_num_fields
description: Devuelve el número de campos contenido en el conjunto de resultados
source_url: https://www.php.net/manual/es/function.db2-num-fields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-num-fields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30950
---

db2_num_fields

Devuelve el número de campos contenido en el conjunto de resultados

## Descripción

```php
db2_num_fields(resource $stmt): int
```php

Devuelve el número de campos contenidos en el conjunto de resultados. Esta función es muy útil cuando se gestionan conjuntos de resultados devueltos por consultas generadas dinámicamente o para conjuntos de resultados devueltos por procedimientos de registro, donde la aplicación no puede hacer otra cosa para obtener y utilizar estos resultados.

## Parámetros

`stmt`  
Un recurso válido que contiene un conjunto de resultados.

## Valores devueltos

Devuelve un entero que representa el número de campos en el conjunto de resultados asociado con el recurso especificado. Devuelve `false` si el recurso no es válido.

## Ejemplos

Ejemplo con `db2_num_fields`

El siguiente ejemplo demuestra cómo obtener el número de campos devueltos en el conjunto de resultados.

```
<?php

$sql = "SELECT id, nom, race, poids FROM animales ORDER BY race";
$stmt = db2_prepare($conn, $sql);
db2_execute($stmt, $sql);
$columns = db2_num_fields($stmt);

echo "Hay {$columns} columnas en el conjunto de resultados.";
?>

   
```php

El ejemplo anterior mostrará:

    Hay 4 columnas en el conjunto de resultados.

## Véase también

db2_execute

db2_field_display_size

db2_field_name

db2_field_num

db2_field_precision

db2_field_scale

db2_field_type

db2_field_width
