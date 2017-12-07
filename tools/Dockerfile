# docker build . -t jupyter && docker run -i -t -p 8888:8888 -e SHELL=/bin/bash -v $PWD/../:/opt/workingdir jupyter
FROM continuumio/anaconda3
RUN conda install -y -c anaconda graphviz
RUN apt-get install -y build-essential
#RUN pip install wordcloud
EXPOSE 8888

ENV data_dir /opt/data

CMD [ "/bin/bash", "-c", "/opt/conda/bin/conda install jupyter -y --quiet && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/workingdir --ip='*' --port=8888 --no-browser --allow-root" ]