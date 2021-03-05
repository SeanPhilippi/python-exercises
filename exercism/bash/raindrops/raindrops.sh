# 3 pling
# 5 plang
# 7 plong
if ! (($1 % 3)); then
    echo "Pling" 
elif ! (($1 % 5)); then
    echo "Plang"
elif ! (($1 % 7)); then
    echo "Plong"
else
    echo $1
fi
