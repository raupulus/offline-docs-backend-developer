---
title: Errores en PHP 7
source_url: https://www.php.net/manual/es/language.errors.php7.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/errors/php7.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 4bf789e98
order: 2300
---

## Errores en PHP 7

PHP 7 cambia la mayoría de los errores notificados por PHP. En lugar de notificar errores a través del mecanismo de notificación de errores tradicional de PHP 5, la mayoría de los errores ahora son notificados lanzando excepciones `Error`.

Al igual que las excepciones normales, las excepciones `Error` se propagarán hasta alcanzar el primer bloque [`catch`](#language.exceptions.catch) coincidente. Si no hay bloques coincidentes, será invocado cualquier manejador de excepciones predeterminado instalado con `set_exception_handler`, y si no hubiera ningún manejador de excepciones predeterminado, la excepción será convertida en un error fatal y será manejada como un error tradicional.

Debido a que la jerarquía de `Error` no hereda de `Exception`, el código que emplee bloques `catch (Exception $e) { ... }` para manejar excepciones no capturadas en PHP 5 encontrará que estos `Error`es no son capturados por dichos bloques. Se requiere, por tanto, un bloque `catch (Error $e) { ... }` o un manejador `set_exception_handler`.

## Jerarquía de `Error`

- `Throwable`

  - `Error`

    - `ArithmeticError`

      - `DivisionByZeroError`

    - `AssertionError`

    - `CompileError`

      - `ParseError`

    - `TypeError`

      - `ArgumentCountError`

    - `ValueError`

    - `UnhandledMatchError`

    - `FiberError`

    - `RequestParseBodyException`

  - `Exception`

    - ...
