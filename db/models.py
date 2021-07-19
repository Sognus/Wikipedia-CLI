# Python library imports
import sys
import json

# 3rd party imports
import wikipedia

# Django import attempt
try:
    from django.db import models
    from django.utils.timezone import now
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


# Wikipedia model
class WikipediaData(models.Model):
    class Meta:
        db_table = "wikidata"

    name = models.TextField(primary_key=True)
    search = models.TextField()
    summary = models.TextField()
    cached_at = models.DateTimeField(default=now)

    def fill_model_from_api(self, name):
        self.name = name
        lookup = wikipedia.search(name)
        self.search = json.dumps(lookup, ensure_ascii=False)

        try:
            # Page was found
            lookup = wikipedia.summary(name, auto_suggest=False)
            first = lookup.find("\n")
            self.summary = lookup[:first]
        except wikipedia.PageError:
            text_base = "Článek s názvem '{}' nebyl nalezen. "
            text_base = text_base.format(name)
            if len(lookup) > 0:
                text = text_base + "Zadaný text se vyskytujev článcích s tímto názvem:"

                for article in lookup:
                    text = text + "\n - " + article

                self.summary = text
            else:
                text = text_base + "Na Váš dotaz nebyly nalezeny žádné výsledky."
                self.summary = text
        except wikipedia.DisambiguationError:
            text = "{} může mít více významů: "
            text = text.format(name.capitalize())

            for article in lookup:
                text = text + "\n - " + article

            self.summary = text

