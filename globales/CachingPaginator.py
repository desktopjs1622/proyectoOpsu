# Standard Library
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
# Librerias Standard
import collections
from math import ceil

# Librerias Django
# Django Library
from django.core.cache import cache
from django.core.paginator import Paginator
from django.db import connection

# To use the paginator, add the following to your admin class:
# from myapp import CachingPaginator
#
# ...
# ...
# paginator = CachingPaginator
#

class CachingPaginator(Paginator):
    '''
    A custom paginator that helps to cut down on the number of 
    SELECT COUNT(*) form table_name queries. These are really slow, therefore
    once we execute the query, we will cache the result which means the page
    numbers are not going to be very accurate but we don't care
    '''

    def _get_count(self):
        """
        Returns the total number of objects, across all pages.
        """

        try:
            if not self.object_list.query.where:
                # This query that avoids a count(*) alltogether is
                # stolen from https://djangosnippets.org/snippets/2593/
                cursor = connection.cursor()
                cursor.execute("SELECT reltuples FROM pg_class WHERE relname = %s", [self.object_list.query.model._meta.db_table])
                self._count = int(cursor.fetchone()[0])
            else:
                self._count = self.object_list.count()
        except:
            # AttributeError if object_list has no count() method.
            # TypeError if object_list.count() requires arguments
            # (i.e. is of type list).
            self._count = len(self.object_list)
        return self._count
    count = property(_get_count)
