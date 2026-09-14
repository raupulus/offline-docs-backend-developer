---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/mysql.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_reviewed: true
translation_revision: 40667918d
order: 52010
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

Es posible especificar opciones de cliente adicionales para las funciones `mysql_connect` y `mysql_pconnect`. Estas constantes son las siguientes:

| Constante | Descripción |
|----|----|
| `MYSQL_CLIENT_COMPRESS` | Utiliza el protocolo con compresión |
| `MYSQL_CLIENT_IGNORE_SPACE` | Permite espacios después de los nombres de función |
| `MYSQL_CLIENT_INTERACTIVE` | Permite `interactive_timeout` segundos de inactividad en la conexión (en lugar de `wait_timeout`). |
| `MYSQL_CLIENT_SSL` | Utilización de cifrado SSL. Esta constante solo está disponible a partir de la versión 4.x y posteriores de la biblioteca cliente MySQL. La versión 3.23.x se proporciona con PHP 4 así como con los binarios para Windows de PHP 5. |

Constantes de cliente MySQL {#mysql.client-flags}

La función `mysql_fetch_array` utiliza una constante para especificar los diferentes tipos de formatos de respuesta. Las constantes siguientes son utilizadas:

| Constante | Descripción |
|----|----|
| `MYSQL_ASSOC` | Las columnas son devueltas en un array cuyos índices son los nombres de columnas. |
| `MYSQL_BOTH` | Las columnas son devueltas en un array con indexación numérica y un sistema de índices correspondiente al nombre de las columnas. |
| `MYSQL_NUM` | Las columnas son devueltas en un array con un índice numérico. Las columnas están numeradas en su orden de aparición. El índice comienza en cero. |

Constantes de `mysql_fetch_array` {#mysql.constants.fetch}
