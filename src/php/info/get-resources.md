---
title: get_resources
description: Devuelve los recursos activos
source_url: https://www.php.net/manual/es/function.get-resources.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/get-resources.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: false
translation_revision: 16805838e
order: 38940
---

get_resources

Devuelve los recursos activos

## Descripción

```php
get_resources([string $type]): array
```php

Devuelve un array de todos los recursos `resource` actualmente activos, opcionalmente filtrados por el tipo de recurso.

> [!NOTE]
> Esta función está destinada a fines de depuración y prueba. No está pensada para ser utilizada en entornos de producción, y mucho menos para acceder o incluso manipular recursos que normalmente no son accesibles (por ejemplo, el recurso de flujo subyacente de las instancias de `SplFileObject`).

## Parámetros

`type`  
Si se define, esto hará que `get_resources` devuelva solo los recursos del tipo dado. [Una lista de tipos de recursos está disponible.](#resource)

Si se proporciona `string` `Unknown` para el tipo, en ese caso solo se devolverán los recursos cuyo tipo es desconocido.

Si se omite, se devolverán todos los recursos.

## Valores devueltos

Devuelve un `array` de los recursos actualmente activos, indexados por el número del recurso.

## Historial de cambios

| Versión | Descripción               |
|---------|---------------------------|
| 8.0.0   | `type` ahora es nullable. |

## Ejemplos

`get_resources` sin filtrar

```
<?php
$fp = tmpfile();
var_dump(get_resources());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      [1]=>
      resource(1) of type (stream)
    }

`get_resources` filtrado

```
<?php
$fp = tmpfile();
var_dump(get_resources('stream'));
var_dump(get_resources('curl'));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      [1]=>
      resource(1) of type (stream)
    }
    array(0) {
    }

## Véase también

`get_loaded_extensions`, `get_defined_constants`, `get_defined_functions`, `get_defined_vars`
