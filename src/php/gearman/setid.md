---
title: GearmanWorker::setId
description: Define un identificador para el worker
source_url: https://www.php.net/manual/es/gearmanworker.setid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gearman/gearmanworker/setid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gearman
translation_status: ready
translation_reviewed: false
translation_revision: cf0a919c1
order: 25890
---

GearmanWorker::setId

Define un identificador para el worker

## Descripción

```php
public GearmanWorker::setId(string $id): bool
```php

Asigna un identificador al worker, permitiendo así que pueda ser identificado cuando gearman solicita la lista de workers disponibles.

## Parámetros

`id`  
Un identificador.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `GearmanWorker::setId`

Define un identificador para un worker simple.

```
<?php
$worker= new GearmanWorker();
$worker->setId('test');
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ejecute el siguiente comando:
    gearadmin --workers

    Output:
    30 ::3a3a:3361:3361:3a33%976303667 - : test
