import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict

file_names = [
    "original-dataset",
    # "nell",
    # "docred",
    # "declarative",
    # "imperative",
    # "interrogative",
    # "exclamatory",
    "history",
    "economics",
    "science",
    "arts",
    "business",
    "politics",
    "sports",
]


results = OrderedDict()

for fn in file_names:
    lines = None
    with open(f"./unparsed-results/{fn}.txt", 'r') as f:
        lines = f.readlines()

    scores = OrderedDict()
    for line in lines:
        if "------------------" in line or "support" in line:
            continue
        items = line.split()
        relation_type, score = items[0].strip(), items[3]

        scores[relation_type] = float(score)

    results[fn] = scores

# create data
# rounds = filenames
# abcd = relation types
df = pd.DataFrame(
    [
        [rt, *[results[f][rt] for f in file_names]]
        for rt in scores.keys()
    ],
    columns=['Relation', *[f for f in file_names]],
)

# view data
print(df)

# plot grouped bar chart
df.plot(
    x='Relation',
    kind='bar',
    stacked=False,
    # alpha=0.75,
    rot=50,
    # title='Grouped Bar Graph with dataframe',
)
plt.savefig(
    './results.png',
    bbox_inches="tight",
    )
