from collections import defaultdict
import yaml

def load_data():
    content = open('data/dps_fixed.yaml').read()
    data = yaml.safe_load(content)
    return data

def analyze_data():
    data = load_data()
    dic = {}
    counts = defaultdict(int)
    actually_different = []
    for row in data:
        name = row['name'] 
        if name not in dic:
            dic[name] = row
        
        if name in dic:
            old_row = dic[name]
            if old_row['cooldown'] != row['cooldown']:
                actually_different.append(row)
                print(f"Diff cd:\n{old_row}\n{row}\n")
            if old_row['hp'] != row['hp']:
                actually_different.append(row)
                print(f"Diff hp:\n{old_row}\n{row}\n")
            if old_row['traits'] != row['traits']:
                actually_different.append(row)
                print(f"Diff traits:\n{old_row}\n{row}\n")
            if 'directDamage' in old_row and 'directDamage' in row and old_row['directDamage'] != row['directDamage']:
                actually_different.append(row)
                print(f"Diff directDamage:\n{old_row}\n{row}\n")
        
        counts[name] += 1

    for name, count in counts.items():
        print(f"{count}:\t{name}")
    yaml.dump(list(dic.values()), open('data/dps_small.yaml', 'w'))

if __name__ == "__main__":
    analyze_data();

