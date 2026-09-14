---
title: $_GET
description: Variables la cadena de consulta
source_url: https://www.php.net/manual/es/reserved.variables.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/variables/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: f56de7ebe
order: 4160
---

\$\_GET

Variables la cadena de consulta

## Descripción

Un array asociativo de variables pasado al script actual vía parámetros URL (también conocida como cadena de consulta). Tenga en cuenta que el array no solo se rellena para las solicitudes GET, sino para todas las solicitudes con una cadena de consulta.

## Ejemplos

Ejemplo de `$_GET`

```php
<?php
echo '¡Hola ' . htmlspecialchars($_GET["name"]) . '!';
?>

    
```

Asumiendo que el usuario introdujo `http://example.com/?name=Hannes`

Resultado del ejemplo anterior es similar a:

    ¡Hola Hannes!

## Notas

> [!NOTE]
> Esto es una 'superglobal', o variable global automática. Esto significa simplemente que esta variable está disponible en todos los contextos del script. No es necesario hacer `global $variable;` para acceder a ella en las funciones o los métodos.

> [!NOTE]
> Las valores en `$_GET` son pasados automáticamente vía `urldecode`.

## Véase también

[Manejo de variables externas](#language.variables.external), [La extensión filter](#book.filter)
