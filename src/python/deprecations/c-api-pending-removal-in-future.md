---
title: Pending removal in future versions
source_url: https://docs.python.org/es/3
source_path: deprecations/c-api-pending-removal-in-future.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: deprecations
order: 860
---

# Pending removal in future versions

Las siguientes APIs están obsoletas y serán eliminadas, aunque
actualmente no hay fecha prevista para su eliminación.

* "Py_TPFLAGS_HAVE_FINALIZE": Innecesaria desde Python 3.8.

* "PyErr_Fetch()": Utilice "PyErr_GetRaisedException()" en su lugar.

* "PyErr_NormalizeException()": Utilice "PyErr_GetRaisedException()"
  en su lugar.

* "PyErr_Restore()": Utilice "PyErr_SetRaisedException()" en su lugar.

* "PyModule_GetFilename()": Utilice "PyModule_GetFilenameObject()" en
  su lugar.

* "PyOS_AfterFork()": Utilice "PyOS_AfterFork_Child()" en su lugar.

* "PySlice_GetIndicesEx()": Utilice "PySlice_Unpack()" y
  "PySlice_AdjustIndices()" en su lugar.

* "PyUnicode_READY()": Innecesaria desde Python 3.12

* "PyErr_Display()": Utilice "PyErr_DisplayException()" en su lugar.

* "_PyErr_ChainExceptions()": Utilice "_PyErr_ChainExceptions1()" en
  su lugar.

* Miembro "PyBytesObject.ob_shash": Llame a "PyObject_Hash()" en su
  lugar.

* API de almacenamiento local de hilos (TLS):

  * "PyThread_create_key()": Utilice "PyThread_tss_alloc()" en su
    lugar.

  * "PyThread_delete_key()": Utilice "PyThread_tss_free()" en su
    lugar.

  * "PyThread_set_key_value()": Utilice "PyThread_tss_set()" en su
    lugar.

  * "PyThread_get_key_value()": Utilice "PyThread_tss_get()" en su
    lugar.

  * "PyThread_delete_key_value()": Utilice "PyThread_tss_delete()" en
    su lugar.

  * "PyThread_ReInitTLS()": Innecesaria desde Python 3.7.
