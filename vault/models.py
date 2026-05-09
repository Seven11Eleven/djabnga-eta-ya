from django.db import models

class MasterRecord(models.Model):
    class Meta:
        managed = False
        db_table = '646a616e676f5f'

def get_part_4():
    hex_data = MasterRecord._meta.db_table
    return bytes.fromhex(hex_data).decode()
