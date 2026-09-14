---
title: Ejemplos
source_url: https://www.php.net/manual/es/rnp.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rnp/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rnp
translation_status: ready
translation_reviewed: false
translation_revision: 462b2bc55
order: 72070
---

## Ejemplos

## Texto firmado en claro

Este ejemplo va a firmar en claro un texto dado.

Ejemplo de firma RNP en claro

```php
<?php
// inicializa el objeto FFI
$ffi = rnp_ffi_create('GPG', 'GPG');

// genera una clave RSA
$key = rnp_op_generate_key($ffi, 'test@example.com', 'RSA');

// firma
$data = "Example text to sign";
$signature = rnp_op_sign_cleartext($ffi, $data, array($key));

echo $signature;

// destruye el objeto FFI
rnp_ffi_destroy($ffi);
?>

   
```
