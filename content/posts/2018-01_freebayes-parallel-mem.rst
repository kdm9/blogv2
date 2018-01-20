:author: Kevin Murray
:date: 2018-01-14
:tags: variant calling, bioinformatics, tips
:category: Short Notes
:status: published
:title: Freebayes uses too much ram without merged BAMs

I've been running some very large variant calling runs lately, and have run into RAM limitations on the cluster. According to `this GitHub issue <https://github.com/ekg/freebayes/issues/312>`_, ``freebayes`` really ought have merged bams as input with many samples. Merging bams reduces the memory footprint from >20GB per core to about 2GB per core.

.. vim: tw=0 wrap et sw=2 ts=2 spell
