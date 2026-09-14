---
title: scandir
description: Lista los ficheros y directorios en un directorio
source_url: https://www.php.net/manual/es/function.scandir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dir/functions/scandir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dir
translation_status: ready
translation_reviewed: false
translation_revision: 3f63f2b26
order: 12080
---

scandir

Lista los ficheros y directorios en un directorio

## Descripción

```php
scandir(string $directory, [int $sorting_order], [resource $context]): array
```php

Devuelve un `array` de ficheros y directorios provenientes de `directory`.

## Parámetros

`directory`  
El directorio que será analizado.

`sorting_order`  
Por omisión, el orden es alfabético ascendente. Si el parámetro opcional `sorting_order` es definido a `SCANDIR_SORT_DESCENDING`, entonces el orden será alfabético descendente. Si este parámetro es definido a `SCANDIR_SORT_NONE`, entonces el resultado no será ordenado.

`context`  
Para una descripción del parámetro `context`, consulte la [sección flujo de datos](#ref.stream) del manual.

## Valores devueltos

Devuelve un `array` de nombres de ficheros en caso de éxito o `false` en caso de fallo. Si `directory` no es un directorio, entonces se devuelve un valor booleano `false` y se genera un error de nivel `E_WARNING`.

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 8.0.0   | `context` ahora es nullable. |

## Ejemplos

Un simple ejemplo con `scandir`

```
<?php
$dir    = '/tmp';
$files1 = scandir($dir);
$files2 = scandir($dir, SCANDIR_SORT_DESCENDING);

print_r($files1);
print_r($files2);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => .
        [1] => ..
        [2] => bar.php
        [3] => foo.txt
        [4] => somedir
    )
    Array
    (
        [0] => somedir
        [1] => foo.txt
        [2] => bar.php
        [3] => ..
        [4] => .
    )

## Notas

> [!TIP]
> Puede utilizar una URL como nombre de archivo con esta función, si el [gestor fopen](#ini.allow-url-fopen) ha sido activado. Véase `fopen` para más detalles sobre cómo especificar el nombre del archivo. Consulte [???](#wrappers) para más información sobre las capacidades de los diferentes gestores, las notas sobre su uso, así como la información sobre las variables predefinidas que proporcionan.

## Véase también

`opendir`, `readdir`, `glob`, `is_dir`, `sort`
