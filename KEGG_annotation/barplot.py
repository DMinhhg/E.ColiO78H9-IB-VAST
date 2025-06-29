import kegganog as kgn
import pandas as pd
import seaborn as sns

palette = sns.color_palette("Blues", n_colors=25)

df = pd.read_csv("/home/minhhg/Downloads/EggNog/KeggaNogSingle/SAMPLE_pathways.tsv", sep="\t")

kgnbar = kgn.barplot(df,
    figsize = (8, 12),
    sort_order="descending",
    yticks_fontsize = 8, 
    cmap = palette,
)

# To plot a fig please use:
kgnbar.plotfig()
kgnbar.savefig("pic_name.png", dpi=600)
