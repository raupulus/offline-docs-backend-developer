---
title: La clase Parle\ErrorInfo
source_url: https://www.php.net/manual/es/class.parle-errorinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle.errorinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 60970
---

## Introducción

La clase representa la información detallada de los errores, tal como se proporciona por el método Parle\Parser::errorInfo

## Sinopsis de la clase

Parle\ErrorInfo

Parle\ErrorInfo

Propiedades

public

int

id

public

int

position

public

mixed

token

Métodos

## Propiedades

`id`  
Identificador del error.

`position`  
Posición en la entrada donde ocurrió el error.

`token`  
Si es aplicable, la clase `Parle\Token` relativa al error, de lo contrario `null`.
