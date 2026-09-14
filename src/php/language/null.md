---
title: 'NULL'
source_url: https://www.php.net/manual/es/language.types.null.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/null.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 3f1dbc451
order: 4480
---

## NULL

El tipo `null` es el tipo unidad de PHP, es decir, que solo tiene un valor: `null`.

Las variables no definidas y `unset` tendrán el valor `null`.

## Sintaxis

Solo hay un valor de tipo `null`, y es la constante insensible a mayúsculas y minúsculas `null`.

```php
<?php
$var = NULL;
?>

   
```

## Conversión a `null`

> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 7.2.0, y *ELIMINADA* a partir de PHP 8.0.0. Depender de esta funcionalidad está altamente desaconsejado.

Convertir una variable a `null` utilizando la sintaxis `(unset) $var` *no borrará* la variable, ni sobrescribirá su valor. Solo devolverá el valor `null`.

## Véase también

`is_null`, `unset`
