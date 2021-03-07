Para executar localmente

docker run -it -p 8888:8888 -e BOOTSTRAP_SERVERS='[kafka-broker-0.dev.com:9093] -e TOPIC='anderovsk' -e FLASK_APP='app'  producer