---
title: is_readable
description: Indica si un fichero existe y es accesible en lectura
source_url: https://www.php.net/manual/es/function.is-readable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/is-readable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 871a231f4
order: 23780
---

is_readable

Indica si un fichero existe y es accesible en lectura

## Descripción

```php
is_readable(string $filename): bool
```php

Indica si un fichero existe y es accesible en lectura.

## Parámetros

`filename`  
Ruta hacia el fichero.

## Valores devueltos

Devuelve `true` si el fichero o el directorio especificado por `filename` existe y es accesible en lectura, `false` en caso contrario.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Ejemplo con `is_readable`

```
<?php
$filename = 'test.txt';
if (is_readable($filename)) {
    echo 'El fichero es accesible en lectura';
} else {
    echo 'El fichero no es accesible en lectura !';
}
?>

    
```php

## Notas

No se olvide que PHP accede a los ficheros con los mismos permisos que el usuario que ejecuta el servidor web (a menudo, es 'nobody', nadie).

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

> [!NOTE]
> La verificación se realiza utilizando el UID/GID real en lugar del efectivo.

Esta función puede devolver `true` para los directorios. Utilice la función `is_dir` para distinguir los ficheros y los directorios.

## Véase también

`is_writable`, `file_exists`, `fgets`
