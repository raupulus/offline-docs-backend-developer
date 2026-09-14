---
title: bindtextdomain
description: Especifica o recupera la ruta de un dominio
source_url: https://www.php.net/manual/es/function.bindtextdomain.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/gettext/functions/bindtextdomain.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: gettext
translation_status: ready
translation_reviewed: false
translation_revision: 679cf93fa
order: 26340
---

bindtextdomain

Especifica o recupera la ruta de un dominio

## Descripción

```php
bindtextdomain(string $domain, [string $directory]): string
```php

La función `bindtextdomain` define o recupera la ruta de un dominio.

## Parámetros

`domain`  
El dominio.

`directory`  
La ruta hacia el directorio. Una cadena vacía significa el directorio actual. Si `null`, se devuelve el directorio actualmente definido.

## Valores devueltos

La ruta completa para el `domain` actualmente definido, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `directory` ahora es opcional. Anteriormente, este parámetro debía ser siempre especificado. |
| 8.0.3 | `directory` ahora es nullable. Anteriormente, no era posible recuperar el directorio actualmente definido. |

## Ejemplos

Ejemplo con `bindtextdomain`

```
<?php

$domain = 'myapp';
echo bindtextdomain($domain, '/usr/share/myapp/locale');

?>

    
```php

El ejemplo anterior mostrará:

    /usr/share/myapp/locale

## Notas

> [!NOTE]
> La información `bindtextdomain` se mantiene por proceso, y no por hilo.
