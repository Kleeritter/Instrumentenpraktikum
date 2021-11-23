#Set the output to a png file
set terminal pngcairo size 1920,1080
# The file well write to
set output 'wind.png'
#Aussehen
my_font = "quicksand,22"

#Regression
f(x)=a*x+b

fit f(x) 'winddaten.txt' via a,b
stats 'winddaten.txt' using 1:2 name "A"
correl= A_correlation **2

title_f(a,b) = sprintf('f(x) = %.3fx + %.3f   r^2=%.3f ', a, b, correl)
farbe_1="#8FBCBB"
farbe_2= "#88C0D0"
farbe_3= "#81A1C1"
farbe_4 = "#5E81AC"
farbe_5 ="#2E3440"

my_line_width = "2"
my_axis_width = "1.5"
my_ps = "1.5"
set pointsize my_ps

set style line 2 linecolor rgbcolor farbe_4 linewidth @my_line_width pt 7
set style line 1 linecolor rgbcolor farbe_1 linewidth @my_line_width pt 7
set style line 3 linecolor rgbcolor farbe_3 linewidth @my_line_width pt 7
set style line 5 linecolor rgbcolor farbe_4 linewidth @my_line_width pt 7
set style line 4 linecolor rgbcolor farbe_5 linewidth @my_line_width pt 7

set style increment user
# The graphic title
set title 'Lineare Regression' font my_font


# Box
#set key box lt -1 lw 2
set key  font my_font
set key left
#Range
#set yrange [0:3500]
#set xrange [350:1000]

#Label
set xlabel "Strom in  A" font my_font
set ylabel "Windgeschwindigkeit in m/s" font my_font

#plot the graphic
plot f(x) title title_f(a,b),'winddaten.txt' title 'Messwerte' with xyerrorbars 
