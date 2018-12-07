import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('cutplace').setLevel(logging.WARNING)

import os.path
import cutplace

# Compute the path of a test file in a system independent manner,
# assuming that the current folder is "docs".
#cid_path = os.path.join(os.pardir, '', 'cid_customers.ods')
cid = cutplace.Cid('cid_customers.ods')

cutplace.validate('cid_customers.ods', 'customer.csv')