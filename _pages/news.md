---
layout: single
title: "News"
permalink: /news/
author_profile: true
header:
  overlay_color: "#30343b"
  overlay_filter: "rgba(48, 52, 59, 0.35)"
  overlay_image: headers/aso-kuju-2026-08-02.webp
  caption: "Photo by Daichi Kusumoto / Aso-Kuju National Park"
---

{% assign news = site.pages | where: "layout", "news_article" | sort: "date" | reverse %}
<div class="news-feed">
  {% for item in news %}
  <article class="news-entry">
    {% include news-gallery.html item=item lazy=true preview=true %}
    <time class="news-date" datetime="{{ item.date | date_to_xmlschema }}">{{ item.date | date: "%B %-d, %Y" }}</time>
    <h2 class="news-title"><a href="{{ item.url | relative_url }}">{{ item.title | escape }}</a></h2>
    <p class="news-body news-excerpt">{{ item.content | markdownify | split: '</p>' | first | strip_html |
    normalize_whitespace }}</p>
  </article>
  {% else %}
  <p>Updates coming soon.</p>
  {% endfor %}
</div>
