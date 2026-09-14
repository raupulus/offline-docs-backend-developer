---
title: gnupg_export
description: Exporta una clave
source_url: https://www.php.net/manual/es/function.gnupg-export.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gnupg/functions/gnupg-export.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gnupg
translation_status: ready
translation_reviewed: false
translation_revision: a148eb08b
order: 29060
---

gnupg_export

Exporta una clave

## Descripción

```php
gnupg_export(resource $identifier, string $fingerprint): string
```php

Exporta la clave `fingerprint`.

## Parámetros

`identifier`  
El identificador gnupg, generado por una llamada a la función `gnupg_init` o a la función `gnupg`.

`fingerprint`  
La huella de la clave.

## Valores devueltos

En caso de éxito, esta función devuelve los datos de la clave. En caso de fallo, esta función devuelve `false`.

## Ejemplos

Ejemplo con `gnupg_export` (Estilo procedimental)

```
<?php
$res = gnupg_init();
$export = gnupg_export($res,"8660281B6051D071D94B5B230549F9DC851566DC");
echo $export;
?>

    
```php

Ejemplo con `gnupg_export` (Estilo orientado a objetos)

```
<?php
$gpg = new gnupg();
$export = $gpg->export("8660281B6051D071D94B5B230549F9DC851566DC");
?>

    
```php
