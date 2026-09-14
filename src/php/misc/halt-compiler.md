---
title: __halt_compiler
description: Detiene la ejecución del compilador
source_url: https://www.php.net/manual/es/function.halt-compiler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/halt-compiler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: false
translation_revision: 4411b371d
order: 47090
---

\_\_halt_compiler

Detiene la ejecución del compilador

## Descripción

```php
__halt_compiler(): void
```php

Detiene la ejecución del compilador. Esto puede ser muy útil para incrustar datos en scripts PHP, como archivos de instalación.

El byte de la posición del inicio de los datos puede ser determinado por la constante `__COMPILER_HALT_OFFSET__` que solo se define si existe una función `__halt_compiler` presente en el archivo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `__halt_compiler`

```
<?php

// Apertura de un archivo
$fp = fopen(__FILE__, 'r');

// Mueve el puntero de archivo hacia los datos
fseek($fp, __COMPILER_HALT_OFFSET__);

// Luego, se muestra
var_dump(stream_get_contents($fp));

// Fin de la ejecución del script
__halt_compiler(); los datos de instalación (ej. tar, gz, PHP, etc..)

    
```php

## Notas

> [!NOTE]
> `__halt_compiler` solo puede ser utilizado desde un ámbito exterior.
