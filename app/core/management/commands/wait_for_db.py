from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError
import time

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for DB connection ...')

        is_db_connected = None
        while not is_db_connected:
            try:
                is_db_connected = connections['default']
            except (OperationalError, Psycopg2OpError):
                self.stdout.write("Retrying DB connection ...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Congrats! PostgreSQL Connection Success!!!"))
