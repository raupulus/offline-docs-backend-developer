---
title: tidy::__construct
description: Construye un nuevo objeto tidy
source_url: https://www.php.net/manual/es/tidy.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_reviewed: true
translation_revision: f02317164
order: 94000
---

tidy::\_\_construct

Construye un nuevo objeto

tidy

## Descripción

```php
public tidy::__construct([string $filename], [array $config], [string $encoding], [bool $useIncludePath])
```php

construye un nuevo objeto `tidy`.

## Parámetros

`filename`  
Si se proporciona el argumento `filename`, esta función también leerá este fichero e inicializará el objeto con este fichero, actuando de la misma forma que la función `tidy_parse_file`.

`config`  
La configuración `config` puede pasarse en forma de `array` o de `string`. Si se pasa una `string`, se interpreta como el nombre del fichero de configuración, y de lo contrario, se interpreta como las opciones mismas.

Para una explicación sobre cada opción, véase <http://api.html-tidy.org/#quick-reference>.

`encoding`  
El argumento `encoding` configura la codificación para los documentos de entrada y salida. Los valores posibles son `ascii`, `latin0`, `latin1`, `raw`, `utf8`, `iso2022`, `mac`, `win1252`, `ibm858`, `utf16`, `utf16le`, `utf16be`, `big5` y `shiftjis`.

`useIncludePath`  
Indica si se debe buscar el fichero en el [include_path](#ini.include-path).

## Errores/Excepciones

Levanta una excepción cuando el constructor falla (por ejemplo, al no poder abrir un fichero).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Los fallos durante la ejecución del constructor ahora lanzan una excepción en lugar de crear silenciosamente un objeto inutilizable. |
| 8.0.0 | `filename`, `config`, `encoding` y `useIncludePath` ahora son nullable. |

## Ejemplos

Ejemplo con `tidy::__construct`

```
<?php

$html = <<< HTML

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head><title>title</title></head>
<body>
<p>paragraph <bt />
text</p>
</body></html>

HTML;

$tidy = new tidy();
$tidy->ParseString($html);

$tidy->cleanRepair();

if ($tidy->errorBuffer) {
    echo "Se han detectado los siguientes errores:\n";
    echo $tidy->errorBuffer;
}

?>

    
```php

El ejemplo anterior mostrará:

    Se han detectado los siguientes errores:
    line 8 column 14 - Error: <bt> no es reconocido!
    line 8 column 14 - Warning: se está descartando <bt> inesperado

## Véase también

tidy::parseFile

tidy::parseString
