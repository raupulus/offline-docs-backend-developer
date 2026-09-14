---
title: tidy::parseFile
description: Analiza las etiquetas de un fichero o de una URI
source_url: https://www.php.net/manual/es/tidy.parsefile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/parsefile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: true
translation_revision: 8bcc6238e
order: 94130
---

tidy::parseFile

tidy_parse_file

Analiza las etiquetas de un fichero o de una URI

## Descripción

Estilo orientado a objetos

```php
public tidy::parseFile(string $filename, [array $config], [string $encoding], [bool $useIncludePath]): bool
```php

Estilo procedimental

```php
tidy_parse_file(string $filename, [array $config], [string $encoding], [bool $useIncludePath]): tidy
```

Analiza el fichero especificado.

## Parámetros

`filename`  
Si el parámetro `filename` es proporcionado, esta función también leerá este fichero e inicializará el objeto con este fichero, de la misma manera que `tidy_parse_file`.

`config`  
La configuración `config` puede ser pasada en forma de `array` o de `string`. Si una `string` es pasada, es interpretada como el nombre del fichero de configuración, y de lo contrario, es interpretada como las opciones mismas.

Para una explicación sobre cada opción, vea <http://api.html-tidy.org/#quick-reference>.

`encoding`  
El parámetro `encoding` configura la codificación para los documentos de entrada y salida. Los valores posibles son `ascii`, `latin0`, `latin1`, `raw`, `utf8`, `iso2022`, `mac`, `win1252`, `ibm858`, `utf16`, `utf16le`, `utf16be`, `big5` y `shiftjis`.

`useIncludePath`  
Activa la búsqueda en el [include_path](#ini.include-path).

## Valores devueltos

tidy::parseFile devuelve `true` en caso de éxito. `tidy_parse_file` devuelve una nueva instancia de `tidy` en caso de éxito. Tanto el método como la función devuelven `false` en caso de error.

## Historial de cambios

| Versión | Descripción                               |
|---------|-------------------------------------------|
| 8.0.0   | `config` y `encoding` son ahora nullable. |

## Ejemplos

Ejemplo con `tidy::parseFile`

```php
<?php
$tidy = tidy_parse_file('file.html');

$tidy->cleanRepair();

if(!empty($tidy->error_buf)) {
   echo 'Los siguientes errores y advertencias han sido encontrados :'."\n";
   echo $tidy->error_buf;
}
?>

    
```

## Véase también

tidy::parseString

tidy::repairFile

tidy::repairString
