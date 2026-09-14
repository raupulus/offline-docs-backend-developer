---
title: opendir
description: Abrir un manejador de directorio
source_url: https://www.php.net/manual/es/function.opendir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dir/functions/opendir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dir
translation_status: ready
translation_revision: 5c7e9e135
order: 12050
---

opendir

Abrir un manejador de directorio

## Descripción

```php
opendir(string $directory, [resource $context]): resource
```php

Abre un manejador de directorio para ser utilizado en llamadas posteriores a `closedir`, `readdir` y `rewinddir`.

## Parámetros

`directory`  
La ruta del directorio a abrir.

`context`  
Para una descripción del parámetro `context`, consulte [la sección de flujos](#ref.stream) del manual.

## Valores devueltos

Devuelve un manejador de directorio en caso de éxito, o `false` si ocurre un error

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

Esto puede ocurrir si `directory` no es un directorio válido, el directorio no puede abrirse debido a restricciones de permisos, o debido a errores del sistema de archivos.

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 8.0.0   | `context` ahora es nullable. |

## Ejemplos

Listar todas las entradas en un directorio, omitiendo los directorios especiales `.` y `..`

Dado que los nombres de archivos y directorios pueden ser strings que PHP considera "falsos" (por ejemplo, un directorio llamado `"0"`) y `readdir` devuelve `false` cuando ha leído todas las entradas en un directorio, se necesita usar el operador de `===` [comparación](#language.operators.comparison) para distinguir correctamente entre una entrada de directorio cuyo nombre es "falso" y haber leído todas las entradas del directorio.

```
<?php

if ($handle = opendir('/path/to/files')) {
    echo "Entradas:\n";

    /* Manejo correcto de las entradas de directorio que pueden ser consideradas falsas */
    while (false !== ($entry = readdir($handle))) {
        if ($entry === '.' || $entry === '..') {
            continue;
        }
        echo "$entry\n";
    }

    closedir($handle);
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Entradas:
    base
    en
    fr
    output.md
    test.php

## Véase también

readdir

rewinddir

closedir

dir

is_dir

glob

scandir
