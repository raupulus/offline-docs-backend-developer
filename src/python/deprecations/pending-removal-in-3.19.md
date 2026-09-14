---
title: Pending removal in Python 3.19
source_url: https://docs.python.org/es/3
source_path: deprecations/pending-removal-in-3.19.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: deprecations
order: 940
---

# Pending removal in Python 3.19

* "ctypes":

  * Implicitly switching to the MSVC-compatible struct layout by
    setting "_pack_" but not "_layout_" on non-Windows platforms.
