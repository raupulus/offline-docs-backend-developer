---
title: posix_eaccess
description: Determina la accesibilidad de un fichero
source_url: https://www.php.net/manual/es/function.posix-eaccess.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-eaccess.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: true
translation_revision: 8d417bd83
order: 65120
---

posix_eaccess

Determina la accesibilidad de un fichero

## Descripción

```php
posix_eaccess(string $filename, [int $flags]): bool
```php

`posix_eaccess` verifica los permisos del usuario efectivo de un fichero.

## Parámetros

`filename`  
El nombre del fichero a probar.

`flags`  
Una máscara compuesta por una o más de las constantes `POSIX_F_OK`, `POSIX_R_OK`, `POSIX_W_OK` y `POSIX_X_OK`.

`POSIX_R_OK`, `POSIX_W_OK` y `POSIX_X_OK` solicitan respectivamente si el fichero existe y tiene permisos de lectura, escritura y ejecución. `POSIX_F_OK` solicita simplemente si el fichero existe.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Verifica el usuario/grupo efectivo para un fichero, difiriendo de `posix_access` que verifica el usuario/grupo real. |

## Ejemplos

Ejemplo de `posix_eaccess`

Este ejemplo verifica si el fichero \$file es legible y escribible, de lo contrario muestra un mensaje de error.

```
<?php

$file = 'some_file';

if (posix_eaccess($file, POSIX_R_OK | POSIX_W_OK)) {
    echo '¡El fichero se puede leer y escribir!';

} else {
    $error = posix_get_last_error();

    echo "Error $error: " . posix_strerror($error);
}

?>

     
```php

## Véase también

`posix_get_last_error`, `posix_strerror`, `posix_access`
