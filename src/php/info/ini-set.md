---
title: ini_set
description: Modifica el valor de una opción de configuración
source_url: https://www.php.net/manual/es/function.ini-set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/ini-set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 0773339dc
order: 39080
---

ini_set

Modifica el valor de una opción de configuración

## Descripción

```php
ini_set(string $option, string $value): string
```php

Cambia el valor de la opción de configuración `varname` y le asigna el valor de `newvalue`. El valor de la opción de configuración será modificado durante toda la ejecución del script y específicamente para este script. Volverá a su valor por omisión al finalizar el script.

## Parámetros

`option`  
Las opciones disponibles no pueden ser todas modificadas con `ini_set`. La lista de todas las opciones disponibles se encuentra en el [apéndice](#ini.list).

`value`  
El nuevo valor para la opción.

## Valores devueltos

Devuelve el valor anterior en caso de éxito, `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | `value` ahora acepta cualquier tipo de valor escalar (incluyendo `null`). Anteriormente, solo se aceptaban valores de tipo `string`. |

## Ejemplos

Define una opción de configuración

```
<?php
echo ini_get('display_errors');

if (!ini_get('display_errors')) {
    ini_set('display_errors', '1');
}

echo ini_get('display_errors');
?>

    
```php

## Véase también

`get_cfg_var`, `ini_get`, `ini_get_all`, `ini_restore`, [Cómo modificar la configuración](#configuration.changes)
