#!/bin/bash
BUCKET="${bucket_name}"
EXPERIMENT="${experiment_name}"
SOURCE="${source_name}"
DATASIZE="${data_size}"
 
export HOME=/home/ubuntu
wget -qO- https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
 
 
# shellcheck disable=SC1091
source "$HOME"/.local/bin/env
sudo apt update
sudo apt install -y python3 python3-pip awscli
 
# Descargamos el script de main.py para realizar el test
aws s3 sync s3://$${BUCKET}/scripts/$${EXPERIMENT}/ /home/ubuntu/$${EXPERIMENT}/
 
aws s3 sync s3://$${BUCKET}/jsondata/$${DATASIZE}/ /home/ubuntu/$${EXPERIMENT}/data/
 
 
 
 
~/.local/bin/uv run /home/ubuntu/$${EXPERIMENT}/main.py --input /home/ubuntu/$${EXPERIMENT}/data > /home/ubuntu/output.log
 
aws s3 cp  "/home/ubuntu/output.log"  s3://$${BUCKET}/results/$${EXPERIMENT}/$${DATASIZE}/output.log













# #!/bin/bash
# BUCKET="${bucket_name}"
# EXPERIMENT="${experiment_name}"
# SOURCE="${source_name}"
 
# export HOME=/home/ubuntu
# wget -qO- https://astral.sh/uv/install.sh | sh
 
# # shellcheck disable=SC1091
# source "$HOME"/.local/bin/env
# sudo apt update
# sudo apt install -y python3 python3-pip awscli
 
# # Descargamos el script
# # aws s3 sync s3://$${BUCKET}/scripts/$${EXPERIMENT}/ /home/ubuntu/$${EXPERIMENT}/
# # aws s3 sync s3://$${BUCKET}/generator /home/ubuntu/$${EXPERIMENT}/data
# aws s3 sync s3://$${BUCKET}/scripts /home/ubuntu/

# aws s3 sync s3://cebaezc1-5615fae7e5b2bd6b/jsondata/15 /home/ubuntu/$${EXPERIMENT}/data/
 
# # uv run /home/ubuntu/generator.py papirelar-db73d78d9436d9b3 --is-bucket --num-files 5000000000000 > logs.log 
# # python3 ./generator.py papirelar-db73d78d9436d9b3 --is-bucket --num-files 5000000000000> logs.log
# uv run /home/ubuntu/$${EXPERIMENT}/main.py /home/ubuntu/$${EXPERIMENT}/data > /home/ubuntu/output.log