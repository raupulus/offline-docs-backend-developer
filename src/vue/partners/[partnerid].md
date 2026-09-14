---
title: '[partnerid]'
source_repo: vuejs/docs
source_ref: main
source_commit: b75d188ab
source_path: partners/[partnerId].md
technology: vue
version: main
license: MIT
retrieved_at: '2026-08-02'
section: partners
order: 890
---

<script setup>
import { useData } from 'vitepress'
import Page from './components/PartnerPage.vue'

const { page } = useData()
</script>

<Page :partner="page.params.partnerId" />
