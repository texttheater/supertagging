supertagging
============

Scripts to produce POS-tagged and supertagged training and testing data for CCG
parsing experiments as described in Zhang and Clark (2011). Put together by
[Kilian Evang](http://kilian.evang.name/).

External dependencies
---------------------

Before you can use this software, make sure the external dependencies are in
place: create the directory `ext` and make sure it contains the following two
resources (you may use symbolic links):

* [`candc`](http://svn.ask.it.usyd.edu.au/trac/candc/), the C&C tools
* `CCGbank1.2`, the 1.2 release of CCGbank

The C&C tools need to be compiled, this can be done by running

    make all bin/generate

from the `candc` directory.

You also need [Produce](https://github.com/texttheater/produce/) to run the
commands below. Just make sure the `produce` script is in your `PATH`.

Usage
-----

To produce the POS-tagged and supertagged training data by 10-fold jacknifing
and adding any missing gold supertags as in Zhang and Clark (2011) on up to 10
cores, run:

    produce -j 10 out/wsj02-21.automultistagged

To produce the POS-tagged and supertagged development test data (using a model
trained on the entire training data), run:

    produce out/wsj00.automultistagged

Similarly for the final test data:

    produce out/wsj22.automultistagged

Bug reports
-----------

Bug reports are very welcome, preferably as GitHub issues.

Literature
----------

Yue Zhang and Stephen Clark (2011):
[Shift-reduce CCG Parsing](https://dl.acm.org/citation.cfm?id=2002559). In
_Proceedings of the 49th Annual Meeting of the Association for Computational
Linguistics: Human Language Technologies – Volume 1_, pages 683–692.
Association for Computational Linguistics.
