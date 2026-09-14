---
title: Tiempos de expiración
source_url: https://www.php.net/manual/es/memcached.expiration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/expiration.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_revision: af4410a7e
order: 46320
---

## Tiempos de expiración

Algunos comandos de almacenamiento implican el envío de un valor de expiración (relativo a un ítem o a una operación solicitada por el cliente) al servidor. En todos los casos, el valor real enviado podría ser en tiempo Unix (un valor de tipo integer con el número de segundos transcurridos desde el 1 de enero de 1970), o el número de segundos comenzando desde el instante actual. En este caso, el número no debe exceder de 60\*60\*24\*30 (que corresponde al número de segundos en 30 días); si se excede el valor del tiempo de expiración, el servidor lo considerará como tiempo Unix en lugar del número de segundos desde el instante actual.

Si el valor de la expiración es `0` (el predeterminado), el ítem nunca caducará (aunque puede ser eliminado del servidor para hacer sitio a otros ítems).
