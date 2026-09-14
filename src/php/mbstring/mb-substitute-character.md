---
title: mb_substitute_character
description: Define/Recupera los caracteres de sustitución
source_url: https://www.php.net/manual/es/function.mb-substitute-character.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-substitute-character.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: d023b296f
order: 45560
---

mb_substitute_character

Define/Recupera los caracteres de sustitución

## Descripción

```php
mb_substitute_character([string $substitute_character]): string
```php

Especifica el carácter de sustitución para caracteres inválidos o codificaciones inválidas. Los caracteres inválidos pueden ser reemplazados por `"none"` (no se muestra, se eliminan), una `string` o un valor `int` (valor de un código de carácter Unicode).

Esta configuración afecta a `mb_convert_encoding`, `mb_convert_variables`, `mb_output_handler`, `mb_scrub`, y `mb_send_mail`.

## Parámetros

`substitute_character`  
Especifica un valor Unicode en forma de `int`, o bien una `string` en las siguientes formas:

- `"none"` : no se muestra

- `"long"` : muestra el valor hexadecimal (Ejemplo: `U+3000`, `JIS+7E7E`)

- `"entity"` : muestra la entidad del carácter (Ejemplo: `&#x200;`)

## Valores devueltos

Si `substitute_character` es proporcionado, `mb_substitute_character` devuelve `true` en caso de éxito, y `false` en caso de error. Si `substitute_character` es omitido, `mb_substitute_character` devuelve un valor Unicode, o bien "`none`"/"`long`".

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Pasar una cadena vacía a `substitute_character` ya no es soportado; `"none"` debería ser proporcionado en su lugar. |
| 8.0.0 | `encoding` ahora acepta `null`. |

## Ejemplos

Ejemplo con `mb_substitute_character`

```
<?php
/* Configura el carácter de sustitución con U+3013 (GETA MARK) */
mb_substitute_character(0x3013);

/* Configura el carácter de sustitución con un formato hexadecimal */
mb_substitute_character("long");

/* Muestra la configuración actual */
echo mb_substitute_character();
?>

    
```php
