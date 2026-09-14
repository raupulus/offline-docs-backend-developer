---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/openssl.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/openssl/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: openssl
translation_status: ready
translation_revision: 244c78863
order: 59650
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre         | Por defecto | Cambiable    | Historial de cambios |
|----------------|-------------|--------------|----------------------|
| openssl.cafile | ""          | `INI_PERDIR` |                      |
| openssl.capath | ""          | `INI_PERDIR` |                      |
| openssl.libctx | "custom"    | `INI_PERDIR` |                      |

openssl Opciones de configuración

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`openssl.cafile` `string`  
Ubicación del archivo de Autoridad de Certificación en el sistema de archivos local que debería ser utilizado con la opción de contexto verify_peer para autenticar la identidad del par remoto.

`openssl.capath` `string`  
Si cafile no está especificado o si el certificado no es encontrado allí, el directorio apuntado por capath es examinado para encontrar un certificado adecuado. capath debe ser un directorio de certificados correctamente hasheado.

`openssl.libctx` `string`  
Especifica el tipo de contexto de biblioteca OpenSSL que se utilizará. El valor predeterminado, `custom`, crea un contexto de biblioteca independiente para cada worker o subproceso. Esto mejora el aislamiento de otras bibliotecas que utilizan OpenSSL y, en compilaciones ZTS, aumenta la separación entre subprocesos. También es posible usar el valor `default`, que hace que PHP utilice el contexto de biblioteca predeterminado global de OpenSSL.

Ver también las opciones del [contexto de flujo SSL](#context.ssl).
