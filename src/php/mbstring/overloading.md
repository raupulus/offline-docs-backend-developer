---
title: Función de sobrecarga
source_url: https://www.php.net/manual/es/mbstring.overload.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/overloading.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: 3f1dbc451
order: 45640
---

## Función de sobrecarga

> [!WARNING]
> Esta funcionalidad está *OBSOLETA* a partir de PHP 7.2.0, y *ELIMINADA* a partir de PHP 8.0.0. Depender de esta funcionalidad está altamente desaconsejado.

Puede resultar difícil lograr que una aplicación PHP existente funcione en un entorno multibyte determinado. Esto se debe a que la mayoría de las aplicaciones PHP están escritas con funciones de string estándar como `substr`, que es conocida por no manejar correctamente los strings codificados en multibyte.

mbstring admite la sobrecarga de funciones, lo que permite añadir compatibilidad con multibyte a este tipo de aplicaciones sin modificar el código, mediante la sobrecarga de las funciones equivalentes para multibyte en las funciones de string estándar. Por ejemplo, si la sobrecarga de funciones está habilitada, se llama a `mb_substr` en lugar de a `substr`. Esta característica facilita la migración de aplicaciones que solo admiten codificaciones de un solo byte a un entorno multibyte en muchos casos.

Para utilizar la sobrecarga de funciones, establezca `mbstring.func_overload`, en el `php.ini`, a un valor positivo que represente una combinación de máscaras de bits especificando las categorías de funciones a sobrecargar. Debe ser definido a 1 para sobrecargar la función `mail`, 2 para las funciones de strings, 4 para las funciones de expresiones regulares. Por ejemplo, con el valor 7, todas las funciones anteriores serán sobrecargadas. A continuación se muestra la lista de funciones sobrecargadas.

| Valor de mbstring.func_overload | Función original | Función de reemplazo |
|---------------------------------|------------------|----------------------|
| 1                               | `mail`           | `mb_send_mail`       |
| 2                               | `strlen`         | `mb_strlen`          |
| 2                               | `strpos`         | `mb_strpos`          |
| 2                               | `strrpos`        | `mb_strrpos`         |
| 2                               | `substr`         | `mb_substr`          |
| 2                               | `strtolower`     | `mb_strtolower`      |
| 2                               | `strtoupper`     | `mb_strtoupper`      |
| 2                               | `stripos`        | `mb_stripos`         |
| 2                               | `strripos`       | `mb_strripos`        |
| 2                               | `strstr`         | `mb_strstr`          |
| 2                               | `stristr`        | `mb_stristr`         |
| 2                               | `strrchr`        | `mb_strrchr`         |
| 2                               | `substr_count`   | `mb_substr_count`    |

Funciones de reemplazo

> [!NOTE]
> No se recomienda utilizar la opción de sobrecarga de funciones en el contexto por directorio, ya que aún no se ha confirmado que sea lo suficientemente estable en un entorno de producción y puede provocar un comportamiento indefinido.
