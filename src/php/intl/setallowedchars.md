---
title: Spoofchecker::setAllowedChars
description: Define el conjunto de caracteres permitidos al ejecutar las comprobaciones
source_url: https://www.php.net/manual/es/spoofchecker.setallowedchars.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/spoofchecker/setallowedchars.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: 20687bf9c
order: 42480
---

Spoofchecker::setAllowedChars

Define el conjunto de caracteres permitidos al ejecutar las comprobaciones

## Descripción

```php
public Spoofchecker::setAllowedChars(string $pattern, [int $patternOptions]): void
```php

Restringe los caracteres que las comprobaciones posteriores consideran aceptables al conjunto descrito por `pattern`. Cualquier carácter fuera de este conjunto provoca que Spoofchecker::isSuspicious reporte un resultado.

## Parámetros

`pattern`  
Un conjunto de caracteres descrito como un patrón `UnicodeSet`, es decir, una clase de caracteres al estilo de las expresiones regulares. Debe comenzar con `[` y terminar con `]`, por ejemplo `[a-z0-9]`.

`patternOptions`  
Una máscara de bits que controla cómo se interpreta `pattern`. Debe ser `0`, o `Spoofchecker::IGNORE_SPACE` por sí solo o combinado con exactamente uno de `Spoofchecker::CASE_INSENSITIVE`, `Spoofchecker::ADD_CASE_MAPPINGS` o `Spoofchecker::SIMPLE_CASE_INSENSITIVE`.

## Valores devueltos

No se devuelve ningún valor.

## Errores/Excepciones

Lanza un ValueError si `pattern` no es un patrón de conjunto de caracteres válido, o si `patternOptions` no es una combinación de opciones válida.

## Ejemplos

Ejemplo de Spoofchecker::setAllowedChars

```
<?php
$checker = new Spoofchecker();
$checker->setAllowedChars('[a-z0-9]');

var_dump($checker->isSuspicious('hello'));
var_dump($checker->isSuspicious('héllo'));
?>

   
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

Spoofchecker::setAllowedLocales

Spoofchecker::isSuspicious
