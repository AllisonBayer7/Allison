import plotly.express as px

from die import Die

# Create a D6 die and roll it.
die = Die()

#Create two D6 dice.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize the results.
title = "Results of rolling a D6 and a D10 50000 times."
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

#further customize the chart.
fig.update_layout(xaxis=dict(dtick=1))

fig.show()


