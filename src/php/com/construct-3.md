---
title: dotnet::__construct
description: Constructor de la clase dotnet
source_url: https://www.php.net/manual/es/dotnet.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/dotnet/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 7640
---

dotnet::\_\_construct

Constructor de la clase dotnet

## Descripción

```php
public dotnet::__construct(string $assembly_name, string $datatype_name, [int $codepage])
```php

Construye un nuevo objeto dotnet.

## Parámetros

`assembly_name`  
Especifica el ensamblado que debe ser cargado.

`datatype_name`  
Especifica la clase en este ensamblado a instanciar.

`codepage`  
Codepage a utilizar para las transformaciones de `string` unicode; ver la clase [???](#class.com) para más detalles sobre los codepages.
