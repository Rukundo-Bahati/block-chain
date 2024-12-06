from flask import Flask, render_template, request, redirect, url_for
from blockchain import Blockchain, Block
import time

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def index():
    """Home page."""
    return render_template('index.html', message=None)

@app.route('/mine_block', methods=['POST'])
def mine_block():
    """Mine a new block and return to the homepage."""
    data = request.form.get('data', 'Default Data')
    new_block = Block(len(blockchain.chain), blockchain.get_latest_block().hash, time.time(), data)
    blockchain.add_block(new_block)
    return render_template('index.html', message="Block mined successfully!")

@app.route('/get_chain', methods=['GET'])
def get_chain():
    """Fetch the blockchain."""
    chain_data = [block.__dict__ for block in blockchain.chain]
    return render_template('blockchain.html', chain=chain_data)

if __name__ == '__main__':
    app.run(debug=True)
