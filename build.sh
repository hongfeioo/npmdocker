docker stop NodePingManage ; docker rm NodePingManage
docker build -t npmimg ./
docker run  --volume=/home/NodePingManage/:/NodePingManage:rw  -itd   --env Interval=60     --name=NodePingManage  --net=host     --restart=always   npmimg:latest 
