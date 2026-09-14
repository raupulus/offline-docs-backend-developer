---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/filter.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filter/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filter
translation_status: ready
translation_revision: 55e2079a8
order: 24240
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [filter.default](#ini.filter.default) | "unsafe_raw" | `INI_PERDIR` | Obsoleto a partir de PHP 8.1.0. |
| [filter.default_flags](#ini.filter.default-flags) | NULL | `INI_PERDIR` |  |

Opciones de configuración de filtros

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`filter.default` `string`  
Filtra todos los datos de `$_GET`, `$_POST`, `$_COOKIE`, `$_REQUEST` y `$_SERVER`. Es posible acceder a los datos originales a través de `filter_input`.

Debe ser el nombre de un filtro que se puede determinar usando `filter_list` y `filter_id`.

> [!NOTE]
> Tenga cuidado con los flags por omisión para los filtros predeterminados. Debería establecerse de forma explicita. Por ejemplo, para configurar el filtro predeterminado para que se comporte exactamente igual que `htmlspecialchars` las flags por omisión deben establecerse a `0`, como se muestra a continuación.
>
> <div class="example">
>
> <div class="title">
>
> Configurando el filtro predeterminado para actuar como htmlspecialchars
>
> </div>
>
> ```
> filter.default = full_special_chars
> filter.default_flags = 0
>
>       
> ```
>
> </div>

> [!WARNING]
> Esta configuración INI está obsoleta a partir de PHP 8.1.0.

`filter.default_flags` `int`  
Flags aplicadas cuando se establece que usen los valores por omisión del filtro. Esto se establece a `FILTER_FLAG_NO_ENCODE_QUOTES` por omisión por razones de compatibilidad. Vea la lista de constantes para los flags disponibles.
