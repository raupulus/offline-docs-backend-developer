---
title: quotemeta
description: Protege los metacaracteres
source_url: https://www.php.net/manual/es/function.quotemeta.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/quotemeta.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 6330e4d73
order: 89010
---

quotemeta

Protege los metacaracteres

## Descripción

```php
quotemeta(string $string): string
```php

Devuelve la cadena `str` después de haber introducido una barra invertida (`\`) delante de todos los caracteres siguientes:

    . \ + * ? [ ^ ] ( $ )

## Parámetros

`string`  
La cadena de entrada.

## Valores devueltos

Devuelve la cadena cuyos metacaracteres han sido protegidos o `false` si una cadena vacía es proporcionada en el argumento `string`.

## Ejemplos

Ejemplo con `quotemeta`

```
<?php

var_dump(quotemeta('PHP is a popular scripting language. Fast, flexible, and pragmatic.'));
?>

    
```php

El ejemplo anterior mostrará:

    string(69) "PHP is a popular scripting language\. Fast, flexible, and pragmatic\."

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`addslashes`, `addcslashes`, `htmlentities`, `htmlspecialchars`, `nl2br`, `stripslashes`, `stripcslashes`, `preg_quote`
