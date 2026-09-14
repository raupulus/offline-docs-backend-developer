---
title: tidy_warning_count
description: Devuelve el número de alertas encontradas en un documento dado
source_url: https://www.php.net/manual/es/function.tidy-warning-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/functions/tidy-warning-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 04f10f9f8
order: 93950
---

tidy_warning_count

Devuelve el número de alertas encontradas en un documento dado

## Descripción

```php
tidy_warning_count(tidy $tidy): int
```php

Devuelve el número de alertas Tidy encontradas en un documento específicado.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Devuelve el número de alertas.

## Ejemplos

Ejemplo de la función `tidy_warning_count`

```
<?php
$html = '<p>test</i>
<bogustag>bogus</bogustag>';

$tidy = tidy_parse_string($html);

echo tidy_error_count($tidy) . "\n"; //1
echo tidy_warning_count($tidy) . "\n"; //5
?>

    
```php

## Véase también

`tidy_error_count`, `tidy_access_count`
