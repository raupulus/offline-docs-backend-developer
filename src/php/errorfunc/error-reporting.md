---
title: error_reporting
description: Establece el nivel de reporte de errores de PHP
source_url: https://www.php.net/manual/es/function.error-reporting.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/errorfunc/functions/error-reporting.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: errorfunc
translation_status: ready
translation_reviewed: true
translation_revision: 9caac4c5c
order: 17640
---

error_reporting

Establece el nivel de reporte de errores de PHP

## Descripción

```php
error_reporting([int $error_level]): int
```php

`error_reporting` modifica la directiva [error_reporting](#ini.error-reporting) durante la ejecución del script. PHP posee varios niveles de errores, utilizar esta función configura este nivel durante la duración (de ejecución) del script. Si el parámetro opcional `error_level` no está definido, `error_reporting` retornará únicamente el nivel de reporte de errores actual.

## Parámetros

`error_level`  
El nuevo nivel [error_reporting](#ini.error-reporting). Puede ser un campo de bits o una combinación de constantes. El uso de constantes es altamente recomendado para asegurar una compatibilidad máxima con las futuras versiones. A medida que se crean nuevos niveles de errores, los valores evolucionan, por lo que los valores antiguos ya no tienen necesariamente el mismo significado.

Las constantes que representan los niveles de errores disponibles y la significación de estos niveles de errores se describe en el manual sobre las [constantes predefinidas](#errorfunc.constants).

## Valores devueltos

Retorna el nivel de [error_reporting](#ini.error-reporting) *antes* de que sea cambiado a `error_level`

> [!NOTE]
> El operador de [control de errores](#language.operators.errorcontrol) `@` modifica el `error_level` durante la gestión de errores.

## Historial de cambios

| Versión | Descripción                      |
|---------|----------------------------------|
| 8.0.0   | `error_level` ahora es nullable. |

## Ejemplos

Ejemplo con `error_reporting`

```
<?php

// Desactivar el reporte de errores
error_reporting(0);

// Reportar errores de ejecución de script
error_reporting(E_ERROR | E_WARNING | E_PARSE);

// Reportar E_NOTICE puede ayudar a mejorar los scripts
// (variables no inicializadas, variables mal escritas..)
error_reporting(E_ERROR | E_WARNING | E_PARSE | E_NOTICE);

// Reportar todas las errores excepto E_NOTICE
// Esta es la configuración por omisión de php.ini
error_reporting(E_ALL & ~E_NOTICE);

// Reportar todas las errores PHP
error_reporting(E_ALL);

// Reportar todas las errores PHP
error_reporting(-1);

// Igual que error_reporting(E_ALL);
ini_set('error_reporting', E_ALL);

?>

    
```php

## Notas

> [!TIP]
> Al pasar el valor `-1`, todas las errores posibles serán mostradas, incluso al agregar nuevos niveles y constantes en las futuras versiones de PHP. Este comportamiento es equivalente a proporcionar la constante `E_ALL`.

## Véase también

La directiva [display_errors](#ini.display-errors), La directiva [html_errors](#ini.html-errors), La directiva [xmlrpc_errors](#ini.xmlrpc-errors), El operador de [control de errores](#language.operators.errorcontrol), `ini_set`
