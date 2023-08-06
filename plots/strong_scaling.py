import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.gridspec as gridspec
import matplotlib
import matplotlib.cm as cm
import seaborn as sns

xs = "nodes"
ys = "All[sec]"

gpu_df = pd.read_csv("../results/chase_gpu_vs_elpa_nccl.csv")
gpu_df_2 = pd.read_csv("../results/chase_gpu_vs_elpa.csv")
gpu_df_3 = pd.read_csv("../results/chase_gpu_vs_elpa_old.csv")
elpa1_df = pd.read_csv("../results/elpa1_gpu.csv")
elpa2_df = pd.read_csv("../results/elpa2_gpu.csv")
#df = pd.concat([cpu_df, gpu_df, cpu_df_old, gpu_df_old])
gpu_df = gpu_df[['solver', 'nodes','All[sec]']]
gpu_df_2 = gpu_df_2[['solver', 'nodes','All[sec]']]
gpu_df_3 = gpu_df_3[['solver', 'nodes','All[sec]']]
elpa1_df = elpa1_df[['solver', 'nodes','All[sec]']]
elpa2_df = elpa2_df[['solver', 'nodes','All[sec]']]


df = pd.concat([gpu_df, gpu_df_2, gpu_df_3, elpa1_df, elpa2_df])

df.sort_values(by=['nodes'])


f, ax = plt.subplots(figsize=(3, 3.2 ))

plt.plot([df['nodes'].min(),df['nodes'].max()], [gpu_df['All[sec]'].max(),gpu_df['All[sec]'].max()*df['nodes'].min()/df['nodes'].max()], linestyle="--",color="gray")

g = sns.lineplot(x=xs, y=ys, hue="solver", style="solver", linewidth=2, markersize=8, markers=['.','.','.','.','.'], palette = "Set1", dashes=False, ci="sd", data=df)

ax.set_yscale('log')
ax.set_xscale('log')

ticks = df['nodes'].drop_duplicates().values.tolist()
ax.set_xticks(ticks)
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
plt.minorticks_off()
ax.tick_params(axis='x', rotation=90)


yLocator = matplotlib.ticker.LogLocator(base=10,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0)) 
ax.get_yaxis().set_major_locator(yLocator)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles[0:], labels=labels[0:], fontsize=7.5,ncol=1,loc='upper right', frameon=False)
#ax.set_title('Strong scaling')
ax.set_xlabel('Number of Nodes', fontsize=12)
ax.set_ylabel('Time to solution (s)',fontsize=12)
ax.set_ylim([0.5,9999])
ax.set_xlim([2,200])

plt.yticks(fontsize=8)
plt.xticks(fontsize=8)
ax.tick_params(axis="x",direction="in", pad=-20 )
ax.tick_params(axis="y",direction="in", pad=-20)

f.savefig('pdf/strong_scaling.pdf', bbox_inches='tight')
