title: 
    name: Paperista
id: paperista
date: 2013
ranks:
    visual: 4
    digital: 4
    textual: 2
category: 
    - id: dataviz
      name: Vizuelizacija podataka
    - id: research
      name: Akademsko istraživanje
    - id: software
      name: Softver
    - id: interactive
      name: Interaktivna umetnost + dizajn
role:
    - id: designer
      name: Ko-dizajner
    - id: programmer
      name: Ko-programer
    - id: researcher
      name: Akademski istraživač
medium:
    - id: dataviz
      name: Interaktivna vizuelizacija podataka
    - id: software
      name: Veb aplikacija
    - id: research
      name: Akademski tekst
team:
    - name: Nikola Milikić
    - name: Bojan Franzee Brankov
    - name: Srđan Keča
    - name: Luka Knežević-Strika
    - name: Jovan Vesić
presentation_title: Presentations
presentations:
    - year: 2013
      events:
        - name: International Conference on Learning Analytics & Knowledge, Leuven, Belgija
publications:
    - year: 2013
      pubs:
        - link: "/download/research/paperista2013.pdf"
          name: "Milikic N., Krcadinac U., Jovanovic J., Brankov B. & Keča S.: Visual Exploration of Semantically Annotated Research Papers, Learning Analytics and Knowledge. Data Challenge, 2013."
img_to_show: 2
img_data:
    - size: "652x654"
      caption: "Paperista Visualization (detalj)"
    - size: "924x658"
      caption: "Paperista Visualization (detalj)"
    - size: "1600x960"
      caption: "Paperista interfejs"
    - size: "1600x1080"
      caption: "Različiti pregledi (views) grafikona s mehurićima (bubble chart): (1) sve godine / sve teme (bez istaknutih); sve godine / sve teme (bez istaknutih); sve godine / grupisane teme (sa istaknutima); po godinama / grupisane teme (sa istaknutima)" 
lead: "Opis treba da se napiše... Connecting interactive data visualization design with artifical intelligence, Paperista is an interactive animated visual browser for semantically annotated research papers in the field of technology-enhanced learning."

Paperista considers the problem of visualizing and exploring a dataset about research publications from the two fields of technology-enhanced learning: <a href="https://en.wikipedia.org/wiki/Learning_analytics" target="_blank">Learning Analytics (LA)</a> and <a href="https://en.wikipedia.org/wiki/Educational_data_mining" target="_blank">Educational Data Mining (EDM)</a>. Our approach is based on semantic annotation that associates publications from the dataset with Wikipedia topics.

As a visualization and exploration tool, Paperista presents these topics in the form of bubble and line charts. The tool provides multiple views, thus allowing users to observe and interact with topics, understand their evolution and relationships over time, and compare data originating from different research fields (i.e., LA and EDM). Moreover, user can explore papers to which the presented topics are related to, and make related Web searches to access the papers themselves.

The Paperista system consists of a Web application and a server
application that provides RESTful API for communicating with
the dataset. The Web-based visualization is written in D3.js.
 
 Paperista was made in collaboration between University of Belgrade's <a href="https://goodoldai.org/" target="_blank">GOOD OLD AI Lab</a> and UZROK Studio. <mark>&#9632;</mark>