---
title: Operador de control de errores
source_url: https://www.php.net/manual/es/language.operators.errorcontrol.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/operators/errorcontrol.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 16934048f
order: 2700
---

## Operador de control de errores

PHP soporta un operador de control de errores: el arroba (`@`). Cuando este operador se añade como prefijo a una expresión PHP, los diagnósticos de errores que pueden ser generados por esta expresión serán ignorados.

Si un gestor de errores personalizado es definido con `set_error_handler`, será llamado aún si el diagnóstico ha sido ignorado.

> [!WARNING]
> Anterior a PHP 8.0.0, la función `error_reporting` llamada en el gestor de errores personalizado siempre retornaba `0` si el error fue ignorado con el operador `@`. A partir de 8.0.0, retorna el valor de esta expresión (bit a bit): `E_ERROR | E_CORE_ERROR | E_COMPILE_ERROR | E_USER_ERROR | E_RECOVERABLE_ERROR | E_PARSE`.

Todos los mensajes de error generados por la expresión están disponibles en el elemento `"message"` del array retornado por la función `error_get_last`. El resultado de la función cambiará con cada error, por lo tanto, es conveniente verificarlo frecuentemente.

Error de fichero intencional

```php
    
<?php
$mon_fichier = @file ('non_persistent_file') or
    die ("Imposible abrir el fichero: El error es: '" . error_get_last()['message'] . "'");
?>

   
```

La expresión de eliminación

```php
<?php
// Esto funciona con cualquier expresión, no solo con funciones
  $value = @$cache[$key];
// la línea anterior no mostrará una alerta si la clave $key del array no existe
?>

   
```

> [!NOTE]
> El operador `@` solo funciona con las [expresiones](#language.expressions). La regla general es: si es posible tomar el valor de algo, entonces se puede preponer el operador `@` a este. Por ejemplo, puede ser prepuesto a variables, llamadas de funciones, ciertas llamadas a construcciones de lenguaje (por ejemplo, `include`), etc. No puede ser prepuesto a definiciones de funciones o clases o estructuras condicionales como `if` y [`foreach`](#control-structures.foreach), etc.

> [!WARNING]
> Anterior a PHP 8.0.0, era posible que el operador `@` desactivara los errores críticos que terminaban la ejecución del script. Por ejemplo, preponer `@` a una llamada de una función que no existe, que esté indisponible o mal escrita, causaba que el script terminara sin ninguna indicación de por qué.

## Véase también

`error_reporting`, [Gestión de Errores y Funciones de Logging](#ref.errorfunc)
