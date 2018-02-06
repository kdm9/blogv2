:author: Kevin Murray
:date: 2018-02-06
:tags: troubleshooting, ngs, mapping
:category: Bioinformatics
:status: published
:title: Next-gen sequencing mappers: they all have warts



| **TL;DR:**   We came across some weird behaviour to do with mapping qualities during read mapping with a promising new tool. We're at a loss to explain it, and hope to hear from others who may have seen this happen in other datasets (or not!). We're not convinced this is not just us mis-using or mis-configuring the tool, so any hints would be greatly appreciated.

One large project I am working on involves sequencing the genomes of many hundred Eucalyptus individuals across the section Adnataria (subgenus Symphyomyrtus). The Eucalyptus reference genome is of *E. grandis*, in an adjacent section within the same sub-genus. Molecularly, this equates to something in the order of 5% of sites diverged between most Adnataria and the reference. Therefore, care is needed when aligning short reads to the reference. The aligner should be sensitive enough to align short reads to a reasonably diverged reference, without increasing the number of false-positive or otherwise erroneous alignments.

Rob Lanfear has `an excellent write-up on this topic <http://robertlanfear.com/blog/files/short_read_mappers.html>`_ in which he compares Stampy, BWA, NGM and BBMap for a similar project (also in Eucalyptus). He finds that NGM performs most sensibly for his uses, while Stampy and BBMap have very weird results. The Stampy weirdness Rob sees is tangential to our situation, so we have only excluded BBMap from contention.

Initially, we had mapped all our data with NGM and BWA, and noticed that the coverage used in SNP calling (and in ANGSD analyses) is much lower when using NGM. Given that the only change in the pipeline was the use of NGM vs BWA, and the purported benefits of NGM for cases with reasonably high divergence, we decided to do a deep dive and investigate the causes of this.


Losing Coverage Through...
==========================

Quality control
---------------

So we initially expect in the order of 5x coverage per sample in terms of raw sequence yield (post demultiplexing), and observe about 1.5-2.5x coverage when looking at the mean coverage of variant sites (post ANGSD/SNP calling). This means we're losing about ½ to ¾ of our yield!! The first place to check is QC trimming and pair merging: if a fragment is shorter than twice the read length (2x150bp for us), then the read pair will only yield the length of the physical fragment. This isn't a loss of coverage *per se*, more that we double-count these bases when calculating expected yield.

.. figure:: {filename}img/2018-01-30_qualinsert/insert-size-joyplot.png
  :alt: Histogram of fragment lengths showing most fragments are shorter than 300bp.
  :figwidth: 600px

  The distribution of insert size/fragment lengths.

  Note that the bulk of fragments are less than 300bp, the mean being somewhere around 220bp.

.. figure:: {filename}img/2018-01-30_qualinsert/qc-yieldloss.png
  :alt: Proportion of yield lost through QC trimming and merging across samples
  :figwidth: 600px

  Most samples lose approximately 25% of their original yield to read merging and quality trimming.


All in all, the quality control and pair merging step takes us from expecting an yield of about 5x per sample down to about 3.5x depending on the sample. There's clearly something else at play here.

Mapping?
--------

So there are not too many ways in which reads (or bases) can be lost during mapping. Mainly, reads can either not be mapped, or mapped but somehow filtered out of later analyses. We briefly investigated if there were vastly more unmapped reads when using NGM, however there are slightly fewer unmapped reads with NGM than BWA in most samples and on average. This lead us to tally the distributions of mapping quality. In ANGSD at least, we have thus far been using a mapping quality threshold of 30 (1e-3; ``-minMapQ 30``).

.. figure:: {filename}img/2018-01-30_qualinsert/mapping-quality-barplot.png
  :alt: alter text

  Distributions of mapping quality for NGM and BWA.

  Note the much higher number of MAPQ=0 reads with NGM and the higher density of very low but non-zero maping qualities.

So this seems to be a likely cause. If we're filtering at ``MapQ>=30``, then we're definitely excluding more reads with NGM than with BWA, and therefore our observed coverages will be much lower. But why? Are these alignments genuinely worse?


What's NGM up to?
==================

Belatedly, we broke out IGV and inspected our alignments visually. There were quite a large number of read alignments which were identical between BWA and NGM, but which NGM gave a mapping quality of zero. In fact, when we summarised this across many samples, we see that for most alignments which NGM calculates a low mapping quality, BWA scores an identical alignment much higher, and in many cases the practical maximum score of 60. This suggests that either NGM is mis-calculating alignment scores, or we're misusing it.

.. figure:: {filename}img/2018-01-30_qualinsert/igv-alignments.svg
  :alt: IGV visualisation of alignments.

  A representative region of the *E. grandis* genome showing different mapping qualities given by NGM and BWA MEM to otherwise identical alignments.

  Note that the white alignments are mapping quality zero, and grey alignments are have mapping qualities greater than zero.


Conclusions
===========

For now, we've reverted to using BWA MEM, despite its allegedly inferior sensitivity when aligning reads to a divergent reference. Given we see no more unmapped reads with BWA MEM than NGM, I'm relatively comfortable that we are not excluding too large a fraction of the genome by doing so.

If anyone has information about the handling of mapping quality in NGM, or has seen similar issues, please get in touch (you can find me on `Twitter <https://twitter.com/kdmurray91>`_ or email me ``myfirstname AT kdmurray DOT id DOT au``).

Many thanks to Rose Andrew for detecting and helping debug this issue, and to Jasmine Janes for her patience while I endlessly re-mapped her dataset!

.. vim: tw=0 wrap et sw=2 ts=2 spell
