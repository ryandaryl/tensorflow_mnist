#https://learningtensorflow.com/lesson7/
import tensorflow as tf
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def fit_line():
    x = tf.placeholder("float")
    y = tf.placeholder("float")
    a = 2
    b = 6

    # w is the variable storing our values. It is initialised with starting "guesses"
    # w[0] is the "a" in our equation, w[1] is the "b"
    w = tf.Variable([1.0, 2.0], name="w")
    # Our model of y = a*x + b
    y_model = tf.multiply(x, w[0]) + w[1]

    error = tf.square(y - y_model)
    train_op = tf.train.GradientDescentOptimizer(0.01).minimize(error)
    model = tf.global_variables_initializer()

    errors = []
    with tf.Session() as session:
        session.run(model)
        for i in range(1000):
            print(i)
            x_train = tf.random_normal((1,), mean=5, stddev=2.0)
            y_train = x_train * a + b
            x_value, y_value = session.run([x_train, y_train])
            _, error_value = session.run([train_op, error], feed_dict={x: x_value, y: y_value})
            errors.append(error_value)
        w_value = session.run(w)
        print("Predicted model: {a:.3f}x + {b:.3f}".format(a=w_value[0], b=w_value[1]))

    fig = plt.figure(figsize=(11,7))
    plt.plot([np.mean(errors[i-50:i]) for i in range(len(errors))])
    plt.show()
    #plt.savefig("errors.png")
    return [fig, a, b] + [str(round(i, 3)) for i in w_value]

if __name__ == '__main__':
    fit_line()