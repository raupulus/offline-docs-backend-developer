---
title: ftell
description: Devuelve la posición actual del puntero de archivo
source_url: https://www.php.net/manual/es/function.ftell.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/ftell.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 23700
---

ftell

Devuelve la posición actual del puntero de archivo

## Descripción

```php
ftell(resource $stream): int
```php

Devuelve la posición actual del puntero de archivo referenciado por `stream`.

## Parámetros

`stream`  
El puntero de archivo debe ser válido y haber sido abierto correctamente por `fopen` o `popen`. `ftell` proporciona resultados no definidos para los flujos "`append-only`" (abiertos con el flag "a").

## Valores devueltos

Devuelve la posición actual del puntero en el archivo identificado por el puntero `stream` en forma de entero, es decir, su posición en el flujo del archivo.

Si ocurre un error, la función devolverá `false`.

> [!NOTE]
> Como el tipo entero de PHP es firmado y que muchas plataformas utilizan enteros de 32 bits, algunas funciones relacionadas con el sistema de archivos pueden retornar resultados extraños para ficheros de tamaño superior a 2 Go.

## Ejemplos

Ejemplo con `ftell`

```
<?php

// Abre un archivo y lee algunos datos
$fp = fopen("/etc/passwd", "r");
$data = fgets($fp, 12);

// ¿Dónde estamos?
echo ftell($fp); // 11

fclose($fp);

?>

    
```php

## Véase también

`fopen`, `popen`, `fseek`, `rewind`
