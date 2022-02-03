from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
	var1 = random.randint(0,100)
	return str(var1)
	# l1 = ['smiling','not_smiling']
	# return random.choice(l1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)


