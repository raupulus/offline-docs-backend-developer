---
title: glob
description: Búsqueda de rutas que coinciden con un patrón
source_url: https://www.php.net/manual/es/function.glob.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/glob.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: bb9bfdfc5
order: 23730
---

glob

Búsqueda de rutas que coinciden con un patrón

## Descripción

```php
glob(string $pattern, [int $flags]): array
```php

`glob` busca todas las rutas que coinciden con el patrón `pattern`, siguiendo las reglas utilizadas por la función `glob()` de la libc, que son las mismas que las utilizadas por el Shell en general.

El comportamiento en sistemas Unix y macOS está determinado por la implementación de glob() del sistema. En Windows, se utiliza una implementación conforme a la definición POSIX 1003.2 de glob(), con una extensión para manejar la convención `[!...]` que permite negar un rango.

## Parámetros

`pattern`  
El patrón. No se realiza sustitución de tilde (`~`) ni de parámetro.

Caracteres especiales:

- `*` - Asocia cero o más caracteres.

- `?` - Asocia exactamente un carácter (cualquier carácter).

- `[...]` - Asocia un carácter de un conjunto de caracteres. Si el primer carácter es `!`, asocia cualquier carácter que no esté en este conjunto.

- `{a,b,c}` - Asocia una cadena de un grupo de cadenas separadas por comas cuando se utiliza el flag `GLOB_BRACE`.

- `\` - Escapa el carácter siguiente, excepto cuando se utiliza el flag `GLOB_NOESCAPE`.

`flags`  
Cualquiera de las constantes `GLOB_*`.

## Valores devueltos

Devuelve un array que contiene los ficheros y directorios que coinciden con el patrón, un array vacío si no hay coincidencias, o `false` si ocurre un error. A menos que se utilice `GLOB_NOSORT`, los nombres serán ordenados alfabéticamente.

## Ejemplos

Un método práctico para reemplazar `opendir` por `glob`

```
<?php
foreach (glob("*.txt") as $filename) {
    echo "$filename ocupa " . filesize($filename) . "\n";
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    funclist.txt ocupa 44686
    funcsummary.txt ocupa 267625
    quickref.txt ocupa 137820

Ejemplo con un patrón más complejo

```
<?php
foreach (glob("path/*/*.{txt,md}", \GLOB_BRACE) as $filename) {
    echo "$filename\n";
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    path/docs/mailinglist-rules.md
    path/docs/README.md
    path/docs/release-process.md
    path/pear/install-pear.txt
    path/Zend/README.md

## Notas

> [!NOTE]
> Esta función no funciona con los [archivos remotos](#features.remote-files), ya que el archivo examinado debe ser accesible en el sistema de archivos del servidor.

> [!NOTE]
> Esta función no está disponible en algunos sistemas (por ejemplo, viejos Sun OS).

## Véase también

`opendir`, `readdir`, `closedir`, `fnmatch`
