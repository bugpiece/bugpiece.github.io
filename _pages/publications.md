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

{% assign publications = site.data.publications | sort: "date" | reverse %}
{% assign me = "Daichi Kusumoto" %}

{% assign journals = publications | where: "type", "journal" %}
{% if journals.size > 0 %}
## Journal Articles
{% assign current_year = "" %}
{% for item in journals %}
{% assign year = item.date | date: "%Y" %}
{% if year != current_year %}
### {{ year }}
{% assign current_year = year %}
{% endif %}
<div class="pub-item">
<div class="pub-title">{% if item.doi %}<a href="https://doi.org/{{ item.doi }}">{{ item.title }}</a>{% else %}{{ item.title }}{% endif %}</div>
<div class="pub-authors">{{ item.authors | replace: me, "<b>Daichi Kusumoto</b>" }}</div>
<div class="pub-venue"><em>{{ item.venue }}</em>{% if item.volume %}, {{ item.volume }}{% endif %}{% if item.articleno %}, {{ item.articleno }}{% endif %} &middot; {{ item.date | date: "%B %Y" }}{% if item.note %} &middot; {{ item.note }}{% endif %}</div>
{% if item.doi %}<div class="pub-links"><a href="https://doi.org/{{ item.doi }}">https://doi.org/{{ item.doi }}</a></div>{% endif %}
</div>
{% endfor %}
{% endif %}

{% assign conferences = publications | where: "type", "conference" %}
{% if conferences.size > 0 %}
## Conference Proceedings
{% assign current_year = "" %}
{% for item in conferences %}
{% assign year = item.date | date: "%Y" %}
{% if year != current_year %}
### {{ year }}
{% assign current_year = year %}
{% endif %}
<div class="pub-item">
<div class="pub-title">{% if item.doi %}<a href="https://doi.org/{{ item.doi }}">{{ item.title }}</a>{% else %}{{ item.title }}{% endif %}</div>
<div class="pub-authors">{{ item.authors | replace: me, "<b>Daichi Kusumoto</b>" }}</div>
<div class="pub-venue"><em>{{ item.venue }}</em>{% if item.location %}, {{ item.location }}{% endif %} &middot; {{ item.date | date: "%B %Y" }}{% if item.note %} &middot; {{ item.note }}{% endif %}</div>
{% if item.doi %}<div class="pub-links"><a href="https://doi.org/{{ item.doi }}">https://doi.org/{{ item.doi }}</a></div>{% endif %}
</div>
{% endfor %}
{% endif %}
