#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Başlangıç değerlerini tanımlayalım
veri = pd.read_csv("TIC279664975 s1.csv")
t0 = 1767.086487
P = 24.57448684

# E değerlerinin listesi
E_values = [i for i in range(0, 94)]  # 0.5'ten 46.5'e kadar 0.5 artışlarla 93 değer
E_values = [0.5 * i for i in E_values]

# T değerlerini hesaplayalım
T_values = [t0 + E * P for E in E_values]

# Sonuçları yazdır
for E, T in zip(E_values, T_values):
    print(f"E = {E:.1f}, T = {T:.6f}")


# In[3]:


# Başlangıç değerlerini tanımlayalım
import pandas as pd
# CSV dosyasını oku
veri = pd.read_csv("TIC298314179 s2.csv")
t0 = 1765.836456
P = 7.557813

# E değerlerinin listesi
E_values = [i for i in range(1, 303)]  
E_values = [0.5 * i for i in E_values]

# T değerlerini hesaplayalım
T_values = [t0 + E * P for E in E_values]

# Sonuçları yazdır
for E, T in zip(E_values, T_values):
    print(f"E = {E:.1f}, T = {T:.6f}")


# In[1]:


# Başlangıç değerlerini tanımlayalım
import pandas as pd
# CSV dosyasını oku
veri = pd.read_csv("TIC279868244 s3.csv")
t0 = 1766.45105
P = 1.6905



# E değerlerinin listesi
E_values = [i for i in range(1, 676)]  
E_values = [0.5 * i for i in E_values]

# T değerlerini hesaplayalım
T_values = [t0 + E * P for E in E_values]

# Sonuçları yazdır
for E, T in zip(E_values, T_values):
    print(f"E = {E:.1f}, T = {T:.6f}")


# In[ ]:




