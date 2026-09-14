---
title: RarEntry::getStream
description: Obtener manejador de archivo para entrada
source_url: https://www.php.net/manual/es/rarentry.getstream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rarentry/getstream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68580
---

RarEntry::getStream

Obtener manejador de archivo para entrada

## Descripción

```php
public RarEntry::getStream([string $password]): resource
```php

Devuelve un manejador de archivo que soporta operaciones de lectura. Este manejador proporciona descompresión al vuelo para esta entrada.

El manejador no es invalidado por llamar a `rar_close`.

> [!WARNING]
> El flujo resultante no tiene verificación de integridad. En particular, archivo corrupto y descifrado con una clave errónea, no será detectado. Es responsabilidad del programador utilizar la entrada CRC para comprobar la integridad, si así lo desea.

## Parámetros

`password`  
La contraseña utilizada para cifrar esta entrada. Si la entrada no está cifrada, este valor no se utilizará y puede ser omitido. Si el parámetro es omitido y la entrada está cifrada, la contraseña dada a `rar_open`, será utilizada. Si una contraseña incorrecta es dada, ya sea explícita o implícitamente via `rar_open`, teste método resultante de flujo producirá error de salida. Si no se especifica la contraseña y se requiere una, este método fallará y devolverá `false`. Puede comprobar si una entrada está cifrada con RarEntry::isEncrypted.

## Valores devueltos

El manejador de archivo o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL rar 3.0.0 | Soporte para archivos RAR con nombres de entrada que se repiten ya no es defectuoso. |

## Ejemplos

Ejemplo de RarEntry::getStream

```
<?php

$rar_file = rar_open('example.rar');
if ($rar_file === false)
    die("Failed to open Rar archive");

$entry = rar_entry_get($rar_file, 'Dir/file.txt');
if ($entry === false)
    die("Failed to find such entry");

$stream = $entry->getStream();
if ($stream === false)
    die("Failed to obtain stream.");

rar_close($rar_file); //flujo es independiente de archivo

while (!feof($stream)) {
    $buff = fread($stream, 8192);
    if ($buff !== false)
        echo $buff;
    else
        break; //error fread
}

fclose($stream);

?>

   
```php

## Véase también

RarEntry::extract

rar://

wrapper
