---
title: posix_access
description: Determinar la accesibilidad de un archivo
source_url: https://www.php.net/manual/es/function.posix-access.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-access.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_revision: 8d417bd83
order: 65100
---

posix_access

Determinar la accesibilidad de un archivo

## Descripción

```php
posix_access(string $filename, [int $flags]): bool
```php

`posix_access` verifica el permiso del usuario sobre un archivo.

## Parámetros

`filename`  
El nombre del archivo a ser probado.

`flags`  
Una máscara consistente de uno o más de los valores `POSIX_F_OK`, `POSIX_R_OK`, `POSIX_W_OK` y `POSIX_X_OK`.

`POSIX_R_OK`, `POSIX_W_OK` y `POSIX_X_OK` solicitan que se verifique si el archivo existe y tiene permisos de lectura, escritura y ejecución, respectivamente. `POSIX_F_OK` simplemente verifica la existencia del archivo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `posix_access`

Este ejemplo verificará si el \$archivo puede leerse y escribirse, de lo contrario imprimirá un mensaje de error.

```
<?php

$archivo = 'algun_archivo';

if (posix_access($archivo, POSIX_R_OK | POSIX_W_OK)) {
    echo '¡El archivo puede leerse y escribirse!';

} else {
    $error = posix_get_last_error();

    echo "Error $error: " . posix_strerror($error);
}

?>

    
```php

## Véase también

`posix_get_last_error`, `posix_strerror`
