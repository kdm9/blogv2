:title: The best JabRef/BetterBibTex citation key
:author: Kevin Murray
:date: 2018-01-21
:tags: latex
:category: Tips & Tricks
:status: published

I like citekeys like "murray17_kwip", which seems the most concise representation. This can be achieved by the following JabRef code::

   [auth:lower][shortyear]_[veryshorttitle:nopunct:fold:lower]

I use Zotero, and the BetterBibtex plugin which allows this to be set. Today's the third time I've had to reverse engineer this code from sparse documentation, so here it is for my future self.



.. vim: tw=0 wrap et sw=2 ts=2 spell
