set terminal postscript eps enhanced
set xrange [-40:40]
set yrange [-40:40]
set size square
set polar
set angle degrees
set grid polar
set style line 1 lt 1 lw 50
set out 'Winddaten.eps'
plot 'Winddaten.txt'using (90.-$1):($2) with imp ls 1 t "Häufigkeit"