---
title: RarArchive::getEntries
description: Obtener la lista completa de entradas del archivo RAR
source_url: https://www.php.net/manual/es/rararchive.getentries.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rararchive/getentries.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68420
---

RarArchive::getEntries

rar_list

Obtener la lista completa de entradas del archivo RAR

## Descripción

Estilo orientado a objetos (método):

```php
public RarArchive::getEntries(): array
```php

Estilo procedimental:

```php
rar_list(RarArchive $rarfile): array
```

Obtener la lista de entradas (archivos y directorios) de el archivo RAR.

> [!NOTE]
> Si el archivo tiene entradas con el mismo nombre, este método, junto con `RarArchive` `foreach` iteraciona y otorga un acceso array-like con índices numéricos, únicos para acceder a todas las entradas (por ejemplo, RarArchive::getEntry y el [ `rar://` wrapper](#wrappers.rar) son insuficientes).

## Parámetros

`rarfile`  
Un objeto `RarArchive`, abierto con `rar_open`.

## Valores devueltos

`rar_list` devuelve array de objetos `RarEntry` o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL rar 3.0.0 | Soporte para archivos RAR con nombres entrada repetidos que ya no produce deficiencias. |

## Ejemplos

Estilo orientado a objetos

```php
<?php
$rar_arch = RarArchive::open('solid.rar');
if ($rar_arch === FALSE)
    die("Could not open RAR archive.");

$rar_entries = $rar_arch->getEntries();
if ($rar_entries === FALSE)
    die("Could retrieve entries.");

echo "Found " . count($rar_entries) . " entries.\n";

foreach ($rar_entries as $e) {
    echo $e;
    echo "\n";
}
$rar_arch->close();
?>

    
```

Resultado del ejemplo anterior es similar a:

    Found 2 entries.
    RarEntry for file "tese.txt" (23b93a7a)
    RarEntry for file "unrardll.txt" (2ed64b6e)

Estilo procedimental

```php
<?php
$rar_arch = rar_open('solid.rar');
if ($rar_arch === FALSE)
    die("Could not open RAR archive.");

$rar_entries = rar_list($rar_arch);
if ($rar_entries === FALSE)
    die("Could not retrieve entries.");

echo "Found " . count($rar_entries) . " entries.\n";

foreach ($rar_entries as $e) {
    echo $e;
    echo "\n";
}
rar_close($rar_arch);
?>

    
```

## Véase también

RarArchive::getEntry

rar://

wrapper
