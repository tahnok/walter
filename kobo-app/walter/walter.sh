cd /mnt/onboard/.adds/walter/
while true
do
	./curl http://192.168.1.153:8000/snapshot --output /tmp/out.png;
	./fbink -i /tmp/out.png;
	sleep 60;
done
