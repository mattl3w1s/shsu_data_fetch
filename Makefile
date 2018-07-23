SHSU_programs_URL = 'http://catalog.shsu.edu/degree-programs/'
GENERATED_FILES = data/SHSU_programs_page.html data/program_links.csv program_data

all: $(GENERATED_FILES)

install:
	python3.6 -m venv env; \
	source env/bin/activate; \
	pip install -r requirements.txt;

clean:
	cd data && rm program_links.csv && rm UHD_programs_page.html
	cd data/program_data && $(MAKE) clean

data/extracted_program_data.csv: program_data
	source env/bin/activate; \
	python processors/parse_for_openrefine.py > $@;

program_data: data/program_links.csv
	cd data/program_data && $(MAKE)

data/program_links.csv: data/SHSU_programs_page.html
	source env/bin/activate; \
	cat $< | python processors/extract_program_links.py > $@

data/SHSU_programs_page.html:
	source env/bin/activate; \
	python processors/jsget.py $(SHSU_programs_URL) > $@

