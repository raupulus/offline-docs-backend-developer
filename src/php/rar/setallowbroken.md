---
title: RarArchive::setAllowBroken
description: Determina si la apertura de archivos dañados se permite
source_url: https://www.php.net/manual/es/rararchive.setallowbroken.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rararchive/setallowbroken.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68470
---

RarArchive::setAllowBroken

Determina si la apertura de archivos dañados se permite

## Descripción

Estilo orientado a objetos (method):

```php
public RarArchive::setAllowBroken(bool $allow_broken): bool
```php

Estilo procedimental:

```php
rar_allow_broken_set(RarArchive $rarfile, bool $allow_broken): bool
```

Este método determina si los archivos dañados pueden ser leidos o todas las operaciones que intenten extraer el archivo de las entradas producirán un error. Los archivos rotos son archivos para los cuales ningún error es detectado cuando el archivo es abierto pero un error se produce cuando leemos las entradas.

## Parámetros

`rarfile`  
Un objeto `RarArchive`, abierto con `rar_open`.

`allow_broken`  
Determina si se permite la lectura de archivos dañados (`true`) o no (`false`).

## Valores devueltos

Devuelve `true` o `false` si ocurre un error. Sólo se producirá un error si el archivo ya fue cerrado.

## Ejemplos

Estilo orientado a objetos

```php
<?php
function retnull() { return null; }
$file = dirname(__FILE__) . "/multi_broken.part1.rar";
/* El tercer argumento omite el mensaje "volumen no encontrado" */
$a = RarArchive::open($file, null, 'retnull');
$a->setAllowBroken(true);
foreach ($a->getEntries() as $e) {
    echo "$e\n";
}
var_dump(count($a));
?>

    
```

Resultado del ejemplo anterior es similar a:

    RarEntry for file "file1.txt" (52b28202)
    int(1)

Estilo procedimental

```php
<?php
function retnull() { return null; }
$file = dirname(__FILE__) . "/multi_broken.part1.rar";
/* El tercer argumento omite el mensaje "volumen no encontrado" */
$a = rar_open($file, null, 'retnull');
rar_allow_broken_set($a, true);
foreach (rar_list($a) as $e) {
    echo "$e\n";
}
var_dump(count($a));
?>

    
```

## Véase también

RarArchive::isBroken
