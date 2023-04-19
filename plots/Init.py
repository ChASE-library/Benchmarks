import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
import matplotlib.gridspec as gridspec
import matplotlib
import matplotlib.cm as cm

def plot_clustered_stacked_2(dfall, output, labels=None, indices=None, title="multiple stacked bar plot", ranges=None, H="///", legend=True, **kwargs):

    n_df = len(dfall)
    n_col = len(dfall[0].columns) 
    n_ind = len(dfall[0].index)
    plt.figure(figsize=(6,6)) 

    axe = plt.subplot(111)

    axe = dfall[0].plot(kind="bar",
                      linewidth=1,
                       #width=0.2,
                      stacked=True,
                      ax=axe,
                      legend=False,
                      grid=False,
                      position=0.35,
                      **kwargs)  # make bar plots
    axe = dfall[1].plot(kind="bar",
                      linewidth=1,
                        #width=0.2,
                      stacked=True,
                      ax=axe,
                      legend=False,
                      grid=False,
                      position=0.35,
                      **kwargs)  # make bar plots

    h,l = axe.get_legend_handles_labels() # get the handles we want to modify
    for i in range(0, n_df * n_col, n_col): # len(h) = n_col * n_df
        for j, pa in enumerate(h[i:i+n_col]):
            for rect in pa.patches: # for each index
                rect.set_x(rect.get_x() + 1. / float(n_df + 1) * i / float(n_col))
                #print(rect.get_x() + 1 / float(n_df + 1) * i / float(n_col))
                rect.set_hatch(H * int(i / n_col)) #edited part     
                rect.set_width(1. / float(n_df + 1))

    axe.set_xticks((np.arange(0, 2 * n_ind, 2) + 1 / float(n_df + 1)) / 2.)
    axe.set_xticklabels(indices, rotation = 0, fontsize=12)
    plt.yticks(fontsize=12)

    axe.set_ylabel("Time (s)",fontsize=12)
    axe.set_xlabel("Number of Nodes",fontsize=12)

    axe.set_title(title)
    if ranges != None:
        axe.set_ylim(ranges)
    # Add invisible data to add another legend
    if legend:
        n=[]    
        for i in range(n_df):
            n.append(axe.bar(0, 0, color="gray", hatch=H * i))

        l1 = axe.legend(h[:n_col], l[:n_col], loc=[1.01, 0.5])
        if labels is not None:
            l2 = plt.legend(n, labels, loc=[1.01, 0.1]) 
        axe.add_artist(l1)

    plt.savefig(output)

    return axe


if __name__ == '__main__':
    df=pd.read_csv('../results/Initialization_overhead_old.csv') 
    df.set_index("Nodes")
    init_old_1=df[(df["Impls"] == "ChASEv1.2 (CPU)") & (df["Kernels"] == "Init")][["Random Generation","Others"]]
    init_old_2=df[(df["Impls"] == "ChASEv1.2 (GPU)") & (df["Kernels"] == "Init")][["Random Generation","Others"]]

    init_old_1["Random Generation"] = init_old_1["Random Generation"] / 1e9
    init_old_2["Random Generation"] = init_old_2["Random Generation"] / 1e9
    init_old_1["Others"] = init_old_1["Others"] / 1e9
    init_old_2["Others"] = init_old_2["Others"] / 1e9

    df=pd.read_csv('../results/Initialization_overhead_new.csv') 
    df.set_index("Nodes")

    init_new_1=df[(df["Impls"] == "ChASEv1.3 (CPU)") & (df["Kernels"] == "Init")][["Random Generation","Others"]]
    init_new_2=df[(df["Impls"] == "ChASEv1.3 (GPU)") & (df["Kernels"] == "Init")][["Random Generation","Others"]]

    init_new_1["Random Generation"] = init_new_1["Random Generation"] / 1e9
    init_new_2["Random Generation"] = init_new_2["Random Generation"] / 1e9
    init_new_1["Others"] = init_new_1["Others"] / 1e9
    init_new_2["Others"] = init_new_2["Others"] / 1e9

    plot_clustered_stacked_2([init_old_1, init_old_2],'./jpeg/Init-old-ChASE.jpeg',["ChASEv1.2 (CPU)", "ChASEv1.2 (GPU)"],["1","4","16","64"],title='Initialization: ChASEv1.2', legend=False,cmap=plt.cm.tab20c)

    plot_clustered_stacked_2([init_new_1, init_new_2],'./jpeg/Init-new-ChASE.jpeg',["ChASEv1.3 (CPU)", "ChASEv1.3 (GPU)"],["1","4","16","64"],title='Initialization: ChASEv1.3', legend=False,cmap=plt.cm.tab20c)

