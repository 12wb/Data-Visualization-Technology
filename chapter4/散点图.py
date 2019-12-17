"""import ggplot as gp
import pandas as pd
import numpy as np
crime = pd.read_csv("crimeRatesByState2005.csv",engine='python')
print(gp.ggplot(gp.aes(x='murder',y='burglary'),data=crime)+gp.geom_point(color='red'))
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
crime = pd.read_csv("crimeRatesByState2005.csv",engine='python')
crime2 = crime[crime.state != "United Ststes"]
crime2 = crime2[crime2.state !="District of Columbia"]
crime2 = crime2.drop(['state'],axis=1)
crime2 = crime2.drop(['population'],axis=1)
g = sns.pairplot(crime2,diag_kind="kde")
plt.show()