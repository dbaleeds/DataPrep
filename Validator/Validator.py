import os.path
import cutplace
import logging
import cutplace.errors
from pathlib import Path


#set up logging
logging.basicConfig(level=logging.WARNING,filename='Validator/validation.log',filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger('cutplace').setLevel(logging.WARNING)

#iterate through data folder
p = Path("Validator/data")
for i in p.glob('*.csv'):
    # log file checked.
    logging.info('%s' % ' checking file ' + i.name)
    try:
        for row_or_error in cutplace.rows('Validator/cid_customers.ods', 'Validator/data/' + i.name, on_error='yield'):
            if isinstance(row_or_error, Exception):
                if isinstance(row_or_error, cutplace.errors.CutplaceError):
                    # log data related error details and move on.
                    logging.warning('%s' % row_or_error )
                else:
                    # Let other, more severe errors terminate the validation.
                    logging.error('%s' %  row_or_error )
            else:
                logging.info('%s'  %  row_or_error + ' Success')
    except Exception as e:
        print(e)
        logging.critical("Exception occurred" + e, exc_info=True)