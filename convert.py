import pandas as pd
import json

df = pd.read_excel('Medicine list.xlsx')

med_list = []
for index, row in df.iterrows():
    brand = str(row['Brand name']).strip()
    form = str(row['Dosage Form']).strip()
    strength = str(row['Strength']).strip()
    
    if brand == 'nan':
        continue
        
    if form.lower() == 'tablet': prefix = 'Tab. '
    elif form.lower() == 'capsule': prefix = 'Cap. '
    elif form.lower() == 'syrup': prefix = 'Syr. '
    elif 'suspension' in form.lower(): prefix = 'Susp. '
    elif 'injection' in form.lower(): prefix = 'Inj. '
    else: prefix = form + ' '
        
    full_name = f"{prefix}{brand} {strength}".strip()
    full_name = ' '.join(full_name.split()) 
    
    if full_name not in med_list:
        med_list.append(full_name)

with open('medicines.js', 'w', encoding='utf-8') as f:
    f.write('const MEDICINES = ' + json.dumps(med_list, ensure_ascii=False) + ';')

print(f"সাকসেস! {len(med_list)} টি ঔষধ নিয়ে medicines.js ফাইল তৈরি হয়েছে!")