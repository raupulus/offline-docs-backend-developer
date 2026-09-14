---
title: RarArchive::getEntry
description: Obtener el objeto entrada desde el archivo RAR
source_url: https://www.php.net/manual/es/rararchive.getentry.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rararchive/getentry.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68430
---

RarArchive::getEntry

rar_entry_get

Obtener el objeto entrada desde el archivo RAR

## Descripción

Estilo orientado a objetos (método):

```php
public RarArchive::getEntry(string $entryname): RarEntry
```php

Estilo procedimental:

```php
rar_entry_get(RarArchive $rarfile, string $entryname): RarEntry
```

Obtener el objeto entrada (archivo o directorio) desde el archivo RAR.

> [!NOTE]
> También puede obtener objetos de entrada utilizando RarArchive::getEntries.
>
> Tenga en cuenta que un archivo RAR puede tener varias entradas con el mismo nombre; este método recuperará sólo el primero.

## Parámetros

`rarfile`  
Un objeto `RarArchive`, abierto con `rar_open`.

`entryname`  
Ruta a la entrada dentro del archivo RAR.

> [!NOTE]
> La ruta debe ser la misma devuelta por RarEntry::getName.

## Valores devueltos

Devuelve el objeto `RarEntry` encontrado o `false` si ocurre un error.

## Ejemplos

Estilo orientado a objetos

```php
<?php
$rar_arch = RarArchive::open('solid.rar');
if ($rar_arch === FALSE)
    die("Could not open RAR archive.");
$rar_entry = $rar_arch->getEntry('tese.txt');
if ($rar_entry === FALSE)
    die("Could not get such entry");
echo get_class($rar_entry)."\n";
echo $rar_entry;
$rar_arch->close();
?>

    
```

Resultado del ejemplo anterior es similar a:

    RarEntry
    RarEntry for file "tese.txt" (23b93a7a)

Estilo procedimental

```php
<?php
$rar_arch = rar_open('solid.rar');
if ($rar_arch === FALSE)
    die("Could not open RAR archive.");
$rar_entry = rar_entry_get($rar_arch, 'tese.txt');
if ($rar_entry === FALSE)
    die("Could not get such entry");
echo get_class($rar_entry)."\n";
echo $rar_entry;
rar_close($rar_arch);
?>

    
```

## Véase también

RarArchive::getEntries

rar://

wrapper
