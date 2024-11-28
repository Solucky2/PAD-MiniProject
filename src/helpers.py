import matplotlib.pyplot as plt
import pandas as pd


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


def calculate_average_prices(dfs:dict):
    results = []
    for df_name, df in dfs.items():
        avg_price = df["new_price [PLN]"].mean()
        results.append({"df_name": df_name, "avg_price [PLN]": avg_price})

    return pd.DataFrame(results)


def calculate_minmax_prices(dfs: dict):
    min_max = []
    for name, df in dfs.items():
        min_row = df.loc[df["new_price [PLN]"].idxmin()]
        max_row = df.loc[df["new_price [PLN]"].idxmax()]

        min_max.append({
            "df_name": name,
            "min_product": min_row["product_name"],
            "min_price [PLN]": min_row["new_price [PLN]"],
            "max_product": max_row["product_name"],
            "max_price [PLN]": max_row["new_price [PLN]"]
        })
    return pd.DataFrame(min_max).set_index("df_name")


def calculate_avg_discounts(dfs: dict):
    avg_disc_perc = []
    for name, df in dfs.items():
        df["discount_percentage"] = ((df["price_old [PLN]"] - df["new_price [PLN]"]) / df["price_old [PLN]"]) * 100
        avg_discount = df["discount_percentage"].mean()
        avg_disc_perc.append({"df_name": name, "avg_discount_percentage": avg_discount})
    return pd.DataFrame(avg_disc_perc)
