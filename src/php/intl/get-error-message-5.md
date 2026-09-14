---
title: ResourceBundle::getErrorMessage
description: Recupera el último mensaje de error desde el haz
source_url: https://www.php.net/manual/es/resourcebundle.geterrormessage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/resourcebundle/get-error-message.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42400
---

ResourceBundle::getErrorMessage

resourcebundle_get_error_message

Recupera el último mensaje de error desde el haz

## Descripción

Estilo orientado a objetos

```php
public ResourceBundle::getErrorMessage(): string
```php

Estilo procedimental

```php
resourcebundle_get_error_message(ResourceBundle $bundle): string
```

Recupera el mensaje de error desde la última función ejecutada sobre el objeto del haz.

## Parámetros

`bundle`  
Un objeto `ResourceBundle`.

## Valores devueltos

Devuelve el mensaje de error desde la última llamada sobre el objeto del haz.

## Ejemplos

Ejemplo con `resourcebundle_get_error_message`

```php
<?php
$r = resourcebundle_create( 'es', "/usr/share/data/myapp");
echo $r['somestring'];
if(intl_is_failure(resourcebundle_get_error_code($r))) {
    report_error("Error en el haz : ".resourcebundle_get_error_message($r));
}
?>

   
```

Ejemplo orientado a objetos

```php
<?php
$r = new ResourceBundle( 'es', "/usr/share/data/myapp");
echo $r['somestring'];
if(intl_is_failure(ResourceBundle::getErrorCode($r))) {
    report_error("Error en el haz : ".ResourceBundle::getErrorMessage($r));
}
?>

   
```

## Véase también

`resourcebundle_get_error_code`, `intl_get_error_code`, `intl_is_failure`
