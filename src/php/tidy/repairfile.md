---
title: tidy::repairFile
description: Repara un archivo y lo devuelve como una cadena
source_url: https://www.php.net/manual/es/tidy.repairfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/repairfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 2b84fa46e
order: 94150
---

tidy::repairFile

tidy_repair_file

Repara un archivo y lo devuelve como una cadena

## Descripción

Estilo orientado a objetos

```php
public static tidy::repairFile(string $filename, [array $config], [string $encoding], [bool $useIncludePath]): string
```php

Estilo procedimental

```php
tidy_repair_file(string $filename, [array $config], [string $encoding], [bool $useIncludePath]): string
```

Repara un archivo dado y devuelve el resultado como una cadena.

## Parámetros

`filename`  
El archivo a ser reparado.

`config`  
La configuración `config` puede ser pasada en forma de un array o una cadena. Si una cadena es pasada, será interpretada como el el nombre del archivo de configuración, de otra forma, será interpretada como opciones en sí mismas.

Revise http://tidy.sourceforge.net/docs/quickref.html para una explicación detallada de cada opción.

`encoding`  
El parámetro `encoding` establece la codificación para entarda/salida de los documentos. Los posibles valores de codificación son: `ascii`, `latin0`, `latin1`, `raw`, `utf8`, `iso2022`, `mac`, `win1252`, `ibm858`, `utf16`, `utf16le`, `utf16be`, `big5`, y `shiftjis`.

`useIncludePath`  
Búsca el archivo en la ruta [include_path](#ini.include-path).

## Valores devueltos

Devuelve el contenido reparado como una cadena, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                                   |
|---------|-----------------------------------------------|
| 8.0.0   | tidy::repairFile es un método estático ahora. |
| 8.0.0   | `config` y `encoding` son anulables ahora.    |

## Ejemplos

Ejemplo de `tidy::repairFile`

```php
<?php
$file = 'file.html';

$tidy = new tidy();
$repaired = $tidy->repairfile($file);
rename($file, $file . '.bak');

file_put_contents($file, $repaired);
?>

    
```

## Véase también

tidy::parseFile

tidy::parseString

tidy::repairString
