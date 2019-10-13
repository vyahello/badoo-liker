FROM vyahello/badoo-liker-base:0.1.0
LABEL version=0.1.0 \
      metadata="The main image for badoo-liker code" \
      maintainer="Volodymyr Yahello <vyahello@gmail.com>"
WORKDIR "/code"
COPY badoo badoo
COPY requirements.txt liker.py docker-entry.sh template-setup.yaml ./
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -v requirements.txt
ENTRYPOINT ["/code/docker-entry.sh"]
