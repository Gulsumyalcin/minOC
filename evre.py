#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyasını oku
veri = pd.read_csv(("./S17_not.csv"))
# time sütununu içeren bir DataFrame oluştur
time_df = veri[['time']]
flux_degerleri = veri["flux"]



# T0 hesapla
T0 = 1765.836456
print(f"T0: {T0}")

dönem =  7.557813

print(f"dönem: {dönem}")

evre= (time_df - T0)/dönem

evre2 = evre - np.floor(evre)

print(f"evre: {evre2}")

# Nokta dağılım grafiği çiz
plt.scatter(evre2, flux_degerleri)
plt.xlabel('Evre')
plt.ylabel('Flux')
plt.title('Evre vs Flux Dağılım Grafiği')
plt.show()


# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyasını oku
veri = pd.read_csv(("./S18_not.csv"))
# time sütununu içeren bir DataFrame oluştur
time_df = veri[['time']]
flux_degerleri = veri["flux"]



# T0 hesapla
T0 = 1765.836456
print(f"T0: {T0}")

dönem =  7.557813

print(f"dönem: {dönem}")

evre= (time_df - T0)/dönem

evre2 = evre - np.floor(evre)

print(f"evre: {evre2}")

# Nokta dağılım grafiği çiz
plt.scatter(evre2, flux_degerleri)
plt.xlabel('Evre')
plt.ylabel('Flux')
plt.title('Evre vs Flux Dağılım Grafiği')
plt.show()


# In[32]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyasını oku
veri = pd.read_csv("./star_not.txt")   
# time sütununu içeren bir DataFrame oluştur
time_df = veri[['time']]
flux_degerleri = veri["flux"]



# T0 hesapla
T0 = 1765.836456
print(f"T0: {T0}")

dönem =  7.557813

print(f"dönem: {dönem}")

evre= (time_df - T0)/dönem

evre2 = evre - np.floor(evre)

print(f"evre: {evre2}")

# Nokta dağılım grafiği çiz
plt.scatter(evre2, flux_degerleri)
plt.xlabel('Evre')
plt.ylabel('Flux')
plt.title('Evre vs Flux Dağılım Grafiği')
plt.show()


# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyasını oku
veri = pd.read_csv(("./S57_not.csv"))
# time sütununu içeren bir DataFrame oluştur
time_df = veri[['time']]
flux_degerleri = veri["flux"]



# T0 hesapla
T0 = 1765.836456
print(f"T0: {T0}")

dönem =  7.557813

print(f"dönem: {dönem}")

evre= (time_df - T0)/dönem

evre2 = evre - np.floor(evre)

print(f"evre: {evre2}")

# Nokta dağılım grafiği çiz
plt.scatter(evre2, flux_degerleri)
plt.xlabel('Evre')
plt.ylabel('Flux')
plt.title('Evre vs Flux Dağılım Grafiği')
plt.show()


# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyasını oku
veri = pd.read_csv(("./S58_note.csv"))
# time sütununu içeren bir DataFrame oluştur
time_df = veri["time"]
flux_degerleri = veri["flux"]



# T0 hesapla
T0 = 1765.836456
print(f"T0: {T0}")

dönem =  7.557813

print(f"dönem: {dönem}")

evre= (time_df - T0)/dönem

evre2 = evre - np.floor(evre)

print(f"evre: {evre2}")

# Nokta dağılım grafiği çiz
plt.scatter(evre2, flux_degerleri)
plt.xlabel('Evre')
plt.ylabel('Flux')
plt.title('Evre vs Flux Dağılım Grafiği')
plt.show()


# In[ ]:




