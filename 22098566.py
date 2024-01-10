#!/usr/bin/env python
# coding: utf-8

# # Import necessary libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Dataset loading

# In[2]:


dataset_path = r'C:\data\matches.csv'
df = pd.read_csv(dataset_path)


# # Summary statistics 

# In[3]:


summary_stats = df.describe()
print('Summary Statistics:')
print(summary_stats)


# # Infographics visualization

# In[4]:


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# Plot 1: Distribution of goals scored (gf) and goals conceded (ga)
sns.histplot(df['gf'], bins=15, kde=True, ax=axes[0, 0], color='skyblue', label='Goals Scored')
sns.histplot(df['ga'], bins=15, kde=True, ax=axes[0, 0], color='orange', label='Goals Conceded')
axes[0, 0].set_title('Distribution of Goals Scored and Conceded')
axes[0, 0].legend()

# Plot 2: Violin plot of Possession vs. Expected Goals (xg)
sns.violinplot(x='poss', y='xg', data=df, ax=axes[0, 1], color='green')
axes[0, 1].set_title('Possession vs. Expected Goals')

# Plot 3: Attendance over time
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
sns.lineplot(x='year', y='attendance', data=df, ax=axes[1, 0], color='purple')
axes[1, 0].set_title('Attendance Over Time')

# Plot 4: Distribution of shots on target (sot)
sns.boxplot(x='season', y='sot', data=df, ax=axes[1, 1], palette='pastel')
axes[1, 1].set_title('Distribution of Shots on Target by Season')

fig.suptitle('Football Matches Analysis - Infographics', fontsize=16)
fig.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('2324VS0011.png', dpi=300)

