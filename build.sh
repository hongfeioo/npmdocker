#tar -czvf Node.tar NodePingManage
docker stop NodePingManage ; docker rm NodePingManage
docker build -t hong ./
docker run  --volume=/root/docker/NodePingManage/:/NodePingManage:rw  -itd   --env Interval=60     --name=NodePingManage  --net=host     --restart=always   hong:latest 
