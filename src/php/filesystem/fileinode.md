---
title: fileinode
description: Lee el número de inodo del fichero
source_url: https://www.php.net/manual/es/function.fileinode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fileinode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 871a231f4
order: 23530
---

fileinode

Lee el número de inodo del fichero

## Descripción

```php
fileinode(string $filename): int
```php

Lee el número de inodo del fichero.

## Parámetros

`filename`  
Ruta de acceso al fichero.

## Valores devueltos

Devuelve el número de inodo del fichero, o `false` si ocurre un error.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Comparación del inodo de un fichero con el fichero actual

```
<?php
$filename = 'index.php';
if (getmyinode() == fileinode($filename)) {
    echo 'Se verifica el fichero actual.';
}
?>

    
```php

## Notas

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`getmyinode`, `stat`
