# Using official python runtime base image
FROM python:2.7
MAINTAINER yhf <hongfeio.o@163.com>



# Set the application directory
WORKDIR /NodePingManage  


#exec main function
ENTRYPOINT ["python", "npm.py"]
#CMD ["echo", "123"]    docker  run  hong  echo ccc   运行完毕就推出，可以被run后的参数覆盖
#CMD ["/bin/sh"]



#RUN pip install -r requirements.txt

# Add files to the image
#RUN mkdir -p /python_sample
#ADD . /python_sample


# Install packages
#RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install openssh-server pwgen
#RUN mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config

#ADD set_root_pw.sh /set_root_pw.sh
#ADD run.sh /run.sh

# Exposed ENV
#ENV PYTHON_VERSION 2.7

# Make port 5000 available for links and/or publish
#EXPOSE 80 22

#RUN chmod 755 /*.sh


# mount local dir to container 
#VOLUME  ["/app"]


