---
title: Pending removal in Python 3.18
source_url: https://docs.python.org/es/3
source_path: deprecations/c-api-pending-removal-in-3.18.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: deprecations
order: 850
---

# Pending removal in Python 3.18

* The following private functions are deprecated and planned for
  removal in Python 3.18:

  * "_PyBytes_Join()": use "PyBytes_Join()".

  * "_PyDict_GetItemStringWithError()": use
    "PyDict_GetItemStringRef()".

  * "_PyDict_Pop()": use "PyDict_Pop()".

  * "_PyLong_Sign()": use "PyLong_GetSign()".

  * "_PyLong_FromDigits()" and "_PyLong_New()": use
    "PyLongWriter_Create()".

  * "_PyThreadState_UncheckedGet()": use
    "PyThreadState_GetUnchecked()".

  * "_PyUnicode_AsString()": use "PyUnicode_AsUTF8()".

  * "_PyUnicodeWriter_Init()": replace
    "_PyUnicodeWriter_Init(&writer)" with "writer =
    PyUnicodeWriter_Create(0)".

  * "_PyUnicodeWriter_Finish()": replace
    "_PyUnicodeWriter_Finish(&writer)" with
    "PyUnicodeWriter_Finish(writer)".

  * "_PyUnicodeWriter_Dealloc()": replace
    "_PyUnicodeWriter_Dealloc(&writer)" with
    "PyUnicodeWriter_Discard(writer)".

  * "_PyUnicodeWriter_WriteChar()": replace
    "_PyUnicodeWriter_WriteChar(&writer, ch)" with
    "PyUnicodeWriter_WriteChar(writer, ch)".

  * "_PyUnicodeWriter_WriteStr()": replace
    "_PyUnicodeWriter_WriteStr(&writer, str)" with
    "PyUnicodeWriter_WriteStr(writer, str)".

  * "_PyUnicodeWriter_WriteSubstring()": replace
    "_PyUnicodeWriter_WriteSubstring(&writer, str, start, end)" with
    "PyUnicodeWriter_WriteSubstring(writer, str, start, end)".

  * "_PyUnicodeWriter_WriteASCIIString()": replace
    "_PyUnicodeWriter_WriteASCIIString(&writer, str)" with
    "PyUnicodeWriter_WriteASCII(writer, str)".

  * "_PyUnicodeWriter_WriteLatin1String()": replace
    "_PyUnicodeWriter_WriteLatin1String(&writer, str)" with
    "PyUnicodeWriter_WriteUTF8(writer, str)".

  * "_PyUnicodeWriter_Prepare()": (no replacement).

  * "_PyUnicodeWriter_PrepareKind()": (no replacement).

  * "_Py_HashPointer()": use "Py_HashPointer()".

  * "_Py_fopen_obj()": use "Py_fopen()".

  The pythoncapi-compat project can be used to get these new public
  functions on Python 3.13 and older. (Contributed by Victor Stinner
  in gh-128863.)
