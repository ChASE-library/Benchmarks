import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df1 = pd.read_csv("../results/hhQR_vs_CholQR_gpu.csv")
    df2 = pd.read_csv("../results/hhQR_vs_CholQR_cpu.csv")

    df = df1.groupby(['Type', 'QR Impl']).mean()
    df_2 = df2.groupby(['Type', 'QR Impl']).mean()

    df=df.round(2)
    df_2=df_2.round(2)

    fig, ax =plt.subplots(2,1,figsize=(24,8))
    ax[0].axis('tight')
    ax[0].axis('off')
    ax[1].axis('tight')
    ax[1].axis('off')

    ax[0].set_title("HHQR vs CholeskyQR: CPUs")
    ax[1].set_title("HHQR vs CholeskyQR: GPUs")
    ax[0].table(cellText=df_2.values,colLabels=df_2.columns,rowLabels=df_2.index,loc="center",cellLoc='center')
    ax[1].table(cellText=df.values,colLabels=df.columns,rowLabels=df.index,loc="center",cellLoc='center')

    fig.savefig("./jpeg/hhQR_vs_CholQR.jpeg")
