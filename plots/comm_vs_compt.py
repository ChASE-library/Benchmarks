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
    plt.figure(figsize=(2,1.8))

    axe = plt.subplot(111)

    for df in dfall : # for each data frame
        axe = df.plot(kind="bar",
                      linewidth=1,
                      stacked=True,
                      ax=axe,
                      legend=False,
                      grid=False,
                      position=0.6,
                      #colormap=cmp_list[cnt],
                      **kwargs)  # make bar plots
    

    c=['#1EA759', '#FC1515', '#1F08EC', '#67C76E', '#F75E61', '#5164EA', '#C2EE88', '#F1BAC1', '#79ADE9']
    
    h,l = axe.get_legend_handles_labels() # get the handles we want to modify
    for i in range(0, n_df * n_col, n_col): # len(h) = n_col * n_df
        for j, pa in enumerate(h[i:i+n_col]):
            for rect in pa.patches: # for each index
                rect.set_x(rect.get_x() + 1. / float(n_df + 1) * i / float(n_col))
                #print(rect.get_x() + 1 / float(n_df + 1) * i / float(n_col))
                #rect.set_hatch(H * int(i / n_col)) #edited part
                rect.set_color(c[i+j])
                #print(i,j, i+j)
                rect.set_width(0.9 / float(n_df + 1))

    axe.set_xticks((np.arange(0, 2 * n_ind, 2) + 1 / float(n_df + 1)) / 2.)
    axe.set_xticklabels(indices, rotation = 0, fontsize=12)
    plt.yticks(fontsize=11)

    axe.set_ylabel("Time (s)",fontsize=13)
    axe.set_xlabel("Number of Nodes",fontsize=13)

    #axe.set_title(title)
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
    
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)

    plt.savefig(output,bbox_inches='tight')

    return axe

if __name__ == '__main__':
    df=pd.read_csv('../results/comm_vs_compute_vs_cpy.csv')
    df.set_index("Nodes")

    filter_gpu_1=df[(df["Impls"] == "ChASE(v1.2.1)") & (df["Kernels"] == "Filter")][["Compt.","Comm.","Copy"]]
    filter_gpu_2=df[(df["Impls"] == "ChASE(w/o NCCL)") & (df["Kernels"] == "Filter")][["Compt.","Comm.","Copy"]]
    filter_gpu_3=df[(df["Impls"] == "ChASE(NCCL)") & (df["Kernels"] == "Filter")][["Compt.","Comm.","Copy"]]

    plot_clustered_stacked([filter_gpu_1, filter_gpu_2, filter_gpu_3],'./pdf/Filter-GPU.pdf',["ChASE(v1.2.1)", "ChASE(w/o NCCL)"],["1","4","16","64"],title='QR on GPUs',  legend=False,cmap=plt.cm.Set1)

    qr_gpu_1=df[(df["Impls"] == "ChASE(v1.2.1)") & (df["Kernels"] == "QR")][["Compt.","Comm.","Copy"]]
    qr_gpu_2=df[(df["Impls"] == "ChASE(w/o NCCL)") & (df["Kernels"] == "QR")][["Compt.","Comm.","Copy"]]
    qr_gpu_3=df[(df["Impls"] == "ChASE(NCCL)") & (df["Kernels"] == "QR")][["Compt.","Comm.","Copy"]]

    plot_clustered_stacked([qr_gpu_1, qr_gpu_2, qr_gpu_3],'./pdf/QR-GPU.pdf',["ChASE(v1.2.1)", "ChASE(w/o NCCL)"],["1","4","16","64"],title='QR on GPUs',  legend=False,cmap=plt.cm.Set1)

    rr_gpu_1=df[(df["Impls"] == "ChASE(v1.2.1)") & (df["Kernels"] == "RR")][["Compt.","Comm.","Copy"]]
    rr_gpu_2=df[(df["Impls"] == "ChASE(w/o NCCL)") & (df["Kernels"] == "RR")][["Compt.","Comm.","Copy"]]
    rr_gpu_3=df[(df["Impls"] == "ChASE(NCCL)") & (df["Kernels"] == "RR")][["Compt.","Comm.","Copy"]]

    plot_clustered_stacked([rr_gpu_1, rr_gpu_2, rr_gpu_3],'./pdf/RR-GPU.pdf',["ChASE(v1.2.1)", "ChASE(w/o NCCL)"],["1","4","16","64"],title='RR on GPUs', legend=False,cmap=plt.cm.Set1)

    resid_gpu_1=df[(df["Impls"] == "ChASE(v1.2.1)") & (df["Kernels"] == "Residual")][["Compt.","Comm.","Copy"]]
    resid_gpu_2=df[(df["Impls"] == "ChASE(w/o NCCL)") & (df["Kernels"] == "Residual")][["Compt.","Comm.","Copy"]]
    resid_gpu_3=df[(df["Impls"] == "ChASE(NCCL)") & (df["Kernels"] == "Residual")][["Compt.","Comm.","Copy"]]

    plot_clustered_stacked([resid_gpu_1, resid_gpu_2, resid_gpu_3],'./pdf/Resid-GPU.pdf',["ChASEv1.2", "ChASEv1.3"],["1","4","16","64"],title='Resid on GPUs',  legend=False,cmap=plt.cm.Set1)


