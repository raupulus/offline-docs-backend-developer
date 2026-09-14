---
title: V8Js::registerExtension
description: Registra extensiones Javascript para V8Js
source_url: https://www.php.net/manual/es/v8js.registerextension.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/v8js/v8js/registerextension.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: v8js
translation_status: ready
translation_revision: 04b11e621
order: 100370
---

V8Js::registerExtension

Registra extensiones Javascript para V8Js

## Descripción

```php
public static V8Js::registerExtension(string $extension_name, string $script, [array $dependencies], [bool $auto_enable]): bool
```php

Registra el código Javascript pasado por el argumento `script` como extensión para ser utilizada en los contextos `V8Js`.

## Parámetros

`extension_name`  
Nombre de la extensión a registrar.

`script`  
El código Javascript a registrar.

`dependencies`  
Un array de nombres de extensiones de las que depende la extensión que se está registrando. Cada una de ellas será activada automáticamente al cargar esta extensión.

> [!NOTE]
> Todas las extensiones, incluyendo las dependencias, deben ser registradas antes de la creación de cualquier objeto `V8Js` que las utilice.

`auto_enable`  
Si se establece en `true`, la extensión será activada automáticamente en todos los contextos `V8Js`.

## Valores devueltos

Devuelve `true` si la extensión se ha registrado con éxito, `false` en caso contrario.
