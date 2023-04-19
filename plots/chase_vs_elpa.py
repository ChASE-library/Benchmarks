import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
import matplotlib.gridspec as gridspec
import matplotlib
import matplotlib.cm as cm
import seaborn as sns

ELPA1_gpu_df = pd.read_csv("../results/elpa1_gpu.csv")
ELPA2_gpu_df = pd.read_csv("../results/elpa2_gpu.csv")
ChASE_cpu_df = pd.read_csv("../results/chase_cpu_vs_elpa.csv")
ChASE_gpu_df = pd.read_csv("../results/chase_gpu_vs_elpa.csv")


ELPA1_gpu_df['All[sec]'] = ELPA1_gpu_df['time[sec]']
ELPA2_gpu_df['All[sec]'] = ELPA2_gpu_df['time[sec]']


ChASE_gpu_df_mean = ChASE_gpu_df.groupby(['nodes']).mean()
ELPA2_gpu_df_mean = ELPA2_gpu_df.groupby(['nodes']).mean()

speedup1 = (ELPA2_gpu_df_mean['All[sec]']/ChASE_gpu_df_mean['All[sec]']).values.tolist()

df = pd.concat([ChASE_cpu_df, ChASE_gpu_df,ELPA1_gpu_df,ELPA2_gpu_df], axis=0, sort=False)

f, ax = plt.subplots(figsize=(12, 6))
g = sns.barplot(x="nodes", y="All[sec]", hue="solver", data=df) 

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles[0:], labels=labels[0:], fontsize=11,ncol=1,loc='upper right')

ax2 = ax.twiny().twinx()

x=np.arange(2.5,5*len(speedup1),5)
ax2.plot(x,speedup1,marker='o',color='black',ls='-.')
for i,j in zip(x,speedup1):
    ax2.annotate(str(round(j,1)),xy=(i,j+0.5))

ax2.set_ylabel('Speedup',fontsize=18)
 
ax2.set_xticks([])
ax2.set_ylim([0,15])
ax2.set_xlim([0,5*len(speedup1)])

ax.set_xlabel('Number of Nodes', fontsize=18)
ax.set_ylabel('Time to solution (s)',fontsize=18)
ax.set_yscale('log')
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
#ax.set_ylim([4,4200])
ax.legend(ncol=2,loc='upper right')

plt.title("ChASE VS ELPA")

f.savefig('jpeg/ChASE_VS_ELPA.jpeg')
