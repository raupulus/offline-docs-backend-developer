---
title: uopz_backup
description: Guarda una función
source_url: https://www.php.net/manual/es/function.uopz-backup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-backup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99190
---

uopz_backup

Guarda una función

> [!WARNING]
> Esta función ha sido *ELIMINADA* en PECL uopz 5.0.0.

## Descripción

```php
uopz_backup(string $function): void
```php

```php
uopz_backup(string $class, string $function): void
```

Guarda una función en tiempo de ejecución.

## Parámetros

`class`  
El nombre de la clase que contiene la función a guardar

`function`  
El nombre de la función

## Valores devueltos

## Ejemplos

Ejemplo con `uopz_backup`

```php
<?php
uopz_backup("fgets");
uopz_function("fgets", function(){
    return true;
});
var_dump(fgets());
?>

   
```

El ejemplo anterior mostrará:

    bool(true)
