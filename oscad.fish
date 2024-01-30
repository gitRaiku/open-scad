function oscad
  inotifywait -m -r -e modify . | 
  while read a b c
    if [ "$c" = "$argv[1]" ]
      echo "python3 $c"
      python3 $c
    end
  end
end
