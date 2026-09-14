---
title: getlastmod
description: Devuelve la fecha de última modificación de la página
source_url: https://www.php.net/manual/es/function.getlastmod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/getlastmod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 8dd14a886
order: 38960
---

getlastmod

Devuelve la fecha de última modificación de la página

## Descripción

```php
getlastmod(): int
```php

Devuelve la fecha de última modificación del script principal en ejecución.

Si se desea obtener la fecha de última modificación de un fichero diferente, se debe utilizar la función `filemtime`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la fecha de última modificación de la página. El valor devuelto es un timestamp UNIX, utilizable como argumento con la función `date`. Devuelve `false` en caso de error.

## Ejemplos

Ejemplo con `getlastmod`

```
<?php
// muestra por ejemplo 'Última modificación: April 20 2004 20:43:59.'
echo "Última modificación : " . date ("F d Y H:i:s.", getlastmod());
?>

    
```php

## Véase también

`date`, `getmyuid`, `getmygid`, `get_current_user`, `getmyinode`, `getmypid`, `filemtime`
