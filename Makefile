.PHONY: build deploy

build:
	hyde -g
	cd deploy/blog && find . -name "*.html" ! -name "index.html" -exec bash -c 'mkdir -p $$(basename {} .html) && mv {} $$(basename {} .html)/index.html' \;


deploy:
	aws s3 sync --delete deploy s3://joshbohde.com
