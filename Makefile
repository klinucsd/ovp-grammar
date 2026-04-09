.PHONY: build generate test ovp2en en2ovp parse shell clean

# Build the Docker image
build:
	docker compose build

# Regenerate Python parser from grammar (run after editing OVP.g4)
generate:
	docker compose run --rm \
		-v $(PWD)/src/generated:/app/src/generated \
		ovp-grammar \
		bash -c "antlr4 -Dlanguage=Python3 -visitor -o /tmp/gen grammar/OVP.g4 \
		         && cp /tmp/gen/grammar/*.py src/generated/ \
		         && cp /tmp/gen/grammar/*.tokens src/generated/ \
		         && cp /tmp/gen/grammar/*.interp src/generated/"
	touch src/generated/__init__.py

# Translate OVP → English:  make ovp2en SENTENCE="isha'-uu pagwi-noka u-zawa-dü"
ovp2en:
	@docker compose run --rm ovp-grammar python -m src.translator "$(SENTENCE)"

# Translate English → OVP:  make en2ovp SENTENCE="That coyote cooks that fish."
en2ovp:
	@docker compose run --rm ovp-grammar python -m src.en_to_ovp "$(SENTENCE)"

# Show parse tree:  make parse SENTENCE="isha'-uu pagwi-noka u-zawa-dü"
parse:
	@docker compose run --rm ovp-grammar python -m src.translator --tree "$(SENTENCE)"

# Run tests
test:
	docker compose run --rm ovp-grammar python -m pytest tests/ -v

# Interactive shell inside container
shell:
	docker compose run --rm ovp-grammar bash

# Remove generated files
clean:
	rm -rf src/generated/*.py src/generated/*.interp src/generated/*.tokens
	touch src/generated/__init__.py
