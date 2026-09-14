---
title: mailparse_rfc822_parse_addresses
description: Procesa direcciones compatibles con RFC 822
source_url: https://www.php.net/manual/es/function.mailparse-rfc822-parse-addresses.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mailparse/functions/mailparse-rfc822-parse-addresses.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mailparse
translation_status: ready
translation_reviewed: false
translation_revision: 01bd007b0
order: 44420
---

mailparse_rfc822_parse_addresses

Procesa direcciones compatibles con RFC 822

## Descripción

```php
mailparse_rfc822_parse_addresses(string $addresses): array
```php

Procesa una lista de recipientes compatible con [RFC 822](https://datatracker.ietf.org/doc/html/rfc822), tal como la que es encontrada en una cabecera `To:`.

## Parámetros

`addresses`  
Una cadena que contiene direcciones, como: `Wez Furlong <wez@example.com>, pepe@example.com`

> [!NOTE]
> Esta cadena no debe contener el nombre de la cabecera.

## Valores devueltos

Devuelve una matriz de matrices asociativas con las siguientes claves para cada recipiente:

|  |  |
|----|----|
| `display` | El nombre del recipiente, para propósitos de muestra. Si esta parte no es definida para un recipiente, esta clave contendrá el mismo valor que `address`. |
| `address` | La dirección de correo electrónico |
| `is_group` | `true` si el recipiente es un grupo de noticias, `false` de lo contrario. |

## Ejemplos

Ejemplo de `mailparse_rfc822_parse_addresses`

```
<?php

$to = 'Wez Furlong <wez@example.com>, pepe@example.com';
var_dump(mailparse_rfc822_parse_addresses($to));

?>

   
```php

El ejemplo anterior mostrará:

    array(2) {
      [0]=>
      array(3) {
        ["display"]=>
        string(11) "Wez Furlong"
        ["address"]=>
        string(15) "wez@example.com"
        ["is_group"]=>
        bool(false)
      }
      [1]=>
      array(3) {
        ["display"]=>
        string(16) "pepe@example.com"
        ["address"]=>
        string(16) "pepe@example.com"
        ["is_group"]=>
        bool(false)
      }
    }
