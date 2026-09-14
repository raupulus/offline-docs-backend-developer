---
title: gnupg_listsignatures
description: Lista las firmas de clave
source_url: https://www.php.net/manual/es/function.gnupg-listsignatures.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-listsignatures.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: true
translation_revision: a148eb08b
order: 29150
---

gnupg_listsignatures

Lista las firmas de clave

## Descripción

```php
gnupg_listsignatures(resource $identifier, string $keyid): array
```php

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`keyid`  
El identificador de clave para listar las firmas.

## Valores devueltos

En caso de éxito, esta función devuelve un array de firmas de clave. En caso de error, esta función devuelve `null`.

## Ejemplos

Ejemplo procedimental `gnupg_listsignatures`

```
<?php
$res = gnupg_init();
$signatures = gnupg_listsignatures($res, "8660281B6051D071D94B5B230549F9DC851566DC");
print_r($signatures);
?>

    
```php

Ejemplo orientado a objetos `gnupg_listsignatures`

```
<?php
$gpg = new gnupg();
$signatures = $gpg->listsignatures("8660281B6051D071D94B5B230549F9DC851566DC");
print_r($signatures);
?>

    
```php
