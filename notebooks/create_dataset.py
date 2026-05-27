import pandas as pd, random, os

rows = []
complaints = [
    ("Water supply cut off for 3 days", "Water Supply"),
    ("No water since morning please help urgently", "Water Supply"),
    ("Water pipeline burst near school flooding street", "Water Supply"),
    ("Tap water brown and smells bad undrinkable", "Water Supply"),
    ("Water tanker not coming for 5 days", "Water Supply"),
    ("Contaminated water supply causing illness", "Water Supply"),
    ("No drinking water in our locality", "Water Supply"),
    ("Leaking water pipe on main road flooding", "Water Supply"),
    ("Water meter reading wrong for 6 months", "Water Supply"),
    ("Overhead tank not filled regularly low pressure", "Water Supply"),
    ("No electricity since yesterday evening urgent", "Electricity"),
    ("Power cuts every evening 4 to 5 hours", "Electricity"),
    ("Transformer burned whole street no power", "Electricity"),
    ("Streetlights not working for a month", "Electricity"),
    ("Wires hanging low near playground dangerous", "Electricity"),
    ("Sparking from transformer near house fire risk", "Electricity"),
    ("Electric pole leaning dangerously on road", "Electricity"),
    ("High tension wire fallen on road dangerous", "Electricity"),
    ("No power supply since 2 days in area", "Electricity"),
    ("Electricity bill extremely high this month wrong", "Electricity"),
    ("Large pothole on main road causing accidents", "Roads"),
    ("Road completely broken vehicles getting damaged", "Roads"),
    ("Dangerous pothole near hospital entrance repair", "Roads"),
    ("Bridge near market has cracks urgent repair", "Roads"),
    ("Road dug for pipeline not restored for months", "Roads"),
    ("Traffic signals not working at busy junction", "Roads"),
    ("Divider broken near school dangerous children", "Roads"),
    ("Road cave in after rain near market area", "Roads"),
    ("Potholes making ambulance trips very difficult", "Roads"),
    ("Road waterlogging every monsoon season problem", "Roads"),
    ("Garbage not collected for 2 weeks foul smell", "Sanitation"),
    ("Sewage overflow outside house very unhygienic", "Sanitation"),
    ("Open drainage near school health hazard children", "Sanitation"),
    ("Sewage water mixing with drinking water critical", "Sanitation"),
    ("Manholes open without covers dangerous at night", "Sanitation"),
    ("Garbage dump fire spreading smoke in area", "Sanitation"),
    ("Dead animals near garbage dump not cleared", "Sanitation"),
    ("Drain overflow flooding our street after rain", "Sanitation"),
    ("Mosquito breeding stagnant water disease risk", "Sanitation"),
    ("Public toilet near market extremely dirty unusable", "Sanitation"),
    ("Bus never arrives on time daily problem", "Transport"),
    ("Auto drivers charging extra fare misbehaving", "Transport"),
    ("No bus service to our area after 8pm", "Transport"),
    ("Driver using phone while driving dangerous", "Transport"),
    ("No public transport near hospital emergency", "Transport"),
    ("Bus overcrowded unsafe for passengers daily", "Transport"),
    ("Speeding bus nearly hit pedestrians near school", "Transport"),
    ("Tempo drivers harassing passengers extra money", "Transport"),
    ("Bus stop has no shelter no bench", "Transport"),
    ("Buses not following schedule during peak hours", "Transport"),
]

urgency_map = {"Water Supply": "High", "Electricity": "High",
               "Roads": "Medium", "Sanitation": "High", "Transport": "Low"}

for complaint, dept in complaints:
    for suffix, urgency in [
        ("", urgency_map[dept]),
        (" urgent action needed", "Critical"),
        (" please fix this soon", "Medium"),
        (" authorities not responding", "High"),
        (" residents suffering daily", urgency_map[dept]),
        (" this has been ignored for weeks", "High"),
    ]:
        rows.append({
            "complaint": complaint + suffix,
            "department": dept,
            "sentiment": "Negative",
            "urgency": urgency
        })

random.seed(42)
random.shuffle(rows)
df = pd.DataFrame(rows)
os.makedirs("data/raw", exist_ok=True)
df.to_csv("data/raw/grievances.csv", index=False)
print(f"Dataset created! Shape: {df.shape}")
print(df["department"].value_counts())