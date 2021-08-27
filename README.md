# Social Network Analysis of ancient Roman Comedy 

* Project currently being developed by:
    - Hans Bork (Assistant Professor of Classics, Stanford University)
    - Salma Kamni (Stanford University)
    - Daniel Bush (Postdoctoral Fellow, Stanford Center for Spatial and Textual Analysis)
    - Stanford Center for Spatial and Textual Analysis (CESTA, https://cesta.stanford.edu)


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


## Example map:

* Currently we are working to develop a *dynamic* (i.e., interactive and non-static) network
  map for the play _Captivi_, by using the [D3.js engine](https://d3js.org).
* Here is an example of a simple, _static_ network map created using Python, `matplotlib`, and
  `networkx`:

![sample map](https://github.com/ancient-drama-SNA/Roman_Comedy-SNA/blob/main/Captivi-prototype/Captivi_map-V1/Captivi_network.png)


## Prototype map:

<div class="codepen" data-height="300" data-default-tab="html,result" data-slug-hash="QWvzXQW" data-user="salmakamni"  data-prefill='{"title":"vue-d3-network RC","tags":[],"scripts":["https://unpkg.com/vue","https://rawgit.com/emiliorizzo/vue-d3-network/master/dist/vue-d3-network.umd.js"],"stylesheets":["https://rawgit.com/emiliorizzo/vue-d3-network/master/dist/vue-d3-network.css"]}'>
  <pre data-lang="html">&lt;!-- full demo here: https://emiliorizzo.github.io/vue-d3-network/
 resources: arrows - https://stackoverflow.com/questions/45480759/labeled-nodes-arrow-on-edges-in-d3-js -->
&lt;body>
  &lt;div id="app">
  &lt;div class="title">
    &lt;h1> &lt;a href="https://github.com/emiliorizzo/vue-d3-network">vue-d3-network&lt;/a> &lt;/h1> 
    &lt;!-- example control -->  
    &lt;ul class="menu">
      &lt;li>
        &lt;label> Node size  &lt;/label>
        &lt;input type="range" min="1" max="100" v-model='nodeSize' /> {{ options.nodeSize }}
      &lt;/li>
      &lt;li>
        &lt;label>Render as  &lt;/label>
      &lt;input type="radio" :value='false' v-model='canvas' />
      &lt;label>SVG&lt;/label>
      &lt;input type="radio" :value='true' v-model='canvas' />
      &lt;label>Canvas&lt;/label>
      &lt;/li>  
    &lt;/ul>
    &lt;/div>
    &lt;d3-network ref='net' :net-nodes="nodes" :net-links="links" :options="options" />
  &lt;/div>
&lt;/body>
</pre>
  <pre data-lang="css">@import url('https://fonts.googleapis.com/css?family=PT+Sans');

body{
  font-family: 'PT Sans', sans-serif;
  background-color: #eee;
}
.title{
  position:absolute;
  text-align: center;
  left: 2em;
}
h1,a{
  color: #1aad8d;
  text-decoration: none;
}

ul.menu {
  list-style: none;
  position: absolute;
  z-index: 100;
  min-width: 20em;
  text-align: left;
}
ul.menu li{
  margin-top: 1em;
  position: relative;
}
</pre>
  <pre data-lang="js">var D3Network = window['vue-d3-network']
new Vue({
  el: '#app',
  components: {
    D3Network
  },
  data () {
    return {
      nodes: [
        { id: 1, name: 'prologus'},
        { id: 2, name: 'Ergasilus'},
        { id: 3, name: 'Hegio'},
        { id: 4, name: 'Lorarii'},
        { id: 5, name: 'Philocrates'},
        { id: 6, name: 'Tyndarus'},
        { id: 7, name: 'Aristophontes'},
        { id: 8, name: 'Puer'},
        { id: 9, name: 'Philopolemus'},
        { id: 10, name: 'Stalagmus'},
        { id: 11, name: 'Grex'},
        { id: 12, name: 'Audience'}
      ],
      links: [
        //prologus
        { sid: 1, tid: 12},
        //ergasilus
        { sid: 2, tid: 12, _svgAttrs:{'stroke-width':8,opacity:1},name:'thrice'},
        { sid: 2, tid: 3, _svgAttrs:{'stroke-width':4,opacity:1},name:'twice'},
        //hegio
        { sid: 3, tid: 4},
        { sid: 3, tid: 2, _svgAttrs:{'stroke-width':4,opacity:1},name:'twice'},
        { sid: 3, tid: 5, _svgAttrs:{'stroke-width':4,opacity:1},name:'twice'},
        { sid: 3, tid: 6, _svgAttrs:{'stroke-width':8,opacity:1},name:'thrice'},
        { sid: 3, tid: 12, _svgAttrs:{'stroke-width':8,opacity:1},name:'thrice'},
        { sid: 3, tid: 7},
        { sid: 3, tid: 9},
        { sid: 3, tid: 10},
        //lorarii
        { sid: 4, tid: 6 },
        { sid: 4, tid: 5 },
        { sid: 4, tid: 3 },
        //philocrates
        { sid: 5, tid: 6,  _svgAttrs:{'stroke-width':4,opacity:1},name:'twice'},
        { sid: 5, tid: 4},
        { sid: 5, tid: 3,  _svgAttrs:{'stroke-width':4,opacity:1},name:'twice'},
        { sid: 5, tid: 10},
        //tyndarus
        { sid: 6, tid: 5,  _svgAttrs:{'stroke-width':4,opacity:1},name:'twice'},
        { sid: 6, tid: 4},
        { sid: 6, tid: 3,  _svgAttrs:{'stroke-width':4,opacity:1},name:'twice'},
        { sid: 6, tid: 12},
        //aristophonte
        { sid: 7, tid: 3 },
        { sid: 7, tid: 6 },
        //puer
        { sid: 8, tid: 12 },
        //philop
        { sid: 9, tid: 3 },
        //stalgamus
        { sid: 10, tid: 3 },
        { sid: 10, tid: 5 },
        //grex
        { sid: 11, tid: 12 }
      ],
      nodeSize:20,
      canvas:false

    }
  },
  computed:{
    options(){
      return{
        force: 3000,
        size:{ w:600, h:600},
        nodeSize: this.nodeSize,
        nodeLabels: true,
        linkLabels:true,
        canvas: this.canvas
      }
    }
  }
})</pre></div>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>


## Project TODO:

- [ ] Develop a project roadmap, based on the existing prototype.
* [ ] Develop a plan for applying the prototype to other texts than *Captivi.*
- [ ] Devise a plan for future development:
    - [ ] Develop a workflow for contributors. E.g., for contributing to various stages of
      work, such as data gathering, data encoding, site coding, and so on.
    - [ ] Compose and publish 'Project Roadmap' to GitHub page.
    - [ ] Recruit individuals to work on the project. E.g., graduate students; colleagues in
      the field; undergraduates; CESTA interns.
- [ ] Advertise the project.
- [ ] Investigate feasible publication options based on the project. E.g., perhaps a short
  article to a DH-specific journal? Or to a more open-minded Classics journal?

## Note to contributors

Hmmm...
