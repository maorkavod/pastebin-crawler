from datetime import timezone
import re
import dateutil.parser

class PasteEntity:
    def __init__(self, title = [''], author = [''], content = [], date = False, external_id = ''):
        
        self.replace_cases_to_empty_string = ['guest','unknown','anonymous','untitled']
        self.title = title[0]
        self.author = author[0]
        self.content = content
        self.date = date
        self.external_id = external_id

    @property
    def get_title(self):
        return self._title
    
    @get_title.setter
    def title(self, value):
        if value.lower() in self.replace_cases_to_empty_string:
            value = ''
        self._title = value

    @property
    def get_author(self):
        return self._author
    
    @get_author.setter
    def author(self, value):
        if value.lower() in self.replace_cases_to_empty_string:
            value = ''
        self._author = value
    
    @property
    def get_content(self):
        return self._content
    
    @get_content.setter
    def content(self, value):
        value = str(''.join(value).encode('ascii','ignore')).strip()
        self._content = re.sub(r"\s+", "", value)

    @property
    def get_date(self):
        return self._date
    
    @get_date.setter
    def date(self, value):
        if value:
            self._date = dateutil.parser.parse(value[0].get('title')).astimezone(timezone.utc)