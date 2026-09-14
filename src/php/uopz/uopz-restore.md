---
title: uopz_restore
description: Restaura una función guardada
source_url: https://www.php.net/manual/es/function.uopz-restore.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-restore.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99370
---

uopz_restore

Restaura una función guardada

> [!WARNING]
> Esta función ha sido *ELIMINADA* en PECL uopz 5.0.0.

## Descripción

```php
uopz_restore(string $function): void
```php

```php
uopz_restore(string $class, string $function): void
```

Restaura una función guardada.

## Parámetros

`class`  
El nombre de la clase que contiene la función a restaurar

`function`  
El nombre de la función

## Valores devueltos

## Ejemplos

Ejemplo con `uopz_restore`

```php
<?php
uopz_backup("fgets");
uopz_function("fgets", function(){
    return true;
});
var_dump(fgets());
uopz_restore('fgets');
fgets();
?>

   
```

Resultado del ejemplo anterior es similar a:

    Advertencia: fgets() espera al menos 1 parámetro, 0 dado en /path/to/script.php en la línea 8
