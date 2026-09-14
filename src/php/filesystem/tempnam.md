---
title: tempnam
description: Crea un fichero con un nombre único
source_url: https://www.php.net/manual/es/function.tempnam.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/tempnam.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: true
translation_revision: 17ebcd2ea
order: 24050
---

tempnam

Crea un fichero con un nombre único

## Descripción

```php
tempnam(string $directory, string $prefix): string
```php

Crea un fichero con un nombre único, con permisos de acceso 0600, en el directorio especificado. Si el directorio no existe o no es accesible en escritura, `tempnam` intentará crear un fichero en el directorio temporal del sistema, y devolverá la ruta completa de dicho fichero, incluyendo su nombre.

## Parámetros

`directory`  
El directorio en el que se creará el fichero temporal.

`prefix`  
El prefijo del fichero temporal generado.

> [!NOTE]
> Solo se utilizan los 63 primeros caracteres del prefijo, el resto se ignora. Windows utiliza únicamente los 3 primeros caracteres del prefijo.

## Valores devueltos

Devuelve un nuevo fichero temporal (con su ruta), o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El nombre de los archivos creados por `tempnam` ahora es 13 bytes más largo. La longitud total sigue dependiendo de la plataforma. |
| 7.1.0 | `tempnam` ahora emite un aviso al recurrir al directorio temporal del sistema. |

## Ejemplos

Ejemplo con `tempnam`

```
<?php
$tmpfname = tempnam("/tmp", "FOO");

$handle = fopen($tmpfname, "w");
fwrite($handle, "Escritura en el fichero temporal");
fclose($handle);

// procesamiento

unlink($tmpfname);
?>

    
```php

## Notas

> [!NOTE]
> Si PHP no puede crear un fichero en el directorio especificado por el argumento `directory`, intentará hacerlo en el directorio por defecto del sistema. En sistemas de archivos NTFS, esto también ocurre si el directorio `directory` contiene más de 65534 ficheros.

## Véase también

`tmpfile`, `sys_get_temp_dir`, `unlink`
