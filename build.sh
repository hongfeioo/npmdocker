docker stop NodePingManage ; docker rm NodePingManage
docker build -t NodePingManageImg ./
docker run  --volume=/root/NodePingManage/:/NodePingManage:rw  -itd   --env Interval=60     --name=NodePingManage  --net=host     --restart=always   NodePingManageImg:latest 