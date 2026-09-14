---
title: La clase Uri\WhatWg\InvalidUrlException
source_url: https://www.php.net/manual/es/class.uri-whatwg-invalidurlexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri.whatwg.invalidurlexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 8a341f6c4
order: 100140
---

## Introducción

Indica que una URL dada es inválida o que una operación resultaría en una URL inválida según el [estándar WHATWG URL](https://url.spec.whatwg.org/).

## Sinopsis de la clase

Uri\WhatWg

InvalidUrlException

extends

Uri\InvalidUriException

Propiedades

public

readonly

array

errors

Propiedades heredadas

Métodos

Métodos heredados

## Propiedades

`errors`  
Un `array` de objetos `Uri\WhatWg\UrlValidationError`.
