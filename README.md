# Tensorflow MNIST example
This web application uses a background worker in Heroku, to learn identification of handwritten single digits, using the MNIST handwritten numbers [dataset](). The Tensorflow code is based on the "MNIST for ML Beginners" [tutorial](https://www.tensorflow.org/versions/r1.1/get_started/mnist/beginners), from Tensorflow's creators.

I've made the 'web' process return a job id instead of the actual job result. The job id can be saved by the client, and used subsequently to long-poll the web process. Once the worker is done, when queried with the job id, the web process returns the result.

## Live demo

See it working [here](https://mnist-rdm.herokuapp.com)



Wait about 30 seconds, then click the link. If it's still not done, wait some more and click again.

I've also added app.json and this readme so you can:

## Deploy to Heroku
By clicking the button below.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)