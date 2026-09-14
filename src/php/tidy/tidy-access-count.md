---
title: tidy_access_count
description: Devuelve el número de alertas de accesibilidad Tidy encontradas en un
  documento dado
source_url: https://www.php.net/manual/es/function.tidy-access-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/functions/tidy-access-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 04f10f9f8
order: 93910
---

tidy_access_count

Devuelve el número de alertas de accesibilidad Tidy encontradas en un documento dado

## Descripción

```php
tidy_access_count(tidy $tidy): int
```php

`tidy_access_count` devuelve el número de alertas de accesibilidad encontradas en un documento específico.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Devuelve el número de alertas.

## Ejemplos

Ejemplo de la función `tidy_access_count`

```
<?php

$html ='<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2//EN">
<html><head><title>Title</title></head>
<body>

<p><img src="img.png"></p>

</body></html>';

// Seleccione el nivel de accesibilidad a revisar: 1, 2 o 3
$config = array('accessibility-check' => 3);

$tidy = new tidy();
$tidy->parseString($html, $config);
$tidy->cleanRepair();

/* No olvide ejecutar esto! */
$tidy->diagnose();

echo tidy_access_count($tidy); //5

?>

    
```php

## Notas

> [!NOTE]
> Dado el diseño de TidyLib, se debe ejecutar `tidy_diagnose` antes de `tidy_access_count` o siempre devolverá `0`. También se necesita habilitar la opción `accessibility-check`.

## Véase también

`tidy_error_count`, `tidy_warning_count`
