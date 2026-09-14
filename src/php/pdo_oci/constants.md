---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/pdo-oci.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_oci/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_oci
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 62420
---

## Constantes predefinidas

Las constantes a continuación son definidas por este controlador y solo estarán disponibles cuando la extensión haya sido compilada en PHP o cargada dinámicamente del motor de ejecución. Además, estas constantes específicas del controlador deberían ser usadas solo si se usa este controlador. Usar atributos específicos de un controlador con otro controlador podría causar un comportamiento inesperado. `PDO::getAttribute` podría ser usado para obtener el atributo `PDO::ATTR_DRIVER_NAME` para verificar el controlador, si su código puede funcionar en múltiples controladores.

`PDO::OCI_ATTR_ACTION` (`int`)  
Proporciona un medio para especificar la acción sobre la sesión de la base de datos.

Existe a partir de PHP 7.2.16 y 7.3.3

`PDO::OCI_ATTR_CLIENT_INFO` (`int`)  
Proporciona un medio para especificar la información del cliente sobre la sesión de la base de datos.

Existe a partir de PHP 7.2.16 y 7.3.3

`PDO::OCI_ATTR_CLIENT_IDENTIFIER` (`int`)  
Proporciona un medio para especificar el identificador del cliente sobre la sesión de la base de datos.

Existe a partir de PHP 7.2.16 y 7.3.3

`PDO::OCI_ATTR_MODULE` (`int`)  
Proporciona un medio para especificar el módulo sobre la sesión de la base de datos.

Existe a partir de PHP 7.2.16 y 7.3.3
