:author: Kevin Murray
:date: 2013-12-11
:tags: spectralphenoclimatron, growth conditions, experiments
:category: Biology
:status: published

The Arabidopsis Transcriptome under Dynamic Light Conditions
############################################################

My Honours project
==================


I wrote my honours thesis in 2013, in the lab of Justin Borevitz. I aimed to develop lab growth facilities that mimic natural rhythms of light, humidity and temperature, and use these facilities to investigate the effects of different lighting conditions on the transcriptomes of Arabidopsis.

Dynamic growth conditions in the SpectralPhenoClimatron
-------------------------------------------------------

The `SpectralPhenoClimatron system <https://borevitzlab.anu.edu.au/spectralphenoclimatron/>`_ consists of several standard Conviron reach-in growth cabinets retrofitted with Heliospectra 7-band or 10-band multispectral lights. The output of all spectral channels of the lights, as well as the temperature and humidity of the growth cabinets can be controlled over the local network.

Kurt Spokas' SolarCalc software can simulate the intensity and spectra of sunlight, temperature, and humidity of a given location on earth at any time on any day of the year. I wrote code `(SPCControl) <https://github.com/borevitzlab/spcControl>`_ which interfaces between SolarCalc and the SpectralPhenoClimatron chambers. SPCControl uses the telnet interfaces of the Heliospectra lights and the Conviron chambers to update the growth conditions, typically every 5 minutes throughout the day and night [#]_.



The SpectralPhenoClimatron cabinets are equipped with a dSLR-based time-lapse phenotyping system, which can take 20+ megapixel top-down images of all plants in  chamber up to every minute. Combined with the `TraitCapture system <https://doi.org/10.1016/j.pbi.2014.02.002>`_, this allows relatively automated phenotyping of plants grown under repeatable laboratory conditions which mimic natural local climates.

Below is a video demonstrating the SpectralPhenoClimatron system running an Arabidopsis experiment.

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/wMt5xtp9sH8?rel=0&amp;showinfo=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


2018 update
~~~~~~~~~~~

We still use the SolarCalc/SPCControl software system to mimic local climates for many experiments. We (primarily Gareth Dunstone) are in the process of preparing a second version of SPCControl. The new version will be highly modular, making it more useful for users of other hardware. In addition, version two will include a reimplementation of SolarCalc's model, and will be controlled by a centralised web control panel. The development repository for SPCControl v2 is `here <https://github.com/borevitzlab/pysolarcalc>`_.


The effect of Excess and Fluctuating light on the Transcriptome
---------------------------------------------------------------

The more biological half of my honours investigated the ways in which excess and fluctuating light is perceived by plants, and how this affects the transcriptome. Plant cells may be damaged when they receive light in excess of that which can be utilised for photosynthesis. Light may be in a constant excess (e.g. full sun), but may also be sporadically in excess throughout the day, perhaps due to shading over time periods from seconds to hours.

.. figure:: https://raw.githubusercontent.com/kdmurray91/hons-thesis/master/img/dc-res-3cond-light.png
   :alt: Excess, sufficient and dynamic light conditions

   Photosynthetically Active Radiation (PAR) levels throughout one day for the Sufficient, Excess, and Fluctuating light conditions.

The bulk of the published work on plant light response has been conducted under rather artificial laboratory conditions, particularly with regards to excess light. The aim of my honours was to investigate the effects of constant excess light and fluctuating excess light under dynamic growth conditions mimicking the local climate of an agricultural region near Canberra, Australia (where I did my Honours). To this end, I designed dynamic growth conditions with approximately the same total photosynthetically active light intensity as standard Arabidopsis growth conditions (approx :math:`100 \mu E`), and conditions with a five-fold excess of light over this (approx :math:`100 \mu E`). A third condition fluctuated between these light intensities in a 5 minutes high, 10 minutes low intensity pattern throughout the day. The relative spectral density of these light conditions was constant; this mimicked a "neutral shade" such as that imposed by cloud, rather than the shade that might be imposed by a canopy/foliage which would alter the red:far-red light ratio.

Transcriptomes of Arabidopsis (Col-0) plants were assayed after two weeks in their respective growth condition, and compared relative to plants grown under regular Arabidopsis growth conditions (:math:`100 \mu E` Fluorescent light, 12 hour days). Unfortunately, for technical reasons outside the experiment itself, RNAseq failed for these accessions, so no useful results could be obtained.

.. [#] Ensuring this control system operates with sufficient reliability to conduct experiments was a significant difficulty. It turns out these systems, especially the growth cabinets, were simply not designed to be updated with the frequency that the SpectralPhenoClimatron system demands. The system remains relatively stable, however manual baby-sitting and the frequent hard power-cycling remain necessary.

.. vim: tw=0 wrap et sw=2 ts=2 spell
