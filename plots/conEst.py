import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.gridspec as gridspec
import matplotlib
import matplotlib.cm as cm

def plot_cond_estimate(df_no, df_opt, title, savepath, with_title=False):
    df_no = df_no.rename(columns={'estimate': 'est. (no-opt)', 'rcond': 'rcond (no-opt)'})
    df_opt = df_opt.rename(columns={'estimate': 'est. (opt)', 'rcond': 'rcond (opt)'})
    ddf=pd.concat([df_no, df_opt.reindex(df_no.index)], axis=1)

    marker = ['o','o', 'v', 'v']
    linestyle = ['solid','dotted','solid','dotted']
    f, axes = plt.subplots(figsize=(2., 1.))
    df=ddf[['est. (no-opt)','rcond (no-opt)','est. (opt)','rcond (opt)']]
    df=df.astype(float)
    df.plot.line(ax=axes, linewidth=2,markersize=6)
    for i, line in enumerate(axes.get_lines()):
        line.set_marker(marker[i])
        line.set_linestyle(linestyle[i])

    axes.set_yscale('log')
    axes.set_xlabel('Iteration index',fontsize=13)
    axes.set_ylabel('cond',fontsize=13)
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=11)
    axes.set_ylim([4e-2,max(df_opt['est. (opt)'].max(), df_no['est. (no-opt)'].max(), df_no['rcond (no-opt)'].max(), df_opt['rcond (opt)'].max())*10])
    axes.xaxis.set_major_locator(MaxNLocator(integer=True))
    #axes.legend(fontsize=10,ncol=2,loc='lower left')
    axes.get_legend().remove()
    plt.tight_layout()
    
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
            hspace = 0, wspace = 0)

    if with_title:
        plt.title(title)
    f.savefig(savepath, bbox_inches='tight')


if __name__ == '__main__':
    nacl9k_no_df = pd.read_csv("../results/NaCl-9k_No_Opt.csv")
    nacl9k_opt_df = pd.read_csv("../results/NaCl-9k_Opt1.csv")
    plot_cond_estimate(nacl9k_no_df,nacl9k_opt_df,'NaCl 9k','./pdf/NaCl_9k.pdf')


    auag13k_no_df = pd.read_csv("../results/AuAg-13k_No_Opt.csv")
    auag13k_opt_df = pd.read_csv("../results/AuAg-13k_Opt1.csv")
    plot_cond_estimate(auag13k_no_df,auag13k_opt_df,'AuAg 13k','pdf/AuAg_13k.pdf')

    tio229k_no_df = pd.read_csv("../results/TiO2-29k_No_Opt.csv")
    tio229k_opt_df = pd.read_csv("../results/TiO2-29k_Opt1.csv")
    plot_cond_estimate(tio229k_no_df,tio229k_opt_df,'TiO2 29k','pdf/TiO2_29k.pdf')


    bse76k_no_df = pd.read_csv("../results/HfO2-76k_No_Opt.csv")
    bse76k_opt_df = pd.read_csv("../results/HfO2-76k_Opt1.csv")
    plot_cond_estimate(bse76k_no_df,bse76k_opt_df,'HfO2 76k','pdf/HfO2_76k.pdf')

    in2o376k_no_df = pd.read_csv("../results/In2O3-76k_No_Opt.csv")
    in2o376k_opt_df = pd.read_csv("../results/In2O3-76k_Opt1.csv")
    plot_cond_estimate(in2o376k_no_df,in2o376k_opt_df,'In2O3 76k','pdf/In2O3_76k.pdf')

    in2o3115k_no_df = pd.read_csv("../results/In2O3-115k_No_Opt.csv")
    in2o3115k_opt_df = pd.read_csv("../results/In2O3-115k_Opt1.csv")
    plot_cond_estimate(in2o3115k_no_df,in2o3115k_opt_df,'In2O3 115k','pdf/In2O3_115k.pdf')
