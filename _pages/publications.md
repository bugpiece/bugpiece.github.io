---
layout: single
title: "Publications"
permalink: /publications/
author_profile: true
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  overlay_image: Kloten_Forest.jpg
  caption: "Photo by Daichi Kusumoto / Kloten, Zurich"
excerpt: "List of journal papers and conference proceedings"

---
<!--
How to use jekyll-scholar: https://open-research.gemmadanks.com/tutorials/how-to-use-jekyll-scholar-with-github-pages/
-->

## Conference Proceedings

{% assign publications = site.data.publications | sort: "date" | reverse %}
{% assign current_year = "" %}
{% for item in publications %}
  {% assign year = item.date | date: "%Y" %}
  {% if year != current_year %}
### {{ year }}
{% assign current_year = year %}
  {% endif %}
- *{{ item.title }}*. {{ item.authors }}. _{{ item.venue }}_, {{ item.location }} ({{ item.date | date: "%B %Y" }}).
{% endfor %}
