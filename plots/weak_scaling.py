import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
import matplotlib.gridspec as gridspec
import matplotlib
import matplotlib.cm as cm
import seaborn as sns

xs = "nodes"
ys = "All[sec]"

gpu_df_nccl = pd.read_csv("../results/weak-scaling-gpu-new-nccl.csv")
gpu_df = pd.read_csv("../results/weak-scaling-gpu-new.csv")
gpu_df_old = pd.read_csv("../results/weak-scaling-gpu-old.csv")

gpu_df_nccl = gpu_df_nccl[['mode', 'nodes','All[sec]']]
gpu_df = gpu_df[['mode', 'nodes','All[sec]']]
gpu_df_old = gpu_df_old[['mode', 'nodes','All[sec]']]

gpu_df_nccl['solver'] = 'ChASE(NCCL)'
gpu_df['solver'] = 'ChASE(STD)'
gpu_df_old['solver'] = 'ChASE(LMS)'

df = pd.concat([gpu_df_nccl, gpu_df, gpu_df_old])
df.sort_values(by=['nodes'])

f, ax = plt.subplots(figsize=(3, 3.2))

plt.plot([df['nodes'].min(),df['nodes'].max()], [gpu_df_nccl['All[sec]'].min(),gpu_df_nccl['All[sec]'].min()], linestyle="--",color="gray")

g = sns.lineplot(x=xs, y=ys, hue="solver", style="solver", linewidth=2, markersize=8, palette = "Set1", markers=['.','.','.'], dashes=False, ci="sd", data=df)

ax.set_yscale('log')
ax.set_xscale('log')


plt.minorticks_off()

ticks = [1,4,9,16,25,36, 64,100,256,400,625,900]
ax.set_xticks(ticks)
ax.tick_params(axis='x', rotation=90)
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
plt.minorticks_off()


yLocator = matplotlib.ticker.LogLocator(base=10,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0)) 
ax.get_yaxis().set_major_locator(yLocator)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles[0:], labels=labels[0:], fontsize=7.5,ncol=1,loc='upper left',frameon=False)
#ax.set_title('Weak scaling')
ax.set_xlabel('Number of Nodes', fontsize=12)
ax.set_ylabel('Time to solution (s)',fontsize=12)
ax.set_ylim([1.1,50]) 
plt.yticks(fontsize=8)
plt.xticks(fontsize=8)
ax.tick_params(axis="x",direction="in", pad=-20 )
ax.tick_params(axis="y",direction="in", pad=-20)

f.savefig('pdf/weak_scaling.pdf', bbox_inches='tight')
