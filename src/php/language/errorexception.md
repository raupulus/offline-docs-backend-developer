---
title: ErrorException
source_url: https://www.php.net/manual/es/class.errorexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/errorexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 2f3c1237b
order: 3280
---

## Introducción

Una excepción para los errores.

## Sinopsis de la clase

ErrorException

extends

Exception

Propiedades

protected

int

severity

E_ERROR

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`severity`  
La severidad de la excepción

## Ejemplos

Uso de `set_error_handler` para cambiar todos los mensajes de error en ErrorException

```php
 
<?php

set_error_handler(function (int $errno, string $errstr, string $errfile, int $errline) {
    if (!(error_reporting() & $errno)) {
        // Este código de error no está incluido en error_reporting.
        return;
    }

    if ($errno === E_DEPRECATED || $errno === E_USER_DEPRECATED) {
        // No lanzar excepción para advertencias de obsolescencia, ya que nuevas o inesperadas
        // obsolescencias podrían romper la aplicación.
        return;
    }

    throw new \ErrorException($errstr, 0, $errno, $errfile, $errline);
});

// Deserializar datos corruptos desencadena una advertencia que será convertida en
// ErrorException por el manejador de errores.
unserialize('broken data');

?>

     
```

Resultado del ejemplo anterior es similar a:

    Fatal error: Uncaught ErrorException: unserialize(): Error at offset 0 of 11 bytes in test.php:16
    Stack trace:
    #0 [internal function]: {closure}(2, 'unserialize(): ...', 'test.php', 16)
    #1 test.php(16): unserialize('broken data')
    #2 {main}
      thrown in test.php on line 16
