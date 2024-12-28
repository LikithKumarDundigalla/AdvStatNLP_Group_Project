FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

LABEL author="Likith Kumar "
LABEL description="Course Project Container"

# This will be our default directory for subsequent commands
WORKDIR /app

# copy executables to path
COPY requirements.txt /app/requirements.txt
COPY NLP_Group_Project.ipynb /app/NLP_Group_Project.ipynb
COPY scripts/generated_functions_gemma.py /app/scripts/generated_functions_gemma.py
COPY scripts/generated_functions_Qwencoder.py /app/scripts/generated_functions_Qwencoder.py
COPY scripts/generated_functions_starcoder.py /app/scripts/generated_functions_starcoder.py
COPY scripts/test.py /app/scripts/test.py


RUN if [ -f "requirements.txt"]; then pip install -r requirements.txt; fi
RUN conda install -y jupyter ipywidgets widgetsnbextension \
    && jupyter nbextension enable --py widgetsnbextension



# launch jupyter by default
CMD ["python", "-m", "jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
