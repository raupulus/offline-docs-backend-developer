---
title: yaz_ccl_parse
description: Invocar el analizador CCL
source_url: https://www.php.net/manual/es/function.yaz-ccl-parse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-ccl-parse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 22583751f
order: 107760
---

yaz_ccl_parse

Invocar el analizador CCL

## Descripción

```php
yaz_ccl_parse(resource $id, string $query, array $result): bool
```php

Esta función invoca un analizador CCL. Convierte una consulta dada CCL FIND a una consulta RPN la cual puede ser pasada también a la función `yaz_search` para ejecutar la búsqueda.

Para definir un conjunto de campos validos CCL llaman preferiblemente a `yaz_ccl_conf` para definirlo en la función.

## Parámetros

`id`  
El recurso de la conexión retornado por `yaz_connect`.

`query`  
La consulta CCL FIND.

`result`  
Si la función fue ejecutada con éxito, Va a ser un arreglo conteniendo la consulta RPN valida dentro de la clave `rpn`.

En caso de fallo, tres índices son establecidos en este arreglo para indicar la causa del fallo:

- `errorcode` - El código de error CCL (entero)

- `errorstring` - El error CCL de cadena

- `errorpos` - aproxima la posición en una consulta de fallo (el entero es el carácter de posición)

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Análisis CCL

Se va a intentar hacer una búsqueda con CCL. En el ejemplo de abajo, `$ccl` es una consulta CCL.

```
<?php

yaz_ccl_conf($id, $fields);  // ver el ejemplo para yaz_ccl_conf
if (!yaz_ccl_parse($id, $ccl, $cclresult)) {
    echo 'Error: ' . $cclresult["errorstring"];
} else {
    $rpn = $cclresult["rpn"];
    yaz_search($id, "rpn", $rpn);
}
?>

   
```php
