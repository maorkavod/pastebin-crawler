from django_cron import CronJobBase, Schedule
from app.models import Paste
from django.conf import settings
import requests
from lxml import html
import sys
import logging
from urllib.parse import urlsplit
from .helpers import PasteEntity

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = settings.GET_POSTS_RUN_EVERY_MINS 
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'app.crawling_pastes'
    
    def do(self):
        url = settings.PASTEBIN_START_URL
        base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
        r = requests.get(settings.PASTEBIN_START_URL)
        if r.status_code == 200:
            tree = html.fromstring(r.content)
            pastes_list = tree.xpath("//ul[@class='sidebar__menu']//li//a")
            for href in pastes_list:
                r = requests.get(base_url + href.get('href').strip("/") )
                if r.status_code == 200:
                    paste_tree = html.fromstring(r.content)
                    paste_craweld = PasteEntity(
                        external_id= href.get('href').strip("/"),
                        title=paste_tree.xpath("//h1//text()"),
                        author=paste_tree.xpath("//div[@class='username']//a//text()"),
                        content=paste_tree.xpath("//div[@class='source']//text()"),
                        date=paste_tree.xpath("//div[@class='date']//span")
                    )
                    obj, created  = Paste.objects.get_or_create(
                        title = paste_craweld.title,
                        author = paste_craweld.author,
                        content = paste_craweld.content,
                        date = paste_craweld.date,
                        external_id = paste_craweld.external_id
                    )
        return '%s crawled pastes' % (len(pastes_list))