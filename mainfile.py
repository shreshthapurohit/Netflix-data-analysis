import pandas as pd
#load dataset
df = pd.read_csv('nykaa_data.csv')
#clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
#handling missing values
df.fillna(0, inplace=True)
#convert date column
#df['date'] = pd.to_datetime(df['date'])
#create metrices
df["ctr"] = df["clicks"] / df["impressions"]
df["lead_rate"] = df["leads"] / df["clicks"]
df["conversion_rate"]= df["conversions"] / df["leads"]
df["roi"] = (df["revenue"] - df["cost"]) / df["cost"]
df["cac"]= df["cost"] / df["conversions"]
#replace in values
df.replace([float('inf'), -float('inf')], 0, inplace=True)
#Funnel Summary
funnel=df[["impressions", "clicks", "leads", "conversions" , "revenue"]].sum()
print(funnel)
#channel performance
channel_performance=df.groupby("channel_used").agg({"revenue": "sum", "cost": "sum", "conversions": "sum"})
channel_performance["roi"] = (channel_performance["revenue"] - channel_performance["cost"]) / channel_performance["cost"]
print("\nChannel Performance:\n")
print(channel_performance)
#audience performance
audience_performance=df.groupby("target_audience").agg({"revenue": "sum", "cost": "sum"})
print("\nAudience Performance:\n")
print(audience_performance)
#save cleaned data for Power BI
df.to_csv('cleaned_nykaa_data.csv', index=False)
