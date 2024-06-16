from System.Config import *

def serve_file(base_dir, filename):
    try:
        parent_dir = os.path.dirname(app.root_path)
        file_dir = os.path.join(parent_dir, 'src', 'static', base_dir)
        filepath = os.path.join(file_dir, filename)

        if not os.path.isfile(filepath):
            return "Arquivo não encontrado", 404

        cache_timeout = 604800
        response = make_response(send_from_directory(file_dir, filename))
        response.headers['Cache-Control'] = f'public, max-age={cache_timeout}'
        return response

    except Exception as error:
        response = jsonify({"status": 777, "details": str(error)})
        return response

@app.route('/Static/Styles/Libs/<path:filename>')
def serve_css_libs(filename):
    return serve_file('Styles/Libs', filename)

@app.route('/Static/Styles/Utils/<path:filename>')
def serve_css_utils(filename):
    return serve_file('Styles/Utils', filename)

@app.route('/Static/JS/Libs/<path:filename>')
def serve_js_libs(filename):
    return serve_file('JS/Libs', filename)

@app.route('/Static/JS/Utils/<path:filename>')
def serve_js_Utils(filename):
    return serve_file('JS/Utils', filename)

@app.route('/Static/img/<path:filename>')
def serve_img(filename):
    return serve_file('img', filename)