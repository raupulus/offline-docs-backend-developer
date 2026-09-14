---
title: PharData::compress
description: Comprime el archivo tar/zip completo utilizando la compresión Gzip o
  Bzip2
source_url: https://www.php.net/manual/es/phardata.compress.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharData/compress.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64490
---

PharData::compress

Comprime el archivo tar/zip completo utilizando la compresión Gzip o Bzip2

## Descripción

```php
public PharData::compress(int $compression, [string $extension]): PharData
```php

Para los archivos tar, este método comprime el archivo completo utilizando la compresión gzip o bzip2. El archivo resultante puede ser manipulado con el comando gunzip/bunzip, o ser accedido directamente y de forma transparente con la extensión Phar.

Para los archivos zip, este método falla al lanzar una excepción. La extensión [zlib](#ref.zlib) debe estar activada para comprimir con gzip, la extensión [bzip2](#ref.bzip2) debe estar activada para comprimir con bzip2.

Asimismo, este método renombra automáticamente el archivo, añadiendo el sufijo `.gz`, `.bz2` o eliminando la extensión si `Phar::NONE` es especificado para eliminar la compresión. De lo contrario, una extensión de archivo puede ser especificada con el segundo argumento.

## Parámetros

`compression`  
La compresión debe ser `Phar::GZ` o `Phar::BZ2` para aplicar una compresión, o `Phar::NONE` para eliminarla.

`extension`  
Por omisión, la extensión es `.tar.gz` o `.tar.bz2` para comprimir un tar, y `.tar` para descomprimir.

## Valores devueltos

Un objeto `PharData` es devuelto en caso de éxito, `null` en caso de error.

## Errores/Excepciones

Levanta una excepción `BadMethodCallException` si la extensión [zlib](#ref.zlib) no está disponible, o si la extensión [bzip2](#ref.bzip2) no está activada.

## Historial de cambios

| Versión | Descripción                    |
|---------|--------------------------------|
| 8.0.0   | `extension` ahora es nullable. |

## Ejemplos

Un ejemplo con `PharData::compress`

```
<?php
$p = new PharData('/ruta/al/mio.tar');
$p['monfichier.txt'] = 'salut';
$p['monfichier2.txt'] = 'salut';
$p1 = $p->compress(Phar::GZ); // copies hacia /path/to/my.tar.gz
$p2 = $p->compress(Phar::BZ2); // copies hacia /path/to/my.tar.bz2
$p3 = $p2->compress(Phar::NONE); // excepción: /path/to/my.tar ya existe
?>

    
```php

## Véase también

`Phar::compress`
