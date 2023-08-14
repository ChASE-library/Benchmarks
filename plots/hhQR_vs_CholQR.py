import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df2 = pd.read_csv("../results/hhQR_vs_CholQR_gpu.csv")

    df_2 = df2.groupby(['Type', 'QR Impl']).mean()

    df_2=df_2.round(2)

    print(df_2)
    fig, ax =plt.subplots(1,1,figsize=(24,8))
    ax.axis('tight')
    ax.axis('off')

    ax.set_title("HHQR vs CholeskyQR")
    ax.table(cellText=df_2.values,colLabels=df_2.columns,rowLabels=df_2.index,loc="center",cellLoc='center')

    fig.savefig("./pdf/hhQR_vs_CholQR.pdf")
