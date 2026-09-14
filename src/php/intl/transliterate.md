---
title: Transliterator::transliterate
description: Translittera un string
source_url: https://www.php.net/manual/es/transliterator.transliterate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/transliterator/transliterate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42600
---

Transliterator::transliterate

transliterator_transliterate

Translittera un string

## Descripción

Estilo orientado a objetos

```php
public Transliterator::transliterate(string $string, [int $start], [int $end]): string
```php

Estilo procedimental

```php
transliterator_transliterate(Transliterator $transliterator, string $string, [int $start], [int $end]): string
```

Transforma un string o solo una parte utilizando un translitterador ICU.

## Parámetros

`transliterator`  
En la versión procedimental, un `Transliterator` o un string desde el cual puede construirse un `Transliterator`.

`string`  
El string a transformar.

`start`  
El índice de inicio (en unidades UTF-16) desde el cual la cadena comenzará a transformarse, inclusivo. Los índices comienzan en 0. El texto antes de este índice permanecerá sin cambios.

`end`  
El índice de fin (en unidades UTF-16) que indica el final de la transformación, exclusivo. Los índices comienzan en 0. El texto después de este índice permanecerá sin cambios.

## Valores devueltos

El string transformado en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Conversión de escapamientos en unidades UTF-16

```php
<?php
$s = "\u304A\u65E9\u3046\u3054\u3056\u3044\u307E\u3059";
echo transliterator_transliterate("Hex-Any/Java", $s), "\n";

//ahora, la operación inversa con un carácter adicional
$supplChar = html_entity_decode('&#x1D11E;');
echo mb_strlen($supplChar, "UTF-8"), "\n";
$encSupplChar = transliterator_transliterate("Any-Hex/Java", $supplChar);
//muestra 2 unidades UTF-16 codificadas
echo $encSupplChar, "\n";
//y el retorno...
echo transliterator_transliterate("Hex-Any/Java", $encSupplChar), "\n";
?>

     
```

Resultado del ejemplo anterior es similar a:

    お早うございます
    1
    \uD834\uDD1E
    𝄞

## Véase también

Transliterator::getErrorMessage, Transliterator::\_\_construct
