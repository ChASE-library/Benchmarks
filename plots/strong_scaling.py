import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.gridspec as gridspec
import matplotlib
import matplotlib.cm as cm
import seaborn as sns

xs = "nodes"
ys = "All[sec]"

cpu_df = pd.read_csv("../results/strong-scaling-cpu-new.csv")
gpu_df = pd.read_csv("../results/strong-scaling-gpu-new.csv")
cpu_df_old = pd.read_csv("../results/strong-scaling-cpu-old.csv")
gpu_df_old = pd.read_csv("../results/strong-scaling-gpu-old.csv")
df = pd.concat([cpu_df, gpu_df, cpu_df_old, gpu_df_old])
df.sort_values(by=['nodes'])

f, ax = plt.subplots(figsize=(6, 6))

g = sns.lineplot(x=xs, y=ys, hue="mode", style="mode", linewidth=2, markersize=8, palette = "Set1", markers=['s','d','o','^'], dashes=False, ci="sd", data=df)

ax.set_yscale('log')
ax.set_xscale('log')

ticks = df['nodes'].drop_duplicates().values.tolist()
ax.set_xticks(ticks)
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
plt.minorticks_off()

plt.plot([df['nodes'].min(),df['nodes'].max()], [df['All[sec]'].max(),df['All[sec]'].max()*df['nodes'].min()/df['nodes'].max()], linestyle="--",color="gray")

yLocator = matplotlib.ticker.LogLocator(base=10,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0)) 
ax.get_yaxis().set_major_locator(yLocator)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles[0:], labels=labels[0:], fontsize=11,ncol=1,loc='upper left')
ax.set_title('Strong scaling')
ax.set_xlabel('Number of Nodes', fontsize=18)
ax.set_ylabel('Time to solution (s)',fontsize=18)
ax.set_ylim([1,10000])
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)
f.savefig('jpeg/strong_scaling.jpeg')

