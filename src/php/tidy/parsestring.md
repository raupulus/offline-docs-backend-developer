---
title: tidy::parseString
description: Analiza un documento HTML contenido en una string
source_url: https://www.php.net/manual/es/tidy.parsestring.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/parsestring.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: true
translation_revision: 2b84fa46e
order: 94140
---

tidy::parseString

tidy_parse_string

Analiza un documento HTML contenido en una string

## Descripción

Estilo orientado a objetos

```php
public tidy::parseString(string $string, [array $config], [string $encoding]): bool
```php

Estilo procedimental

```php
tidy_parse_string(string $string, [array $config], [string $encoding]): tidy
```

Analiza un documento contenido en una string.

## Parámetros

`string`  
Los datos a analizar.

`config`  
La configuración `config` puede ser pasada en forma de `array` o de `string`. Si una `string` es pasada, es interpretada como el nombre del fichero de configuración, y si no, es interpretada como las opciones mismas.

Para una explicación sobre cada opción, véase <http://api.html-tidy.org/#quick-reference>.

`encoding`  
El parámetro `encoding` configura la codificación para los documentos de entrada y salida. Los valores posibles son `ascii`, `latin0`, `latin1`, `raw`, `utf8`, `iso2022`, `mac`, `win1252`, `ibm858`, `utf16`, `utf16le`, `utf16be`, `big5` y `shiftjis`.

## Valores devueltos

tidy::parseString devuelve `true` en caso de éxito. `tidy_parse_string` devuelve una nueva instancia de `tidy` en caso de éxito. Ambos, el método y la función devuelven `false` en caso de fallo.

## Historial de cambios

| Versión | Descripción                               |
|---------|-------------------------------------------|
| 8.0.0   | `config` y `encoding` son ahora nullable. |

## Ejemplos

Ejemplo con `tidy::parseString`

```php
<?php
ob_start();
?>

<html>
 <head>
  <title>test</title>
 </head>
 <body>
  <p>error<br />otra línea</p>
 </body>
</html>

<?php
$buffer = ob_get_clean();
$config = array('indent' => TRUE,
   'output-xhtml' => TRUE,
   'wrap' => 200);

$tidy = tidy_parse_string($buffer, $config, 'UTF8');

$tidy->cleanRepair();

echo $tidy;
?>

    
```

El ejemplo anterior mostrará:

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
               "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
     <head>
      <title>
       test
      </title>
     </head>
     <body>
      <p>
       error<br />
       otra línea
      </p>
     </body>
    </html>

## Véase también

tidy::parseFile

tidy::repairFile

tidy::repairString
