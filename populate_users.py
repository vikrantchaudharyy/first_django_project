import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_django_project.settings')

import django
# Import settings
django.setup()

import random
from first_app.models import WebPage, Topic, AccessRecord
from faker import Faker

fakegen = Faker()

TOPIC_LIST = ['Social', 'Search', 'Games', 'News', 'MarketPlace']
def addTopic():
    t = Topic.objects.get_or_create(top_name=random.choice(TOPIC_LIST))[0]
    t.save()
    return t


def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        topic = addTopic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = WebPage.objects.get_or_create(topic=topic, name=fake_name, url=fake_url)[0]
        # webpg.save()

        access_record = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        # access_record.save()

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
