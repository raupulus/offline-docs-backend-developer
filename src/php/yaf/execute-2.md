---
title: Yaf_Application::execute
description: Ejecutar una llamada de retorno
source_url: https://www.php.net/manual/es/yaf-application.execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_application/execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: 9e0f03ac3
order: 104990
---

Yaf_Application::execute

Ejecutar una llamada de retorno

## Descripción

```php
public Yaf_Application::execute(callable $entry, string ...$args): void
```php

Este método normalmente se usa para ejecutar Yaf_Application en un trabajo de crontab. Hacer el trabajo de contrab también puede usar el autocargador y el mecanismo de arranque.

## Parámetros

`entry`  
Una llamada de retorno válida

`args`  
Los parámetros de se le pasarán a la llamada de retorno

## Valores devueltos

## Ejemplos

Ejemplo de `Yaf_Application::execute`

```
<?php
function main($argc, $argv) {
}

$config = array(
    "application" => array(
        "directory" => realpath(dirname(__FILE__)) . "/application",
    ),
);

/** Yaf_Application */
$application = new Yaf_Application($config);
$application->execute("main", $argc,  $argv);
?>

   
```php

Resultado del ejemplo anterior es similar a:
