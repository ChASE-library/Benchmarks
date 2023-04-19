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

    marker = ['s','o', 'v', 'P']

    f, axes = plt.subplots(figsize=(8, 6))
    df=ddf[['est. (no-opt)','rcond (no-opt)','est. (opt)','rcond (opt)']]
    df=df.astype(float)
    df.plot.line(ax=axes, linewidth=2,markersize=6)
    for i, line in enumerate(axes.get_lines()):
        line.set_marker(marker[i])

    axes.set_yscale('log')
    axes.set_xlabel('Iteration index',fontsize=16)
    axes.set_ylabel('condition number',fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    axes.set_ylim([4e-4,max(df_opt['est. (opt)'].max(), df_no['est. (no-opt)'].max(), df_no['rcond (no-opt)'].max(), df_opt['rcond (opt)'].max())*10])
    axes.xaxis.set_major_locator(MaxNLocator(integer=True))
    axes.legend(fontsize=10,ncol=2,loc='lower left')

    if with_title:
        plt.title(title)
    f.savefig(savepath)


if __name__ == '__main__':
    nacl9k_no_df = pd.read_csv("../results/NaCl-9k_No_Opt.csv")
    nacl9k_opt_df = pd.read_csv("../results/NaCl-9k_Opt1.csv")
    plot_cond_estimate(nacl9k_no_df,nacl9k_opt_df,'NaCl 9k','./jpeg/NaCl_9k.jpeg',with_title=True)

    auag13k_no_df = pd.read_csv("../results/AuAg-13k_No_Opt.csv")
    auag13k_opt_df = pd.read_csv("../results/AuAg-13k_Opt1.csv")
    plot_cond_estimate(auag13k_no_df,auag13k_opt_df,'AuAg 13k','jpeg/AuAg_13k.jpeg',with_title=True)

    tio212k_no_df = pd.read_csv("../results/TiO2-12k_No_Opt.csv")
    tio212k_opt_df = pd.read_csv("../results/TiO2-12k_Opt1.csv")
    plot_cond_estimate(tio212k_no_df,tio212k_opt_df,'TiO2 12k','jpeg/TiO2_12k.jpeg',with_title=True)

    tio229k_no_df = pd.read_csv("../results/TiO2-29k_No_Opt.csv")
    tio229k_opt_df = pd.read_csv("../results/TiO2-29k_Opt1.csv")
    plot_cond_estimate(tio229k_no_df,tio229k_opt_df,'TiO2 29k','jpeg/TiO2_29k.jpeg',with_title=True)

    bse62k_no_df = pd.read_csv("../results/HfO2-62k_No_Opt.csv")
    bse62k_opt_df = pd.read_csv("../results/HfO2-62k_Opt1.csv")
    plot_cond_estimate(bse62k_no_df,bse62k_opt_df,'HfO2 62k','jpeg/HfO2_62k.jpeg')

    bse76k_no_df = pd.read_csv("../results/HfO2-76k_No_Opt.csv")
    bse76k_opt_df = pd.read_csv("../results/HfO2-76k_Opt1.csv")
    plot_cond_estimate(bse76k_no_df,bse76k_opt_df,'HfO2 76k','jpeg/HfO2_76k.jpeg')

    in2o376k_no_df = pd.read_csv("../results/In2O3-76k_No_Opt.csv")
    in2o376k_opt_df = pd.read_csv("../results/In2O3-76k_Opt1.csv")
    plot_cond_estimate(in2o376k_no_df,in2o376k_opt_df,'In2O3 76k','jpeg/In2O3_76k.jpeg')

    in2o3115k_no_df = pd.read_csv("../results/In2O3-115k_No_Opt.csv")
    in2o3115k_opt_df = pd.read_csv("../results/In2O3-115k_Opt1.csv")
    plot_cond_estimate(in2o3115k_no_df,in2o3115k_opt_df,'In2O3 115k','jpeg/In2O3_115k.jpeg')
