---
title: Ejemplos
source_url: https://www.php.net/manual/es/mhash.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mhash/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mhash
translation_status: ready
translation_reviewed: false
translation_revision: a164d0139
order: 46920
---

## Ejemplos

Calcule el MD5 y el hmac, luego lo muestra como un hexadecimal

```php
<?php
$input = "what do ya want for nothing?";
$hash = mhash(MHASH_MD5, $input);
echo "El hash vale " . bin2hex($hash) . "<br />\n";
$hash = mhash(MHASH_MD5, $input, "Jefe");
echo "El hmac vale " . bin2hex($hash) . "<br />\n";
?>

   
```

El ejemplo anterior mostrará:

    El hash vale d03cb659cbf9192dcd066272249f8412
    El hmac vale 750c783e6ab0b503eaa86e310a5db738
