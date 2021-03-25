import tempfile, os
import pandas as pd
import tensorflow_data_validation as tfdv

userdata_json = pd.read_json(r'https://api.moonshots.cl/benefits/userdata')

BASE_DIR = tempfile.mkdtemp(prefix='tfx-data')
OUTPUT_FILE = os.path.join(BASE_DIR, 'output.csv')


userdata_json.to_csv (OUTPUT_FILE, index = None)
train_stats = tfdv.generate_statistics_from_csv(data_location=OUTPUT_FILE)

tfdv.visualize_statistics(train_stats)