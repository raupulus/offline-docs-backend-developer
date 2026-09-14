---
title: imap_rfc822_parse_adrlist
description: Analiza una dirección de correo electrónico
source_url: https://www.php.net/manual/es/function.imap-rfc822-parse-adrlist.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-rfc822-parse-adrlist.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: e2f50c240
order: 38460
---

imap_rfc822_parse_adrlist

Analiza una dirección de correo electrónico

## Descripción

```php
imap_rfc822_parse_adrlist(string $string, string $default_hostname): array
```php

Analiza la cadena `address`, tal como se define en la [RFC2822](https://datatracker.ietf.org/doc/html/rfc2822).

## Parámetros

`string`  
Un string que contiene las direcciones

`default_hostname`  
El nombre del host por omisión

## Valores devueltos

Devuelve un array de objetos. Las propiedades de los objetos son:

- `"mailbox"` : El nombre del buzón de correo (nombre de usuario)

- `"host"` : El nombre del host

- `"personal"` : El nombre personal

- `"adl"` : ruta de origen «at-domain»

## Ejemplos

Ejemplo con `imap_rfc822_parse_adrlist`

```
<?php

$address_string = "Joe Doe <doe@example.com>, postmaster@example.com, root";
$address_array  = imap_rfc822_parse_adrlist($address_string, "example.com");
if (!is_array($address_array) || count($address_array) < 1) {
    die("¡Error!\n");
}

foreach ($address_array as $id => $val) {
    echo "# $id\n";
    echo "  Buzón   : " . $val->mailbox . "\n";
    echo "  Host    : " . $val->host . "\n";
    echo "  Nombre  : " . $val->personal . "\n";
    echo "  adl     : " . $val->adl . "\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    # 0
      Buzón   : doe
      Host    : example.com
      Nombre  : Joe Doe
      adl     :
    # 1
      Buzón   : postmaster
      Host    : example.com
      Nombre  :
      adl     :
    # 2
      Buzón   : root
      Host    : example.com
      Nombre  :
      adl     :

## Véase también

`imap_rfc822_parse_headers`
