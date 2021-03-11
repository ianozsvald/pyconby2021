import os

ROOT = os.path.expanduser('~/data/land_registry/202103')
RAW_DATA = os.path.join(ROOT, "pp-complete-202103.csv")
PICKLE = os.path.join(ROOT, "pp-complete-202103.pickle")
PICKLE_PROT4 = os.path.join(ROOT, "pp-complete-202103-prot4.pickle")
COLUMNS = ['tin', 'price', 'date', 'postcode', 'pt', 'new', 'duration', 'paon', 'saon',
           'street', 'locality', 'town', 'district', 'county', 'ppd_cat', 'status']

