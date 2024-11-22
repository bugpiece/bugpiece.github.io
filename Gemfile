source "https://rubygems.org"

# 共通のGem
gem "jekyll"
gem "webrick", "~> 1.7"
gem "nokogiri", "< 1.16" # nokogiriのバージョン制限

# ローカル環境用のGem
group :development do
  gem "jekyll-scholar", group: :jekyll_plugins
end

# GitHub Pages環境用のGem
group :jekyll_plugins do
  gem "github-pages", "<= 227"
  gem "jekyll-feed"
  gem "jekyll-sitemap"
  gem "hawkins"
  gem "dotenv"
end

# Windows特有のGem
gem "wdm", "~> 0.1.0" if Gem.win_platform?