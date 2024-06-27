FROM gcr.io/quantum-builds/github.com/quantumlib/jupyter_qsim:latest

# Install the required packages
RUN pip install --upgrade pip

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

# Copy the contents of the repository into the container at /content
COPY . /content

# Set the working directory to /content
WORKDIR /content

# Run the command to start the notebook server locally
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]