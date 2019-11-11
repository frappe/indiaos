class TailwindExtractor {
  static extract(content) {
    return content.match(/[\w-/:]+(?<!:)/g) || [];
  }
}

module.exports = {
  extractors: [
	{
		extractor: TailwindExtractor,
		extensions: ['.html']
	}
  ],
  content: [
    "./conference/www/index.html",
    "./conference/www/travel.html",
    "./conference/templates/game.html",
    "./conference/templates/conference.html",
    "./conference/templates/includes/footer.html",
    "./conference/templates/includes/navbar.html",
    "./conference/templates/includes/modal.html",
  ],
  css: ["./conference/public/css/tailwind.css"]
};

// purgecss -c purgecss.config.js --out conference/public/css/build/