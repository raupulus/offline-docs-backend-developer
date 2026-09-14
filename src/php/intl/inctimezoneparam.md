---
title: inctimezoneparam
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/inctimezoneparam.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 9906c5636
order: 39950
---

- `null`, en cuyo caso se usará la zona horaria predeterminada, tal como está especificada en el ajuste ini [date.timezone](#ini.date.timezone) o a través de la función `date_default_timezone_set` y como es devuelto por `date_default_timezone_get`.

- Un `IntlTimeZone`, que se usará directamente.

- Un `DateTimeZone`. Su identificador será extraido y se creará un objeto de zona horaria de ICU; la zona horaria será proporcionada por la base de datos de ICU, no por la de PHP.

- Un `string`, que debería ser un identificador de zona horaria de ICU válido. Véase `IntlTimeZone::createTimeZoneIDEnumeration`. Los índices puros como `"GMT+08:30"` también se aceptan.
