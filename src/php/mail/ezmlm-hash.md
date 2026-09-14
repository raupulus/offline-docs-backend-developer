---
title: ezmlm_hash
description: Calcula el hash solicitado por EZMLM
source_url: https://www.php.net/manual/es/function.ezmlm-hash.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mail/functions/ezmlm-hash.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mail
translation_status: ready
translation_reviewed: true
translation_revision: f112cc1ec
order: 44250
---

ezmlm_hash

Calcula el hash solicitado por EZMLM

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.4.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
ezmlm_hash(string $addr): int
```php

`ezmlm_hash` calcula el hash necesario durante la gestión de listas de difusión EZMLM con una base de datos MySQL.

## Parámetros

`addr`  
La dirección de correo electrónico que debe ser hasheada.

## Valores devueltos

El valor del hash de `addr`.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | Esta función ha sido eliminada. |
| 7.2.0   | Esta función está obsoleta.     |

## Ejemplos

Cálculo del hash y registro de un usuario de lista de difusión

```
<?php

     $user = "joecool@example.com";
     $hash = ezmlm_hash($user);
     $query = sprintf("INSERT INTO sample VALUES (%s, '%s')", $hash, $user);
     $db->query($query); // utilización de la interfaz PHPLIB

?>

    
```php
