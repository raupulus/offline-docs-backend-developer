---
title: gnupg_gettrustlist
description: Busca los elementos de confianza
source_url: https://www.php.net/manual/es/function.gnupg-gettrustlist.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-gettrustlist.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: true
translation_revision: a148eb08b
order: 29110
---

gnupg_gettrustlist

Busca los elementos de confianza

## Descripción

```php
gnupg_gettrustlist(resource $identifier, string $pattern): array
```php

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`pattern`  
Una expresión para limitar la lista de elementos de confianza a los elementos que coinciden con el patrón.

## Valores devueltos

En caso de éxito, esta función devuelve un array de elementos de confianza. En caso de error, esta función devuelve `null`.

## Ejemplos

Ejemplo procedimental `gnupg_gettrustlist`

```
<?php
$res = gnupg_init();
$items = gnupg_gettrustlist($res);
print_r($items);
?>

    
```php

Ejemplo orientado a objetos `gnupg_gettrustlist`

```
<?php
$gpg = new gnupg();
$items = $gpg->gettrustlist();
print_r($items);
?>

    
```php
