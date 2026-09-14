---
title: fgets
description: Recupera la línea actual a partir de la posición del puntero de archivo
source_url: https://www.php.net/manual/es/function.fgets.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fgets.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 32e694be4
order: 23440
---

fgets

Recupera la línea actual a partir de la posición del puntero de archivo

## Descripción

```php
fgets(resource $stream, [int $length]): string
```php

Recupera la línea actual a partir de la posición del puntero de archivo.

## Parámetros

`stream`  
El puntero de fichero debe ser válido y apuntar a un archivo abierto con éxito por `fopen` o `fsockopen` (y no cerrado aún por `fclose`).

`length`  
Lee hasta la longitud `length` - 1 byte desde el puntero de archivo `stream`, o bien el final del archivo, o una nueva línea (que es incluida en el valor devuelto), o un EOF (el que llegue primero). Si no se proporciona longitud, la función leerá el flujo hasta el final de la línea.

## Valores devueltos

Devuelve un `string` que contiene los `length` primeros caracteres, menos 1 byte desde el puntero de archivo `stream`. `false` es devuelto si no hay más datos para leer.

Si ocurre un error, la función devuelve `false`.

## Ejemplos

Lectura de un archivo línea por línea

```
<?php

$fp = @fopen("/tmp/inputfile.txt", "r");

if ($fp) {
    while (($buffer = fgets($fp, 4096)) !== false) {
        echo $buffer, PHP_EOL;
    }
    if (!feof($fp)) {
        echo "Error: fgets() falló\n";
    }

    fclose($fp);
}

?>

    
```php

## Notas

> [!NOTE]
> Si PHP no reconoce correctamente los finales de línea al leer ficheros que han sido creados o leídos en un Macintosh, la activación de la opción de configuración [auto_detect_line_endings](#ini.auto-detect-line-endings) puede resolver el problema.

> [!NOTE]
> Los programadores acostumbrados a la programación 'C' notarán que `fgets` no se comporta como su equivalente en C al encontrar el final del archivo.

## Véase también

`fgetss`, `fread`, `fgetc`, `stream_get_line`, `fopen`, `popen`, `fsockopen`, `stream_set_timeout`
