---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/pdo-sqlsrv.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_sqlsrv/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 62810
---

## Constantes predefinidas

Las constantes a continuación son definidas por este controlador y solo estarán disponibles cuando la extensión haya sido compilada en PHP o cargada dinámicamente del motor de ejecución. Además, estas constantes específicas del controlador deberían ser usadas solo si se usa este controlador. Usar atributos específicos de un controlador con otro controlador podría causar un comportamiento inesperado. `PDO::getAttribute` podría ser usado para obtener el atributo `PDO::ATTR_DRIVER_NAME` para verificar el controlador, si su código puede funcionar en múltiples controladores.

`PDO::SQLSRV_TXN_READ_UNCOMMITTED` (`int`)  
Esta constante es un valor posible para la clave "TransactionIsolation" del DSN para SQLSRV. Esta constante establece el nivel de aislamiento de la transacción a "Read Uncommitted".

`PDO::SQLSRV_TXN_READ_COMMITTED` (`int`)  
Esta constante es un valor posible para la clave "TransactionIsolation" del DSN para SQLSRV. Esta constante establece el nivel de aislamiento de la transacción a "Read Committed".

`PDO::SQLSRV_TXN_REPEATABLE_READ` (`int`)  
Esta constante es un valor posible para la clave "TransactionIsolation" del DSN para SQLSRV. Esta constante establece el nivel de aislamiento de la transacción a "Repeatable Read".

`PDO::SQLSRV_TXN_SNAPSHOT` (`int`)  
Esta constante es un valor posible para la clave "TransactionIsolation" del DSN para SQLSRV. Esta constante establece el nivel de aislamiento de la transacción a "Snapshot".

`PDO::SQLSRV_TXN_SERIALIZABLE` (`int`)  
Esta constante es un valor posible para la clave "TransactionIsolation" del DSN para SQLSRV. Esta constante establece el nivel de aislamiento de la transacción a "Serializable".

`PDO::SQLSRV_ENCODING_BINARY` (`int`)  
Especifica que estos datos son enviados al (o recibidos del) servidor como un flujo de bytes, sin realizar codificación o traducción. Esta constante puede ser utilizada en las llamadas a PDOStatement::setAttribute, PDO::prepare, PDOStatement::bindColumn, y PDOStatement::bindParam.

`PDO::SQLSRV_ENCODING_SYSTEM` (`int`)  
Especifica que estos datos son enviados al (o recibidos del) servidor como un flujo de caracteres 8 bits, como se especifica en la página de código de la configuración local de Windows activa en el sistema. Todo carácter multibyte, o carácter que no existe en esta página de código, es sustituido por un simple signo de interrogación (?). Esta constante puede ser utilizada en las llamadas a PDOStatement::setAttribute, PDO::setAttribute, PDO::prepare, PDOStatement::bindColumn, y PDOStatement::bindParam.

`PDO::SQLSRV_ENCODING_UTF8` (`int`)  
Especifica que estos datos son enviados al (o recibidos del) servidor como un flujo de caracteres UTF-8. Se trata de la codificación por defecto. Esta constante puede ser utilizada en las llamadas a PDOStatement::setAttribute, PDO::setAttribute, PDO::prepare, PDOStatement::bindColumn, y PDOStatement::bindParam.

`PDO::SQLSRV_ENCODING_DEFAULT` (`int`)  
Especifica que estos datos son enviados al (o recibidos del) servidor utilizando la codificación PDO::SQLSRV_ENCODING_SYSTEM si es especificada durante la conexión. Si es especificada en una instrucción "prepare", se utiliza la codificación de la conexión. Esta constante puede ser utilizada en las llamadas a PDOStatement::setAttribute, PDO::setAttribute, PDO::prepare, PDOStatement::bindColumn, y PDOStatement::bindParam.

`PDO::SQLSRV_ATTR_QUERY_TIMEOUT` (`int`)  
Un entero positivo o nulo que representa la duración del tiempo límite, en segundos. Cero (0) es el valor por omisión y significa que no hay tiempo límite. Esta constante puede ser utilizada en las llamadas a PDOStatement::setAttribute, PDO::setAttribute, y PDO::prepare.

`PDO::SQLSRV_ATTR_DIRECT_QUERY` (`int`)  
Indica una consulta que debe ser ejecutada directamente, sin ser preparada. Esta constante puede ser utilizada en las llamadas a PDO::setAttribute, y PDO::prepare. Para más información, ver (en inglés) [Direct and Prepared Statement Execution](http://msdn.microsoft.com/en-us/library/ff754356.aspx).
