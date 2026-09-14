---
title: fpassthru
description: Muestra el resto del fichero
source_url: https://www.php.net/manual/es/function.fpassthru.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fpassthru.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 98f2a733b
order: 23620
---

fpassthru

Muestra el resto del fichero

## Descripción

```php
fpassthru(resource $stream): int
```php

Lee todo el resto de un fichero hasta el final y dirige el resultado hacia la salida estándar.

Es necesario llamar a la función `rewind` para reiniciar el puntero de fichero al principio si ya se han escrito datos en el fichero.

Si se desea únicamente copiar el contenido de un fichero en el buffer de salida, sin modificarlo previamente o colocar el puntero en un lugar particular, debe utilizarse la función `readfile`, lo que evita tener que llamar a la función `fopen`.

## Parámetros

`stream`  
El puntero de fichero debe ser válido y apuntar a un archivo abierto con éxito por `fopen` o `fsockopen` (y no cerrado aún por `fclose`).

## Valores devueltos

Devuelve el número de caracteres leídos desde `stream` y pasados a la salida estándar.

## Ejemplos

Uso de `fpassthru` con un fichero binario

```
<?php

// abre un fichero en modo binario
$name = './img/ok.png';
$fp = fopen($name, 'rb');

// envía los encabezados correctos
header("Content-Type: image/png");
header("Content-Length: " . filesize($name));

// envía el contenido del fichero, luego detiene el script
fpassthru($fp);
exit;

?>

    
```php

## Notas

> [!NOTE]
> Cuando se utiliza la función `fpassthru` sobre un fichero binario en Windows, asegúrese de haber abierto el fichero en modo binario añadiendo la letra `b` al modo de acceso utilizado en `fopen`.
>
> Se recomienda utilizar la opción `b` al trabajar con ficheros binarios, incluso si el sistema no lo requiere, para garantizar la portabilidad de los scripts.

## Véase también

`readfile`, `fopen`, `popen`, `fsockopen`
