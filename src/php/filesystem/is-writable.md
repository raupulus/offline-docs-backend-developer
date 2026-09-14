---
title: is_writable
description: Indica si un fichero es accesible en escritura
source_url: https://www.php.net/manual/es/function.is-writable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/is-writable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: fccc7eb70
order: 23800
---

is_writable

Indica si un fichero es accesible en escritura

## Descripción

```php
is_writable(string $filename): bool
```php

devuelve `true` si `filename` existe y es accesible en escritura. El argumento puede ser el nombre de un directorio, permitiendo así verificar si el directorio es accesible en escritura.

No se olvide que PHP accede a los ficheros con los mismos permisos que el usuario que ejecuta el servidor web (a menudo, es '`nobody`', nadie).

## Parámetros

`filename`  
El nombre del fichero a verificar.

## Valores devueltos

Devuelve `true` si el fichero `filename` existe y es accesible en escritura.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Ejemplo con `is_writable`

```
<?php
$filename = 'test.txt';
if (is_writable($filename)) {
    echo 'El fichero es accesible en escritura.';
} else {
    echo 'El fichero no es accesible en escritura !';
}
?>

    
```php

## Notas

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`is_readable`, `file_exists`, `fwrite`
