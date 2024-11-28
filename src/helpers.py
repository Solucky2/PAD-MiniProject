import matplotlib.pyplot as plt

def plot_bar_chart_for_price(df, column_name, color):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(df)), df[column_name], color=color)
    plt.xticks([])
    plt.title("Ceny produktów", fontsize=16)
    plt.xlabel("Produkty", fontsize=12)
    plt.ylabel("Cena [PLN]", fontsize=12)
    plt.show()


def plot_bar_chart_for_discounts(df, column_percentage: str, color: str):
    plt.figure(figsize=(10, 6))
    plt.bar(df.index, df[column_percentage], color=color)
    plt.xlabel("")
    plt.ylabel("(%) Średnia obniżka cen", fontsize=12)
    plt.title("(%) Różnica średniej obniżki", fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    for i, val in enumerate(df[column_percentage]):
        plt.text(i, val + 1, f"{val:.1f}%", ha='center', va='bottom', fontsize=12)
    plt.show()