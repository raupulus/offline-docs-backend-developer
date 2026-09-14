---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/yaml.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaml/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaml
translation_status: ready
translation_revision: d4d5216e7
order: 107430
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [yaml.decode_binary](#ini.yaml.decode-binary) | 0 | `INI_ALL` |  |
| [yaml.decode_php](#ini.yaml.decode-php) | 0 | `INI_ALL` | Añadido en 1.2.0, antes de 2.0.0 el valor predeterminado era 1 |
| [yaml.decode_timestamp](#ini.yaml.decode-timestamp) | 0 | `INI_ALL` |  |
| [yaml.output_canonical](#ini.yaml.output-canonical) | 0 | `INI_ALL` |  |
| [yaml.output_indent](#ini.yaml.output-indent) | 2 | `INI_ALL` |  |
| [yaml.output_width](#ini.yaml.output-width) | 80 | `INI_ALL` |  |

Opciones de configuración de Yaml

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`yaml.decode_binary` `bool`  
Off por omisión, pero puede estar activado el uso de entidades base64 codificadas binariamente que tenga explicitamente el tag "tag:yaml.org,2002:binary" para ser decodificado.

`yaml.decode_php` `bool`  
Desactivado por omisión, pero puede ser configurado como activado para que los objetos PHP serializados que tienen la etiqueta explícita "!php/object" sean deserializados.

`yaml.decode_timestamp` `int`  
Controla la decodificación de los escalares "tag:yaml.org,2002:timestamp" tanto implícitos como explícitos en el flujo del documento YAML. La configuración predeterminada de `0` no aplicará ninguna decodificación. Una configuración de `1` utilizará `strtotime` para analizar el valor de la marca de tiempo como una marca de tiempo Unix. Una configuración de `2` utilizará `date_create` para analizar el valor de la marca de tiempo como un objeto `DateTime`.

`yaml.output_canonical` `bool`  
Off por omisión, pero puede estar activado de manera convencional desde su salida.

`yaml.output_indent` `int`  
Números de espacios para la identación. El valor debe comprender entre `1` y `10`.

`yaml.output_width` `int`  
Establece el ancho de línea de preferencia. `-1` significa sin límite.
