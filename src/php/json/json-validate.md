---
title: json_validate
description: Verifica si una string contiene JSON válido
source_url: https://www.php.net/manual/es/function.json-validate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/json/functions/json-validate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: json
translation_status: ready
translation_reviewed: true
translation_revision: d715365c0
order: 42870
---

json_validate

Verifica si una string contiene JSON válido

## Descripción

```php
json_validate(string $json, [int $depth], [int $flags]): bool
```php

Devuelve si la `string` dada es sintácticamente JSON válido. Si `json_validate` devuelve `true`, `json_decode` decodificará con éxito la string dada utilizando los mismos `depth` y `flags`.

Si `json_validate` devuelve `false`, la causa puede ser recuperada utilizando `json_last_error` y `json_last_error_msg`.

`json_validate` utiliza menos memoria que `json_decode` si el contenido JSON decodificado no es utilizado, ya que no necesita construir la estructura de array o de objeto que contiene el contenido.

> [!CAUTION]
> Llamar a `json_validate` inmediatamente antes de `json_decode` analizará innecesariamente la string dos veces, ya que `json_decode` realiza implícitamente una validación durante la decodificación.
>
> `json_validate` no debe ser utilizado a menos que la decodificación del contenido JSON no sea inmediatamente utilizada y que sea necesario saber si la string contiene JSON válido.

## Parámetros

`json`  
La string a validar.

Esta función solo funciona con strings codificadas en UTF-8.

> [!NOTE]
> PHP implementa un superconjunto de JSON tal como se especifica en el [RFC 7159](https://datatracker.ietf.org/doc/html/rfc7159) original.

`depth`  
El nivel máximo de profundidad de la estructura a decodificar. El valor debe ser mayor que `0`, y menor o igual a `2147483647`.

`flags`  
Actualmente, solo `JSON_INVALID_UTF8_IGNORE` es aceptado.

## Valores devueltos

Devuelve `true` si la string dada es sintácticamente JSON válido, de lo contrario devuelve `false`.

## Errores/Excepciones

Si `depth` está fuera del rango permitido, se lanza una `ValueError`.

Si `flags` no es un flag válido, se lanza una `ValueError`.

## Ejemplos

Ejemplos de `json_validate`

```
<?php
var_dump(json_validate('{ "test": { "foo": "bar" } }'));
var_dump(json_validate('{ "": "": "" } }'));
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

## Véase también

`json_decode`, `json_last_error`, `json_last_error_msg`
