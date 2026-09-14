---
title: Job Control Variables
source_url: https://www.gnu.org/software/bash/manual
source_path: 038-job-control-variables.md
technology: bash
version: '5.3'
license: GFDL-1.3
retrieved_at: '2026-08-02'
order: 380
---

## Job Control Variables

<span class="indexterm vr" role="vr"></span>`auto_resume`  
This variable controls how the shell interacts with the user and job control. If this variable exists then simple commands consisting of only a single word, without redirections, are treated as candidates for resumption of an existing job. There is no ambiguity allowed; if there is more than one job beginning with or containing the word, then this selects the most recently accessed job. The name of a stopped job, in this context, is the command line used to start it, as displayed by `jobs`. If this variable is set to the value ‘`exact`’, the word must match the name of a stopped job exactly; if set to ‘`substring`’, the word needs to match a substring of the name of a stopped job. The ‘`substring`’ value provides functionality analogous to the ‘`%?string`’ job ID (see [Job Control Basics](#Job-Control-Basics)). If set to any other value (e.g., ‘`prefix`’), the word must be a prefix of a stopped job’s name; this provides functionality analogous to the ‘`%string`’ job ID.

Readline, how to use
