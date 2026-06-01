import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

# ==========================================
# 1) Load Data
# ==========================================
df = pd.read_csv("reels_attention_span_dataset_12000.csv")
print("Data Shape:", df.shape)
print(df.head())

# ==========================================
# 2) Statistical Calculations
# ==========================================
col = "attention_span_score"

print("\n===== Statistics =====")
print(f"Mean:               {df[col].mean():.2f}")
print(f"Median:             {df[col].median():.2f}")
print(f"Mode:               {df[col].mode()[0]:.2f}")
print(f"Range:              {df[col].max() - df[col].min():.2f}")
print(f"Variance:           {df[col].var():.2f}")
print(f"Std Deviation:      {df[col].std():.2f}")

# ==========================================
# 3) Plots
# ==========================================

# --- Bar Plot ---
plt.figure(figsize=(8, 5))
platform_avg = df.groupby("platform")["attention_span_score"].mean()
platform_avg.plot(kind="bar", color=["steelblue", "coral", "mediumseagreen"])
plt.title("Average Attention Span Score per Platform")
plt.xlabel("Platform")
plt.ylabel("Average Attention Span Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("barplot.png")
plt.show()

# --- Scatter Plot ---
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="reels_watch_time_hours", y="attention_span_score",
                hue="platform", alpha=0.5)
plt.title("Reels Watch Time vs Attention Span Score")
plt.xlabel("Reels Watch Time (Hours)")
plt.ylabel("Attention Span Score")
plt.tight_layout()
plt.savefig("scatterplot.png")
plt.show()

# --- Histogram---
plt.figure(figsize=(8, 5))
plt.hist(df["attention_span_score"], bins=30, color="mediumpurple", edgecolor="black")
plt.title("Distribution of Attention Span Score")
plt.xlabel("Attention Span Score")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()

# --- Box Plot ---
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="stress_level", y="attention_span_score",
            palette="Set2", order=["Low", "Medium", "High"])
plt.title("Attention Span Score by Stress Level")
plt.xlabel("Stress Level")
plt.ylabel("Attention Span Score")
plt.tight_layout()
plt.savefig("boxplot.png")
plt.show()

# --- Pie Chart ---
plt.figure(figsize=(7, 7))
stress_counts = df["stress_level"].value_counts()
plt.pie(stress_counts, labels=stress_counts.index, autopct="%1.1f%%",
        colors=["lightgreen", "gold", "tomato"])
plt.title("Stress Level Distribution")
plt.tight_layout()
plt.savefig("piechart.png")
plt.show()

print("\nDone! All plots saved successfully ")
