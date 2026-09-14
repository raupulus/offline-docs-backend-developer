---
title: RarEntry::extract
description: Extraer entrada del archivo
source_url: https://www.php.net/manual/es/rarentry.extract.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarentry/extract.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68500
---

RarEntry::extract

Extraer entrada del archivo

## Descripción

```php
public RarEntry::extract(string $dir, [string $filepath], [string $password], [bool $extended_data]): bool
```php

RarEntry::extract extrae los datos de entrada. Esto creará un nuevo archivo en el `dir` especificado con el mismo nombre que el nombre de la entrada, a menos que el segundo argumento sea especificado. Siga leyendo más abajo para obtener mayor información.

## Parámetros

`dir`  
Ruta al directorio donde los archivos deben ser extraídos. Este parámetro es considerado si y sólo si no es `filepath`. Si ambos parámetros están vacíos se intentará una extracción en el directorio actual.

`filepath`  
Ruta (relativa o absoluta) que contiene el directorio y el nombre del archivo extraído. Este parámetro anula los parámetros `dir` y el nombre del archivo original.

`password`  
La contraseña utilizada para cifrar esta entrada. Si la entrada no está cifrada, este valor no se utilizará y puede ser omitido. Si se omite este parámetro y la entrada está cifrada, la contraseña dada a `rar_open`, será utlizada. Si una contraseña incorrecta es dada, de forma explicita o implicita via `rar_open`, la comprobación CRC fallará y este método fallará y devolverá `false`. Si no se da la contraseña y se requiere una, este método fallará y devolverá `false`. Puede comprobar si una entrada está cifrada con RarEntry::isEncrypted.

`extended_data`  
Si `true`, información extendida tales como NTFS ACLs e información propietaria Unix será establecida en los archivos extraidos, siempre que esta esté presente en el archivo.

> [!WARNING]
> Antes de la versión 2.0.0, esta función no manejaba las rutas relativas correctamente. Utilice `realpath` como una solución.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL rar 3.0.0 | `extended_data` fue añadido. |
| PECL rar 3.0.0 | Soporte para archivos RAR con nombres de entrada que se repiten ya no es defectuoso |

## Ejemplos

Ejemplo de RarEntry::extract

```
<?php

$rar_file = rar_open('example.rar') or die("Failed to open Rar archive");

$entry = rar_entry_get($rar_file, 'Dir/file.txt') or die("Failed to find such entry");

$entry->extract('/dir/to'); // crear /dir/to/Dir/file.txt
$entry->extract(false, '/dir/to/new_name.txt'); // crear /dir/to/new_name.txt

?>

    
```php

¿Cómo extraer todos los archivos en archivo?:

```
<?php

/* ejemplo por Erik Jenssen también conocido como erix */

$filename = "foobar.rar";
$filepath = "/home/foo/bar/";

$rar_file = rar_open($filepath.$filename);
$list = rar_list($rar_file);
foreach($list as $file) {
    $entry = rar_entry_get($rar_file, $file);
    $entry->extract("."); // extraer el directorio actual
}
rar_close($rar_file);

?>

    
```php

## Véase también

RarEntry::getStream

rar://

wrapper
