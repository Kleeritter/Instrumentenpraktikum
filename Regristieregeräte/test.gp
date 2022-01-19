set terminal postscript eps enhanced
set size square
set polar
set angle degrees
set grid polar
set style line 1 lt 1 lw 50
unset key
unset ytics
unset xtics
unset border
set out 'Winddaten.eps'
plot 'neu.txt'using (90.-$1):($2) with imp ls 1 t "Häufigkeit"