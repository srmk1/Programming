from bokeh.plotting import figure, output_file, show

factors = ["a", "b", "c", "d", "e", "f", "g", "h"]
x = [50, 40, 65, 10, 25, 37, 80, 60, 70, 80, 90, 100, 110]

test = ["a", "b", "c", "d", "b", "f", "g", "a", "f", "g", "a"]
output_file("categorical.html")

p = figure(y_range=factors)

p.circle(x, test, size=15, fill_color="orange", line_color="green", line_width=3)

show(p)
