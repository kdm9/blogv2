:title: My PhD Project
:author: Kevin Murray
:date: 2018-01-18

I started my PhD in March 2015, aiming to devise and implement methods to accelerate the analysis of population resequencing data. This is a summary of my work thus far, and for the remainder of my time as a PhD candidate.

Improved tools and pipelines for GBS analysis
=============================================

`Genotyping By Sequencing <DOI HERE>`_ is a common, reasonably priced sequencing method to assay large numbers of samples at a subset of their genomes. I have created a series of small tools to aid the analysis of GBS data. In particular, `Axe </projects/axe/>`_ is one of the few sequence read demultiplexers which can demultiplex GBS reads with combinatorial index sequences of differing length, while tolerating mismatches.


Reference- and Alignment-free estimation of genetic distance
============================================================

One important output of population re-sequencing experiments is the genetic distance between samples. Often, this is an initial result which guides further analysis, and in some cases this may even be the only desired output. `kWIP </projects/kwip/>`_, the k-mer Weighted Inner Product is a method to estimate genetic distance directly from sequencing data, without reliance on a reference genome. In our `PLoS Comp. Biol. paper <DOI HERE>`_, we show that kWIP performs well even at modest coverage or low divergence.


.. vim: tw=0 wrap et sw=2 ts=2 spell
