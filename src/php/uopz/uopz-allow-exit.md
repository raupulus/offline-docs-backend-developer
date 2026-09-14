---
title: uopz_allow_exit
description: Permite controlar el opcode exit desactivado
source_url: https://www.php.net/manual/es/function.uopz-allow-exit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-allow-exit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: 961ac1b44
order: 99180
---

uopz_allow_exit

Permite controlar el opcode exit desactivado

## Descripción

```php
uopz_allow_exit(bool $allow): void
```php

Por omisión, uopz desactiva el opcode exit, por lo que las llamadas a `exit` son prácticamente ignoradas. `uopz_allow_exit` permite controlar este comportamiento.

## Parámetros

`allow`  
Permitir o no la ejecución de los opcodes exit.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `uopz_allow_exit`

```
<?php
exit(1);
echo 1;
uopz_allow_exit(true);
exit(2);
echo 2;
?>

   
```php

El ejemplo anterior mostrará:

    1

## Notas

> [!CAUTION]
> [OPcache](#book.opcache) optimiza el código muerto después de una salida incondicional.

## Véase también

uopz_get_exit_status
