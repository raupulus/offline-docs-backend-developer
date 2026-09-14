---
title: mb_internal_encoding
description: Lee/modifica la codificación interna
source_url: https://www.php.net/manual/es/function.mb-internal-encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-internal-encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: 5b3fc18be
order: 45250
---

mb_internal_encoding

Lee/modifica la codificación interna

## Descripción

```php
mb_internal_encoding([string $encoding]): string
```php

Lee/modifica la codificación interna.

## Parámetros

`encoding`  
`encoding` se utiliza durante las conversiones de strings provenientes y dirigidas hacia la web, así como durante la creación de strings con el módulo mbstring. Se debe tener en cuenta que la codificación interna es completamente diferente de la de las regex multioctetos.

## Valores devueltos

Si `encoding` es proporcionado, Esta función retorna `true` en caso de éxito o `false` si ocurre un error. En este caso, la codificación de caracteres para las regex multioctetos no se cambia. Si `encoding` es omitido, `mb_internal_encoding` devuelve el nombre de la codificación actual.

## Errores/Excepciones

A partir de PHP 8.0.0, se lanza una `ValueError` si el valor de `encoding` es una codificación inválida. Anterior a PHP 8.0.0, se emitía una `E_WARNING` en su lugar.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `encoding` ahora acepta `null`. |
| 8.0.0 | Ahora lanza una `ValueError` si `encoding` es una codificación inválida. Anteriormente, se emitía una `E_WARNING` en su lugar. |

## Ejemplos

Ejemplo con `mb_internal_encoding`

```
<?php
/* Utiliza la codificación interna UTF-8 */
mb_internal_encoding("UTF-8");

/* Muestra la codificación interna actual */
echo mb_internal_encoding();
?>

    
```php

## Véase también

`mb_http_input`, `mb_http_output`, `mb_detect_order`, `mb_regex_encoding`
