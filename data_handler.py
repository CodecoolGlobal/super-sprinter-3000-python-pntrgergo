import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']
DATABASE_FILE = 'data.csv'


def get_all_user_story():
    list_of_stories = []
    with open(DATABASE_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list_of_stories.append(row)
    return list_of_stories


def read_from_file(filename):
    list_of_stories = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list_of_stories.append(row)
    return list_of_stories


def write_to_file(stories):
    with open(DATABASE_FILE, 'w', newline='') as csvfile:
        fieldnames = DATA_HEADER
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for story in stories:
            writer.writerow({'id': story['id'],
                             'title': story['title'],
                             'user_story': story['user_story'],
                             'acceptance_criteria': story['acceptance_criteria'],
                             'business_value': story['business_value'],
                             'estimation': story['estimation'],
                             'status': story['status']
                             })
