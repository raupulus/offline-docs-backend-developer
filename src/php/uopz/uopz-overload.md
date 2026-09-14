---
title: uopz_overload
description: Sobrecarga un opcode de la VM
source_url: https://www.php.net/manual/es/function.uopz-overload.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-overload.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99340
---

uopz_overload

Sobrecarga un opcode de la VM

> [!WARNING]
> Esta función ha sido *ELIMINADA* en PECL uopz 5.0.0.

## Descripción

```php
uopz_overload(int $opcode, Callable $callable): void
```php

Sobrecarga el `opcode` especificado con una función definida por el usuario.

## Parámetros

`opcode`  
Un opcode válido; consulte las constantes para más detalles sobre los códigos admitidos.

`callable`  

## Valores devueltos

## Ejemplos

Ejemplo con `uopz_overload`

```
<?php
uopz_overload(ZEND_EXIT, function(){});

exit();
echo "Hello World";
?>

   
```php

El ejemplo anterior mostrará:

    Hello World
