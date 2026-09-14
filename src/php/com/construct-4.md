---
title: variant::__construct
description: Constructor de la clase variant
source_url: https://www.php.net/manual/es/variant.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/variant/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 89ae180a8
order: 8020
---

variant::\_\_construct

Constructor de la clase variant

## Descripción

```php
public variant::__construct([mixed $value], [int $type], [int $codepage])
```php

Construye un nuevo objeto variant.

## Parámetros

`value`  
Valor inicial. Si se omite, o se establece en `null`, se crea un objeto VT_EMPTY vacío.

`type`  
Especifica el tipo de contenido del objeto variant. Los valores posibles son una de las constantes `VT_*` [???](#com.constants).

PHP puede detectar los argumentos pasados por referencia automáticamente; No necesitan ser pasados como objetos variant.

Consulte la biblioteca MSDN para obtener información adicional sobre el tipo VARIANT.

`codepage`  
Especifica la codepage que se utiliza para convertir los `string` a unicode. Vea el argumento con el mismo nombre en la clase [???](#class.com) para más información.
