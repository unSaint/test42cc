PROJECT_NAME=test42cc
PYTHONPATH=$(CURDIR):$(CURDIR)/$(PROJECT_NAME)

MANAGE= PYTHONPATH=$(PYTHONPATH) python $ manage.py

runserver:
	$(MANAGE) runserver --settings=test42cc.settings

shell:
	$(MANAGE) shell --settings=test42cc.settings

syncdb:
	$(MANAGE) syncdb --settings=test42cc.settings

migrate:
	$(MANAGE) migrate --settings=test42cc.settings

test:
	$(MANAGE) test