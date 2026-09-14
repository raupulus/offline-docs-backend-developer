---
title: Instalación
source_url: https://www.php.net/manual/es/pcre.installation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_reviewed: false
translation_revision: 62a00eed7
order: 61540
---

## Instalación

La extensión PCRE es una extensión nativa de PHP, por lo que siempre está activada. Por omisión, esta extensión se compila utilizando la biblioteca PCRE empaquetada. Opcionalmente, puede utilizarse una biblioteca PCRE externa pasando la opción de configuración `--with-pcre-regex=DIR` donde `DIR` es la ruta de acceso a los ficheros de la biblioteca PCRE. Se recomienda utilizar PCRE 8.10 o más reciente; a partir de PHP 7.3.0, PCRE2 es requerido.

La compilación Just In Time (JIT) de PCRE es soportada por omisión, pudiendo ser desactivada con la opción de configuración `--without-pcre-jit` a partir de PHP 7.0.12.

La versión Windows de PHP dispone del soporte automático de esta extensión. No es necesario añadir ninguna biblioteca adicional para disponer de estas funciones.

PCRE es un proyecto activo y a medida que cambia, las funcionalidades de PHP también lo hacen. Es posible que algunas partes del manual de PHP estén obsoletas y no cubran las nuevas funcionalidades proporcionadas por PCRE. Para una lista de modificaciones, consúltese el [registro de cambios de la biblioteca PCRE](http://www.pcre.org/original/changelog.txt) así como el historial siguiente de la versión PCRE incluida en PHP:

| Versión PHP | Versión PCRE actualizada | Notas |
|----|----|----|
| 8.2.0 | 10.40 |  |
| 8.1.0 | 10.39 |  |
| 7.4.12, 8.0.0 | 10.35 |  |
| 7.4.6 | 10.34 |  |
| 7.4.0 | 10.33 |  |
| 7.3.0 | 10.32 |  |
| 7.2.0 | 8.41 |  |
| 7.0.3 | 8.38 | Ver CVE-2015-8383, CVE-2015-8386, CVE-2015-8387, CVE-2015-8389, CVE-2015-8390, CVE-2015-8391, CVE-2015-8393, CVE-2015-8394 |
| 7.0.0 | 8.37 | Ver CVE-2015-2325, CVE-2015-2326 |

Historial de actualizaciones de la biblioteca PCRE incluida en PHP
