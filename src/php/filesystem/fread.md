---
title: fread
description: Lectura del archivo en modo binario
source_url: https://www.php.net/manual/es/function.fread.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fread.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: ae5b5761e
order: 23650
---

fread

Lectura del archivo en modo binario

## Descripción

```php
fread(resource $stream, int $length): string
```php

`fread` lee hasta `length` bytes en el archivo referenciado por `stream`. La lectura se detiene cuando se presenta alguna de las siguientes condiciones:

- `length` bytes han sido leídos

- se alcanza el final del archivo

- un paquete se vuelve disponible o el tiempo [ socket timeout](#function.socket-set-timeout) ha pasado (para flujos de red)

- si el flujo se lee desde el buffer, y no representa un archivo completo, entonces al menos una lectura de un número de bytes equivalente al tamaño del bloque (generalmente 8192) se realiza; siguiendo los datos del buffer anterior, el tamaño de los datos devueltos puede ser superior al tamaño del bloque.

## Parámetros

`stream`  
Un puntero al sistema de ficheros de tipo `resource` que típicamente se crea utilizando `fopen`.

`length`  
Tamaño `length` de bytes a leer.

## Valores devueltos

Devuelve la cadena leída, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `fread`

```
<?php
// Lee un archivo y lo coloca en una cadena
$filename = "/usr/local/something.txt";
$handle = fopen($filename, "r");
$contents = fread($handle, filesize($filename));
fclose($handle);
?>

    
```php

Ejemplo con `fread` y un archivo binario

> [!WARNING]
> En los sistemas que diferencian los archivos de texto y binarios (por ejemplo, Windows) el archivo debe ser abierto con la letra 'b' añadida al parámetro de modo de la función `fopen`.

```
<?php
$filename = "c:\\files\\somepic.gif";
$handle = fopen($filename, "rb");
$contents = fread($handle, filesize($filename));
fclose($handle);
?>

    
```php

Ejemplo con `fread` y un archivo remoto

> [!WARNING]
> Cuando se lee desde cualquier fuente que no sea un archivo local, como flujos devueltos al leer [archivos remotos](#features.remote-files) o desde `popen` y `fsockopen`, la lectura se detiene después de recibir un paquete. Por lo tanto, se deben hacer bucles para recolectar los datos por paquete, como se presenta a continuación.

```
<?php
$handle = fopen("http://www.example.com/", "rb");
$contents = stream_get_contents($handle);
fclose($handle);
?>

    
```php

```
<?php
$handle = fopen("http://www.example.com/", "rb");
if (FALSE === $handle) {
    exit("Fallo al abrir el flujo hacia la URL");
}

$contents = '';

while (!feof($handle)) {
    $contents .= fread($handle, 8192);
}
fclose($handle);
?>

    
```php

## Notas

> [!NOTE]
> Si se desea leer el contenido de un archivo en una cadena de caracteres, es preferible utilizar `file_get_contents` que es mucho más rápido que el código anterior.

> [!NOTE]
> Se observa que la función `fread` lee la posición actual del puntero de archivo. Utilice la función `ftell` para encontrar la posición actual del puntero y la función `rewind` para reinicializar la posición del puntero.

## Véase también

`fwrite`, `fopen`, `fsockopen`, `popen`, `fgets`, `fgetss`, `fscanf`, `file`, `fpassthru`, `fseek`, `ftell`, `rewind`, `unpack`
