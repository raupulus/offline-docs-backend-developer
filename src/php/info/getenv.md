---
title: getenv
description: Retorna el valor de una o todas las variables de entorno
source_url: https://www.php.net/manual/es/function.getenv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/getenv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: 1299a9808
order: 38950
---

getenv

Retorna el valor de una o todas las variables de entorno

## Descripción

```php
getenv([string $name], [bool $local_only]): string
```php

Retorna el valor de una o todas las variables de entorno.

Puede verse una lista completa de las variables de entorno utilizando la función `phpinfo`. Puede encontrarse el significado de cada una de ellas consultando la [RFC 3875](https://datatracker.ietf.org/doc/html/rfc3875), en particular la sección 4.1 "Request Meta-Variables".

## Parámetros

`name`  
El nombre de la variable como `string` o `null`.

`local_only`  
Cuando se establece en `true`, solo se retornan las variables de entorno locales, definidas por el sistema operativo o putenv. Esto solo tiene efecto cuando `name` es un `string`.

## Valores devueltos

Retorna el valor de la variable de entorno `name`, o `false` si la variable de entorno `name` no existe. Si `name` es omitido, todas las variables de entorno son retornadas como un `array` asociativo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | El `name` ahora es nullable. |
| 7.1.0 | `name` ahora puede ser omitido para recuperar un `array` asociativo de todas las variables de entorno. |
| 7.0.9 | Se ha añadido el parámetro `local_only`. |

## Ejemplos

Ejemplo con `getenv`

```
<?php
// Ejemplo de uso de getenv()
$ip = getenv('REMOTE_ADDR');

// O simplemente usar una Superglobal ($_SERVER o $_ENV)
$ip = $_SERVER['REMOTE_ADDR'];

// Obtener de forma segura el valor de una variable de entorno,
// ignorando si ha sido definida por un SAPI o modificada con putenv
$ip = getenv('REMOTE_ADDR', true) ?: getenv('REMOTE_ADDR')
?>

    
```php

## Notas

> [!WARNING]
> Si PHP se ejecuta en un SAPI como Fast CGI, esta función retornará siempre el valor de una variable de entorno definida por el SAPI, incluso si `putenv` ha sido utilizado para definir una variable de entorno local con el mismo nombre. El parámetro `local_only` debe ser utilizado para retornar los valores de variables de entorno definidas localmente.

## Véase también

`putenv`, `apache_getenv`, [Superglobales](#language.variables.superglobals)
