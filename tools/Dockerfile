# docker build . -t jupyter && docker run -i -t -p 8888:8888 -v $PWD/../:/opt/workingdir jupyter
FROM continuumio/anaconda3
EXPOSE 8888

ENV data_dir /opt/data

CMD [ "/bin/bash", "-c", "/opt/conda/bin/conda install jupyter -y --quiet && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/workingdir --ip='*' --port=8888 --no-browser --allow-root" ]