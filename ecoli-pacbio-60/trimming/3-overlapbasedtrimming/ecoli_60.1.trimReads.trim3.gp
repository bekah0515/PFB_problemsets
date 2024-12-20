set title 'trim3'
set xlabel 'length, bin width = 25'
set ylabel 'number'

binwidth=25
set boxwidth binwidth
bin(x,width) = width*floor(x/width) + binwidth/2.0

set terminal png size 1024,1024
set output './ecoli_60.1.trimReads.trim3.png'
plot [] [0:] './ecoli_60.1.trimReads.trim3.dat' using (bin($1,binwidth)):(1.0) smooth freq with boxes title ''
