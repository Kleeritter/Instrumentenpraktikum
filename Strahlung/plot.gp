#Set the output to a png file
set terminal pngcairo size 1920,1080
# The file well write to
set output 'ccd.png'
#Aussehen
my_font = "quicksand,22"

#Regression
f(x)=a*x+b

fit f(x) 'data.txt' via a,b
stats 'data.txt' using 1:2 name "A"
correl= A_correlation **2

title_f(a,b) = sprintf('f(x) = %.3fx + %.3f   r^2=%.3f ', a, b, correl)
blau_1="#8666F4"
turk= "#52F1EB"
blau_3= "#6391F3"
black = "#000000"
blau_2 ="#2596be"

my_line_width = "2"
my_axis_width = "1.5"
my_ps = "0.5"
set pointsize my_ps

set style line 2 linecolor rgbcolor blau_1 linewidth @my_line_width pt 7
set style line 1 linecolor rgbcolor black linewidth @my_line_width pt 7
set style line 3 linecolor rgbcolor blau_3 linewidth @my_line_width pt 7
set style line 5 linecolor rgbcolor blau_2 linewidth @my_line_width pt 7
set style line 4 linecolor rgbcolor turk linewidth @my_line_width pt 7
set style line 6 linecolor rgbcolor blau_3 linewidth @my_line_width pt 7
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
set xlabel "Spannung in mV" font my_font
set ylabel "L_Diff in W/m^2" font my_font

#plot the graphic
plot 'data.txt' title 'Messwerte' with xyerrorbars , f(x) title title_f(a,b)
