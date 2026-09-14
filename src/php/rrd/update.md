---
title: RRDUpdater::update
description: Actualiza el archivo de base de datos RRD
source_url: https://www.php.net/manual/es/rrdupdater.update.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/rrdupdater/update.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72800
---

RRDUpdater::update

Actualiza el archivo de base de datos RRD

## Descripción

```php
public RRDUpdater::update(array $values, [string $time]): bool
```php

Actualiza el archivo RRD definido a través de RRDUpdater::\_\_construct. El archivo se actualiza con un valor específico.

## Parámetros

`values`  
Los datos de actualización. Key del array es el nombre del origen de datos.

`time`  
Valor del tiempo para la actualización del RRD con unos datos particulares. El valor predeterminado es la hora actual.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Lanza una `Exception` en caso de error.

## Ejemplos

Ejemplos de RRDUpdater::update

```
<?php
$updator = new RRDUpdater("speed.rrd");
//actualiza el dato de origen "speed" con el valor "12411"
//para un tiempo definido por timestamp "920807700"
$updator->update(array("speed" => "12411"), "920807700");
?>

   
```php
