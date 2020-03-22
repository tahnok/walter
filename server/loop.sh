while true;
do
    echo "Capturing..."
    firefox --headless --screenshot static/out.png --window-size 600,800 http://127.0.0.1:8000
    echo "done";
    sleep 30
done