from flask import Flask, redirect, url_for, \
    request, render_template

app = Flask(__name__)


@app.route('/result/<sentence>/<src_lan>/<tar_lan>')
def result(sentence, src_lan, tar_lan):
    result = 'Done! ' + sentence + ' 源语言是' + src_lan + ' 目标语言是' + tar_lan
    return render_template('target.html', result=result)


@app.route('/translate/', methods=['POST', 'GET'])
def translate():
    original_sen = request.args.get('sentence')
    src = request.args.get('src_lan')
    print("src:", src)
    tar = request.args.get('tar_lan')
    print("tar:", tar)
    return redirect(url_for('result', sentence=original_sen, src_lan=src, tar_lan=tar))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
