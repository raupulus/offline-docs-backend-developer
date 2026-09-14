---
title: El atributo SensitiveParameter
source_url: https://www.php.net/manual/es/class.sensitiveparameter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/attributes/sensitiveparameter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 77325b622
order: 2980
---

## Introducción

Este atributo se utiliza para marcar un parámetro que es sensible y cuya valor debe ser censurado si está presente en un rastro de pila.

## Sinopsis de la clase

\#\[\Attribute\]

final

SensitiveParameter

Métodos

## Ejemplos

```php
<?php

function defaultBehavior(
    string $secret,
    string $normal
) {
    throw new Exception('Error!');
}

function sensitiveParametersWithAttribute(
    #[\SensitiveParameter]
    string $secret,
    string $normal
) {
    throw new Exception('Error!');
}

try {
    defaultBehavior('password', 'normal');
} catch (Exception $e) {
    echo $e, PHP_EOL, PHP_EOL;
}

try {
    sensitiveParametersWithAttribute('password', 'normal');
} catch (Exception $e) {
    echo $e, PHP_EOL, PHP_EOL;
}

?>

    
```

Resultado del ejemplo anterior en PHP 8.2 es similar a:

    Exception: Error! in example.php:7
    Stack trace:
    #0 example.php(19): defaultBehavior('password', 'normal')
    #1 {main}

    Exception: Error! in example.php:15
    Stack trace:
    #0 example.php(25): sensitiveParametersWithAttribute(Object(SensitiveParameterValue), 'normal')
    #1 {main}

## Véase también

[Visión general de los atributos](#language.attributes), `SensitiveParameterValue`
