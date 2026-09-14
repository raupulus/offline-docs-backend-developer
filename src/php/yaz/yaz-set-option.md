---
title: yaz_set_option
description: Configura una o más opciones de la conexión
source_url: https://www.php.net/manual/es/function.yaz-set-option.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-set-option.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 107950
---

yaz_set_option

Configura una o más opciones de la conexión

## Descripción

```php
yaz_set_option(resource $id, string $name, string $value): void
```php

```php
yaz_set_option(resource $id, array $options): void
```

Configura una o más opciones de la conexión dada.

## Parámetros

`id`  
El recurso de conexión devuelta por `yaz_connect`.

`name` o `options`  
Puede ser un string o un array.

Si se informa un string, será el nombre de la opción a configurar. Será necesario especificar su `value`.

Si se informa un array, será un array asociativo (nombre opción =\> valor opción).

| Nombre | Descripción |
|----|----|
| implementationName | nombre de la implementación del servidor |
| implementationVersion | versión de implementación del servidor |
| implementationId | ID de implementación del servidor |
| schema | esquema de recuperación. Por defecto, no se utiliza ningún esquema. Configurar esta opción es equivalente a utilizar la función `yaz_schema` |
| preferredRecordSyntax | sintaxis del registro para la recuperación. Por defecto, no se utiliza sintaxis. Configurar esta opción es equivalente a utilizar la función `yaz_syntax` |
| start | desplazamiento para el primer registro a ser obtenido vía `yaz_search` o `yaz_present`. El primer registro está numerado con un valor inicial de 0. El segundo registro tiene valor de inicio 1. Configurar esta opción en combinación con la opción `count` tiene el mismo efecto que llamar a `yaz_range` excepto que los registros están numerados a partir de de 1 con `yaz_range` |
| count | número máximo de registros a recuperar vía `yaz_search` o `yaz_present`. |
| elementSetName | nombre del conjunto de elementos para la recuperación. Configurar esta opción es equivalente a llamar a `yaz_element`. |

Opciones de Conexión PHP/YAZ

`value`  
El nuevo valor de la opción. Utilizar este parámetro únicamente si el argumento previo es un string.

## Valores devueltos

No se retorna ningún valor.
