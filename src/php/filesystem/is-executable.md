---
title: is_executable
description: Indica si el fichero es ejecutable
source_url: https://www.php.net/manual/es/function.is-executable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/is-executable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 8d8cd43bf
order: 23750
---

is_executable

Indica si el fichero es ejecutable

## Descripción

```php
is_executable(string $filename): bool
```php

Indica si el fichero es ejecutable.

## Parámetros

`filename`  
Ruta de acceso al fichero.

## Valores devueltos

Devuelve `true` si el fichero existe y es ejecutable, `false` en caso contrario. En los sistemas POSIX, un fichero es ejecutable si el bit ejecutable de los permisos del fichero está definido. En Windows, véase la nota a continuación.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Ejemplo con `is_executable`

```
<?php

$file = '/home/vincent/somefile.sh';

if (is_executable($file)) {
    echo $file.' es ejecutable';
} else {
    echo $file.' no es ejecutable';
}

?>

    
```php

## Notas

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

> [!NOTE]
> En Windows, un fichero se considera ejecutable si es un fichero ejecutable propio según lo reportado por la API Win `GetBinaryType()`; por razones de retrocompatibilidad, los ficheros con extensión `.bat` o `.cmd` también se consideran ejecutables. Anterior a PHP 7.4.0, cualquier fichero no vacío con extensión `.exe` o `.com` se consideraba ejecutable. Cabe señalar que `PATHEXT` no es relevante para `is_executable`.

## Véase también

`is_file`, `is_link`
