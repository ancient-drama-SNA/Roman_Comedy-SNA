# Social Network Analysis of ancient Roman Comedy

* Project currently being developed by:
    - Hans Bork (Assistant Professor of Classics, Stanford University)
    * Marguerite DeMarco (Stanford University)
    * Annie Lamar (PhD Candidate, Classics Dept., Stanford University)
    - Stanford Center for Spatial and Textual Analysis (CESTA, https://cesta.stanford.edu)
    - With previous contributions from:
        - Salma Kamni (Stanford University)
        - Daniel Bush (Postdoctoral Fellow, Stanford Center for Spatial and Textual Analysis)


## Project Overview:

This project aims to devise a methodology for generating "social network maps" among
characters in Ancient Roman Comedy, using different indices of interaction. For example: total
lines spoken between characters, vs. total time onstage vs. total number of characters in a
play; and so on. 

Plautus is an important figure in Latin literature because (among other things), his work is
one of the few places where we can see people of different statuses, ethnicities, economic
classes, and genders interacting with one-another. (Most of the Latin literature from ancient
Rome tends to feature elite, Roman, male figures; Plautus is a rare exception.) The
interactions among Plautine characters are thus important evidence for our understanding of
ancient Roman society—but, so far as I know, they have never been examined from a contemporary
networking perspective. Until now!


## Project Goals

The major *short-term* goals of the project are: 
    1) to develop a simple workflow for mapping "social network relationships" in Roman Comedy
       (initially, the plays of Plautus, with later work on Terence);
    2) to make the generated maps open to various queries—i.e., let users query them for
       various data points, such as "network interactions involving enslaved characters";
    3) to make the generated maps (and associated data) available online, for free, for use by
       scholars and interested non-specialists.

Long-term goals include opening up the developed framework to ancient drama generally (e.g.,
Greek and Roman Tragedy; Senecan drama; etc.), and to allow comparison of data among the
various mapped data-sets. (E.g., comparing number of interactions by certain character-types
across all of Greco-Latin drama.) Advanced use-cases might include e.g. filtering
network interactions by defined categories or tags (e.g., "all soliloquies in Roman comedy";
"all instances where non-dramatic entities seem to appear onstage"; and so on).

By working with CESTA I hope to, ultimately, develop a system that will easily make social
network maps—and corresponding textual data—of Plautus' character interactions available
online, and thus accessible for anyone to use. And, if the system works well, then I could see
extending it to other ancient playwrights (of which there are quite a few).  This is of course
a long-term goal; current work is devoted to developing prototype workflow and methodology, by
mapping character relationships in a single play by Plautus ('Captivi'). This text will be a
"laboratory" for how we can (and cannot) graphically model character interactions in different
ways; the developed methodology will then be extended to all of the other plays in Plautus'
corpus.


## Example STATIC map:

* Currently we are working to develop a *dynamic* (i.e., interactive and non-static) network
  map for the play *Captivi*, by using the [D3.js engine](https://d3js.org).
* Here is an example of a simple, *static* network map created using Python, `matplotlib`, and
  `networkx`:

![sample map,75](https://github.com/ancient-drama-SNA/Roman_Comedy-SNA/blob/main/Captivi-prototype/Captivi_map-V1/Captivi_network.png)


## Prototype DYNAMIC map:

* The dynamic prototype is being developed using D3.js and the Jekyll web platform.
* [Current Prototype Available Here](https://ancient-drama-sna.github.io/Roman_comedy_networks/)
    - Repo for the GitHub Pages site [available here](https://github.com/ancient-drama-SNA/Roman_comedy_networks).


## Project TODO:

- [X] Develop a prototype workflow and toolkit to publish SNA data online.
- [ ] Develop a project roadmap, based on the existing prototype.
- [ ] Develop a plan for applying the prototype to other texts than *Captivi.*
- [ ] Devise a plan for future development:
    - [ ] Develop a workflow for contributors. E.g., for contributing to various stages of work, such as data gathering, data encoding, site coding, and so on.
    - [ ] Compose and publish 'Project Roadmap' to GitHub page.
    - [ ] Recruit individuals to work on the project. E.g., graduate students; colleagues in
      the field; undergraduates; CESTA interns.
- [ ] Advertise the project.
- [ ] Investigate feasible publication options based on the project. E.g., perhaps a short
  article to a DH-specific journal? Or to a more open-minded Classics journal?



## Note to contributors

Hmmm...
