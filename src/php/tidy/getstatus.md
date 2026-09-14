---
title: tidy::getStatus
description: Obtiene el status de un documento especificado
source_url: https://www.php.net/manual/es/tidy.getstatus.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/getstatus.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 2b84fa46e
order: 94080
---

tidy::getStatus

tidy_get_status

Obtiene el status de un documento especificado

## Descripción

Estilo orientado a objetos

```php
public tidy::getStatus(): int
```php

Estilo procedimental

```php
tidy_get_status(tidy $tidy): int
```

Devuelve el status del objeto `tidy` tidy especificado.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Devuelve 0 si no hay errores/alertas, 1 para alertas de accesibilidad, o 2 para los errores.

## Ejemplos

Ejemplo de `tidy::getStatus`

```php
<?php
$html = '<p>paragraph</i>';
$tidy = new tidy();
$tidy->parseString($html);

$tidy2 = new tidy();
$html2 = '<bogus>test</bogus>';
$tidy2->parseString($html2);

echo $tidy->getStatus(); //1

echo $tidy2->getStatus(); //2
?>

    
```
