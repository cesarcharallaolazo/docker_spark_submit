build:
	cp ./spark/newrun.py ./target
	cd ./spark && zip -x newrun.py -r ../target/spark.zip .
