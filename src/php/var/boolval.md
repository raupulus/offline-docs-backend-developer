---
title: boolval
description: Obtiene el valor booleano de una variable
source_url: https://www.php.net/manual/es/function.boolval.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/boolval.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 100440
---

boolval

Obtiene el valor booleano de una variable

## Descripción

```php
boolval(mixed $value): bool
```php

Devuelve el valor `bool` de la variable proporcionada en el argumento `value`.

## Parámetros

`value`  
El valor escalar que será convertido a `bool`.

## Valores devueltos

El valor `bool` del argumento `value`.

## Ejemplos

Ejemplo con `boolval`

```
<?php
echo '0:        '.(boolval(0) ? 'true' : 'false')."\n";
echo '42:       '.(boolval(42) ? 'true' : 'false')."\n";
echo '0.0:      '.(boolval(0.0) ? 'true' : 'false')."\n";
echo '4.2:      '.(boolval(4.2) ? 'true' : 'false')."\n";
echo '"":       '.(boolval("") ? 'true' : 'false')."\n";
echo '"string": '.(boolval("string") ? 'true' : 'false')."\n";
echo '"0":      '.(boolval("0") ? 'true' : 'false')."\n";
echo '"1":      '.(boolval("1") ? 'true' : 'false')."\n";
echo '[1, 2]:   '.(boolval([1, 2]) ? 'true' : 'false')."\n";
echo '[]:       '.(boolval([]) ? 'true' : 'false')."\n";
echo 'stdClass: '.(boolval(new stdClass) ? 'true' : 'false')."\n";
?>

    
```php

El ejemplo anterior mostrará:

    0:        false
    42:       true
    0.0:      false
    4.2:      true
    "":       false
    "string": true
    "0":      false
    "1":      true
    [1, 2]:   true
    []:       false
    stdClass: true

## Véase también

`floatval`, `intval`, `strval`, `settype`, `is_bool`, El [manipulación de tipos](#language.types.type-juggling)
