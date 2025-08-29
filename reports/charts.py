import pandas as pd
import plotly.express as px

def generate_report_chart(queryset):
    df = pd.DataFrame([{"name": r.name, "generated_at": r.generated_at, "id": r.id} for r in queryset])
    fig = px.bar(df, x="name", y="id", title="Reports Chart")
    return fig.to_html(full_html=False)
