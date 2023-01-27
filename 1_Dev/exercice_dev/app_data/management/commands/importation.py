from django.core.management.base import BaseCommand, CommandError
from app_data.models import Annonce
import csv

class Command(BaseCommand):
    help = 'Import data'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(r'D:\Docs\Documents\Script Python\Test_technique_Copro\1_Dev\exercice_dev\app_data\dataset_annonces.csv', encoding='utf-8') as csv_file:

            next(csv_file)
            csv_reader = csv.reader(csv_file, delimiter = ',')
            
            for row in csv_reader:
                try:
                    if int(row[3] != 1):
                        if int(row[3]) > 3:
                            break
                        try:
                            annonce = Annonce(prix = int(row[11]), departement = int(row[3]),
                                              ville = row[5], code_ville = int(row[4]))
                            annonce.save()
                        except:
                            pass
                except:
                    pass
        self.stdout.write(self.style.SUCCESS('Successfully import data'))
                              
