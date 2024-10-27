import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

labels = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]
df = pd.read_csv("magic_dataset/magic04.data", names=labels)
df["class"] = (df["class"] == "g").astype(int)

for label in labels:
    plt.hist(df[df["class"] == 1][label], color='blue', alpha=0.5, label="gamma", density=True)
    plt.hist(df[df["class"] == 0][label], color='red', alpha=0.5, label="hadron", density=True)
    plt.title(label)
    plt.xlabel(label)
    plt.ylabel("Probability")
    plt.legend()
    plt.show()