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
    "./indiaos/www/index.html",
    "./indiaos/www/travel.html",
    "./indiaos/templates/game.html",
    "./indiaos/templates/conference.html",
    "./indiaos/templates/includes/footer.html",
    "./indiaos/templates/includes/navbar.html",
    "./indiaos/templates/includes/modal.html",
  ],
  css: ["./indiaos/public/css/tailwind.css"]
};

// purgecss -c purgecss.config.js --out indiaos/public/css/build/