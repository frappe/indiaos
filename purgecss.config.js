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
    "./indiaos/indiaos/doctype/*/templates/*.html",
    "./indiaos/www/*.html",
    "./indiaos/templates/*.html",
    "./indiaos/templates/includes/*.html",
  ],
  css: ["./indiaos/public/css/tailwind.css"]
};

// purgecss -c purgecss.config.js --out indiaos/public/css/build/