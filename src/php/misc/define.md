---
title: define
description: Define una constante
source_url: https://www.php.net/manual/es/function.define.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/define.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: a124543dd
order: 47030
---

define

Define una constante

## Descripción

```php
define(string $constant_name, mixed $value, [bool $case_insensitive]): bool
```php

Define una constante durante la ejecución.

## Parámetros

`constant_name`  
El nombre de la constante.

> [!NOTE]
> Es posible definir con `define` constantes con nombres reservados o incluso inválidos, donde sus valores pueden (solo) ser recuperados con la función `constant`. Sin embargo, hacer esto no se recomienda.

`value`  
El valor de la constante.

> [!WARNING]
> Aunque es técnicamente posible definir constantes de tipo `resource`, esto se desaconseja y puede causar comportamientos inesperados.

`case_insensitive`  
Si es `true`, el nombre de la constante será insensible a mayúsculas/minúsculas: `CONSTANT` y `Constant` representan valores idénticos.

> [!WARNING]
> Definir constantes insensibles a mayúsculas/minúsculas está deprecado a partir de PHP 7.3.0. A partir de PHP 8.0.0, solo `false` es un valor aceptable, pasar `true` producirá una advertencia.

> [!NOTE]
> Las constantes insensibles a mayúsculas/minúsculas se almacenan en minúsculas.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | `value` ahora puede ser un objeto. |
| 8.0.0 | Pasar `true` a `case_insensitive` ahora emite una `E_WARNING`. Pasar `false` sigue siendo permitido. |
| 7.3.0 | `case_insensitive` está deprecado y será eliminado en la versión 8.0.0. |

## Ejemplos

Definición de una constante

```
<?php
define("CONSTANT", "Hola mundo.");
echo CONSTANT; // muestra "Hola mundo."
echo Constant; // muestra "Constant" y emite una advertencia

define("GREETING", "Hola tú.", true);
echo GREETING; // muestra "Hola tú."
echo Greeting; // muestra "Hola tú."

// Funciona desde PHP 7
define('ANIMALS', array(
    'perro',
    'gato',
    'aves'
));
echo ANIMALS[1]; // muestra "gato"

?>

    
```php

Constantes con Nombres Reservados

Este ejemplo ilustra la *posibilidad* de definir una constante con el mismo nombre que una [constante mágica](#language.constants.magic). Dado que el comportamiento resultante es confuso, esta práctica no se recomienda.

```
<?php
var_dump(defined('__LINE__'));
var_dump(define('__LINE__', 'test'));
var_dump(constant('__LINE__'));
var_dump(__LINE__);
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)
    string(4) "test"
    int(5)

## Véase también

`defined`, `constant`, La sección sobre las [constantes](#language.constants)
