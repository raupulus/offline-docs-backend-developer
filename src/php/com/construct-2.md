---
title: COMPersistHelper::__construct
description: Construye un objeto COMPersistHelper
source_url: https://www.php.net/manual/es/compersisthelper.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/compersisthelper/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 49ff12041
order: 7540
---

COMPersistHelper::\_\_construct

Construye un objeto COMPersistHelper

## Descripción

```php
public COMPersistHelper::__construct([variant $variant])
```php

Construye un objeto de ayuda a la persistencia, generalmente asociado a un `variant`.

## Parámetros

`variant`  
Un objeto COM que implementa IDispatch. Para poder llamar con éxito a uno de los métodos de `COMPersistHelper`, el objeto debe implementar IPersistFile, IPersistStream y/o IPersistStreamInit.

Pasar `null` como `variant` solo es útil si el objeto debe ser cargado desde un stream llamando a COMPersistHelper::LoadFromStream.
