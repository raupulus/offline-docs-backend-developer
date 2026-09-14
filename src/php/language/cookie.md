---
title: $_COOKIE
description: Cookies HTTP
source_url: https://www.php.net/manual/es/reserved.variables.cookies.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/variables/cookie.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: a6d209f4f
order: 4130
---

\$\_COOKIE

Cookies HTTP

## Descripción

Una variable tipo `array` asociativo de variables pasadas al script actual a través de Cookies HTTP.

## Ejemplos

Ejemplo de `$_COOKIE`

```php
<?php
echo '¡Hola ' . htmlspecialchars($_COOKIE["nombre"]) . '!';
?>

    
```

Asumiendo que la cookie "nombre" ha sido definida anteriormente

Resultado del ejemplo anterior es similar a:

    ¡Hola Juan!

## Notas

> [!NOTE]
> Esto es una 'superglobal', o variable global automática. Esto significa simplemente que esta variable está disponible en todos los contextos del script. No es necesario hacer `global $variable;` para acceder a ella en las funciones o los métodos.

## Véase también

`setcookie`, [Gestión de variables externas](#language.variables.external), [La extensión filter](#book.filter)
