import altair as alt
import pandas as pd

def vis_timer_levert_stacked(df: pd.DataFrame):
    df["Levert"] = df["Levert"].astype(bool)

    grouped = (
        df.groupby(["Avdeling", "Levert"])
        .size()
        .unstack(fill_value=0)
        .rename(columns={True: "Levert", False: "Ikke levert"})
    )

    chart_data = grouped.reset_index().melt(
        id_vars="Avdeling",
        value_vars=["Levert", "Ikke levert"],
        var_name="Status",
        value_name="Antall"
    )

    return (
        alt.Chart(chart_data)
        .mark_bar()
        .encode(
            x="Avdeling:N",
            y="Antall:Q",
            color=alt.Color("Status:N", scale=alt.Scale(
                domain=["Ikke levert", "Levert"],
                range=["#d62728", "#2ca02c"]
            )),
            tooltip=["Avdeling", "Status", "Antall"]
        )
        .properties(title="Leveringsstatus per avdeling")
    )
