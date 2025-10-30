
FROM continuumio/miniconda3

WORKDIR /app


COPY env.yml ./

COPY ./src ./src
COPY ./data ./data

SHELL ["/bin/bash", "--login", "-c"]




RUN conda init bash \
    && conda env create -f env.yml -q -y
 
EXPOSE 5001

CMD conda activate backend_rest \
    && python3 src/BackendRest.py
    



