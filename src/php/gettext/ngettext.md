---
title: ngettext
description: Versión plural de gettext
source_url: https://www.php.net/manual/es/function.ngettext.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gettext/functions/ngettext.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gettext
translation_status: ready
translation_reviewed: false
translation_revision: ad2b7b45a
order: 26400
---

ngettext

Versión plural de gettext

## Descripción

```php
ngettext(string $singular, string $plural, int $count): string
```php

Versión plural de `gettext`. Algunas lenguas tienen más de una forma de mensajes plurales dependiendo del contador.

## Parámetros

`singular`  
El ID singular del mensaje.

`plural`  
El ID plural del mensaje.

`count`  
El número (es decir, número de elementos) para determinar la traducción del número gramatical respectivo.

## Valores devueltos

Devuelve un mensaje plural identificado por `msgid1` y `msgid2` para el contador `n`.

## Ejemplos

Ejemplo con `ngettext`

```
<?php

setlocale(LC_ALL, 'cs_CZ');
printf(ngettext("%d window", "%d windows", 1), 1); // 1 okno
printf(ngettext("%d window", "%d windows", 2), 2); // 2 okna
printf(ngettext("%d window", "%d windows", 5), 5); // 5 oken

?>

    
```php
