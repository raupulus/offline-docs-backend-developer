---
title: tidy_error_count
description: Devuelve el número de errores Tidy encontrados en un documento dado
source_url: https://www.php.net/manual/es/function.tidy-error-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/functions/tidy-error-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 04f10f9f8
order: 93930
---

tidy_error_count

Devuelve el número de errores Tidy encontrados en un documento dado

## Descripción

```php
tidy_error_count(tidy $tidy): int
```php

Devuelve el número de errores Tidy encontrados en un documento específico.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Devuelve el número de errores.

## Ejemplos

Ejemplo de la función `tidy_error_count`

```
<?php
$html = '<p>test</i>
<bogustag>bogus</bogustag>';

$tidy = tidy_parse_string($html);

echo tidy_error_count($tidy) . "\n"; //1

echo $tidy->errorBuffer;
?>

    
```php

El ejemplo anterior mostrará:

    1
    line 1 column 1 - Warning: missing <!DOCTYPE> declaration
    line 1 column 8 - Warning: discarding unexpected </i>
    line 2 column 1 - Error: <bogustag> is not recognized!
    line 2 column 1 - Warning: discarding unexpected <bogustag>
    line 2 column 16 - Warning: discarding unexpected </bogustag>
    line 1 column 1 - Warning: inserting missing 'title' element

## Véase también

tidy_access_count

tidy_warning_count
