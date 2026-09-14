---
title: Ejemplos
source_url: https://www.php.net/manual/es/gmp.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gmp/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gmp
translation_status: ready
translation_revision: 9ddd75d72
order: 28340
---

## Ejemplos

Función factorial usando GMP

```php
<?php
function fact($x)
{
    $return = 1;
    for ($i=2; $i <= $x; $i++) {
        $return = gmp_mul($return, $i);
    }
    return $return;
}

echo gmp_strval(fact(1000)) . "\n";
?>

   
```

Esto va a calcular el factorial de 1000 (Un bonito gran número) muy rápido.
