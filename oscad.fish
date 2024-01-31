# Defined interactively
function oscad
inotifywait -m -r -e modify /home/raiku/Misc/Openscad/ | 
while read a b c
echo "python3 $argv[1]"
python3 $argv[1]
end
end
