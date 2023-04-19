import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator
import matplotlib.gridspec as gridspec
import matplotlib
import matplotlib.cm as cm

def plot_clustered_stacked(dfall, output, labels=None, indices=None, title="multiple stacked bar plot", ranges=None, H="///", legend=True, **kwargs):

    n_df = len(dfall)
    n_col = len(dfall[0].columns)
    n_ind = len(dfall[0].index)
    plt.figure(figsize=(8,6))

    axe = plt.subplot(111)

    for df in dfall : # for each data frame
        axe = df.plot(kind="bar",
                      linewidth=1,
                      stacked=True,
                      ax=axe,
                      legend=False,
                      grid=False,
                      position=0.35,
                      #colormap=cmp_list[cnt],
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
    df=pd.read_csv('../results/chase_Kernel_comm_vs_compute.csv')
    df.set_index("Nodes")

    qr_cpu_1=df[(df["Impls"] == "ChASEv1.2 (CPU)") & (df["Kernels"] == "QR")][["Compt.","Comm."]]
    qr_cpu_2=df[(df["Impls"] == "ChASEv1.3 (CPU)") & (df["Kernels"] == "QR")][["Compt.","Comm."]]

    qr_cpu_1["Compt."] = qr_cpu_1["Compt."]/1e9
    qr_cpu_1["Comm."] = qr_cpu_1["Comm."]/1e9
    qr_cpu_2["Compt."] = qr_cpu_2["Compt."]/1e9
    qr_cpu_2["Comm."] = qr_cpu_2["Comm."]/1e9
    plot_clustered_stacked([qr_cpu_1, qr_cpu_2],'./jpeg/QR-CPU.jpeg', ["ChASEv1.2 (CPU)", "ChASEv1.3 (CPU)"],["1","4","16","64"],title='QR on CPUs', legend=False,cmap=plt.cm.Set1)


    rr_cpu_1=df[(df["Impls"] == "ChASEv1.2 (CPU)") & (df["Kernels"] == "RR")][["Compt.","Comm."]]
    rr_cpu_2=df[(df["Impls"] == "ChASEv1.3 (CPU)") & (df["Kernels"] == "RR")][["Compt.","Comm."]]

    rr_cpu_1["Compt."] = rr_cpu_1["Compt."]/1e9
    rr_cpu_1["Comm."] = rr_cpu_1["Comm."]/1e9
    rr_cpu_2["Compt."] = rr_cpu_2["Compt."]/1e9
    rr_cpu_2["Comm."] = rr_cpu_2["Comm."]/1e9

    plot_clustered_stacked([rr_cpu_1, rr_cpu_2],'./jpeg/RR-CPU.jpeg', ["ChASEv1.2 (CPU)", "ChASEv1.3 (CPU)"],["1","4","16","64"],title='RR on CPUs', legend=False,cmap=plt.cm.Set1)


    resid_cpu_1=df[(df["Impls"] == "ChASEv1.2 (CPU)") & (df["Kernels"] == "Resid")][["Compt.","Comm."]]
    resid_cpu_2=df[(df["Impls"] == "ChASEv1.3 (CPU)") & (df["Kernels"] == "Resid")][["Compt.","Comm."]]
    resid_cpu_1["Compt."] = resid_cpu_1["Compt."]/1e9
    resid_cpu_1["Comm."] = resid_cpu_1["Comm."]/1e9
    resid_cpu_2["Compt."] = resid_cpu_2["Compt."]/1e9
    resid_cpu_2["Comm."] = resid_cpu_2["Comm."]/1e9

    plot_clustered_stacked([resid_cpu_1, resid_cpu_2],'./jpeg/Resid-CPU.jpeg',["ChASEv1.2", "ChASEv1.3"],["1","4","16","64"],title='Resid on CPUs',  legend=False,cmap=plt.cm.Set1)


    qr_gpu_1=df[(df["Impls"] == "ChASEv1.2 (GPU)") & (df["Kernels"] == "QR")][["Compt.","Comm."]]
    qr_gpu_2=df[(df["Impls"] == "ChASEv1.3 (GPU)") & (df["Kernels"] == "QR")][["Compt.","Comm."]]
    qr_gpu_1["Compt."] = qr_gpu_1["Compt."]/1e9
    qr_gpu_1["Comm."] = qr_gpu_1["Comm."]/1e9
    qr_gpu_2["Compt."] = qr_gpu_2["Compt."]/1e9
    qr_gpu_2["Comm."] = qr_gpu_2["Comm."]/1e9

    plot_clustered_stacked([qr_gpu_1, qr_gpu_2],'./jpeg/QR-GPU.jpeg',["ChASEv1.2 (GPU)", "ChASEv1.3 (GPU)"],["1","4","16","64"],title='QR on GPUs',  legend=False,cmap=plt.cm.Set1)

    rr_gpu_1=df[(df["Impls"] == "ChASEv1.2 (GPU)") & (df["Kernels"] == "RR")][["Compt.","Comm."]]
    rr_gpu_2=df[(df["Impls"] == "ChASEv1.3 (GPU)") & (df["Kernels"] == "RR")][["Compt.","Comm."]]
    rr_gpu_1["Compt."] = rr_gpu_1["Compt."]/1e9
    rr_gpu_1["Comm."] = rr_gpu_1["Comm."]/1e9
    rr_gpu_2["Compt."] = rr_gpu_2["Compt."]/1e9
    rr_gpu_2["Comm."] = rr_gpu_2["Comm."]/1e9

    plot_clustered_stacked([rr_gpu_1, rr_gpu_2],'./jpeg/RR-GPU.jpeg',["ChASEv1.2 (GPU)", "ChASEv1.3 (GPU)"],["1","4","16","64"],title='RR on GPUs', ranges=[0,14], legend=False,cmap=plt.cm.Set1)

    resid_gpu_1=df[(df["Impls"] == "ChASEv1.2 (GPU)") & (df["Kernels"] == "Resid")][["Compt.","Comm."]]
    resid_gpu_2=df[(df["Impls"] == "ChASEv1.3 (GPU)") & (df["Kernels"] == "Resid")][["Compt.","Comm."]]
    resid_gpu_1["Compt."] = resid_gpu_1["Compt."]/1e9
    resid_gpu_1["Comm."] = resid_gpu_1["Comm."]/1e9
    resid_gpu_2["Compt."] = resid_gpu_2["Compt."]/1e9
    resid_gpu_2["Comm."] = resid_gpu_2["Comm."]/1e9

    plot_clustered_stacked([resid_gpu_1, resid_gpu_2],'./jpeg/Resid-GPU.jpeg',["ChASEv1.2", "ChASEv1.3"],["1","4","16","64"],title='Resid on GPUs',  legend=False,cmap=plt.cm.Set1)


