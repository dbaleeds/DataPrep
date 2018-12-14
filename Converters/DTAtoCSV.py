
import pandas as pd
from pathlib import Path

p = Path("Converters/DTA")

for i in p.glob('*.dta'):
    data = pd.io.stata.read_stata("Converters/DTA/"+ i.name)
    data.to_csv("Converters/DTA/CSV/"+ i.name.replace("dta","csv"))
