---
title: ResourceBundle::getErrorCode
description: Recupera el último código de error del haz
source_url: https://www.php.net/manual/es/resourcebundle.geterrorcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/resourcebundle/get-error-code.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42390
---

ResourceBundle::getErrorCode

resourcebundle_get_error_code

Recupera el último código de error del haz

## Descripción

Estilo orientado a objetos

```php
public ResourceBundle::getErrorCode(): int
```php

Estilo procedimental

```php
resourcebundle_get_error_code(ResourceBundle $bundle): int
```

Recupera el último código de error desde la última función ejecutada sobre el objeto que representa el haz.

## Parámetros

`bundle`  
Un objeto `ResourceBundle`.

## Valores devueltos

Devuelve el código de error desde la última llamada al objeto que representa el haz.

## Ejemplos

Ejemplo con `resourcebundle_get_error_code`

```php
<?php
$r = resourcebundle_create( 'es', "/usr/share/data/myapp");
echo $r['somestring'];
if(intl_is_failure(resourcebundle_get_error_code($r))) {
    report_error("Error en el haz");
}
?>

   
```

Ejemplo orientado a objetos

```php
<?php
$r = new ResourceBundle( 'es', "/usr/share/data/myapp");
echo $r['somestring'];
if(intl_is_failure(ResourceBundle::getErrorCode($r))) {
    report_error("Error en el haz");
}
?>

   
```

## Véase también

`resourcebundle_get_error_message`, `intl_get_error_code`, `intl_is_failure`
