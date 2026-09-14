---
title: tidy::repairString
description: Repara una cadena HTML usando un archivo de configuración opcional
source_url: https://www.php.net/manual/es/tidy.repairstring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/repairstring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 2b84fa46e
order: 94160
---

tidy::repairString

tidy_repair_string

Repara una cadena HTML usando un archivo de configuración opcional

## Descripción

Estilo orientado a objetos

```php
public static tidy::repairString(string $string, [array $config], [string $encoding]): string
```php

Estilo procedimental

```php
tidy_repair_string(string $string, [array $config], [string $encoding]): string
```

Repara una cadena dada.

## Parámetros

`string`  
Los datos a ser reparados.

`config`  
La configuración `config` puede ser pasada en forma de un array o una cadena. Si una cadena es pasada, será interpretada como el el nombre del archivo de configuración, de otra forma, será interpretada como opciones en sí mismas.

Revise <http://api.html-tidy.org/#quick-reference> para una explicación detallada sobre cada opción.

`encoding`  
El parámetro `encoding` establece la codificación para entarda/salida de los documentos. Los posibles valores de codificación son: `ascii`, `latin0`, `latin1`, `raw`, `utf8`, `iso2022`, `mac`, `win1252`, `ibm858`, `utf16`, `utf16le`, `utf16be`, `big5`, y `shiftjis`.

## Valores devueltos

Devuelve la cadena reparada, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                                              |
|---------|----------------------------------------------------------|
| 8.0.0   | tidy::repairString es un método estático ahora.          |
| 8.0.0   | `config` y `encoding` son anulables ahora.               |
| 8.0.0   | Esta función ya no acepta el parámetro `useIncludePath`. |

## Ejemplos

Ejemplo de `tidy::repairString`

```php
<?php
ob_start();
?>

<html>
  <head>
    <title>test</title>
  </head>
  <body>
    <p>error</i>
  </body>
</html>

<?php

$buffer = ob_get_clean();
$tidy = new tidy();
$clean = $tidy->repairString($buffer);

echo $clean;
?>

    
```

El ejemplo anterior mostrará:

    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2//EN">
    <html>
    <head>
    <title>test</title>
    </head>
    <body>
    <p>error</p>
    </body>
    </html>

## Véase también

tidy::parseFile

tidy::parseString

tidy::repairFile
